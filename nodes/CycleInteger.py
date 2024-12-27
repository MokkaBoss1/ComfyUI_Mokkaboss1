# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

                                                                                                                 
import random
import re

class CycleInteger:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_int": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "cycle_range": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),

        }}

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("o_int",)
    FUNCTION = "cyc_int"
    CATEGORY = "👑 MokkaBoss1/Other"

    def cyc_int(self, i_int, cycle_range, documentation): 
        o_int = i_int % cycle_range
        return (o_int, )

NODE_CLASS_MAPPINGS = {"CycleInteger": CycleInteger}
NODE_DISPLAY_NAME_MAPPINGS = {"CycleInteger": "👑 CycleInteger"}
