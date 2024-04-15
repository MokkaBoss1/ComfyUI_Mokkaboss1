# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import colorsys

colors_dict = {
    "Red": 0,
    "Red-Orange": 15,
    "Orange": 30,
    "Orange-Yellow": 45,
    "Yellow": 60,
    "Yellow-Green": 75,
    "Green": 90,
    "Green-Cyan": 105,
    "Cyan": 120,
    "Cyan-Blue": 135,
    "Blue": 150,
    "Blue-Violet": 165,
    "Violet": 180,
    "Violet-Magenta": 195,
    "Magenta": 210,
    "Magenta-Red": 225,
    "Rose": 240,
    "Light Pink": 255,
    "Pastel Orange": 270,
    "Peach": 285,
    "Light Yellow": 300,
    "Pale Green": 315,
    "Aquamarine": 330,
    "Turquoise": 345
}


colors_list = [
    "Red",
    "Red-Orange",
    "Orange",
    "Orange-Yellow",
    "Yellow",
    "Yellow-Green",
    "Green",
    "Green-Cyan",
    "Cyan",
    "Cyan-Blue",
    "Blue",
    "Blue-Violet",
    "Violet",
    "Violet-Magenta",
    "Magenta",
    "Magenta-Red",
    "Rose",
    "Light Pink",
    "Pastel Orange",
    "Peach",
    "Light Yellow",
    "Pale Green",
    "Aquamarine",
    "Turquoise"
]


class HSL:

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

		
NODE_CLASS_MAPPINGS = {"HSL": HSL}
NODE_DISPLAY_NAME_MAPPINGS = {"HSL": "👑 HSL"}
