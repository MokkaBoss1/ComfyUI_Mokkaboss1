# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for the Specific Styles directories
base_path = "D:\\Midjourney\\Month2\\Specific Styles\\"

# List of specific style directories
specific_styles = [
    "Abstract full", "airbrush painting full", "alpine dirndl full", "alpine dirndl half",
    "Art Deco full", "Art Deco half", "Avril Lavigne", "caligraphy drawing full",
    "caligraphy drawing half", "comic drawing full", "comic drawing half", "cubism full",
    "detailed line drawing full", "detailed line drawing half", "digital painting full",
    "digital painting half", "disney full", "disney half", "emo full", "Emo half",
    "gothic full", "gothic half", "gothic vampire full", "gothic vampire half",
    "k-pop full", "k-pop half", "leather rocker full", "oil painting full", "oil painting half",
    "paper craft full", "paper craft half", "Pointilism full", "popart full", "popart half",
    "princess full", "princess half", "punk full", "real barbie full", "real barbie half",
    "Skater Girl full", "Steampunk full", "steampunk half", "watercolour full", "watercolour half"
]

# Dictionary mapping each style to its full path
specific_style_paths = {style: base_path + style for style in specific_styles}



class SpecificStylesDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((specific_styles), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen_f"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen_f(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = specific_style_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"SpecificStylesDir": SpecificStylesDir}
NODE_DISPLAY_NAME_MAPPINGS = {"SpecificStylesDir": "👑 SpecificStylesDir"}
