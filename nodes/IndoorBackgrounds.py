# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
import random
import re

indoor_moods = [
    "Random",
    "None",
    "Warm and cozy",
    "Soft and romantic",
    "Bright and cheerful",
    "Dim and intimate",
    "Natural and sunlit",
    "Cool and calming",
    "Elegant and sophisticated",
    "Moody and atmospheric",
    "Vintage and nostalgic",
    "Dramatic and contrasting",
    "Industrial and edgy",
    "Minimalist and modern",
    "Whimsical and playful",
    "Artistic and creative",
    "Serene and tranquil"
]
indoor_moods.remove("Random")
indoor_moods.remove("None")
indoor_moods = list(set(indoor_moods))
indoor_moods.sort()
indoor_moods.insert(0, "None")
indoor_moods.insert(0, "Random")
indoor_scenes = [
    "Random",
    "None",
    "Living room with a fireplace",
    "Kitchen with a breakfast bar",
    "Bedroom with a cozy bed",
    "Home office with a desk and bookshelves",
    "Bathroom with a bathtub",
    "Dining room with a chandelier",
    "Library with floor-to-ceiling shelves",
    "Art studio with easels and paints",
    "Music room with instruments",
    "Gym with exercise equipment",
    "Home theater with plush seating",
    "Wine cellar with wine racks",
    "Game room with a pool table",
    "Sunroom with indoor plants",
    "Conservatory with a grand piano",
    "Attic with vintage furniture",
    "Basement lounge with a bar",
    "Children's playroom with toys",
    "Craft room with sewing machine",
    "Laundry room with washing machine",
    "Mudroom with storage cubbies",
    "Walk-in closet with shelves and mirrors",
    "Pantry with shelves stocked with food",
    "Garage with tools and workbench",
    "Studio apartment with minimalist decor",
    "Loft with exposed brick walls",
    "Apartment balcony with city views",
    "Hotel lobby with luxurious furnishings",
    "Restaurant with elegant decor",
    "Café with cozy seating",
    "Bookstore with reading nooks",
    "Art gallery with white walls and spotlights",
    "Museum exhibit with artifacts",
    "Theater stage with velvet curtains",
    "Recording studio with soundproofing",
    "University lecture hall with rows of seats",
    "Hospital room with medical equipment",
    "Classroom with chalkboard and desks",
    "Conference room with a long table",
    "Hotel room with a king-size bed",
    "Spa with massage tables and candles",
    "Beauty salon with hair styling stations",
    "Tattoo parlor with art-covered walls",
    "Photography studio with backdrop and lights",
    "Dance studio with mirrored walls",
    "Yoga studio with mats and meditation area",
    "Indoor pool with lounge chairs",
    "Bowling alley with polished lanes"
]
indoor_scenes.remove("Random")
indoor_scenes.remove("None")
indoor_scenes = list(set(indoor_scenes))
indoor_scenes.sort()
indoor_scenes.insert(0, "None")
indoor_scenes.insert(0, "Random")
color_textures = [
    "Random",
    "None",
    "Vivid & Smooth: Bright colors, polished surface",
    "Earthy & Rough: Natural tones, textured feel",
    "Pastel & Soft: Subtle hues, velvety touch",
    "Monochrome & Sleek: Single color, glossy finish",
    "Contrasting & Coarse: Bold colors, gritty texture",
    "Warm & Tactile: Rich tones, cozy texture",
    "Cool & Icy: Chilled shades, frosty surface",
    "Multicolored & Mosaic: Diverse hues, mosaic-like texture",
    "Neutral & Matte: Subdued tones, flat surface",
    "Gradient & Varied: Smooth transitions, varied texture",
    "Bold & Glossy: Striking colors, reflective sheen",
    "Subdued & Velvety: Soft tones, plush feel",
    "Tropical & Exotic: Vibrant colors, lush texture",
    "Dramatic & Jagged: High contrast, rough texture",
    "Soft & Silky: Gentle hues, smooth finish"
]
color_textures.remove("Random")
color_textures.remove("None")
color_textures = list(set(color_textures))
color_textures.sort()
color_textures.insert(0, "None")
color_textures.insert(0, "Random")

depthfocus_list = [
    "Random",
    "None",
    "background blurred",
    "background slightly blurred",
    "background sharp",
    "Softly focused background",
    "Bokeh background"
]

depthfocus_list.remove("Random")
depthfocus_list.remove("None")
depthfocus_list = list(set(depthfocus_list))
depthfocus_list.sort()
depthfocus_list.insert(0, "None")
depthfocus_list.insert(0, "Random")



num_indoor_scenes    = len(indoor_scenes)-1
num_indoor_moods    = len(indoor_moods)-1
num_depth_focus   = len(depthfocus_list)-1
num_color_textures = len(color_textures)-1

class IndoorBackgrounds:

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "pre_text": ("STRING", {"multiline": True, "default": ""}),
                    "post_text": ("STRING", {"multiline": True, "default": ""}),
                    "indoor_scene": ((indoor_scenes), ),
                    "indoor_mood": ((indoor_moods), ),
                    "depth_focus": ((depthfocus_list), ),
                    "color_texture": ((color_textures), ),
                    }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Positive Prompt",)
    FUNCTION = "test3"
    CATEGORY = "👑 MokkaBoss1/Text"
    
    def test3(self, seed, pre_text, post_text, indoor_scene, indoor_mood, depth_focus, color_texture):

        if indoor_scene == "Random":
            random_indoor_scene = random.randint(1, num_indoor_scenes-1)
            indoor_scene = indoor_scenes[random_indoor_scene]
        if indoor_scene == "None":
            indoor_scene = ""
            
        if indoor_mood == "Random":
            random_indoor_mood = random.randint(1, num_indoor_moods-1)
            indoor_mood = indoor_moods[random_indoor_mood]
        if indoor_mood == "None":
            indoor_mood = ""
        
        if depth_focus == "Random":
            random_depth_focus = random.randint(1, num_depth_focus-1)
            depth_focus = depthfocus_list[random_depth_focus]
        if depth_focus == "None":
            depth_focus = ""
        
        if color_texture =="Random":
            random_color_texture = random.randint(1,num_color_textures-1)
            color_texture = color_textures[random_color_texture]
        if color_texture == "None":
            color_texture = ""
            
        positive_prompt = f"{pre_text} {indoor_mood} {indoor_scene} {depth_focus} {color_texture}, {post_text}"

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

        print(positive_prompt)

        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"IndoorBackgrounds": IndoorBackgrounds}
NODE_DISPLAY_NAME_MAPPINGS = {"IndoorBackgrounds": "👑 Indoor Backgrounds"}           
