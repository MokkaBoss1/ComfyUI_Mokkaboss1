from PIL import Image
import numpy as np
import torch
from comfy.model_management import InterruptProcessingException

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ChooseImage:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "select_image": (["required_image1", "required_image2", "optional_image3", "optional_image4", "optional_image5", "optional_image6", "optional_image7", "optional_image8", "stop workflow"], ),
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
    FUNCTION = "Choose_Image"
    CATEGORY = "👑 MokkaBoss1/Image"

    def Choose_Image(self, select_image, required_image1, required_image2, optional_image3=None, optional_image4=None, optional_image5=None, optional_image6=None, optional_image7=None, optional_image8=None):
        if select_image == "stop workflow":
            raise InterruptProcessingException()

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

        images = {
            "required_image1": required_image1,
            "required_image2": required_image2,
            "optional_image3": optional_image3,
            "optional_image4": optional_image4,
            "optional_image5": optional_image5,
            "optional_image6": optional_image6,
            "optional_image7": optional_image7,
            "optional_image8": optional_image8
        }

        # Select the image or fallback to the first image if the selected image is None
        selected_image = images.get(select_image)
        if selected_image is None:
            selected_image = required_image1

        # Convert the selected image to a tensor
        output_image = pil2tensor(selected_image)

        return (output_image,)
		
NODE_CLASS_MAPPINGS = {"ChooseImage": ChooseImage}
NODE_DISPLAY_NAME_MAPPINGS = {"ChooseImage": "👑 ChooseImage"}
