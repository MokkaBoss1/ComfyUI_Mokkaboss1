#https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
import random

nature_colors_dict = {
    "Sky Blue": "#87CEEB",
    "Ocean Blue": "#1E90FF",
    "Forest Green": "#228B22",
    "Grass Green": "#7CFC00",
    "Leaf Green": "#6B8E23",
    "Sunflower Yellow": "#FFD700",
    "Sandy Brown": "#F4A460",
    "Beige": "#F5F5DC",
    "Rock Gray": "#808080",
    "Mountain Brown": "#8B4513",
    "Snow White": "#FFFAFA",
    "Cloud White": "#F5F5F5",
    "Lagoon Blue": "#00CED1",
    "Lilac Purple": "#C8A2C8",
    "Desert Sand": "#EDC9AF",
    "Rose Pink": "#FFC0CB",
    "Sunset Orange": "#FF4500",
    "Coral Pink": "#FF7F50",
    "Lavender Purple": "#E6E6FA",
    "Pine Green": "#01796F",
    "Moss Green": "#8A9A5B",
    "Fern Green": "#4F7942",
    "Clay Brown": "#8C7154",
    "Terra Cotta": "#E2725B",
    "Sand Yellow": "#E6BE8A",
    "Turquoise Blue": "#40E0D0",
    "Ocean Green": "#48BF91",
    "Crimson Red": "#DC143C",
    "Cinnamon Brown": "#CD7F32",
    "Amber Yellow": "#FFBF00"
}

nature_colors_list = [
    "Amber Yellow",
    "Beige",
    "Cinnamon Brown",
    "Clay Brown",
    "Cloud White",
    "Coral Pink",
    "Crimson Red",
    "Desert Sand",
    "Fern Green",
    "Forest Green",
    "Grass Green",
    "Lagoon Blue",
    "Lavender Purple",
    "Leaf Green",
    "Lilac Purple",
    "Moss Green",
    "Mountain Brown",
    "Ocean Blue",
    "Ocean Green",
    "Pine Green",
    "Rock Gray",
    "Rose Pink",
    "Sand Yellow",
    "Sandy Brown",
    "Sky Blue",
    "Snow White",
    "Sunflower Yellow",
    "Sunset Orange",
    "Terra Cotta",
    "Turquoise Blue"
]

class NatureColours:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
#			"seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
			"colour": ((nature_colors_list), ),
		}}

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("hex_colour", )
    FUNCTION = "NatureColours"
    CATEGORY = "👑 MokkaBoss1/Image"

    def NatureColours(self, colour):

        hex_colour = None

        for key, value in nature_colors_dict.items():
            if key == colour:
                hex_colour = value
                break

        return (hex_colour,)
		
NODE_CLASS_MAPPINGS = {"NatureColours": NatureColours}
NODE_DISPLAY_NAME_MAPPINGS = {"NatureColours": "👑 NatureColours"}
