# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for the anime cosplay directories within the 1by1 subdirectory
base_path = "D:\\Midjourney\\Month2\\anime cosplay\\1by1\\"

# List of anime cosplay directories
anime_cosplay_directories = [
    "Asuna", "cocktail", "Coral", "emerald", "ethereal",
    "Ezra", "fantasy", "fire", "galactic", "goddess",
    "golden", "Hinata", "Homura", "Kiki", "Kotori",
    "Lucy", "Lum", "Mikasa", "Moka", "Mokoto",
    "Nami", "neon", "Nico", "ocean", "pastel",
    "rei", "Rem", "Ryuko", "sailor", "Sailor M",
    "Sakura", "Sapphire", "schoolgirl", "sci-fi", "space",
    "time", "Yuno", "Zero Two"
]

# Dictionary mapping each character to its full path
anime_cosplay_paths = {directory: base_path + directory for directory in anime_cosplay_directories}



class AnimeCosplayDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((anime_cosplay_directories), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen_f"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen_f(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = anime_cosplay_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"AnimeCosplayDir": AnimeCosplayDir}
NODE_DISPLAY_NAME_MAPPINGS = {"AnimeCosplayDir": "👑 AnimeCosplayDir"}
