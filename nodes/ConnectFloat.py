# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class ConnectFloat:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_float": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 99999999.0, "step": 0.01}),
        }}

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("o_float",)
    FUNCTION = "con_float"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_float(self, i_float, documentation): 
        o_float = i_float
        return (o_float, )

NODE_CLASS_MAPPINGS = {"ConnectFloat": ConnectFloat}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectFloat": "👑 ConnectFloat"}
