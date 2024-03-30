# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
import random

urban_colours_dict = {
    "Asphalt Black": "#130F0F",
    "Bicycle Rack Gray": "#808080",
    "Brick Red": "#8B0000",
    "Bus Shelter Gray": "#A9A9A9",
    "Bus Stop Pole Gray": "#808080",
    "Bus Stop Sign Red": "#B22222",
    "Bus Stop Sign White": "#FFFFFF",
    "Concrete Barrier Gray": "#D3D3D3",
    "Concrete Gray": "#A9A9A9",
    "Construction Site Yellow": "#FFD700",
    "Crosswalk White": "#FFFFFF",
    "Hard Hat White": "#F0F0F0",
    "Metal Fence Gray": "#696969",
    "Neon Blue": "#00FFFF",
    "Neon Cyan": "#00FFFF",
    "Neon Green": "#39FF14",
    "Neon Lime": "#BFFF00",
    "Neon Magenta": "#FF00FF",
    "Neon Orange": "#FFA500",
    "Neon Pink": "#FF6EC7",
    "Neon Purple": "#FF00FF",
    "Neon Red": "#FF033E",
    "Neon Yellow": "#FFFF33",
    "Office Building Gray": "#A9A9A9",
    "Painted Line White": "#F5F5F5",
    "Park Bench Gray": "#808080",
    "Parking Garage Gray": "#A9A9A9",
    "Parking Lot Gray": "#A9A9A9",
    "Parking Spot White": "#FFFFFF",
    "Pedestrian Crossing Green": "#008000",
    "Pedestrian Crossing White": "#FFFFFF",
    "Road Marking White": "#F0F8FF",
    "Safety Vest Yellow": "#FFFF00",
    "Security Camera Gray": "#C0C0C0",
    "Steel Gray": "#708090",
    "Street Bench Gray": "#808080",
    "Street Light Yellow": "#FFD700",
    "Street Sign Green": "#008000",
    "Street Sign White": "#FFFFFF",
    "Traffic Cone Orange": "#FFA500",
    "Traffic Light Green": "#008000",
    "Traffic Light Red": "#FF0000",
    "Traffic Light Yellow": "#FFFF00",
    "Trash Can Gray": "#808080",
    "Utility Pole Brown": "#8B4513",
    "Warning Sign Yellow": "#FFCC00",
    "Wire Fence Gray": "#808080"
}

urban_colours_list = [
    "Asphalt Black",
    "Bicycle Rack Gray",
    "Brick Red",
    "Bus Shelter Gray",
    "Bus Stop Pole Gray",
    "Bus Stop Sign Red",
    "Bus Stop Sign White",
    "Concrete Barrier Gray",
    "Concrete Gray",
    "Construction Site Yellow",
    "Crosswalk White",
    "Hard Hat White",
    "Metal Fence Gray",
    "Neon Blue",
    "Neon Cyan",
    "Neon Green",
    "Neon Lime",
    "Neon Magenta",
    "Neon Orange",
    "Neon Pink",
    "Neon Purple",
    "Neon Red",
    "Neon Yellow",
    "Office Building Gray",
    "Painted Line White",
    "Park Bench Gray",
    "Parking Garage Gray",
    "Parking Lot Gray",
    "Parking Spot White",
    "Pedestrian Crossing Green",
    "Pedestrian Crossing White",
    "Road Marking White",
    "Safety Vest Yellow",
    "Security Camera Gray",
    "Steel Gray",
    "Street Bench Gray",
    "Street Light Yellow",
    "Street Sign Green",
    "Street Sign White",
    "Traffic Cone Orange",
    "Traffic Light Green",
    "Traffic Light Red",
    "Traffic Light Yellow",
    "Trash Can Gray",
    "Utility Pole Brown",
    "Warning Sign Yellow",
    "Wire Fence Gray"
]


class UrbanColours:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
#			"seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
			"colour": ((urban_colours_list), ),
		}}

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("hex_colour", )
    FUNCTION = "UrbanColours"
    CATEGORY = "👑 MokkaBoss1"

    def UrbanColours(self, colour):

        hex_colour = None

        for key, value in urban_colours_dict.items():
            if key == colour:
                hex_colour = value
                break

        return (hex_colour,)
		
NODE_CLASS_MAPPINGS = {"UrbanColours": UrbanColours}
NODE_DISPLAY_NAME_MAPPINGS = {"UrbanColours": "👑 UrbanColours"}
