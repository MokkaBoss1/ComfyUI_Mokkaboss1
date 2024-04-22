# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for the makeup styles directories within the 1by1 subdirectory
base_path = "D:\\Midjourney\\Month2\\makeup styles\\1by1\\"

# List of makeup style directories
makeup_styles = [
    "Artistic", "Boho", "Bold", "Cat", "Edgy",
    "Fairy", "Festival", "Geometric", "Glitter", "Gothic",
    "Grunge", "Hollywood", "Mermaid", "Mono", "Natural",
    "Smokey", "Unicorn", "Vintage Glam"
]

# Dictionary mapping each makeup style to its full path
makeup_style_paths = {style: base_path + style for style in makeup_styles}



class MakeupStylesDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((makeup_styles), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen_f"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen_f(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = makeup_style_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"MakeupStylesDir": MakeupStylesDir}
NODE_DISPLAY_NAME_MAPPINGS = {"MakeupStylesDir": "👑 MakeupStylesDir"}
