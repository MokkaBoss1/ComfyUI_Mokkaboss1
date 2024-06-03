from PIL import Image
import numpy as np
import torch

combinations = [
    '3 x 4 = 12',
    '3 x 3 = 9',
    '2 x 6 = 12',
    '2 x 5 = 10',
    '2 x 4 = 8',
    '2 x 3 = 6',
    '2 x 2 = 4',
    '1 x 12 = 12',
    '1 x 11 = 11',
    '1 x 10 = 10',
    '1 x 9 = 9',
    '1 x 8 = 8',
    '1 x 7 = 7',
    '1 x 6 = 6',
    '1 x 5 = 5',
    '1 x 4 = 4',
    '1 x 3 = 3',
    '1 x 2 = 2',
    '1 x 1 = 1'
]

def pil2tensor(image):
    tensor = torch.from_numpy(np.array(image).astype(np.float32) / 255.0).permute(2, 0, 1)
    print(f"Converted PIL to tensor: {tensor.shape}")
    return tensor

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

class SplitImages:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "split_combination": (combinations, ),
                "image": ("IMAGE", ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image_batch",)
    FUNCTION = "SplitImages"
    CATEGORY = "👑 MokkaBoss1/Image"

    def SplitImages(self, split_combination, image):
        print(f"Input image shape: {image.shape}")
        image = tensor2pil(image)  # Convert tensor to PIL
        split_combination = split_combination.split(' x ')
        cols = int(split_combination[0])
        rows = int(split_combination[1].split(' = ')[0])
        
        img_width, img_height = image.size
        tile_width = img_width // cols
        tile_height = img_height // rows
        
        images = []
        
        for i in range(rows):
            for j in range(cols):
                left = j * tile_width
                upper = i * tile_height
                right = left + tile_width
                lower = upper + tile_height
                cropped_image = image.crop((left, upper, right, lower))
                
                # Call pil2tensor separately
                tensor_image = pil2tensor(cropped_image)
                tensor_image = tensor_image.unsqueeze(0)  # Add batch dimension
                
                print(f"Cropped image tensor shape: {tensor_image.shape}")
                images.append(tensor_image)

        # Concatenate all images along the batch dimension
        image_batch = torch.cat(images[:12], dim=0)  # Limiting to 12 images
        print(f"Output image batch shape: {image_batch.shape}")

        # Ensure all images are in the correct format
        image_batch = image_batch.permute(0, 2, 3, 1)  # Change shape to (N, H, W, C)
        image_batch = image_batch.contiguous()  # Make tensor contiguous
        print(f"Final image batch shape: {image_batch.shape}")

        return (image_batch,)

NODE_CLASS_MAPPINGS = {"SplitImages": SplitImages}
NODE_DISPLAY_NAME_MAPPINGS = {"SplitImages": "👑 SplitImages"}
