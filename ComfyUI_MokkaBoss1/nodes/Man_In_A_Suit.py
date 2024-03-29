#https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
import random
import re

ethnicities = [
    "Random",
    "None",
    "American",
    "British",
    "English",
    "Scottish",
    "Welsh",
    "French",
    "German",
    "Italian",
    "Spanish",
    "Japanese",
    "Chinese",
    "Russian",
    "Brazilian",
    "Indian",
    "Mexican",
    "Australian",
    "Canadian",
    "Swedish",
    "Dutch",
    "Irish",
    "Korean",
    "Norwegian",
    "Swiss",
    "Danish",
    "Israeli",
    "Greek",
    "Turkish",
    "Portuguese",
    "Belgian",
    "Austrian",
    "Polish",
    "South African",
    "Egyptian",
    "Thai",
    "Argentinian",
    "Chilean",
    "Colombian",
    "Peruvian",
    "Filipino",
    "Vietnamese",
    "Indonesian",
    "Malaysian",
    "Singaporean",
    "New Zealander",
    "Finnish",
    "Czech",
    "Hungarian",
    "Ukrainian",
    "Moroccan",
    "Saudi Arabian",
    "Emirati"
]
ethnicities.remove("Random")
ethnicities.remove("None")
ethnicities = list(set(ethnicities))
ethnicities.sort()
ethnicities.insert(0, "Random")
ethnicities.insert(0, "None")

    

haircolours = [
    "Random",
    "None",
    "black",
    "brown",
    "blonde",
    "platinum blonde",
    "red",
    "brunette",
    "auburn",
    "chestnut",
    "honey",
    "dark brown",
    "light brown"
]

haircolours.remove("Random")
haircolours.remove("None")
haircolours = list(set(haircolours))
haircolours.sort()
haircolours.insert(0, "Random")
haircolours.insert(0, "None")


hairstyles = [
    "Random",
    "None",
    "Crew cut",
    "Buzz cut",
    "Pompadour",
    "Undercut",
    "Fade haircut",
    "Quiff",
    "Comb over",
    "Side part",
    "Slicked back",
    "Ivy League haircut",
    "High and tight haircut",
    "Caesar cut",
    "Man bun",
    "French crop",
    "Textured crop",
    "Spiky hair",
    "Taper haircut",
    "Flat top haircut",
    "Mohawk",
    "Afro"
]

hairstyles.remove("Random")
hairstyles.remove("None")
hairstyles = list(set(hairstyles))
hairstyles.sort()
hairstyles.insert(0, "Random")
hairstyles.insert(0, "None")

    
suit_styles = [
    "Random",
    "None",
    "business suit",
    "tuxedo",
    "casual shirt and jeans",
    "polo shirt and chinos",
    "button-up shirt and dress pants",
    "blazer with jeans",
    "sweater and khakis",
    "hoodie and sweatpants",
    "dress shirt with a tie and slacks",
    "vest with trousers",
    "short-sleeve shirt with shorts",
    "denim jacket with cargo pants",
    "leather jacket with jeans",
    "bomber jacket and joggers",
    "flannel shirt with denim",
    "sport coat with corduroy pants",
    "pea coat with trousers",
    "turtleneck with tailored trousers",
    "graphic tee with shorts",
    "tank top with athletic shorts",
    "zip-up hoodie with track pants",
    "vest with a button-up shirt and jeans",
    "collared shirt with linen pants",
    "cardigan with chino shorts",
    "blazer with a graphic tee and jeans",
    "denim shirt with cargo shorts",
    "fleece jacket with cargo pants",
    "vest with a polo shirt and khakis",
    "overcoat with dress pants",
    "plaid shirt with corduroy pants",
    "pullover sweater with denim",
    "windbreaker with athletic shorts",
    "vest with a hoodie and chinos",
    "dress shirt with suspenders and trousers",
    "half-zip sweater with chino shorts",
    "biker jacket with leather pants",
    "varsity jacket with jogger pants",
    "trench coat with slacks",
    "button-down shirt with tailored shorts",
    "sweatshirt paired with joggers",
    "hoodie paired with cargo pants",
    "tank top paired with capri pants",
    "t-shirt paired with Bermuda shorts",
    "t-shirt layered under overalls",
    "one-piece swimsuit with floral print",
    "high-waisted bikini with ruffled top",
    "sporty tankini set",
    "cutout monokini",
    "wrap-front bikini with sarong",
    "classic triangle bikini with string ties",
    "retro halter-neck swimsuit",
    "color-blocked rash guard with board shorts",
    "strapless bandeau bikini with side-tie bottoms",
    "mesh-panel swimsuit with plunging neckline",
    "roleplay costume"
]

suit_styles.remove("Random")
suit_styles.remove("None")
suit_styles = list(set(suit_styles))
suit_styles.sort()
suit_styles.insert(0, "Random")
suit_styles.insert(0, "None")




