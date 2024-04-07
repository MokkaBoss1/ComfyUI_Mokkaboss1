# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class ConnectImage:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "documentation": ("STRING", {"default": "Documentation", "multiline": True}),
            "i_image": ("IMAGE", )
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("o_image",)
    FUNCTION = "con_image"
    CATEGORY = "👑 MokkaBoss1/Other"

    def con_image(self, i_image, documentation):         
        o_image = i_image
        return (o_image, )

NODE_CLASS_MAPPINGS = {"ConnectImage": ConnectImage}
NODE_DISPLAY_NAME_MAPPINGS = {"ConnectImage": "👑 ConnectImage"}
