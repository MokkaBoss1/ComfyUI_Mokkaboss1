# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ███████╗███╗   ███╗██████╗ ███████╗██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
# ██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
# █████╗  ██╔████╔██║██████╔╝█████╗  ██║  ██║██║  ██║██║██╔██╗ ██║██║  ███╗██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
# ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██║  ██║██║  ██║██║██║╚██╗██║██║   ██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
# ███████╗██║ ╚═╝ ██║██████╔╝███████╗██████╔╝██████╔╝██║██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
# ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                          


import random
import re
import folder_paths
import comfy.sd  # Import the necessary module containing `load_checkpoint_guess_config`
#from ..model_settings.model_data import multi_field_list  # Import multi_field_list.

class EmbeddingLoader:

    def __init__(self):
        pass

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "emb_loader"
    CATEGORY = "👑 MokkaBoss1/Other"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "embedding_name": ("STRING", {"multiline": False, "default": ""}),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.1}),
                "text_value": ("STRING", {"multiline": True, "default": "Color Palettes XL, RBW-XL.pt, RBW-XL"}),
#                "daisy_chain_text": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    def emb_loader(self, embedding_name, strength, text_value,):
    # Initialize variables to store chosen values
    
        chosen_embedding_modelname = None
        chosen_embedding_filename = None
        chosen_embedding_keywords = None
        
        # Split the text_value into lines
        lines = text_value.strip().split('\n')
        
        # Iterate over each line
        for line in lines:
            # Split the line by comma
            parts = line.strip().split(',')
            
            # Check if the line has at least 3 parts
            if len(parts) >= 3:
                # Extract values from the line
                embedding_modelname = parts[0]
                embedding_filename = parts[1]
                embedding_keywords = ','.join(parts[2:])  # Join remaining parts as keywords
                
                # Check if the embedding_name matches the model name in the line
                if embedding_modelname == embedding_name:
                             
                    # Construct the embedding string
                    print(f"""(embedding:{embedding_filename}:{strength}), {embedding_keywords},""")
                    embedding_string = f"""(embedding:{embedding_filename}:{strength}), {embedding_keywords},"""
                    
                    # No need to continue searching if a match is found
                    break
                else:
                    print ("did not find the embedding")
                    embedding_string = ""
 
        
        # Return the embedding string
        return (embedding_string,)


NODE_CLASS_MAPPINGS = {"EmbeddingLoader": EmbeddingLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"EmbeddingLoader": "👑 EmbeddingLoader"}



#=================================================
#
# My Embeddings
#
#=================================================
# Color Palettes XL, RBW-XL.pt, RBW-XL (https://civitai.com/models/369342/color-palettes-xl)
# CharTurner, charturnerv2.pt, charturnerv2 (https://civitai.com/models/3036?modelVersionId=8387)
# Daisy Ridley - Embedding, emb-daisy.pt, emb-daisy (https://civitai.com/models/6147?modelVersionId=7191)
# Empire Style, style-empire.pt,style-empire, (https://civitai.com/models/2032/empire-style)
# Empire Style XL, Empire_SDXL_OnSite.safetensors, Victorian London Empire, (https://civitai.com/models/141328/empire-style-xl)
# Atompunk Style, atompunkstylesd15.pt, atompunkstylesd15 (https://civitai.com/models/26250/atompunk-style)
# Style Sylva Magic, style-sylvamagic.pt, style-sylvamagic, (https://civitai.com/models/7523/style-sylva-magic)
# Style Paint Magic, style-paintmagic.pt, style-paintmagic, (https://civitai.com/models/18052/style-paint-magic)
# Glorious Style, Style-Glorious.pt, Style-Glorious, (https://civitai.com/models/2110/glorious-style)
# Coloring Book Style, coloring-book-style.pt, coloring-book-style, (https://civitai.com/models/49040/coloring-book-style)
# Hieronymus Bosch Style embedding, bosch.safetensors, bosch, (https://civitai.com/models/325971/hieronymus-bosch-style-embedding?modelVersionId=365396)
# Dark World Dreams, dw01-3400.safetensors, dw01-3400, (https://civitai.com/models/243600/dark-world-dreams?modelVersionId=274855)
# CrystaliTIXL, cs-cr1stal-v2.safetensors, cs-cr1stal-v2, (https://civitai.com/models/139230/crystalitixl?modelVersionId=371565)
# Metallicity, cs-m3tal-ok_v06-1000.safetensors, cs-m3tal-ok_v06-1000, (https://civitai.com/models/295776/metallicity?modelVersionId=353500)
# Ultimate Text Embeddings SDXL Pack (Digitial Art), SK_DIGITALART.safetensors, SK_DIGITALART, (https://civitai.com/models/148131?modelVersionId=167640)
# Ultimate Text Embeddings SDXL Pack (Vector Art), SK_VECTORART.safetensors, SK_VECTORART, (https://civitai.com/models/148131?modelVersionId=167642)
# 