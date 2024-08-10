# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ██████╗ ██╗███╗   ███╗███████╗███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗
# ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██║████╗ ████║██╔════╝████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝
# ██║██╔████╔██║███████║██║  ███╗█████╗      ██║  ██║██║██╔████╔██║█████╗  ██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║███████╗
# ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██║  ██║██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║╚════██║
# ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██████╔╝██║██║ ╚═╝ ██║███████╗██║ ╚████║███████║██║╚██████╔╝██║ ╚████║███████║
# ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                                                                         
from PIL import Image
import numpy as np
import torch

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ImageDimensions:
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "FLOAT", "FLOAT", "STRING")
    RETURN_NAMES = ("output_image", "width", "height", "ratio", "megapixels", "kilopixels", "parameters")
    FUNCTION = "im_dim"
    CATEGORY = "👑 MokkaBoss1/Image"

    def im_dim(self, input_image):
        # Convert tensor to PIL image
        try:
            image = tensor2pil(input_image)
        except Exception as e:
            raise ValueError(f"Failed to convert tensor to PIL image: {e}")

        width, height = image.size  # Get the width and height of the image
        ratio = round((width / height), 3)
        megapixels = round(((width * height) / 1048576), 6)
        kilopixels = megapixels * 1000
        parameters = f"Width: {width}\nHeight: {height}\nAspect Ratio: {ratio}\nMegapixels: {megapixels}"

        # Convert PIL image back to tensor
        try:
            output_image = pil2tensor(image)
        except Exception as e:
            raise ValueError(f"Failed to convert PIL image to tensor: {e}")

        print ( parameters )      

        return (output_image, width, height, ratio, megapixels, kilopixels, parameters)

NODE_CLASS_MAPPINGS = {"ImageDimensions": ImageDimensions}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageDimensions": "👑 ImageDimensions"}
