# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ██████╗  ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
# ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██║██╔████╔██║███████║██║  ███╗█████╗      ██████╔╝██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝
# ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██╔══██╗██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗
# ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██████╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
# ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                            
from PIL import Image, ImageDraw
import numpy as np
import torch
import colorsys

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class imageborder:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "hexcolor": ("STRING", {"default": "#FFFFFF", "multiline": False}),
            "border_width": ("INT", {"default": 20, "min": 0, "max": 1000}),
            "i_image": ("IMAGE", )
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("o_image",)
    FUNCTION = "image_border"
    CATEGORY = "👑 MokkaBoss1/Other"

    def image_border(self, i_image, border_width, hexcolor):         
        # Convert tensor image to PIL image
        temp_image = tensor2pil(i_image)
        
        # Calculate new size
        width, height = temp_image.size
        new_width = width + 2 * border_width
        new_height = height + 2 * border_width
        
        # Create new image with border
        bordered_image = Image.new("RGB", (new_width, new_height), hexcolor)
        bordered_image.paste(temp_image, (border_width, border_width))
        
        # Convert back to tensor
        o_image = pil2tensor(bordered_image)
        
        return (o_image, )

NODE_CLASS_MAPPINGS = {"imageborder": imageborder}
NODE_DISPLAY_NAME_MAPPINGS = {"imageborder": "👑 Image Border"}

