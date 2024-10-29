# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


#  ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗██╗███╗   ██╗████████╗███████╗ ██████╗ ███████╗██████╗ 
# ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║╚══██╔══╝██╔════╝██╔════╝ ██╔════╝██╔══██╗
# ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   ██║██╔██╗ ██║   ██║   █████╗  ██║  ███╗█████╗  ██████╔╝
# ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██║   ██║██╔══╝  ██╔══██╗
# ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   ██║██║ ╚████║   ██║   ███████╗╚██████╔╝███████╗██║  ██║
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                     


import random
import re

class ConnectInteger2:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_int1": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "i_int2": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "i_int3": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "i_int4": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "i_int5": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),
            "i_int6": ("INT", {"default": 1, "min": 1, "max": 99999999, "step": 1}),

        }}

    RETURN_TYPES = ("INT","INT","INT","INT","INT","INT",)
    RETURN_NAMES = ("o_int1","o_int2","o_int3","o_int4","o_int5","o_int6",)
    FUNCTION = "con_int2"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_int2(self, i_int1, i_int2, i_int3, i_int4, i_int5, i_int6, documentation): 
        o_int1 = i_int1
        o_int2 = i_int2
        o_int3 = i_int3
        o_int4 = i_int4
        o_int5 = i_int5
        o_int6 = i_int6
        
        return (o_int1, o_int2, o_int3, o_int4, o_int5, o_int6, )

NODE_CLASS_MAPPINGS = {"ConnectInteger2": ConnectInteger2}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectInteger2": "👑 ConnectInteger2"}
