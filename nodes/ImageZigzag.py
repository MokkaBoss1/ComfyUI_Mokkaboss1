from PIL import Image, ImageDraw
import numpy as np
import torch

# functions

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def create_rect_image(hex_color, width, height):
    # Check if the hex_color is a valid hex code
    if not isinstance(hex_color, str) or not hex_color.startswith('#') or len(hex_color) not in [4, 7]:
        raise ValueError("Invalid hex color code. It should start with '#' followed by 3 or 6 hexadecimal characters.")
    
    # Convert shorthand hex code to full length
    if len(hex_color) == 4:
        hex_color = f"#{hex_color[1]*2}{hex_color[2]*2}{hex_color[3]*2}"
    
    # Create a new image with the given dimensions and color
    image = Image.new('RGB', (width, height), hex_color)
    
    return image

# main class

class ImageZigzag:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "colour1": ("STRING", {"default": "#000000", "multiline": False}),
            "colour2": ("STRING", {"default": "#FFFFFF", "multiline": False}),
            "width": ("INT", {"default": 512, "min": 32, "max": 2048}),
            "height": ("INT", {"default": 512, "min": 32, "max": 2048}),
            "amplitude": ("INT", {"default": 100, "min": 1, "max": 2048}),
            "wavenumber": ("INT", {"default": 10, "min": 1, "max": 2048}),
        }}

    RETURN_TYPES = ("IMAGE", "STRING",)
    RETURN_NAMES = ("image", "parameters",)
    FUNCTION = "Zigzagcalc"
    CATEGORY = "👑 MokkaBoss1/Image"

    def Zigzagcalc(self, colour1, colour2, width, height, amplitude, wavenumber):
        # Create base image
        base_image = create_rect_image(colour1, width, height)
        
        draw = ImageDraw.Draw(base_image)
        
        step_x = width / (wavenumber * 2)  # width of each segment
        line_thickness = height - amplitude  # thickness of the zigzag line

        points = []
        # Upper part of the zigzag
        for i in range(wavenumber * 2 + 1):
            x = i * step_x
            y = 0 if i % 2 == 0 else amplitude
            points.append((x, y))
        
        # Lower part of the zigzag
        for i in range(wavenumber * 2, -1, -1):
            x = i * step_x
            y = line_thickness if i % 2 == 0 else line_thickness + amplitude
            points.append((x, y))
        
        draw.polygon(points, fill=colour2)

        output_image = base_image
        
        parameters = f"colour1: {colour1}, colour2: {colour2}, width: {width}, height: {height}, amplitude: {amplitude}, cycles: {wavenumber}"
        image = pil2tensor(output_image)
        
        return (image, parameters)

NODE_CLASS_MAPPINGS = {"ImageZigzag": ImageZigzag}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageZigzag": "👑 ImageZigzag"}
