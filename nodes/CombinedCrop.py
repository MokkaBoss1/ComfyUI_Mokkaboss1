from PIL import Image, ImageDraw
import numpy as np
import torch

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

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

class CombinedCrop:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "input_image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ((oc_aspectratios),),
            "exact_aspect_ratio": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 10.0, "step": 0.001}),
            "zoom": ("FLOAT", {"default": 1.0, "min": 1, "max": 10.0, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
            "megapixels": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 50.0}),
        }}

    RETURN_TYPES = ("IMAGE", "FLOAT" )
    RETURN_NAMES = ("output_image", "exact_aspect_ratio",)
    FUNCTION = "process_image"
    CATEGORY = "👑 MokkaBoss1/Image"

    def process_image(self, input_image, rounding, aspect_ratio, exact_aspect_ratio, zoom, x_offset, y_offset, megapixels):
        try:
            if exact_aspect_ratio != 0.0:
                width, height = self.calculate_exact_dimensions(exact_aspect_ratio)
            elif aspect_ratio != "unchanged":
                width, height = self.get_aspect_dimensions(aspect_ratio)
            else:
                width, height = input_image.shape[2], input_image.shape[1]

            ratio = float(width / height)
            _, input_height, input_width, _ = input_image.shape

            # Apply aspect ratio crop first
            output_width = int(min(input_width, input_height * ratio))
            output_height = int(output_width / ratio)

            output_width = output_width - (output_width % rounding)
            output_height = output_height - (output_height % rounding)

            # Normalize x_offset and y_offset
            x_offset_normalized = x_offset / 100.0
            y_offset_normalized = y_offset / 100.0

            # Apply the normalized offsets for the aspect ratio crop
            x_offset_aspect = int((input_width - output_width) * 0.5) + int((input_width - output_width) * x_offset_normalized * 0.5)
            y_offset_aspect = int((input_height - output_height) * 0.5) + int((input_height - output_height) * y_offset_normalized * 0.5)

            crop_x1_aspect = max(0, min(input_width - output_width, x_offset_aspect))
            crop_y1_aspect = max(0, min(input_height - output_height, y_offset_aspect))
            crop_x2_aspect = min(input_width, crop_x1_aspect + output_width)
            crop_y2_aspect = min(input_height, crop_y1_aspect + output_height)

            cropped_image_aspect = input_image[:, crop_y1_aspect:crop_y2_aspect, crop_x1_aspect:crop_x2_aspect, :]

            # Apply zoom crop next
            _, cropped_height, cropped_width, _ = cropped_image_aspect.shape
            output_width_zoom = int(cropped_width / zoom)
            output_height_zoom = int(cropped_height / zoom)

            # Normalize x_offset and y_offset for zoom crop
            x_offset_zoom_normalized = x_offset / 100.0
            y_offset_zoom_normalized = y_offset / 100.0

            # Apply the normalized offsets for the zoom crop
            x = int((cropped_width - output_width_zoom) * 0.5) + int((cropped_width - output_width_zoom) * x_offset_zoom_normalized * 0.5)
            y = int((cropped_height - output_height_zoom) * 0.5) + int((cropped_height - output_height_zoom) * y_offset_zoom_normalized * 0.5)

            crop_x1_zoom = max(0, min(cropped_width - output_width_zoom, x))
            crop_y1_zoom = max(0, min(cropped_height - output_height_zoom, y))
            crop_x2_zoom = min(cropped_width, crop_x1_zoom + output_width_zoom)
            crop_y2_zoom = min(cropped_height, crop_y1_zoom + output_height_zoom)

            crop_image = cropped_image_aspect[:, crop_y1_zoom:crop_y2_zoom, crop_x1_zoom:crop_x2_zoom, :]

            # Convert tensor back to PIL image if it is not already in that format
            if isinstance(crop_image, torch.Tensor):
                crop_image = Image.fromarray((crop_image.squeeze().numpy() * 255).astype(np.uint8))

            # Calculate new dimensions if megapixels is greater than 0
            if megapixels > 0.0:
                original_width, original_height = crop_image.size
                original_megapixels = (original_width * original_height) / 1048576

                # Calculate the scale factor
                scale_factor = (megapixels / original_megapixels) ** 0.5
                new_width = int(original_width * scale_factor)
                new_height = int(original_height * scale_factor)

                # Resize the image
                crop_image = crop_image.resize((new_width, new_height), Image.LANCZOS)

            # Convert the resized image back to a tensor
            exact_aspect_ratio = width / height
            
            output_image = pil2tensor(crop_image)
            return (output_image, exact_aspect_ratio, )

        except Exception as e:
            print(f"Exception during processing: {e}")
            return input_image  # Return the original image in case of an error

    def get_aspect_dimensions(self, aspect_ratio):
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

    def calculate_exact_dimensions(self, exact_aspect_ratio):
        if exact_aspect_ratio >= 1:
            width = 1024
            height = int(width / exact_aspect_ratio)
        else:
            height = 1024
            width = int(height * exact_aspect_ratio)
        return width, height

NODE_CLASS_MAPPINGS = {"CombinedCrop": CombinedCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"CombinedCrop": "👑 CombinedCrop"}

