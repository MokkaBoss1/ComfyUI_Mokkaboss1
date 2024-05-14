# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██╗  ██╗        ██╗███╗   ██╗         █████╗         ██████╗ ██████╗ ███████╗███████╗███████╗
# ╚██╗██╔╝        ██║████╗  ██║        ██╔══██╗        ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
#  ╚███╔╝         ██║██╔██╗ ██║        ███████║        ██║  ██║██████╔╝█████╗  ███████╗███████╗
#  ██╔██╗         ██║██║╚██╗██║        ██╔══██║        ██║  ██║██╔══██╗██╔══╝  ╚════██║╚════██║
# ██╔╝ ██╗███████╗██║██║ ╚████║███████╗██║  ██║███████╗██████╔╝██║  ██║███████╗███████║███████║
# ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                                                             
import random
import re

genders = [
    "woman",
    "man",
    "female man",
    "male woman",
]    

ethnicities = sorted([
    "American", "British", "English", "Scottish", "Welsh", "French", "German", "Italian", 
    "Spanish", "Japanese", "Chinese", "Russian", "Brazilian", "Indian", "Mexican", 
    "Australian", "Canadian", "Swedish", "Dutch", "Irish", "Korean", "Norwegian", "Swiss", 
    "Danish", "Israeli", "Greek", "Turkish", "Portuguese", "Belgian", "Austrian", "Polish", 
    "South African", "Egyptian", "Thai", "Argentinian", "Chilean", "Colombian", "Peruvian", 
    "Filipino", "Vietnamese", "Indonesian", "Malaysian", "Singaporean", "New Zealander", 
    "Finnish", "Czech", "Hungarian", "Ukrainian", "Moroccan", "Saudi Arabian", "Emirati",
    "Afghan", "Algerian", "Bangladeshi", "Bulgarian", "Ethiopian", "Ghanaian", "Iranian", 
    "Iraqi", "Jamaican", "Jordanian", "Kenyan", "Lebanese", "Malian", "Nepalese", 
    "Pakistani", "Romanian", "Senegalese", "Somali", "Sri Lankan", "Syrian", "Tunisian"
])

haircolours = sorted([
    "black", "brown", "blonde", "platinum blonde", "red", "brunette", "auburn", 
    "chestnut", "honey", "dark brown", "light brown",
    "ash blonde", "burgundy", "caramel", "copper", "dirty blonde", "golden blonde", 
    "jet black", "mahogany", "sandy blonde", "silver", "strawberry blonde"
])

hairstyles = sorted([
    "blunt bob hairstyle", "long bob hairstyle", "messy bun hairstyle", "beach waves hairstyle", 
    "sleek straight hairstyle", "wavy lob hairstyle", "balayage hairstyle", "ombre hairstyle", 
    "Egyptian bob hairstyle", "half-up half-down hairstyle", "space buns hairstyle", 
    "long layers hairstyle", "high ponytail hairstyle", "bubble ponytail hairstyle", 
    "slicked back hairstyle", "shaggy layers hairstyle", "curtain bangs hairstyle", 
    "asymmetrical pixie hairstyle", "feathered layers hairstyle", "layered shag hairstyle",
    "afro hairstyle", "braided crown hairstyle", "buzz cut hairstyle", "chignon hairstyle", 
    "cornrows hairstyle", "dutch braids hairstyle", "fishtail braid hairstyle", 
    "french twist hairstyle", "mohawk hairstyle", "pixie cut hairstyle", "pompadour hairstyle", 
    "side swept bangs hairstyle", "top knot hairstyle", "updo hairstyle", 
    "victory rolls hairstyle"
])

dress_styles = sorted([
    "shift dress", "a-line dress", "ball gown", "sheath dress", "wrap dress", "maxi dress", 
    "midi dress", "mini dress", "bodycon dress", "fit and flare dress", "empire waist dress", 
    "peplum dress", "shirt dress", "halter neck dress", "off-the-shoulder dress", 
    "one-shoulder dress", "strapless dress", "high-low dress", "mermaid dress", "princess dress", 
    "tiered dress", "tunic dress", "chemise dress", "slip dress", "jumper dress", "cape dress", 
    "kimono dress", "corset dress", "flapper dress", "printed belted shirt dress", 
    "belted v-neck midi dress", "cotton padded t-shirt dress", "embroidered bell sleeve mini dress", 
    "open back chiffon midi dress", "printed chiffon midi dress", "printed chiffon mini dress", 
    "printed crêpe midi dress", "ribbed off-shoulder midi dress", "short-sleeve mini dress", 
    "sleeveless peplum mini dress", "sleeveless punto mini dress", "structured mini dress", 
    "striped padded t-shirt dress", "t-shirt midi dress", "textured flounced hem mini dress", 
    "3/4 sleeve crêpe midi dress", "lingerie set", "bodysuit", "corset and garter belt set", 
    "babydoll and chemise", "tailored blazer paired with trousers", "button-up shirt tucked into high-waisted pants", 
    "knit sweater layered over a collared shirt with trousers", "blouse with a pencil skirt and a belt", 
    "sleeveless top paired with wide-leg pants", "structured suit jacket with matching pants", 
    "cropped top paired with culottes", "crop top and mini skirt", "crop top and shorts", 
    "turtleneck sweater paired with tailored shorts", "sleeveless blouse tucked into a midi skirt", 
    "jacket layered over a tank top with jeans", "cardigan worn over a camisole with leggings", 
    "fitted top with a maxi skirt and a statement belt", "tunic top paired with leggings or jeggings", 
    "button-down shirt with tailored shorts", "crop top paired with high-waisted trousers", 
    "sweatshirt paired with joggers", "hoodie paired with cargo pants", "tank top paired with capri pants", 
    "t-shirt paired with Bermuda shorts", "turtleneck top layered under overalls", "one-piece swimsuit with floral print", 
    "high-waisted bikini with ruffled top", "sporty tankini set", "cutout monokini", "wrap-front bikini with sarong", 
    "classic triangle bikini with string ties", "retro halter-neck swimsuit", "color-blocked rash guard with board shorts", 
    "strapless bandeau bikini with side-tie bottoms", "mesh-panel swimsuit with plunging neckline", 
    "roleplay costume", "jumpsuit", "romper", "palazzo pants", "pinafore dress", "kaftan", 
    "boho dress", "sweater dress", "denim dress", "athleisure set (leggings and sports bra)", 
    "tracksuit", "culottes", "skort", "bolero jacket", "puffer jacket", "trench coat", "denim jacket"
])

