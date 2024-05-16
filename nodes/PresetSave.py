# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██████╗ ██████╗ ███████╗███████╗███████╗████████╗███████╗ █████╗ ██╗   ██╗███████╗
# ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║   ██║██╔════╝
# ██████╔╝██████╔╝█████╗  ███████╗█████╗     ██║   ███████╗███████║██║   ██║█████╗  
# ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║   ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  
# ██║     ██║  ██║███████╗███████║███████╗   ██║   ███████║██║  ██║ ╚████╔╝ ███████╗
# ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
                                                                                  
import json
import os

class PresetSave:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "", "multiline": False}),
                "pos_prompt": ("STRING", {"default": "", "multiline": True}),
                "neg_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)  # Single return type
    RETURN_NAMES = ("prompt_summary",)  # Name the return value
    FUNCTION = "savepreset"
    CATEGORY = "👑 MokkaBoss1/Text"

    def savepreset(self, name, pos_prompt, neg_prompt):
        # Step 0: Ensure the name is not blank or only contains spaces
        if not name.strip():
            return ""
        
        preset_path = os.path.join(os.path.dirname(__file__), '../presets/presetlist.json')
        
        # Step 1: Read the json file called "presetlist.json"
        if os.path.exists(preset_path):
            with open(preset_path, 'r', encoding='utf-8') as file:
                presets = json.load(file)
        else:
            presets = []

        # Step 2: Check if there is an entry with the same name
        existing_entry = next((preset for preset in presets if preset['name'] == name), None)

        # Step 3 and 4: Add or overwrite the entry
        new_entry = {
            "name": name,
            "prompt": pos_prompt,
            "negative_prompt": neg_prompt
        }

        if existing_entry:
            existing_entry.update(new_entry)
        else:
            presets.append(new_entry)

        # Step 5: Save the updated list back to the JSON file
        with open(preset_path, 'w', encoding='utf-8') as file:
            json.dump(presets, file, indent=4)
        
        # Create the concatenated string
        prompt_summary = f"positive prompt: {pos_prompt}\nnegative prompt: {neg_prompt}"
        print (prompt_summary)
        
        # Return the concatenated string
        return (prompt_summary, )

NODE_CLASS_MAPPINGS = {"PresetSave": PresetSave}
NODE_DISPLAY_NAME_MAPPINGS = {"PresetSave": "👑 PresetSave"}

