# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class ConnectLatent:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_lat": ("LATENT", ),

        }}

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("o_lat",)
    FUNCTION = "con_lat"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_lat(self, i_lat, documentation): 
        o_lat = i_lat
        return (o_lat, )

NODE_CLASS_MAPPINGS = {"ConnectLatent": ConnectLatent}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectLatent": "👑 ConnectLatent"}
