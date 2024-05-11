    # https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack                                                                                                                                                      

from PIL import Image, ImageDraw
import numpy as np
import torch

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

join_type_list = ["horizontal", "vertical"]

class FuseImages2:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "join_type": (join_type_list, ),
                "required_image1": ("IMAGE", ),
                "required_image2": ("IMAGE", ),
            },
            "optional": {
                "optional_image3": ("IMAGE", ),
                "optional_image4": ("IMAGE", ),
                "optional_image5": ("IMAGE", ),
                "optional_image6": ("IMAGE", ),
                "optional_image7": ("IMAGE", ),
                "optional_image8": ("IMAGE", ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "FuseImages_two"
    CATEGORY = "👑 MokkaBoss1/Image"

    def FuseImages_two(self, required_image1, required_image2, optional_image3=None, optional_image4=None, optional_image5=None, optional_image6=None, optional_image7=None, optional_image8=None, join_type="horizontal"):
        # Convert tensors back to PIL images if they are not already in that format
        def tensor_to_pil(tensor_image):
            if isinstance(tensor_image, torch.Tensor):
                return Image.fromarray((tensor_image.squeeze().numpy() * 255).astype(np.uint8))
            return tensor_image

        required_image1 = tensor_to_pil(required_image1)
        required_image2 = tensor_to_pil(required_image2)
        optional_image3 = tensor_to_pil(optional_image3) if optional_image3 is not None else None
        optional_image4 = tensor_to_pil(optional_image4) if optional_image4 is not None else None
        optional_image5 = tensor_to_pil(optional_image5) if optional_image5 is not None else None
        optional_image6 = tensor_to_pil(optional_image6) if optional_image6 is not None else None
        optional_image7 = tensor_to_pil(optional_image7) if optional_image7 is not None else None
        optional_image8 = tensor_to_pil(optional_image8) if optional_image8 is not None else None

        images = [required_image1, required_image2, optional_image3, optional_image4, optional_image5, optional_image6, optional_image7, optional_image8]
        images = [img for img in images if img is not None]  # Remove None values

        if join_type == "horizontal":
            total_width = sum(img.width for img in images)
            max_height = max(img.height for img in images)
            new_image = Image.new("RGB", (total_width, max_height))
            x_offset = 0
            for img in images:
                new_image.paste(img, (x_offset, 0))
                x_offset += img.width
        else:  # vertical
            max_width = max(img.width for img in images)
            total_height = sum(img.height for img in images)
            new_image = Image.new("RGB", (max_width, total_height))
            y_offset = 0
            for img in images:
                new_image.paste(img, (0, y_offset))
                y_offset += img.height

        # Convert the combined image to a tensor
        output_image = pil2tensor(new_image)

        return (output_image,)
		
NODE_CLASS_MAPPINGS = {"FuseImages2": FuseImages2}
NODE_DISPLAY_NAME_MAPPINGS = {"FuseImages2": "👑 FuseImages2"}
