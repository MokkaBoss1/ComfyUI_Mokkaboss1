# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██████╗ ██████╗ ███████╗███████╗███████╗████████╗██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
# ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
# ██████╔╝██████╔╝█████╗  ███████╗█████╗     ██║   ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  
# ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  
# ██║     ██║  ██║███████╗███████║███████╗   ██║   ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗
# ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝
                                                                                                      
import json
import os

class PresetRemove:

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

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("preset_list",)
    FUNCTION = "removepreset"
    CATEGORY = "👑 MokkaBoss1/Text"

    def removepreset(self, name, seed): 
        preset_path = os.path.join(os.path.dirname(__file__), '../presets/presetlist.json')
        
        # Step 1: read the json file called "presetlist.json"
        if os.path.exists(preset_path):
            with open(preset_path, 'r', encoding='utf-8') as file:
                presets = json.load(file)
        else:
            raise FileNotFoundError(f"The file {preset_path} does not exist.")

        # Step 2: create a multiline string of all preset names before removal
        preset_list = "\n".join([preset['name'] for preset in presets])

        # Step 3: find the entry with the given name and remove it if it exists
        initial_count = len(presets)
        if name != "<select name>" and name in [preset['name'] for preset in presets]:
            presets = [preset for preset in presets if preset['name'] != name]

            # Step 4: check if an entry was removed and save the updated list if necessary
            if len(presets) < initial_count:
                with open(preset_path, 'w', encoding='utf-8') as file:
                    json.dump(presets, file, indent=4)

            # Step 5: create a multiline string of all preset names after removal
            preset_list = "\n".join([preset['name'] for preset in presets])

        # Debugging output to ensure names are correctly retrieved
        print("Preset names in the list after removal:")
        print(preset_list)
        
        return (preset_list,)

# Example invocation
if __name__ == "__main__":
    preset_remover = PresetRemove()
    result = preset_remover.removepreset("example_name", 12345)
    print(result)

NODE_CLASS_MAPPINGS = {"PresetRemove": PresetRemove}
NODE_DISPLAY_NAME_MAPPINGS = {"PresetRemove": "👑 PresetRemove"}
