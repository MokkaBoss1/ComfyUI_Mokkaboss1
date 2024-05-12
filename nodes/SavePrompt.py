# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

import random
import re

class SavePrompt:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "positive_prompt": ("STRING", {"default": "", "ForceInput": True}),
            "negative_prompt": ("STRING", {"default": "", "ForceInput": True}),
            "model_name": ("STRING", {"default": "", "ForceInput": True}),
            "sampler_name": ("STRING", {"default": "", "ForceInput": True}),
            "scheduler_name": ("STRING", {"default": "", "ForceInput": True}),
            "steps": ("INT", {"ForceInput": True}),
            "cfg": ("FLOAT", {"ForceInput": True}),
            "width": ("INT", {"ForceInput": True}),
            "height": ("INT", {"ForceInput": True}),
            "seed": ("INT", {"ForceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("save_string",)
    FUNCTION = "SavePrompt"
    CATEGORY = "👑 MokkaBoss1/Other"

    def SavePrompt(self, positive_prompt, negative_prompt, model_name, sampler_name, scheduler_name, steps, cfg, width, height, seed): 
        ar = round(float(width) / float(height), 3)
        mp = round(float(width) * float(height) / (1024 * 1024), 3)
        part1 = f"Positive Prompt\n{positive_prompt}\n\nNegative Prompt\n{negative_prompt}\n\n"
        part2 = f"Dimensions\nWidth: {width}\nHeight: {height}\nAspect Ratio: {ar}\nMegapixels: {mp}\n\n"
        part3 = f"Generation Parameters\nModel Name: {model_name}\nSampler Name: {sampler_name}\nScheduler: {scheduler_name}\nSteps: {steps}\nCfg: {cfg}\nSeed: {seed}"
        save_string = part1 + part2 + part3
        
        return (save_string, )

NODE_CLASS_MAPPINGS = {"SavePrompt": SavePrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"SavePrompt": "👑 SavePrompt"}
