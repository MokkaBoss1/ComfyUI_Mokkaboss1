# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class ConnectInteger:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_int": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),

        }}

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("o_int",)
    FUNCTION = "con_int"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_int(self, i_int, documentation): 
        o_int = i_int
        return (o_int, )

NODE_CLASS_MAPPINGS = {"ConnectInteger": ConnectInteger}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectInteger": "👑 ConnectInteger"}
