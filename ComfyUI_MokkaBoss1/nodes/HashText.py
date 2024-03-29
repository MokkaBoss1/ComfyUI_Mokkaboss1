# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class HashText:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "prompt": ("STRING", {"default": "prompt", "multiline": True})
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "test"
    CATEGORY = "👑 MokkaBoss1"

    def test(self, prompt): 
        pattern = r"#(.*?)#"
        clean_text = re.sub(pattern, '', prompt)
        clean_text2 = clean_text.replace("\n", "")
        prompt = clean_text2
        return (prompt, )

NODE_CLASS_MAPPINGS = {"HashText": HashText}
NODE_DISPLAY_NAME_MAPPINGS = {"HashText": "👑 HashText"}
