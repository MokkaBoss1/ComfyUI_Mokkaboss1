# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
# colors provided by icolorpalette.com based on the hexvalue
import colorsys

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


colors_list = [
    "Red Rubiate (0)",
    "Husky Orange (15)",
    "Beeswax Candle Orange (30)",
    "Tiki Torch Yellow (45)",
    "Tropic Canary Yellow (60)",
    "Green Caterpillar (75)",
    "Hill Lands Green (90)",
    "Skirret Green (105)",
    "Grass Green (120)",
    "Artificial Turf (135)",
    "Esmeralda Green (150)",
    "Macau Green (165)",
    "Montego Bay Blue (180)",
    "Fairy Tale Blue (195)",
    "Tufts Blue (210)",
    "Free Speech Blue (225)",
    "Early Spring Night Blue (240)",
    "Dragonlord Purple (255)",
    "Purple Rain (270)",
    "Akebi Purple (285)",
    "Ultraviolet Cryner (300)",
    "Boat Orchid Pink (315)",
    "Razzle Dazzle (330)",
    "Saffron Desires (345)"
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
