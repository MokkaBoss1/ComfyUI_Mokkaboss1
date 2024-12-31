# Removed unused imports
# import random
# import re

formulae = [
    'c+(a-b)/2',
    'c+(a+b)/2',
    'a*b',
    'a/b',
    'a*b+c',
    'a*b/c',
    'a/b*c',    
    'a+b+c',
    'a-b-c',
    'a*b*c',
]

class FloatEvaluate:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 1.0, "min": 0.001, "max": 99999999.000, "step": 0.0000001, "forceInput": False}),
                "b": ("FLOAT", {"default": 1.0, "min": 0.001, "max": 99999999.000, "step": 0.0000001, "forceInput": False}),
                "c": ("FLOAT", {"default": 1.0, "min": 0.001, "max": 99999999.000, "step": 0.0000001, "forceInput": False}),
                "formula": ((formulae), ),
            }
        }

    RETURN_TYPES = ("INT", "STRING", "FLOAT")
    RETURN_NAMES = ("output_int", "output_string", "output_float",)
    FUNCTION = "ave_int"
    CATEGORY = "👑 MokkaBoss1/Other"

    def ave_int(self, a, b, c, formula):
        if formula == 'c+(a-b)/2':
            output = c + (a - b) / 2
        elif formula == 'c+(a+b)/2':
            output = c + (a + b) / 2
        elif formula == 'a*b':
            output = a * b
        elif formula == 'a/b':
            output = a / b
        elif formula == 'a*b+c':
            output = a * b + c
        elif formula == 'a*b/c':
            output = (a * b) / c
        elif formula == 'a/b*c':
            output = (a / b) * c
        elif formula == 'a+b+c':
            output = a + b + c
        elif formula == 'a-b-c':
            output = a - b - c
        elif formula == 'a*b*c':
            output = a * b * c
        else:
            raise ValueError("Invalid formula provided.")
            
        output_int = int(output)
        output_string = str(output)
        output_float = float(output)
        
        return output_int, output_string, output_float

NODE_CLASS_MAPPINGS = {"FloatEvaluate": FloatEvaluate}
NODE_DISPLAY_NAME_MAPPINGS = {"FloatEvaluate": "👑 FloatEvaluate"}
