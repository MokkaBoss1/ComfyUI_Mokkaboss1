# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


base_path = "D:\\Midjourney\\Month2\\Landscapes\\"
directories = [
    "alien planet", "alpine meadow", "antarctic", "bog", "cave", 
    "chaparrel", "city", "city snow", "coral reef", "death valley", 
    "desert", "dune", "english countryside", "english garden", "estuary", 
    "fen", "forest", "forest fire", "grassland", "hydrothermal", 
    "kelp", "lagoon", "lake", "limestone", "mangrove", 
    "Mountain Ridge", "night street corner", "oasis", "pebble beach", "polar", 
    "prarie", "Rainforest", "riverbank", "saltwater marsh", "sandy english beach", 
    "savannah", "scrapyard", "taiga", "tropical beach", "tundra", 
    "urban backdrop", "urban wasteland", "vernal pool", "volcanic crater", "wetland"
]

directory_paths = {directory: base_path + directory for directory in directories}

class LandscapeDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((directories), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = directory_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"LandscapeDir": LandscapeDir}
NODE_DISPLAY_NAME_MAPPINGS = {"LandscapeDir": "👑 LandscapeDir"}
        


NODE_CLASS_MAPPINGS = {"LandscapeDir": LandscapeDir}
NODE_DISPLAY_NAME_MAPPINGS = {"LandscapeDir": "👑 LandscapeDir"}
