# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ██████╗  ██████╗ ███████╗████████╗███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗  ██████╗██████╗  ██████╗ ██████╗ 
# ██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗
# ██████╔╝██║   ██║███████╗   ██║   ███████╗███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝██║     ██████╔╝██║   ██║██████╔╝
# ██╔═══╝ ██║   ██║╚════██║   ██║   ╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██╗██║     ██╔══██╗██║   ██║██╔═══╝ 
# ██║     ╚██████╔╝███████║   ██║   ███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║╚██████╗██║  ██║╚██████╔╝██║     
# ╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                                              



from PIL import Image
import numpy as np
import math
import torch

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def calculate_image_dimensions(megapixels, aspect_ratio):
    total_pixels = megapixels * 1048576  # Using 1024 * 1024 for precise megapixel calculation
    height = math.sqrt(total_pixels / aspect_ratio)
    width = aspect_ratio * height
    return int(width), int(height)

class PostSamplerCrop:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "image": ("IMAGE", ),
            "target_aspect_ratio": ("FLOAT", {"default": 1.00, "min": 0.25, "max": 3.00, "step": 0.01}),
            "target_megapixels": ("FLOAT", {"default": 1.00, "min": 0.10, "max": 30.00, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
        }}

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("crop_image", )
    FUNCTION = "post_sampler_crop"
    CATEGORY = "👑 MokkaBoss1/Image"

    def post_sampler_crop(self, image, target_aspect_ratio, target_megapixels, x_offset, y_offset):
        image = tensor2pil(image)
        
        if not image or image.size == (0, 0):
            raise ValueError("Input image is empty")

        input_width, input_height = image.size
        
        # Calculate target dimensions based on aspect ratio
        if input_width / input_height > target_aspect_ratio:
            # Image is too wide
            new_width = int(target_aspect_ratio * input_height)
            new_height = input_height
        else:
            # Image is too tall
            new_height = int(input_width / target_aspect_ratio)
            new_width = input_width

        # Compute the cropping coordinates centered on the image with offsets
        left = (input_width - new_width) // 2 + x_offset
        top = (input_height - new_height) // 2 + y_offset
        right = left + new_width
        bottom = top + new_height

        # Ensure the crop coordinates are within the image bounds
        left = max(0, min(input_width - new_width, left))
        top = max(0, min(input_height - new_height, top))
        right = min(input_width, left + new_width)
        bottom = min(input_height, top + new_height)

        # Crop to the target aspect ratio
        crop_image = image.crop((left, top, right, bottom))
        
        # Calculate the dimensions for the target megapixels
        target_width, target_height = calculate_image_dimensions(target_megapixels, target_aspect_ratio)

        # Resize to the target megapixels
        crop_image = crop_image.resize((target_width, target_height), Image.LANCZOS)

        # Convert back to tensor
        crop_image = pil2tensor(crop_image)

        return (crop_image, )

NODE_CLASS_MAPPINGS = {"PostSamplerCrop": PostSamplerCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"PostSamplerCrop": "👑 Post Sampler Crop"}
