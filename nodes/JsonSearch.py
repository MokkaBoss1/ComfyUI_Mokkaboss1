# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

#      ██╗███████╗ ██████╗ ███╗   ██╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
#      ██║██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
#      ██║███████╗██║   ██║██╔██╗ ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
# ██   ██║╚════██║██║   ██║██║╚██╗██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
# ╚█████╔╝███████║╚██████╔╝██║ ╚████║███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
#  ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                                   
import json

class JsonSearch:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "search_terms": ("STRING", {"forceInput": False}),
            "filename": ("STRING", {"default": "F:\\COMFYAPRIL\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\ComfyUI_Mokkaboss1\\presets\\presetlist.json"}),
            "max_number_displayed": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1, "forceInput": False}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("o_string",)
    FUNCTION = "json_search"
    CATEGORY = "👑 MokkaBoss1/Other"

    def json_search(self, search_terms, filename, max_number_displayed, seed):
        def read_json_file(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                return data
            except Exception as e:
                return f"Error reading JSON file: {e}"

        def search_data(data, search_terms, max_number_displayed):
            results = []
            count = 0
            for entry in data:
                if all(term.lower() in entry.get('prompt', '').lower() for term in search_terms):
                    results.append(entry)
                    count += 1
                    if count >= max_number_displayed:
                        break
            return results

        data = read_json_file(filename)
        if isinstance(data, str):  # If there's an error message instead of data
            return (data,)

        search_terms = [term.strip() for term in search_terms.split(',')]
        results = search_data(data, search_terms, max_number_displayed)

        if not results:
            o_string = "No entries found for the given search terms."
        else:
            o_string = "\n".join(
                f"Name: {result['name']}\nPrompt: {result['prompt']}\nNegative Prompt: {result.get('negative_prompt', 'N/A')}\n{'-'*40}"
                for result in results
            )

        return (o_string,)

NODE_CLASS_MAPPINGS = {"JsonSearch": JsonSearch}
NODE_DISPLAY_NAME_MAPPINGS = {"JsonSearch": "👑 JsonSearch"}




