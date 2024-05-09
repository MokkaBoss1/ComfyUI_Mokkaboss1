# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

#██╗███╗   ██╗████████╗    ███████╗██╗   ██╗ █████╗ ██╗     ██╗   ██╗ █████╗ ████████╗███████╗
#██║████╗  ██║╚══██╔══╝    ██╔════╝██║   ██║██╔══██╗██║     ██║   ██║██╔══██╗╚══██╔══╝██╔════╝
#██║██╔██╗ ██║   ██║       █████╗  ██║   ██║███████║██║     ██║   ██║███████║   ██║   █████╗  
#██║██║╚██╗██║   ██║       ██╔══╝  ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██║   ██║   ██╔══╝  
#██║██║ ╚████║   ██║       ███████╗ ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║   ██║   ███████╗
#╚═╝╚═╝  ╚═══╝   ╚═╝       ╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                                                             
# Mokkaboss1 May 2024

import random
import re

formulae = [
    """c+(a-b)/2""",
    """c+(a+b)/2""",
    """(a*b)""",
    """(a/b)""",
    """(a*b)+c""",
    """(a*b)/c""",
    """(a+b+c)""",
    """(a-b-c)""",
    """(a*b*c)""",
    ]
class IntEvaluate:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1, "forceInput": False}),
                "b": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1, "forceInput": False}),
                "c": ("INT", {"default": 1, "min": -99999999, "max": 99999999, "step": 1, "forceInput": False}),
                "formula": ((formulae), ),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("output",)
    FUNCTION = "ave_int"
    CATEGORY = "👑 MokkaBoss1/Other"

    def ave_int(self, a, b, c, formula): 
        if formula == """c+(a-b)/2""":
            output = int(c+(a - b)/2)
        elif formula == """c+(a+b)/2""":
            output = int(c+(a+b)/2)
        elif formula == """(a*b)""":
            output = int(a*b)
        elif formula == """(a/b)""":
            output = int(a/b)
        elif formula == """(a*b)+c""":
            output = int(a*b + c)
        elif formula == """(a*b)/c""":
            output = int((a*b)/c)
        elif formula == """(a+b+c)""":
            output = int(a+b+c)
        elif formula == """(a-b-c)""":
            output = int(a-b-c)
        elif formula == """(a*b*c)""":
            output = int(a*b*c)
        else:
            output = 0
        return (output, )

NODE_CLASS_MAPPINGS = {"IntEvaluate": IntEvaluate}
NODE_DISPLAY_NAME_MAPPINGS = {"IntEvaluate": "👑 IntEvaluate"}
