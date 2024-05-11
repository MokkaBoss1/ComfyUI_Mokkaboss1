# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

#      ██╗ ██████╗ ██╗███╗   ██╗██╗███╗   ███╗ █████╗  ██████╗ ███████╗███████╗
#      ██║██╔═══██╗██║████╗  ██║██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔════╝
#      ██║██║   ██║██║██╔██╗ ██║██║██╔████╔██║███████║██║  ███╗█████╗  ███████╗
# ██   ██║██║   ██║██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ╚════██║
# ╚█████╔╝╚██████╔╝██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗███████║
#  ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                                                                                       
from PIL import Image, ImageDraw
import numpy as np
import torch
import colorsys

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

join_type_list = ["horizontal", "vertical"]

class FuseImages:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "join_type": (join_type_list, ),
            "image1": ("IMAGE", ),
            "image2": ("IMAGE", ),
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "JoinImgages"
    CATEGORY = "👑 MokkaBoss1/Image"

    def JoinImgages(self, image1, image2, join_type):
        # Convert tensors back to PIL images if they are not already in that format
        if isinstance(image1, torch.Tensor):
            image1 = Image.fromarray((image1.squeeze().numpy() * 255).astype(np.uint8))
        if isinstance(image2, torch.Tensor):
            image2 = Image.fromarray((image2.squeeze().numpy() * 255).astype(np.uint8))

        # Determine dimensions for the new image
        if join_type == "horizontal":
            new_width = image1.width + image2.width
            new_height = max(image1.height, image2.height)
        else:  # vertical
            new_width = max(image1.width, image2.width)
            new_height = image1.height + image2.height

        # Create a new image with the appropriate dimensions
        new_image = Image.new("RGB", (new_width, new_height))

        # Paste the images into the new image
        if join_type == "horizontal":
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (image1.width, 0))
        else:  # vertical
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (0, image1.height))

        # Convert the combined image to a tensor
        output_image = pil2tensor(new_image)

        return (output_image,)
		
NODE_CLASS_MAPPINGS = {"FuseImages": FuseImages}
NODE_DISPLAY_NAME_MAPPINGS = {"FuseImages": "👑 FuseImages"}

