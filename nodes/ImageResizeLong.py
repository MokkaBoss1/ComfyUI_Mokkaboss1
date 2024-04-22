from PIL import Image
import numpy as np
import torch

def tensor2pil(image):
    # Convert PyTorch tensor to PIL image, assuming image is scaled between 0 and 1
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    # Convert PIL image to PyTorch tensor, scale it to 0-1
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ImageResizeLong:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "subject_image": ("IMAGE", ),
            "background_image": ("IMAGE", ),
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "resize"
    CATEGORY = "👑 MokkaBoss1/Image"

    def resize(self, subject_image, background_image):
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
        # We need to maintain aspect ratio, so compute scale factor for both dimensions and use the smallest
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
        return (subject_image_return,)

NODE_CLASS_MAPPINGS = {"ImageResizeLong": ImageResizeLong}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageResizeLong": "👑 ImageResizeLong"}
