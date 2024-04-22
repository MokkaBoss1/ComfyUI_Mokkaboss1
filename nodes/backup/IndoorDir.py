# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for the new set of directories
base_path = "D:\\Midjourney\\Month2\\Interiors\\"

# List of new directories
interior_directories = [
    "bedroom classical evening", "circus arena", "cocktail bar",
    "gothic cathedral", "gothic house", "hotel lobby", "hotel room",
    "large ballroom classical evening", "large ballroom day", "large ballroom evening",
    "large living room classical evening", "large social hall evening",
    "moden living room evening", "modern bedroom", "modern library",
    "modern living room day", "modern social hall evening", "modern university",
    "night club", "old university", "restaurant", "royal bedroom",
    "royal concert hall", "royal palace hall", "spa", "spaceship",
    "underground aquarium", "walls"
]

# Dictionary that maps each directory to its full path
interior_directory_paths = {directory: base_path + directory for directory in interior_directories}

class IndoorDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((interior_directories), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = interior_directory_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"IndoorDir": IndoorDir}
NODE_DISPLAY_NAME_MAPPINGS = {"IndoorDir": "👑 IndoorDir"}
