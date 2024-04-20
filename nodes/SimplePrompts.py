# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class SimplePrompts:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "pos_prompt": ("STRING", {"default": "# Positive Prompt #", "multiline": True}),
            "neg_prompt": ("STRING", {"default": "# Negative Prompt #", "multiline": True}),
        }}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("pos_prompt", "neg_prompt",)
    FUNCTION = "simple_prompts"
    CATEGORY = "👑 MokkaBoss1/Text"

    def simple_prompts(self, pos_prompt, neg_prompt): 
        
        pattern = r"#(.*?)#"
        clean_text = re.sub(pattern, '', pos_prompt)
        clean_text2 = clean_text.replace("\n", "")
        pos_prompt = clean_text2
        clean_text = re.sub(pattern, '', neg_prompt)
        clean_text2 = clean_text.replace("\n", "")
        neg_prompt = clean_text2
        
        
        return (pos_prompt, neg_prompt, )

NODE_CLASS_MAPPINGS = {"SimplePrompts": SimplePrompts}
NODE_DISPLAY_NAME_MAPPINGS = {"SimplePrompts": "👑 SimplePrompts"}
