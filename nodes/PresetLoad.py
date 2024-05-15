# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ██████╗ ██████╗ ███████╗███████╗███████╗████████╗██╗      ██████╗  █████╗ ██████╗ 
# ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██║     ██╔═══██╗██╔══██╗██╔══██╗
# ██████╔╝██████╔╝█████╗  ███████╗█████╗     ██║   ██║     ██║   ██║███████║██║  ██║
# ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║   ██║     ██║   ██║██╔══██║██║  ██║
# ██║     ██║  ██║███████╗███████║███████╗   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                 

import json
import os

class PresetLoad:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        def get_preset_names():
            # Path to the JSON file
            preset_path = os.path.join(os.path.dirname(__file__), '../presets/presetlist.json')
            
            # Initialize an empty list for preset names
            preset_names = ["<select name>"]

            # Try to read the JSON file and extract preset names
            if os.path.exists(preset_path):
                try:
                    with open(preset_path, 'r', encoding='utf-8') as file:
                        presets = json.load(file)
                        preset_names.extend([preset['name'] for preset in presets if 'name' in preset])
                except Exception as e:
                    print(f"An error occurred while reading {preset_path}: {str(e)}")
            else:
                print(f"Warning: The file {preset_path} does not exist.")
            
            return preset_names

        # Get the preset names by calling the helper function
        preset_names = get_preset_names()

        return {
            "required": {
                "name": (preset_names, {"default": "<select name>"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("pos_prompt", "neg_prompt", "preset_list")
    FUNCTION = "loadpreset"
    CATEGORY = "👑 MokkaBoss1/Text"

    def loadpreset(self, name, seed):
        preset_path = os.path.join(os.path.dirname(__file__), '../presets/presetlist.json')
        
        # Step 1: read the json file called "presetlist.json"
        if os.path.exists(preset_path):
            with open(preset_path, 'r', encoding='utf-8') as file:
                presets = json.load(file)
        else:
            raise FileNotFoundError(f"The file {preset_path} does not exist.")

        # Step 2: create a multiline string of all preset names
        preset_list = "\n".join([preset['name'] for preset in presets])

        # Refresh the list of names in case the content has changed
        preset_names = [preset['name'] for preset in presets if 'name' in preset]

        if not name or name == "<select name>" or name not in preset_names:
            # Return empty strings if name is not selected or not in the updated list
            return "", "", preset_list

        # Step 3: find the entry with the given name
        entry = next((preset for preset in presets if preset['name'] == name), None)

        if entry:
            # Step 4: return the pos_prompt and neg_prompt
            pos_prompt = entry.get('prompt', '')
            neg_prompt = entry.get('negative_prompt', '')
        else:
            pos_prompt = ""
            neg_prompt = ""

        return pos_prompt, neg_prompt, preset_list

NODE_CLASS_MAPPINGS = {"PresetLoad": PresetLoad}
NODE_DISPLAY_NAME_MAPPINGS = {"PresetLoad": "👑 PresetLoad"}

