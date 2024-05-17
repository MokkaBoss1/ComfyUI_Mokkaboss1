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
        return {
            "required": {
                "name": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("pos_prompt", "neg_prompt", "preset_list")
    FUNCTION = "loadpreset"
    CATEGORY = "👑 MokkaBoss1/Text"

    def loadpreset(self, name, seed):
        preset_path = os.path.join(os.path.dirname(__file__), '../../../mokkaboss1_presetlist.json')
        
        # Step 1: read the json file called "presetlist.json"
        if os.path.exists(preset_path):
            with open(preset_path, 'r', encoding='utf-8') as file:
                presets = json.load(file)
        else:
            raise FileNotFoundError(f"The file {preset_path} does not exist.")

        # Step 2: create a multiline string of all preset names
        preset_list = "\n".join([preset['name'] for preset in presets if 'name' in preset])

        if not name or name not in [preset['name'] for preset in presets if 'name' in preset]:
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
