from PIL import Image
import numpy as np
import torch

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ImageDimensionsBatch:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "image": ("INT", {"default": 1, "min": 1, "max": 100}),
            "i_image": ("IMAGE", )
        }}

    RETURN_TYPES = ("IMAGE", "INT", "INT", "FLOAT", "FLOAT", "STRING")  
    RETURN_NAMES = ("o_image", "width", "height", "ratio", "megapixels", "parameters")
    FUNCTION = "sel_image"
    CATEGORY = "👑 MokkaBoss1/Other"

    def sel_image(self, i_image, image):
        print(f"Received image batch: {i_image}")
        print(f"Selected image index: {image}")

        # Convert input batch of tensors to a list of PIL images
        pil_images = [tensor2pil(img) for img in i_image]

        # Ensure the image index is valid
        num_images = len(pil_images)
        if image > num_images:
            selected_image = pil_images[0]  # Select the first image if index is out of range
        else:
            selected_image = pil_images[image - 1]  # Select the specified image (1-based index)

        # Convert the selected PIL image back to tensor
        o_image = pil2tensor(selected_image)
        
        width, height = selected_image.size  # Get the width and height of the image
        ratio = round((width / height), 3)
        megapixels = round(((width * height) / 1048576), 3)
        parameters = f"Width: {width}\nHeight: {height}\nAspect Ratio: {ratio}\nMegapixels: {megapixels}"
        
        

        return (o_image, width, height, ratio, megapixels, parameters)

NODE_CLASS_MAPPINGS = {"ImageDimensionsBatch": ImageDimensionsBatch}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageDimensionsBatch": "👑 ImageDimensionsBatch"}
