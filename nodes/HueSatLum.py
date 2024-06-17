import torch
from PIL import Image
import numpy as np
import colorsys

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class HueSatLum:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
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

        return {
            "required": {
                "aspectRatio": ([
                    "9:21 640x1536  (0.42)",
                    "9:19 704x1472  (0.48)",
                    "9:16 768x1344  (0.57)",
                    "5:8  768x1216  (0.63)",
                    "2:3  832x1216  (0.68)",
                    "3:4  896x1152  (0.78)",
                    "1:1  1024x1024 (1.00)",
                    "4:3  1152x896  (1.29)",
                    "3:2  1216x832  (1.46)",
                    "8:5  1216x768  (1.58)",
                    "16:9 1344x768  (1.75)",
                    "19:9 1472x704  (2.09)",
                    "21:9 1536x640  (2.40)"
                ],),
                "width": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "height": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "hue_preset": ((colors_list), ),
                "custom_hue": ("INT", {"default": 0, "min": 0, "max": 360}),
                "saturation": ("INT", {"default": 50, "min": 0, "max": 100}),
                "luminosity": ("INT", {"default": 50, "min": 0, "max": 100}),
                "megapixels": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 50.0})
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "INT", "INT", "FLOAT")
    RETURN_NAMES = ("final_image", "hex_color", "Width", "Height", "Ratio")
    FUNCTION = "consolidated_func"
    CATEGORY = "👑 MokkaBoss1/Image"

    def consolidated_func(self, aspectRatio, width, height, hue_preset, custom_hue, saturation, luminosity, megapixels):
        # Aspect Ratio Handling
        aspect_ratios = {
            "1:1  1024x1024 (1.00)": (1024, 1024),
            "2:3  832x1216  (0.68)": (832, 1216),
            "3:4  896x1152  (0.78)": (896, 1152),
            "5:8  768x1216  (0.63)": (768, 1216),
            "9:16 768x1344  (0.57)": (768, 1344),
            "9:19 704x1472  (0.48)": (704, 1472),
            "9:21 640x1536  (0.42)": (640, 1536),
            "3:2  1216x832  (1.46)": (1216, 832),
            "4:3  1152x896  (1.29)": (1152, 896),
            "8:5  1216x768  (1.58)": (1216, 768),
            "16:9 1344x768  (1.75)": (1344, 768),
            "19:9 1472x704  (2.09)": (1472, 704),
            "21:9 1536x640  (2.40)": (1536, 640)
        }

        if width != 0 and height != 0:
            ratio = round(float(width / height), 3)
        else:
            width, height = aspect_ratios[aspectRatio]
            ratio = round(float(width / height), 3)

        # Color Handling
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

        hue_value = colors_dict[hue_preset]

        if custom_hue != 0:
            hue_value = custom_hue

        hue_degrees = hue_value / 360.0
        saturation_value = saturation / 100.0
        luminosity_value = luminosity / 100.0

        r, g, b = colorsys.hls_to_rgb(hue_degrees, luminosity_value, saturation_value)
        hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

        image = Image.new("RGB", (width, height), color=(int(r * 255), int(g * 255), int(b * 255)))
        image_tensor = pil2tensor(image)

        # Image resizing based on megapixels
        if megapixels > 0.0:
            original_width, original_height = image.size
            original_megapixels = (original_width * original_height) / 1048576

            scale_factor = (megapixels / original_megapixels) ** 0.5

            # Ensure the new dimensions are within reasonable bounds
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)

            new_width = max(1, min(new_width, 10000))
            new_height = max(1, min(new_height, 10000))

            image = image.resize((new_width, new_height), Image.ANTIALIAS)
        
        final_image = pil2tensor(image)
        return (final_image, hex_color, width, height, ratio)

NODE_CLASS_MAPPINGS = {
    "HueSatLum": HueSatLum
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "HueSatLum": "👑 HueSatLum"
}
