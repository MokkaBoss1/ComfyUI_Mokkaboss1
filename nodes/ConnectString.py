# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class ConnectString:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_string": ("STRING", {"default": "string", "multiline": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("o_string",)
    FUNCTION = "con_string"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_string(self, i_string, documentation): 
        o_string = i_string
        return (o_string, )

NODE_CLASS_MAPPINGS = {"ConnectString": ConnectString}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectString": "👑 ConnectString"}
