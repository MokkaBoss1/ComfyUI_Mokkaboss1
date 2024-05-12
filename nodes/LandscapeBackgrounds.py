#https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██╗      █████╗ ███╗   ██╗██████╗ ███████╗ ██████╗ █████╗ ██████╗ ███████╗██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ ███████╗
# ██║     ██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗██╔════╝
# ██║     ███████║██╔██╗ ██║██║  ██║███████╗██║     ███████║██████╔╝█████╗  ██████╔╝███████║██║     █████╔╝ ██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║███████╗
# ██║     ██╔══██║██║╚██╗██║██║  ██║╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║╚════██║
# ███████╗██║  ██║██║ ╚████║██████╔╝███████║╚██████╗██║  ██║██║     ███████╗██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝███████║
# ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
                                                                                                                                                                       
import random
import re

color_textures = [
    "Random",
    "None",
    "Simple, Plain, Minimal details, Uniform background",
    "Sparse, Basic, Few details, Straightforward background",
    "Clean, Neat, Moderate details, Organized background",
    "Balanced, Orderly, Balanced details, Structured background",
    "Average, Decent, Standard details, Typical background",
    "Elaborate, Engaging, Abundant details, Engaging background",
    "Rich, Intricate, Detailed elements, Rich background",
    "Complex, Varied, Diverse details, Intricate background",
    "Exquisite, Ornate, Elaborate details, Ornate background",
    "Intricate, Detailed, Highly detailed scene, Intricate background"
]

depthfocus_list = [
    "Random",
    "None",
    "background blurred",
    "background slightly blurred",
    "background sharp",
    "softly focused background",
    "bokeh background"
]
depthfocus_list.remove("Random")
depthfocus_list.remove("None")
depthfocus_list = list(set(depthfocus_list))
depthfocus_list.sort()
depthfocus_list.insert(0, "None")
depthfocus_list.insert(0, "Random")
moods = [
    "Random",
    "None",
    "Tranquil",
    "Vibrant",
    "Mysterious",
    "Serene",
    "Melancholic",
    "Energetic",
    "Dramatic",
    "Dreamy",
    "Peaceful",
    "Chaotic",
    "Romantic",
    "Surreal",
    "Nostalgic",
    "Foreboding",
    "Joyful"
]
moods.remove("Random")
moods.remove("None")
moods = list(set(moods))
moods.sort()
moods.insert(0, "None")
moods.insert(0, "Random")
lightings =  [
    "Random",
    "None",
    "Clear night with starry skies and moonlight",
    "Cloudy day with warm sunlight",
    "Cloudy day with warm sunlight reflecting off water",
    "Foggy night with eerie moonlight",
    "Foggy night with moonlit silhouettes",
    "Misty day with glowing light",
    "Misty day with glowing light during sunrise",
    "Overcast day with dimmed sunlight",
    "Overcast day with gentle diffused light",
    "Overcast day with soft, ethereal light",
    "Overcast day with foggy conditions",
    "Rainy day with misty light",
    "Overcast day with sleet",
    "Snowy day with sparkling light on fresh snow",
    "Sunny day with clear blue skies",
    "Sunny day with soft sunlight",
    "Sunny day with soft sunlight filtering through clouds",
    "Sunny day with vibrant sunlight",
    "Sunny day with warm golden light",
    "Sunset with golden hour light",
    "Sunrise with clear sky",
]
lightings.remove("Random")
lightings.remove("None")
lightings = list(set(lightings))
lightings.sort()
lightings.insert(0, "None")
lightings.insert(0, "Random")

