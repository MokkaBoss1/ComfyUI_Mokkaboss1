# Removed unused imports
# import random
# import re

class LinEqEval:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "x_min": ("INT", {"default": 0, "min": -99999999, "max": 99999999, "step": 1, "forceInput": False}),
                "x_max": ("INT", {"default": 10, "min": -99999999, "max": 99999999, "step": 1, "forceInput": False}),
                "y_min": ("FLOAT", {"default": 0.0, "min": -99999999.0, "max": 99999999.0, "step": 0.0000001, "forceInput": False}),
                "y_max": ("FLOAT", {"default": 10.0, "min": -99999999.0, "max": 99999999.0, "step": 0.0000001, "forceInput": False}),
                "x": ("INT", {"default": 5, "min": 0, "max": 10, "step": 1, "forceInput": False}),
            }
        }

    RETURN_TYPES = ("INT", "STRING", "FLOAT")
    RETURN_NAMES = ("output_int", "output_string", "output_float",)
    FUNCTION = "Lin_EqEval"
    CATEGORY = "👑 MokkaBoss1/Other"

    def Lin_EqEval(self, x_min, x_max, y_min, y_max, x):
        # Ensure x is between x_min and x_max
        if not (x_min <= x <= x_max):
            raise ValueError(f"x should be between {x_min} and {x_max}")

        # Linear equation to calculate y
        y = y_min + ((x - x_min) * (y_max - y_min)) / (x_max - x_min)
        
        output_int = int(y)
        output_string = str(y)
        output_float = float(y)
        
        return output_int, output_string, output_float

NODE_CLASS_MAPPINGS = {"LinEqEval": LinEqEval}
NODE_DISPLAY_NAME_MAPPINGS = {"LinEqEval": "👑 LinEqEval"}
