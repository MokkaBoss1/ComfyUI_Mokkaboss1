import random
import re

genders = [
    "woman",
    "man",
    "female man",
    "male woman",
]    

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
    "blunt bob hairstyle",
    "long bob hairstyle",
    "messy bun hairstyle",
    "beach waves hairstyle",
    "sleek straight hairstyle",
    "wavy lob hairstyle",
    "balayage hairstyle",
    "ombre hairstyle",
    "Egyptian bob hairstyle",
    "half-up half-down hairstyle",
    "space buns hairstyle",
#    "Box Braids hairstyle",
    "long layers hairstyle",
    "high ponytail hairstyle",
#    "Fishtail Braid hairstyle",
    "bubble ponytail hairstyle",
    "slicked back hairstyle",
    "shaggy layers hairstyle",
    "curtain bangs hairstyle",
    "asymmetrical pixie hairstyle",
    "feathered layers hairstyle",
    "layered shag hairstyle"
]
hairstyles.remove("Random")
hairstyles.remove("None")
hairstyles = list(set(hairstyles))
hairstyles.sort()
hairstyles.insert(0, "Random")
hairstyles.insert(0, "None")

    
dress_styles = [
    "Random",
    "None",
    "shift dress",
    "a-line dress",
    "ball gown",
    "sheath dress",
    "wrap dress",
    "maxi dress",
    "midi dress",
    "mini dress",
    "bodycon dress",
    "fit and flare dress",
    "empire waist dress",
    "peplum dress",
    "shirt dress",
    "halter neck dress",
    "off-the-shoulder dress",
    "one-shoulder dress",
    "strapless dress",
    "high-low dress",
    "mermaid dress",
    "princess dress",
    "tiered dress",
    "tunic dress",
    "chemise dress",
    "slip dress",
    "jumper dress",
#    "balloon dress",
    "cape dress",
    "kimono dress",
    "corset dress",
    "flapper dress",
    "belted shirt dress",
    "belted v-neck midi dress",
    "cotton padded t-shirt dress",
    "embroidered bell sleeve mini dress",
    "open back chiffon midi dress",
    "printed belted shirt dress",
    "printed chiffon midi dress",
    "printed chiffon mini dress",
    "printed crêpe chiffon mini dress",
    "printed crêpe midi dress",
    "print v-neck midi dress",
    "ribbed off-shoulder midi dress",
    "short-sleeve mini dress",
    "sleeveless crêpe chiffon mini dress",
    "sleeveless peplum mini dress",
    "sleeveless punto mini dress",
    "structured mini dress",
    "striped padded t-shirt dress",
    "t-shirt midi dress",
    "textured flounced hem mini dress",
    "3/4 sleeve crêpe midi dress",
    "lingerie Set",
    "bodysuit",
    "corset and garter belt set",
    "babydoll and chemise",
    "tailored blazer paired with trousers",
    "button-up shirt tucked into high-waisted pants",
    "knit sweater layered over a collared shirt with trousers",
    "blouse with a pencil skirt and a belt",
    "sleeveless top paired with wide-leg pants",
    "structured suit jacket with matching pants",
    "cropped top paired with culottes",
    "crop top and mini skirt",
    "crop top and shorts",
    "turtleneck sweater paired with tailored shorts",
    "sleeveless blouse tucked into a midi skirt",
    "jacket layered over a tank top with jeans",
    "cardigan worn over a camisole with leggings",
    "fitted top with a maxi skirt and a statement belt",
    "tunic top paired with leggings or jeggings",
    "button-down shirt with tailored shorts",
    "crop top paired with high-waisted trousers",
    "sweatshirt paired with joggers",
    "hoodie paired with cargo pants",
    "tank top paired with capri pants",
    "t-shirt paired with Bermuda shorts",
    "turtleneck top layered under overalls",
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

dress_styles.remove("Random")
dress_styles.remove("None")
dress_styles = list(set(dress_styles))
dress_styles.sort()
dress_styles.insert(0, "Random")
dress_styles.insert(0, "None")




dress_colours = [
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


dress_colours.remove("Random")
dress_colours.remove("None")
dress_colours = list(set(dress_colours))
dress_colours.sort()
dress_colours.insert(0, "Random")
dress_colours.insert(0, "None")


dress_patterns_textures = [
    "Random",
    "None",
    "abstract",
    "animal print",
    "batik",
    "brocade",
    "checkered",
    "chiffon",
    "chiffon",
    "cotton",
    "crochet",
    "denim",
    "denim",
    "embroidery",
    "floral",
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
    "tulle",
    "velvet",
    "velvet",
    "zebra patterned"
]

dress_patterns_textures.remove("Random")
dress_patterns_textures.remove("None")
dress_patterns_textures = list(set(dress_patterns_textures))
dress_patterns_textures.sort()
dress_patterns_textures.insert(0, "Random")
dress_patterns_textures.insert(0, "None")


num_ethnicities = len(ethnicities)-1
num_hairstyles = len(hairstyles)-1
num_haircolours = len(haircolours)-1
num_styles = len(dress_styles)-1
num_colours = len(dress_colours)-1
num_patterns = len(dress_patterns_textures)-1






class Woman_In_A_Dress:

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
                    "dress_style": ((dress_styles), ),
                    "dress_colour": ((dress_colours), ),
                    "pattern_or_texture": ((dress_patterns_textures), ),
                    }
                }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Positive Prompt",)
    FUNCTION = "test3"
    CATEGORY = "👑 MokkaBoss1"

    def test3(self, seed, pre_text, post_text, gender, ethnicity, hair_colour, hair_style, dress_style, dress_colour, pattern_or_texture):

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
        
        if dress_style =="Random":
            random_dressstyle = random.randint(2, num_styles-2)
            dress_style = dress_styles[random_dressstyle].lower()
        
        if dress_colour == "Random":
            random_colour = random.randint(2,num_colours-2)
            dress_colour = dress_colours[random_colour].lower()
        if dress_colour == "None":
            dress_colour = ""
        
        if pattern_or_texture =="Random":
            random_pattern = random.randint(2,num_patterns-2)
            pattern_or_texture = dress_patterns_textures[random_pattern].lower()
        if pattern_or_texture == "None":
            pattern_or_texture = ""
        if dress_style == "None":
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, {post_text}"
        else:
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, wearing a {dress_colour} {pattern_or_texture} {dress_style}, {post_text}"

        if seed == 999:
            positive_prompt = f"{pre_text} {post_text} "
        
        positive_prompt = re.sub(r'with  , ', '', positive_prompt)
        positive_prompt = re.sub(r'  ', ' ', positive_prompt)

        print(positive_prompt)

        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"Woman_In_A_Dress": Woman_In_A_Dress}
NODE_DISPLAY_NAME_MAPPINGS = {"Woman_In_A_Dress": "👑 Woman_In_A_Dress"}
