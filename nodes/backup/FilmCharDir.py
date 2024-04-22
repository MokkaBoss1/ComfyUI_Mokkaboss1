# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for film character directories
base_path = "D:\\Midjourney\\Month2\\Film Characters\\"

# List of film character directories
film_characters = [
    "Alice - Resident Evil", "Alice in Wonderland", "Aloy", "Ariel", "Artemis",
    "Arwen", "Arya Stark", "Beauty and the Beast", "Black Widow", "Buffy",
    "Daenerys", "Dorothy", "Effie", "elektra", "Eliza",
    "Elle Woods", "Ellen Ripley", "Elsa", "Eowyn", "Fiona",
    "Galadriel", "Gamora", "Harley", "Hela", "Hermione",
    "Holly", "Jasmine", "Katniss", "Katrina", "LeeLoo",
    "Luna Lovegood", "Maleficent", "Marge", "Marie", "Mary",
    "Megara", "Merida", "Mia", "Mia Wallace", "Morticia",
    "Mulan", "Pocahontas", "Princess Buttercup", "Princess Leia", "Princess Mononoke",
    "Rapunzel", "ray", "Sailor Moon", "Samantha", "Sansa Stark",
    "Scarlett", "Scarlett Witch", "Selene", "Selina", "Sleeping",
    "Super Girl", "Trinity", "Violett", "Wednesday", "Wendy", "Wonder Woman"
]

# Dictionary mapping each character to its full path
film_character_paths = {character: base_path + character for character in film_characters}


class FilmCharDir:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "path": ((film_characters), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen_f"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen_f(self, path):
        # Retrieve the path from the directory_paths dictionary
        path_value = film_character_paths.get(path, "Directory name not found")
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"FilmCharDir": FilmCharDir}
NODE_DISPLAY_NAME_MAPPINGS = {"FilmCharDir": "👑 FilmCharDir"}
