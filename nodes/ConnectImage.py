# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

from PIL import Image, ImageDraw
import numpy as np
import torch
import colorsys

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
        # Convert tensor back to PIL image if it is not already in that format
        if isinstance(i_image, torch.Tensor):
            i_image = Image.fromarray((i_image.squeeze().numpy() * 255).astype(np.uint8))

        # Calculate new dimensions if megapixels is greater than 0
        if megapixels > 0.0:
            original_width, original_height = i_image.size
            original_megapixels = (original_width * original_height) / 1048576
            
            # Calculate the scale factor
            scale_factor = (megapixels / original_megapixels) ** 0.5
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            
            # Resize the image
            i_image = i_image.resize((new_width, new_height), Image.ANTIALIAS)

        # Convert the resized image back to a tensor
        o_image = pil2tensor(i_image)
        return (o_image, )

NODE_CLASS_MAPPINGS = {"ConnectImage": ConnectImage}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectImage": "👑 ConnectImage"}
