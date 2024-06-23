from PIL import Image, ImageDraw
import numpy as np
import torch

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ConnectImage:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "megapixels": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 50.0}),
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_image": ("IMAGE", )
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("o_image",)
    FUNCTION = "con_image"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_image(self, i_image, megapixels, documentation):         
        # Check if i_image is a batch of images
        if isinstance(i_image, torch.Tensor) and i_image.ndim == 4:
            batch_size = i_image.size(0)
            processed_images = []
            for i in range(batch_size):
                single_image = i_image[i]
                pil_image = Image.fromarray((single_image.squeeze().numpy() * 255).astype(np.uint8))
                processed_pil_image = self.process_single_image(pil_image, megapixels)
                processed_images.append(pil2tensor(processed_pil_image).squeeze(0))
            o_image = torch.stack(processed_images)
        else:
            if isinstance(i_image, torch.Tensor):
                i_image = Image.fromarray((i_image.squeeze().numpy() * 255).astype(np.uint8))
            o_image = pil2tensor(self.process_single_image(i_image, megapixels))
        return (o_image, )

    def process_single_image(self, i_image, megapixels):
        # Calculate new dimensions if megapixels is greater than 0
        if megapixels > 0.0:
            original_width, original_height = i_image.size
            original_megapixels = (original_width * original_height) / 1048576
            
            # Calculate the scale factor
            scale_factor = (megapixels / original_megapixels) ** 0.5
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            
            # Resize the image
            i_image = i_image.resize((new_width, new_height), Image.LANCZOS)
        return i_image

NODE_CLASS_MAPPINGS = {"ConnectImage": ConnectImage}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectImage": "👑 ConnectImage"}
