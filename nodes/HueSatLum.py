# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
# colors provided by icolorpalette.com based on the hexvalue

from PIL import Image, ImageDraw
import numpy as np
import torch
import colorsys

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)



colors_dict = {
    "Red Rubiate (0)": 0,
    "Husky Orange (15)": 15,
    "Beeswax Candle Orange (30)": 30,
    "Tiki Torch Yellow (45)": 45,
    "Tropic Canary Yellow (60)": 60,
    "Green Caterpillar (75)": 75,
    "Hill Lands Green (90)": 90,
    "Skirret Green (105)": 105,
    "Grass Green (120)": 120,
    "Artificial Turf (135)": 135,
    "Esmeralda Green (150)": 150,
    "Macau Green (165)": 165,
    "Montego Bay Blue (180)": 180,
    "Fairy Tale Blue (195)": 195,
    "Tufts Blue (210)": 210,
    "Free Speech Blue (225)": 225,
    "Early Spring Night Blue (240)": 240,
    "Dragonlord Purple (255)": 255,
    "Purple Rain (270)": 270,
    "Akebi Purple (285)": 285,
    "Ultraviolet Cryner (300)": 300,
    "Boat Orchid Pink (315)": 315,
    "Razzle Dazzle (330)": 330,
    "Saffron Desires (345)": 345
}

colors_list = list(colors_dict.keys())

class HueSatLum:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "hue_preset": ((colors_list), ),
            "custom_hue": ("INT", {"default": 0, "min": 0, "max": 360}),
            "saturation": ("INT", {"default": 50, "min": 0, "max": 100}),
            "luminosity": ("INT", {"default": 50, "min": 0, "max": 100}),
            "width": ("INT", {"default": 512, "min": 0, "max": 99999}),
            "height": ("INT", {"default": 512, "min": 0, "max": 99999}),
            "custom_hue": ("INT", {"default": 0, "min": 0, "max": 360}),
        }}

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("hex_color", "image")
    FUNCTION = "hsl_func"
    CATEGORY = "👑 MokkaBoss1/Image"

    def hsl_func(self, hue_preset, custom_hue, saturation, luminosity, width, height):

        hex_color = None
        
        # Retrieve hue value from colors_dict
        hue_value = colors_dict[hue_preset]

        if custom_hue != 0:
            hue_value = custom_hue

        # Convert hue value to degrees
        hue_degrees = hue_value / 360.0

        # Convert saturation and luminosity to values between 0 and 1
        saturation_value = saturation / 100.0
        luminosity_value = luminosity / 100.0

        # Convert HSL to RGB
        r, g, b = colorsys.hls_to_rgb(hue_degrees, luminosity_value, saturation_value)

        # Convert RGB to hex color
        hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

        # Generate 100x100 pixel image with the calculated color
        image = Image.new("RGB", (width, height), color=(int(r * 255), int(g * 255), int(b * 255)))

        # Convert PIL image to tensor
        image_tensor = pil2tensor(image)

        return (hex_color, image_tensor)
		
NODE_CLASS_MAPPINGS = {"HueSatLum": HueSatLum}
NODE_DISPLAY_NAME_MAPPINGS = {"HueSatLum": "👑 HueSatLum"}
