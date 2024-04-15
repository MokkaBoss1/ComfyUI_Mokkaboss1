from PIL import Image
import numpy as np
import torch

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class TricolorComposition:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "input_image": ("IMAGE", ),
            "white_replace_hex": ("STRING", {"default": "FFFFFF", "multiline": False}),
            "grey_replace_hex": ("STRING", {"default": "808080", "multiline": False}),
            "black_replace_hex": ("STRING", {"default": "000000", "multiline": False}),
            "tolerance": ("INT", {"default": 30, "min": 0, "max": 255})
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "color_comp"
    CATEGORY = "👑 MokkaBoss1/Image"

    def color_comp(self, input_image, white_replace_hex, grey_replace_hex, black_replace_hex, tolerance): 
        # Remove '#' symbol if it exists
        if white_replace_hex.startswith("#"):
            white_replace_hex = white_replace_hex[1:]
        if grey_replace_hex.startswith("#"):
            grey_replace_hex = grey_replace_hex[1:]
        if black_replace_hex.startswith("#"):
            black_replace_hex = black_replace_hex[1:]

        # Convert hex color codes to RGB tuples
        white_rgb = tuple(int(white_replace_hex[i:i+2], 16) for i in (0, 2, 4))
        black_rgb = tuple(int(black_replace_hex[i:i+2], 16) for i in (0, 2, 4))
        grey_rgb = tuple(int(grey_replace_hex[i:i+2], 16) for i in (0, 2, 4))

        # Convert tensor to PIL image
        image_pil = tensor2pil(input_image)

        # Replace colors
        pixels = image_pil.load()
        width, height = image_pil.size
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                r, g, b = pixel
                # Check if the pixel color is within the tolerance level of white or black
                if r >= (255 - tolerance) and g >= (255 - tolerance) and b >= (255 - tolerance):
                    pixels[x, y] = white_rgb
                elif r <= tolerance and g <= tolerance and b <= tolerance:
                    pixels[x, y] = black_rgb
                # Check if the pixel color is closer to grey than white or black
                elif abs(r - g) <= tolerance and abs(g - b) <= tolerance and abs(b - r) <= tolerance:
                    pixels[x, y] = grey_rgb

        # Convert PIL image back to tensor
        output_image = pil2tensor(image_pil)

        # Return the modified image
        return (output_image,)

NODE_CLASS_MAPPINGS = {"TricolorComposition": TricolorComposition}
NODE_DISPLAY_NAME_MAPPINGS = {"TricolorComposition": "👑 TricolorComposition"}
