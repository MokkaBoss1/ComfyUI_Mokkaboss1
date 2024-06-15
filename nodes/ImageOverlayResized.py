from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy as np
import torch

def tensor2pil(image):
    # Convert PyTorch tensor to PIL image, assuming image is scaled between 0 and 1
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    # Convert PIL image to PyTorch tensor, scale it to 0-1
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ImageOverlayResized:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "background_image": ("IMAGE",),
                "subject_image": ("IMAGE",),
                "overlay_resize": (["None", "Fit", "Resize by rescale_factor", "Resize to width & height"],),
                "resize_method": (["nearest-exact", "bilinear", "area"],),
                "rescale_factor": ("FLOAT", {"default": 1, "min": 0.01, "max": 16.0, "step": 0.1}),
                "width": ("INT", {"default": 512, "min": 0, "max": 48000, "step": 64}),
                "height": ("INT", {"default": 512, "min": 0, "max": 48000, "step": 64}),
                "x_offset": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 1}),
                "y_offset": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 1}),
                "rotation": ("INT", {"default": 0, "min": -180, "max": 180, "step": 5}),
                "opacity": ("FLOAT", {"default": 0, "min": 0, "max": 100, "step": 5}),
            },
            "optional": {"subject_mask": ("MASK",),}
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_overlay_resized"
    CATEGORY = "Custom Nodes/Image"

    def resize_subject_image(self, subject_image, background_image):
        # Convert tensors to PIL images
        subject_image_pil = tensor2pil(subject_image)
        background_image_pil = tensor2pil(background_image)

        # Get dimensions of both images
        subject_image_width, subject_image_height = subject_image_pil.size
        background_image_width, background_image_height = background_image_pil.size

        # Determine orientations
        subject_image_type = "landscape" if subject_image_width >= subject_image_height else "portrait"
        background_image_type = "landscape" if background_image_width >= background_image_height else "portrait"

        # Resize subject to fit inside background
        scale_width = background_image_width / subject_image_width
        scale_height = background_image_height / subject_image_height
        scale_factor = min(scale_width, scale_height)

        # Compute new size preserving aspect ratio
        new_width = int(subject_image_width * scale_factor)
        new_height = int(subject_image_height * scale_factor)

        # Resize the subject image using the LANCZOS resampling algorithm for high quality
        resized_subject_image = subject_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Convert back to tensor
        subject_image_return = pil2tensor(resized_subject_image)

        parameters = f"New height: {new_height}\nNew width: {new_width}\nScale factor: {scale_factor}\nScale width: {scale_width}\nScale height: {scale_height}\nSubject image type: {subject_image_type}\nBackground image type: {background_image_type}\nSubject image width: {subject_image_width}\nSubject image height: {subject_image_height}\nBackground image width: {background_image_width}\nBackground image height: {background_image_height}"

        return subject_image_return, parameters

    def apply_overlay_resized(self, background_image, subject_image, overlay_resize, resize_method, rescale_factor,
                              width, height, x_offset, y_offset, rotation, opacity, subject_mask=None):

        # Resize the subject image to fit the background image
        subject_image, _ = self.resize_subject_image(subject_image, background_image)

        # Convert subject image to PIL
        subject_image = tensor2pil(subject_image)
        subject_image = subject_image.convert('RGBA')
        subject_image.putalpha(Image.new("L", subject_image.size, 255))

        # If mask connected, check if the subject image has an alpha channel
        if subject_mask is not None:
            mask = tensor2pil(subject_mask)
            mask = mask.resize(subject_image.size)
            subject_image.putalpha(ImageOps.invert(mask))

        # Rotate the subject image
        subject_image = subject_image.rotate(rotation, expand=True)

        # Apply opacity on subject image
        r, g, b, a = subject_image.split()
        a = a.point(lambda x: max(0, int(x * (1 - opacity / 100))))
        subject_image.putalpha(a)

        # Split the background image tensor along the first dimension to get a list of tensors
        background_image_list = torch.unbind(background_image, dim=0)

        # Convert each tensor to a PIL image, apply the overlay, and then convert it back to a tensor
        processed_background_image_list = []
        for tensor in background_image_list:
            image = tensor2pil(tensor)

            # Calculate the center point for the overlay
            background_center_x = image.width // 2
            background_center_y = image.height // 2
            overlay_center_x = subject_image.width // 2
            overlay_center_y = subject_image.height // 2
            new_location = (background_center_x - overlay_center_x + x_offset, background_center_y - overlay_center_y + y_offset)

            # Paste the subject image onto the background image
            if subject_mask is None:
                image.paste(subject_image, new_location, subject_image)
            else:
                image.paste(subject_image, new_location, subject_image)

            processed_tensor = pil2tensor(image)
            processed_background_image_list.append(processed_tensor)

        background_image = torch.stack([tensor.squeeze() for tensor in processed_background_image_list])

        return background_image,

NODE_CLASS_MAPPINGS = {"ImageOverlayResized": ImageOverlayResized}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageOverlayResized": "👑 ImageOverlayResized"}
