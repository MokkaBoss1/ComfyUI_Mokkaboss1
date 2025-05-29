from PIL import Image
import numpy as np
import torch

# List of aspect-ratio choices for dropdown
oc_aspectratios = [
    "9:21 640x1536 (0.42)",
    "9:19 704x1472 (0.48)",
    "9:16 768x1344 (0.57)",
    "5:8 768x1216 (0.63)",
    "2:3 832x1216 (0.68)",
    "3:4 896x1152 (0.78)",
    "1:1 1024x1024 (1.00)",
    "4:3 1152x896 (1.29)",
    "3:2 1216x832 (1.46)",
    "8:5 1216x768 (1.58)",
    "16:9 1344x768 (1.75)",
    "19:9 1472x704 (2.09)",
    "21:9 1536x640 (2.40)",
    "unchanged"
]

# Choices for preserve input dimensions dropdown
preserve_dim = ["yes", "no"]


def pil2tensor(image: Image.Image) -> torch.Tensor:
    """
    Convert a PIL Image to a normalized float32 torch Tensor of shape [1, H, W, C].
    """
    arr = np.array(image).astype(np.float32) / 255.0
    return torch.from_numpy(arr).unsqueeze(0)

class CombinedCrop:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "input_image": ("IMAGE",),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ((oc_aspectratios),),
            "exact_aspect_ratio": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 10.0, "step": 0.001}),
            "zoom": ("FLOAT", {"default": 1.0, "min": 1.0, "max": 10.0, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
            "megapixels": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 50.0, "step": 0.1}),
            "preserve_input_dimensions": ((preserve_dim),),
        }}

    RETURN_TYPES = ("IMAGE", "FLOAT")
    RETURN_NAMES = ("output_image", "exact_aspect_ratio")
    FUNCTION = "process_image"
    CATEGORY = "👑 MokkaBoss1/Image"

    def process_image(
            self,
            input_image: torch.Tensor,
            rounding: int,
            aspect_ratio: str,
            exact_aspect_ratio: float,
            zoom: float,
            x_offset: int,
            y_offset: int,
            megapixels: float,
            preserve_input_dimensions: str
    ):
        try:
            # Store original dimensions
            _, h0, w0, _ = input_image.shape

            # Early exit: no changes requested
            if (
                exact_aspect_ratio == 0.0 and
                aspect_ratio == "unchanged" and
                zoom == 1.0 and
                megapixels == 0.0 and
                preserve_input_dimensions == "no"
            ):
                return input_image, float(w0) / float(h0)

            # Determine target dimensions
            if exact_aspect_ratio != 0.0:
                target_w, target_h = self.calculate_exact_dimensions(exact_aspect_ratio)
            elif aspect_ratio != "unchanged":
                target_w, target_h = self.get_aspect_dimensions(aspect_ratio)
            else:
                target_w, target_h = None, None

            _, h, w, _ = input_image.shape
            nx = x_offset / 100.0
            ny = y_offset / 100.0

            # Aspect-ratio crop
            if target_w is None:
                out_w, out_h = w, h
            else:
                ratio = float(target_w) / float(target_h)
                out_w = int(round(min(w, h * ratio)))
                out_h = int(round(out_w / ratio))
                out_w -= (out_w % rounding)
                out_h -= (out_h % rounding)

            x1 = int(round((w - out_w) * (0.5 + 0.5 * nx)))
            y1 = int(round((h - out_h) * (0.5 + 0.5 * ny)))
            x1 = max(0, min(w - out_w, x1))
            y1 = max(0, min(h - out_h, y1))
            cropped = input_image[:, y1:y1+out_h, x1:x1+out_w, :]

            # Zoom crop
            _, ch, cw, _ = cropped.shape
            z_w = int(round(cw / zoom))
            z_h = int(round(ch / zoom))
            zx1 = int(round((cw - z_w) * (0.5 + 0.5 * nx)))
            zy1 = int(round((ch - z_h) * (0.5 + 0.5 * ny)))
            zx1 = max(0, min(cw - z_w, zx1))
            zy1 = max(0, min(ch - z_h, zy1))
            zoomed = cropped[:, zy1:zy1+z_h, zx1:zx1+z_w, :]

            # Megapixel resize
            if megapixels > 0.0:
                img = Image.fromarray((zoomed.squeeze().numpy() * 255).astype(np.uint8))
                curr_mp = (img.width * img.height) / 1048576.0
                sf = (megapixels / curr_mp) ** 0.5
                new_w = int(round(img.width * sf))
                new_h = int(round(img.height * sf))
                img = img.resize((new_w, new_h), Image.LANCZOS)
                output = pil2tensor(img)
                exact_ratio = float(new_w) / float(new_h)
            else:
                output = zoomed
                _, oh, ow, _ = output.shape
                exact_ratio = float(ow) / float(oh)

            # Preserve input dimensions
            if preserve_input_dimensions == "yes":
                img = Image.fromarray((output.squeeze().numpy() * 255).astype(np.uint8))
                img = img.resize((w0, h0), Image.LANCZOS)
                output = pil2tensor(img)
                exact_ratio = float(w0) / float(h0)

            return output, exact_ratio
        except Exception as e:
            print(f"Exception during processing: {e}")
            _, ih, iw, _ = input_image.shape
            return input_image, float(iw) / float(ih)

    def get_aspect_dimensions(self, aspect_ratio: str):
        aspect_map = {
            "1:1 1024x1024 (1.00)": (1024, 1024),
            "2:3 832x1216 (0.68)": (832, 1216),
            "3:4 896x1152 (0.78)": (896, 1152),
            "5:8 768x1216 (0.63)": (768, 1216),
            "9:16 768x1344 (0.57)": (768, 1344),
            "9:19 704x1472 (0.48)": (704, 1472),
            "9:21 640x1536 (0.42)": (640, 1536),
            "3:2 1216x832 (1.46)": (1216, 832),
            "4:3 1152x896 (1.29)": (1152, 896),
            "8:5 1216x768 (1.58)": (1216, 768),
            "16:9 1344x768 (1.75)": (1344, 768),
            "19:9 1472x704 (2.09)": (1472, 704),
            "21:9 1536x640 (2.40)": (1536, 640)
        }
        return aspect_map.get(aspect_ratio, (1024, 1024))

    def calculate_exact_dimensions(self, exact_aspect_ratio: float):
        if exact_aspect_ratio >= 1.0:
            w = 1024
            h = int(round(w / exact_aspect_ratio))
        else:
            h = 1024
            w = int(round(h * exact_aspect_ratio))
        return w, h

NODE_CLASS_MAPPINGS = {"CombinedCrop": CombinedCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"CombinedCrop": "👑 CombinedCrop"}