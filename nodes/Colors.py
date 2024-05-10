# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

#  ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
# ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
# ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
# ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
# ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
#  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                  
# Define color dictionary without duplicates

colors_dict = {
    "Black (H0,S0,L0)": "#000000",
    "Dark Grey (H0,S0,L20)": "#333333",
    "Medium Grey (H0,S0,L40)": "#666666",
    "Light Grey (H0,S0,L60)": "#999999",
    "White (H0,S0,L100)": "#FFFFFF",
    "Bright Red (H0,S67,L67)": "#FF4040",
    "Bright Orange (H18,S67,L67)": "#FF9C40",
    "Bright Amber (H36,S67,L67)": "#FFDF40",
    "Bright Yellow (H54,S67,L67)": "#DFFF40",
    "Bright Green (H72,S67,L67)": "#40FF40",
    "Bright Emerald (H90,S67,L67)": "#40FF80",
    "Bright Turquoise (H108,S67,L67)": "#40FFDF",
    "Bright Sky Blue (H126,S67,L67)": "#40DFFF",
    "Bright Cornflower Blue (H144,S67,L67)": "#4080FF",
    "Bright Royal Blue (H162,S67,L67)": "#4040FF",
    "Bright Deep Indigo (H180,S67,L67)": "#8040FF",
    "Bright Violet (H198,S67,L67)": "#DF40FF",
    "Bright Magenta (H216,S67,L67)": "#FF40FF",
    "Bright Deep Pink (H234,S67,L67)": "#FF40DF",
    "Bright Rose (H252,S67,L67)": "#FF4080",
    "Sunrise Red (H270,S67,L67)": "#CC3333",
    "Sunset Orange (H288,S67,L67)": "#CC6A33",
    "Amber (H306,S67,L67)": "#CCAA33",
    "Sunflower Yellow (H324,S67,L67)": "#99CC33",
    "Lawn Green (H342,S67,L67)": "#66CC33",
    "Sunrise Red (H0,S67,L33)": "#CC3333",
    "Sunset Orange (H18,S67,L33)": "#CC6A33",
    "Amber (H36,S67,L33)": "#CCAA33",
    "Sunflower Yellow (H54,S67,L33)": "#99CC33",
    "Lawn Green (H72,S67,L33)": "#66CC33",
    "Emerald Green (H90,S67,L33)": "#33CC33",
    "Turquoise (H108,S67,L33)": "#33CC66",
    "Sky Blue (H126,S67,L33)": "#33CC99",
    "Cornflower Blue (H144,S67,L33)": "#3399CC",
    "Royal Blue (H162,S67,L33)": "#3366CC",
    "Deep Indigo (H180,S67,L33)": "#3333CC",
    "Violet (H198,S67,L33)": "#6633CC",
    "Magenta (H216,S67,L33)": "#9933CC",
    "Deep Pink (H234,S67,L33)": "#CC33CC",
    "Rose (H252,S67,L33)": "#CC3399",
    "Bright Red (H270,S67,L33)": "#CC3333",
    "Bright Orange (H288,S67,L33)": "#CC6A33",
    "Bright Amber (H306,S67,L33)": "#CCAA33",
    "Bright Yellow (H324,S67,L33)": "#99CC33",
    "Bright Green (H342,S67,L33)": "#66CC33"
}

# Define color list
colors_list = list(colors_dict.keys())

class Colors:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "color": (colors_list, ),
        }}

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("hex_color", )
    FUNCTION = "Colors"
    CATEGORY = "👑 MokkaBoss1/Image"

    def Colors(self, color):
        # Direct dictionary lookup
        hex_color = colors_dict.get(color, None)
        return (hex_color,)

# Node class mappings
NODE_CLASS_MAPPINGS = {"Colors": Colors}
NODE_DISPLAY_NAME_MAPPINGS = {"Colors": "👑 Colors"}
