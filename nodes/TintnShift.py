import torch
import numpy as np
from PIL import Image, ImageDraw, ImageStat, ImageFilter

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 

def get_color_values(color, color_hex, color_mapping):
    
    #Get RGB values for the text and background colors.

    if color == "custom":
        color_rgb = hex_to_rgb(color_hex)
    else:
        color_rgb = color_mapping.get(color, (0, 0, 0))  # Default to black if the color is not found

    return color_rgb 

def hex_to_rgb(color_hex):
    # Remove the hash at the beginning if it's there
    color_hex = color_hex.lstrip('#')

    # Convert the hex to RGB
    rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

    return rgb


#---------------------------------------------------------------------------------------------------------------------#
# Based on Color Tint node by hnmr293
class TintnShift:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        #tints = COLORS.append('sepia')
        
        tints = ["custom", "white", "black", "sepia", "red", "green", "blue",
            "cyan", "magenta", "yellow", "purple", "orange", "warm",
            "cool",  "lime", "navy", "vintage", "rose", "teal",
            "maroon", "peach", "lavender", "olive"]
           
        return {
            "required": {"image": ("IMAGE",),
                         "strength": ("FLOAT", {"default": 1.0,"min": 0.01,"max": 1.0,"step": 0.01}),
                         "mode": (tints,),
                         "x_offset": ("INT", {"default": 0, "min": -1000, "max": 1000}),
                         "y_offset": ("INT", {"default": 0, "min": -1000, "max": 1000}),
                        },
            "optional": {"tint_color_hex": ("STRING", {"multiline": False, "default": "#000000"}),} 
        }

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("IMAGE", )    
    FUNCTION = "color_tint_and_shift"
    CATEGORY = "👑 MokkaBoss1/Image"

    def color_tint_and_shift(self, image: torch.Tensor, strength, mode: str="sepia", tint_color_hex='#000000', x_offset=0, y_offset=0):
    
        if strength == 0:
            return (image,)
            
        # Get RGB values for the tint color  
        tint_color = get_color_values(mode, tint_color_hex, color_mapping)    
        color_rgb = tuple([value / 255 for value in tint_color])
        
        sepia_weights = torch.tensor([0.2989, 0.5870, 0.1140]).view(1, 1, 1, 3).to(image.device)
        
        mode_filters = {
            "custom": torch.tensor([color_rgb[0], color_rgb[1], color_rgb[2]]),
            "white": torch.tensor([1, 1, 1]),
            "black": torch.tensor([0, 0, 0]),
            "sepia": torch.tensor([1.0, 0.8, 0.6]),
            "red": torch.tensor([1.0, 0.6, 0.6]),
            "green": torch.tensor([0.6, 1.0, 0.6]),
            "blue": torch.tensor([0.6, 0.8, 1.0]),
            "cyan": torch.tensor([0.6, 1.0, 1.0]),
            "magenta": torch.tensor([1.0, 0.6, 1.0]),
            "yellow": torch.tensor([1.0, 1.0, 0.6]),
            "purple": torch.tensor([0.8, 0.6, 1.0]),
            "orange": torch.tensor([1.0, 0.7, 0.3]),
            "warm": torch.tensor([1.0, 0.9, 0.7]),
            "cool": torch.tensor([0.7, 0.9, 1.0]),
            "lime": torch.tensor([0.7, 1.0, 0.3]),
            "navy": torch.tensor([0.3, 0.4, 0.7]),
            "vintage": torch.tensor([0.9, 0.85, 0.7]),
            "rose": torch.tensor([1.0, 0.8, 0.9]),
            "teal": torch.tensor([0.3, 0.8, 0.8]),
            "maroon": torch.tensor([0.7, 0.3, 0.5]),
            "peach": torch.tensor([1.0, 0.8, 0.6]),
            "lavender": torch.tensor([0.8, 0.6, 1.0]),
            "olive": torch.tensor([0.6, 0.7, 0.4]),
        }

        scale_filter = mode_filters[mode].view(1, 1, 1, 3).to(image.device)

        grayscale = torch.sum(image * sepia_weights, dim=-1, keepdim=True)
        tinted = grayscale * scale_filter

        result = tinted * strength + image * (1 - strength)
        
        # Create PIL image to shift it
        pil_image = tensor2pil(result)
        width, height = pil_image.size
        shifted_image = Image.new("RGB", (width, height), (0, 0, 0))
        shifted_image.paste(pil_image, (x_offset, y_offset))
        
        # Convert back to tensor
        result = pil2tensor(shifted_image)
        
                
        return (result, ) 


NODE_CLASS_MAPPINGS = {"TintnShift": TintnShift}
NODE_DISPLAY_NAME_MAPPINGS = {"TintnShift": "👑 TintnShift"}           



color_mapping = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (160, 85, 15),
    "gray": (128, 128, 128),
    "lightgray": (211, 211, 211),
    "darkgray": (102, 102, 102),
    "olive": (128, 128, 0),
    "lime": (0, 128, 0),
    "teal": (0, 128, 128),
    "navy": (0, 0, 128),
    "maroon": (128, 0, 0),
    "fuchsia": (255, 0, 128),
    "aqua": (0, 255, 128),
    "silver": (192, 192, 192),
    "gold": (255, 215, 0),
    "turquoise": (64, 224, 208),
    "lavender": (230, 230, 250),
    "violet": (238, 130, 238),
    "coral": (255, 127, 80),
    "indigo": (75, 0, 130),    
}

COLORS = ["custom", "white", "black", "red", "green", "blue", "yellow",
          "cyan", "magenta", "orange", "purple", "pink", "brown", "gray",
          "lightgray", "darkgray", "olive", "lime", "teal", "navy", "maroon",
          "fuchsia", "aqua", "silver", "gold", "turquoise", "lavender",
          "violet", "coral", "indigo"]