adjectives = [
    "Random",
    "None",
    "Majestic",
    "Spectacular",
    "Serene",
    "Breathtaking",
    "Picturesque",
    "Tranquil",
    "Scenic",
    "Idyllic",
    "Untouched",
    "Pristine",
    "Vibrant",
    "Lush",
    "Barren",
    "Dramatic",
    "Mystical",
    "Rugged",
    "Enchanting",
    "Surreal",
    "Awe-inspiring",
    "Ethereal"
]
adjectives.remove("Random")
adjectives.remove("None")
adjectives = list(set(adjectives))
adjectives.sort()
adjectives.insert(0, "None")
adjectives.insert(0, "Random")
landscapes = [
    "Random",
    "None",
    "Mountains",
    "Valleys",
    "Plateaus",
    "Plains",
    "Deserts",
    "Canyons",
    "Glaciers",
    "Tundras",
    "Forests",
    "Rainforests",
    "Swamps",
    "Marshes",
    "Grasslands",
    "Savannas",
    "Taigas",
    "Tropical islands",
    "Archipelagos",
    "Cliffs",
    "Caves",
    "Volcanoes",
    "Lakes",
    "Rivers",
    "Waterfalls",
    "Oceans",
    "Seas",
    "Bays",
    "Fjords",
    "Coral reefs",
    "Icebergs",
    "Sand dunes",
    "City skyline",
    "Urban park",
    "Botanical garden",
    "Zoo",
    "Amusement park",
    "Skyscraper",
    "Bridge",
    "Highway interchange",
    "Train station",
    "Airport",
    "Shopping mall",
    "Residential neighborhood",
    "Office complex",
    "Industrial area",
    "Sports stadium",
    "Convention center",
    "Theme park",
    "Historical landmark",
    "Cemetery",
    "Seaport",
    "Harbor",
    "Oil refinery",
    "Power plant",
    "Dam",
    "Canal",
    "Aqueduct",
    "Wind farm",
    "Solar farm",
    "Spaceport",
    "Prison complex"
]
landscapes.remove("Random")
landscapes.remove("None")
landscapes = list(set(landscapes))
landscapes.sort()
landscapes.insert(0, "None")
landscapes.insert(0, "Random")

num_landscapes    = len(landscapes)-1
num_adjectives    = len(adjectives)-1
num_lightings      = len(lightings)-1
num_moods         = len(moods)-1
num_depthfocus_list   = len(depthfocus_list)-1
num_color_textures = len(color_textures)-1

class LandscapeBackgrounds:

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "pre_text": ("STRING", {"multiline": True, "default": ""}),
                    "post_text": ("STRING", {"multiline": True, "default": ""}),
                    "adjective": ((adjectives), ),
                    "landscape": ((landscapes), ),
                    "lighting": ((lightings), ),
                    "mood": ((moods), ),
                    "depth_focus": ((depthfocus_list), ),
                    "color_texture": ((color_textures), ),
                    }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Positive Prompt",)
    FUNCTION = "test3"
    CATEGORY = "👑 MokkaBoss1/Text"
    
    def test3(self, seed, pre_text, post_text, adjective, landscape, lighting, mood, depth_focus, color_texture):

        if landscape == "Random":
            random_landscape = random.randint(2, num_landscapes-2)
            landscape = landscapes[random_landscape]
        if landscape == "None":
            landscape =""
            
        if adjective == "Random":
            random_adjective = random.randint(2, num_adjectives-2)
            adjective = adjectives[random_adjective]
        if adjective == "None":
            adjective = ""
        
        if lighting == "Random":
            random_lighting = random.randint(2, num_lightings-2)
            lighting = lightings[random_lighting]
        if lighting == "None":
            lighting = ""
        
        if mood == "Random":
            random_mood = random.randint(2, num_moods-2)
            mood = moods[random_mood]
        if mood == "None":
            mood = ""
        
        if depth_focus == "Random":
            random_depth_focus = random.randint(2, num_depthfocus_list-2)
            depth_focus = depthfocus_list[random_depth_focus]
            print(f"Depth Focus Random selection is: {depth_focus}")
        if depth_focus == "None":
            depth_focus = ""
        
        if color_texture == "Random":
            random_color_texture = random.randint(2,num_color_textures-2)
            color_texture = color_textures[random_color_texture]
        if color_texture == "None":
            color_texture = ""
            
        positive_prompt = f"{pre_text} {adjective} {landscape} {lighting} {mood} {depth_focus} {color_texture}, {post_text}"

        if seed == 999:
            positive_prompt = f"{pre_text} {post_text}"
            
        #remove extra spaces    
        positive_prompt = re.sub(r'      ', ' ', positive_prompt)
        positive_prompt = re.sub(r'     ', ' ', positive_prompt)
        positive_prompt = re.sub(r'    ', ' ', positive_prompt)
        positive_prompt = re.sub(r'   ', ' ', positive_prompt)       
        positive_prompt = re.sub(r' , ', ', ', positive_prompt)
        positive_prompt = re.sub(r'  ', ' ', positive_prompt)
        if positive_prompt == ", ":
            positive_prompt = ""
        if positive_prompt == " ":
            positive_prompt = ""
            
        result = re.sub(r'[A-Z]', lambda x: x.group(0).lower(), positive_prompt)
        
        print(positive_prompt)

        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"LandscapeBackgrounds": LandscapeBackgrounds}
NODE_DISPLAY_NAME_MAPPINGS = {"LandscapeBackgrounds": "👑 Landscape Backgrounds"}           
