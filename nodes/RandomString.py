# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

options = [
    "random number",
    "random hexadecimal",
    "random ascii code",
    "random ascii & number"
]

class RandomString:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "option": (options,),
            "digits": ("INT", {"default": 1, "min": 1, "max": 12, "step": 1}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("o_string",)
    FUNCTION = "ran_string"
    CATEGORY = "👑 MokkaBoss1/Other"

    def ran_string(self, option, digits, seed):
        if option == "random number":
            o_string = ''.join(random.choices('0123456789', k=digits))
        elif option == "random hexadecimal":
            o_string = ''.join(random.choices('0123456789abcdef', k=digits))
        elif option == "random ascii code":
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            o_string = ''.join(random.choices(chars, k=digits))
        elif option == "random ascii & number":
            chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            o_string = ''.join(random.choices(chars, k=digits))
        else:
            o_string = ""

        return (o_string,)

NODE_CLASS_MAPPINGS = {"RandomString": RandomString}
NODE_DISPLAY_NAME_MAPPINGS = {"RandomString": "👑 RandomString"}


