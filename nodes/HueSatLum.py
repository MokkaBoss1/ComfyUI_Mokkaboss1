# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import colorsys

colors_dict = {
    "Red (0)": 0,
    "Red-Orange (15)": 15,
    "Orange (30)": 30,
    "Orange-Yellow (45)": 45,
    "Yellow (60)": 60,
    "Lime (75)": 75,
    "Yellow-Green (90)": 90,
    "Spring Green (105)": 105,
    "Green (120)": 120,
    "Mint green (135)": 135,
    "Seafoam green (150)": 150,
    "Cyan (165)": 165,
    "Sky Blue (180)": 180,
    "Azure Blue (195)": 195,
    "Blue (210)": 210,
    "Cornflower Blue (225)": 225,
    "Periwinkle Blue (240)": 240,
    "Violet (255)": 255,
    "Lavender (270)": 270,
    "Magenta (285)": 285,
    "Fuchsia (300)": 300,
    "Pink (315)": 315,
    "Coral Pink (330)": 330,
    "Rose Red (345)": 345
}


colors_list = [
    "Red (0)",
    "Red-Orange (15)",
    "Orange (30)",
    "Orange-Yellow (45)",
    "Yellow (60)",
    "Lime (75)",
    "Yellow-Green (90)",
    "Spring Green (105)",
    "Green (120)",
    "Mint green (135)",
    "Seafoam green (150)",
    "Cyan (165)",
    "Sky Blue (180)",
    "Azure Blue (195)",
    "Blue (210)",
    "Cornflower Blue (225)",
    "Periwinkle Blue (240)",
    "Violet (255)",
    "Lavender (270)",
    "Magenta (285)",
    "Fuchsia (300)",
    "Pink (315)",
    "Coral Pink (330)",
    "Rose Red (345)"
]


class HueSatLum:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
			"hue": ((colors_list), ),
            "saturation": ("INT", {"default": 50, "min": 0, "max": 100}),
            "luminosity": ("INT", {"default": 50, "min": 0, "max": 100}),
		}}

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("hex_color", )
    FUNCTION = "hsl_func"
    CATEGORY = "👑 MokkaBoss1/Image"

    def hsl_func(self, hue, saturation, luminosity):

        hex_color = None
        
        # Retrieve hue value from colors_dict
        hue_value = colors_dict[hue]

        # Convert hue value to degrees
        hue_degrees = hue_value / 360.0

        # Convert saturation and luminosity to values between 0 and 1
        saturation_value = saturation / 100.0
        luminosity_value = luminosity / 100.0

        # Convert HSL to RGB
        r, g, b = colorsys.hls_to_rgb(hue_degrees, luminosity_value, saturation_value)

        # Convert RGB to hex color
        hex_color = "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

        return (hex_color,)

		
NODE_CLASS_MAPPINGS = {"HueSatLum": HueSatLum}
NODE_DISPLAY_NAME_MAPPINGS = {"HueSatLum": "👑 HueSatLum"}
