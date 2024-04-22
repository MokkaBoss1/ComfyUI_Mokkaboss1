# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# Base path for the new set of directories
base_path_interior = "D:\\Midjourney\\Month2\\Interiors\\"
base_path_makeup = "D:\\Midjourney\\Month2\\makeup styles\\1by1\\"
base_path_anime = "D:\\Midjourney\\Month2\\anime cosplay\\1by1\\"
base_path_filmchar = "D:\\Midjourney\\Month2\\Film Characters\\"
base_path_landscape = "D:\\Midjourney\\Month2\\Landscapes\\"
base_path_specific = "D:\\Midjourney\\Month2\\Specific Styles\\"


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

makeup_styles = [
    "Artistic", "Boho", "Bold", "Cat", "Edgy",
    "Fairy", "Festival", "Geometric", "Glitter", "Gothic",
    "Grunge", "Hollywood", "Mermaid", "Mono", "Natural",
    "Smokey", "Unicorn", "Vintage Glam"
]

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

# Dictionary that maps each directory to its full path
interior_directory_paths = {directory: base_path_interior + directory for directory in interior_directories}
makeup_style_paths = {style: base_path_makeup + style for style in makeup_styles}
anime_cosplay_paths = {directory: base_path_anime + directory for directory in anime_cosplay_directories}
film_character_paths = {character: base_path_filmchar + character for character in film_characters}
directory_paths = {directory: base_path_landscape + directory for directory in directories}
specific_style_paths = {style: base_path_specific + style for style in specific_styles}

class DirSelector:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "choice": ("INT", {"default": 1, "min": 1, "max": 6}),
            "choice1_interiors": ((interior_directories), ),
            "choice2_makeup_styles": ((makeup_styles), ),
            "choice3_anime_cosplay": ((anime_cosplay_directories), ),
            "choice4_film_characters": ((film_characters), ),
            "choice5_landscapes": ((directories), ),
            "choice6_specific_styles": ((specific_styles), ),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path_value",)
    FUNCTION = "path_gen"
    CATEGORY = "👑 MokkaBoss1/Text"

    def path_gen(self, choice, choice1_interiors, choice2_makeup_styles, choice3_anime_cosplay, choice4_film_characters, choice5_landscapes, choice6_specific_styles):
        if choice == 1:
            path_value = interior_directory_paths.get(choice1_interiors, "Directory name not found")
        if choice == 2:
            path_value = makeup_style_paths.get(choice2_makeup_styles, "Directory name not found")
        if choice == 3:
            path_value = anime_cosplay_paths.get(choice3_anime_cosplay, "Directory name not found")
        if choice == 4:
            path_value = film_character_paths.get(choice4_film_characters, "Directory name not found")
        if choice == 5:
            path_value = directory_paths.get(choice5_landscapes, "Directory name not found")
        if choice == 6:
            path_value = specific_style_paths.get(choice6_specific_styles, "Directory name not found")
        
        return (path_value,)

# Dictionary for node class and display name mappings
NODE_CLASS_MAPPINGS = {"DirSelector": DirSelector}
NODE_DISPLAY_NAME_MAPPINGS = {"DirSelector": "👑 DirSelector"}