suit_colours = [
    "Random",
    "None",
    "beige coloured",
    "black coloured",
    "blue coloured",
    "brown coloured",
    "charcoal coloured",
    "chocolate coloured",
    "coral coloured",
    "crimson coloured",
    "forest green coloured",
    "gold coloured",
    "gray coloured",
    "green coloured",
    "indigo coloured",
    "ivory coloured",
    "lavender coloured",
    "lemon coloured",
    "magenta coloured",
    "maroon coloured",
    "mint coloured",
    "navy coloured",
    "olive coloured",
    "orange coloured",
    "orchid coloured",
    "peach coloured",
    "pink coloured",
    "purple coloured",
    "red coloured",
    "rose coloured",
    "royal blue coloured",
    "salmon coloured",
    "slate coloured",
    "silver coloured",
    "sky blue coloured",
    "tan coloured",
    "teal coloured",
    "turquoise coloured",
    "violet coloured",
    "white coloured",
    "yellow coloured"
]


suit_colours.remove("Random")
suit_colours.remove("None")
suit_colours = list(set(suit_colours))
suit_colours.sort()
suit_colours.insert(0, "Random")
suit_colours.insert(0, "None")


suit_patterns_textures = [
    "Random",
    "None",
    "abstract",
    "animal print",
    "batik",
    "brocade",
    "checkered",
    "cotton",
    "crochet",
    "denim",
    "embroidery",
    "fringe",
    "geometric",
    "gingham",
    "houndstooth",
    "jacquard",
    "jersey",
    "lace",
    "leather",
    "linen",
    "mesh",
    "ombre",
    "paisley",
    "plaid",
    "polka dots",
    "polyester",
    "rayon",
    "ruffles",
    "satin",
    "seamless",
    "sequins",
    "silk",
    "stripes",
    "tartan",
    "tie-dye",
    "tulle",
    "velvet",
    "zebra patterned"
]

suit_patterns_textures.remove("Random")
suit_patterns_textures.remove("None")
suit_patterns_textures = list(set(suit_patterns_textures))
suit_patterns_textures.sort()
suit_patterns_textures.insert(0, "Random")
suit_patterns_textures.insert(0, "None")

genders = [
    "man",
    "woman",
    "female man",
    "male woman",
]


num_ethnicities = len(ethnicities)-1
num_hairstyles = len(hairstyles)-1
num_haircolours = len(haircolours)-1
num_styles = len(suit_styles)-1
num_colours = len(suit_colours)-1
num_patterns = len(suit_patterns_textures)-1






class Man_In_A_Suit:

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "pre_text": ("STRING", {"multiline": True, "default": ""}),
                    "post_text": ("STRING", {"multiline": True, "default": ""}),
                    "gender": ((genders), ),
                    "ethnicity": ((ethnicities), ),
                    "hair_colour": ((haircolours), ),
                    "hair_style": ((hairstyles), ),
                    "suit_style": ((suit_styles), ),
                    "suit_colour": ((suit_colours), ),
                    "pattern_or_texture": ((suit_patterns_textures), ),
                    }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Positive Prompt",)
    FUNCTION = "test3"
    CATEGORY = "👑 MokkaBoss1"

    def test3(self, seed, pre_text, post_text, gender, ethnicity, hair_colour, hair_style, suit_style, suit_colour, pattern_or_texture):

        if ethnicity == "Random":
            random_ethnicity = random.randint(2, num_ethnicities-2)
            ethnicity = ethnicities[random_ethnicity].lower()
        if ethnicity == "None":
            ethnicity = ""
            
        if hair_colour == "Random":
            random_haircolour = random.randint(2, num_haircolours-2)
            hair_colour = haircolours[random_haircolour].lower()
        if hair_colour == "None":
            hair_colour = ""
            
        if hair_style == "Random":
            random_hairstyle = random.randint(2, num_hairstyles-2)
            hair_style = hairstyles[random_hairstyle].lower()
        if hair_style == "None":
            hair_style = ""
            hair_colour = ""
        
        if suit_style =="Random":
            random_suitstyle = random.randint(2, num_styles-2)
            suit_style = suit_styles[random_suitstyle].lower()
        
        if suit_colour == "Random":
            random_colour = random.randint(2,num_colours-2)
            suit_colour = suit_colours[random_colour].lower()
        if suit_colour == "None":
            suit_colour = ""
        
        if pattern_or_texture =="Random":
            random_pattern = random.randint(2,num_patterns-2)
            pattern_or_texture = suit_patterns_textures[random_pattern].lower()
        if pattern_or_texture == "None":
            pattern_or_texture = ""
        if suit_style == "None":
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, {post_text}"
        else:
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, wearing a {suit_colour} {pattern_or_texture} {suit_style}, {post_text}"

        if seed == 999:
            positive_prompt = f"{pre_text} {post_text} "
        
        positive_prompt = re.sub(r'with  , ', '', positive_prompt)
        positive_prompt = re.sub(r'  ', ' ', positive_prompt)
        
        if positive_prompt == f"{pre_text} man {post_text}":
            positive_prompt = f"{pre_text} {post_text}"
        positive_prompt = re.sub(r'  ', ' ', positive_prompt)
        print(positive_prompt)

        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"Man_In_A_Suit)": Man_In_A_Suit}
NODE_DISPLAY_NAME_MAPPINGS = {"Man_In_A_Suit": "👑 Man_In_A_Suit"}