dress_colours = sorted([
    "beige coloured", "black coloured", "blue coloured", "brown coloured", "charcoal coloured", 
    "chocolate coloured", "coral coloured", "crimson coloured", "forest green coloured", 
    "gold coloured", "gray coloured", "green coloured", "indigo coloured", "ivory coloured", 
    "lavender coloured", "lemon coloured", "magenta coloured", "maroon coloured", "mint coloured", 
    "navy coloured", "olive coloured", "orange coloured", "orchid coloured", "peach coloured", 
    "pink coloured", "purple coloured", "red coloured", "rose coloured", "royal blue coloured", 
    "salmon coloured", "slate coloured", "silver coloured", "sky blue coloured", "tan coloured", 
    "teal coloured", "turquoise coloured", "violet coloured", "white coloured", "yellow coloured",
    "aqua coloured", "burgundy coloured", "cyan coloured", "emerald coloured", "fuchsia coloured", 
    "khaki coloured", "lilac coloured", "mauve coloured", "mustard coloured", "periwinkle coloured", 
    "plum coloured", "ruby coloured", "scarlet coloured", "taupe coloured"
])

dress_patterns_textures = sorted([
    "abstract", "animal print", "batik", "brocade", "checkered", "chiffon", "cotton", "crochet", 
    "denim", "embroidery", "floral", "fringe", "geometric", "gingham", "houndstooth", "jacquard", 
    "jersey", "lace", "leather", "linen", "mesh", "ombre", "paisley", "plaid", "polka dots", 
    "polyester", "rayon", "ruffles", "satin", "seamless", "sequins", "silk", "stripes", "tartan", 
    "tie-dye", "tulle", "velvet", "zebra patterned", "argyle", "baroque", "cable knit", 
    "damask", "dobby", "eyelet", "faux fur", "herringbone", "matelassé", "organza", "piqué", 
    "quilted", "ribbed", "sheer", "smocked", "swiss dot", "tweed", "waffle knit"
])

# Function to preprocess lists
def preprocess_list(options):
    unique_options = sorted(set(options))
    return ["Random", "None"] + unique_options

ethnicities = preprocess_list(ethnicities)
haircolours = preprocess_list(haircolours)
hairstyles = preprocess_list(hairstyles)
dress_styles = preprocess_list(dress_styles)
dress_colours = preprocess_list(dress_colours)
dress_patterns_textures = preprocess_list(dress_patterns_textures)

class X_In_a_Dress:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
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
    FUNCTION = "generate_prompt"
    CATEGORY = "👑 MokkaBoss1/Text"

    def generate_prompt(self, seed, pre_text, post_text, gender, ethnicity, hair_colour, hair_style, dress_style, dress_colour, pattern_or_texture):
        def get_random_choice(option_list):
            return random.choice(option_list[2:]).lower()

        # Process each attribute
        if ethnicity == "Random":
            ethnicity = get_random_choice(ethnicities)
        elif ethnicity == "None":
            ethnicity = ""
            
        if hair_colour == "Random":
            hair_colour = get_random_choice(haircolours)
        elif hair_colour == "None":
            hair_colour = ""
            
        if hair_style == "Random":
            hair_style = get_random_choice(hairstyles)
        elif hair_style == "None":
            hair_style = ""
            hair_colour = ""
        
        if dress_style == "Random":
            dress_style = get_random_choice(dress_styles)
        
        if dress_colour == "Random":
            dress_colour = get_random_choice(dress_colours)
        elif dress_colour == "None":
            dress_colour = ""
        
        if pattern_or_texture == "Random":
            pattern_or_texture = get_random_choice(dress_patterns_textures)
        elif pattern_or_texture == "None":
            pattern_or_texture = ""
        
        if dress_style == "None":
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, {post_text}"
        else:
            positive_prompt = f"{pre_text} {ethnicity} {gender} with {hair_colour} {hair_style}, wearing a {dress_colour} {pattern_or_texture} {dress_style}, {post_text}"

        if seed == 999:
            positive_prompt = f"{pre_text} {post_text}"
        
        # Clean up prompt
        positive_prompt = re.sub(r'with  , ', '', positive_prompt)
        positive_prompt = re.sub(r'  ', ' ', positive_prompt).strip()

        print(positive_prompt)
        return [positive_prompt]

NODE_CLASS_MAPPINGS = {"X_In_a_Dress": X_In_a_Dress}
NODE_DISPLAY_NAME_MAPPINGS = {"X_In_a_Dress": "👑 X_In_a_Dress"}

