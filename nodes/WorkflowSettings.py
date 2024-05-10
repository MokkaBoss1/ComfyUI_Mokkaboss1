# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗██╗      ██████╗ ██╗    ██╗███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
# ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║     ██╔═══██╗██║    ██║██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
# ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║     ██║   ██║██║ █╗ ██║███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
# ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║     ██║   ██║██║███╗██║╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
# ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║     ███████╗╚██████╔╝╚███╔███╔╝███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                                                                                      
import random
import re
import folder_paths
import comfy.sd  # Import the necessary module containing `load_checkpoint_guess_config`
#from ..model_settings.model_data import multi_field_list  # Import multi_field_list.

# Attempt to import hide_sampler from a file two directories up
try:
    import sys
    sys.path.append('../../../')  # Adds the directory two levels up to the path
    from mokkaboss1_workflowsettings import hide_sampler
    from mokkaboss1_workflowsettings import hide_parameters
except ImportError:
    hide_sampler = 0
    hide_parameters = 0
finally:
    sys.path.remove('../../../')  # Clean up by removing the added path

parameters = """0,devlishphotorealism_sdxl15.safetensors,30,4.0,dpmpp_2m_sde,karras
1,sdxlUnstableDiffusers_v8HEAVENSWRATH.safetensors,30,4.0,dpmpp_2m_sde,karras
2,lovexlAllInOneMega_v20.safetensors,30,4.0,dpmpp_2m_sde,karras
3,juggernautXL_v9Rdphoto2Lightning.safetensors,5,1.5,dpmpp_sde,karras
4,dreamshaperXL_v21TurboDPMSDE.safetensors,6,2.0,dpmpp_sde,karras
5,devlish LoveXL 050.safetensors,30,4.0,dpmpp_2m_sde,karras
6,sdxlUnstableDiffusers_v11.safetensors,30,4.0,dpmpp_2m_sde,karras
7,DEVLISH LIGHTNING.safetensors,5,1.5,dpmpp_sde,karras
8,sdxlUnstableDiffusers_nihilmania.safetensors,30,4.0,dpmpp_2m_sde,karras
9,realvisxlV40_v40Bakedvae.safetensors,30,4.0,dpmpp_2m,karras
10,realvisxlV40_v40LightningBakedvae.safetensors,5,1.5,dpmpp_sde,karras
11,juggernautXL_v8Rundiffusion.safetensors,30,4.0,dpmpp_2m,karras
12,amuz_v30.safetensors,30,4.0,dpmpp_2m_sde_gpu,karras
13,CHEYENNE_v16.safetensors,30,4.0,dpmpp_2m_sde_gpu,karras
14,devlish loveXL 050.safetensors,30,4.0,dpmpp_2m_sde_gpu,karras
15,loveXL Lightning.safetensors,8,1.5,dpmpp_sde,karras
16,Cheyenne Devlish Amz.safetensors,30,4.0,dpmpp_2m_sde_gpu,karras
"""

class WorkflowSettings:

    def __init__(self):
        pass

    if hide_sampler == 0:
        RETURN_TYPES = ("INT", "FLOAT", comfy.samplers.KSampler.SAMPLERS, "STRING", comfy.samplers.KSampler.SCHEDULERS, "STRING", "STRING", "MODEL", "CLIP", "VAE", "STRING",)
        RETURN_NAMES = ("chosen_steps", "chosen_cfg", "chosen_sampler", "sampler_string", "chosen_scheduler", "scheduler_string", "modelname_string", "MODEL", "CLIP", "VAE", "settings")
    else:
        RETURN_TYPES = ("INT", "FLOAT", "STRING", "STRING", "STRING", "MODEL", "CLIP", "VAE", "STRING",)
        RETURN_NAMES = ("chosen_steps", "chosen_cfg", "sampler_string", "scheduler_string", "modelname_string", "MODEL", "CLIP", "VAE", "settings")
    FUNCTION = "load_checkpoint"
    CATEGORY = "👑 MokkaBoss1/Other"
    
    @classmethod
    def INPUT_TYPES(cls):
        if hide_parameters == 0:     
            return {
                "required": {
                    "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                    "text_value": ("STRING", {"multiline": True, "default": "0,juggernautXL_v9Rdphoto2Lightning.safetensors,5,1.5,dpmpp_sde,karras"}),
                },
            }
        else:
            return {
                "required": {
                    "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                    "text_value": ("STRING", {"multiline": True, "default": parameters}),
                },
            }
        
    
        
    
    def load_checkpoint(self, ckpt_name, text_value, output_vae=True, output_clip=True):
        
        
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        

        multi_line_string = text_value
        result_dict = {}

        lines = multi_line_string.strip().split('\n')

        for line in lines:
            parts = line.strip().split(',')
            
            if len(parts) == 6:  # Ensure there are 6 parts in the line
                try:
                    line_key = int(parts[0])  # Convert the first part to an integer for the key
                    modelname = parts[1]
                    steps = int(parts[2])
                    cfg = float(parts[3])
                    sampler = parts[4]
                    scheduler = parts[5]
                    
                    # Create a tuple with extracted values
                    value_tuple = (modelname, steps, cfg, sampler, scheduler)
                    result_dict[line_key] = value_tuple
                except (ValueError, IndexError):
                    pass  # Ignore lines that cannot be converted as expected
        
        # Look up the ckpt_name in the dictionary and return corresponding value
        chosen_modelname = None
        chosen_steps = None
        chosen_cfg = None
        chosen_sampler = None
        chosen_scheduler = None
        scheduler_string = ""
        sampler_string = ""
        modelname_string = ""

        # Check if the specified modelname exists in the dictionary
        for key, values in result_dict.items():
            if values[0] == ckpt_name: 
                chosen_modelname = values[0]
                if len(values) > 1:
                    chosen_steps = values[1]
                if len(values) > 2:
                    chosen_cfg = values[2]
                if len(values) > 3:
                    chosen_sampler = values[3]
                if len(values) > 4:
                    chosen_scheduler = values[4]
                break  # Found the desired line, no need to continue searching
        model_found = "Model could be identified from the text field"
        if chosen_modelname is None:
            model_found = "The model could not be identified from the text field: Check the proper structure of the data (resulting to default settings)"
            first_line_values = next(iter(result_dict.values()), None)
            if first_line_values:
                chosen_modelname = first_line_values[0]
                if len(first_line_values) > 1:
                    chosen_steps = first_line_values[1]
                if len(first_line_values) > 2:
                    chosen_cfg = first_line_values[2]
                if len(first_line_values) > 3:
                    chosen_sampler = first_line_values[3]
                if len(first_line_values) > 4:
                    chosen_scheduler = first_line_values[4]
        
        scheduler_string = str(chosen_scheduler)
        sampler_string = str(chosen_sampler)
        modelname_string = str(chosen_modelname)
        
        
        settings = f"{model_found}: model: {ckpt_name}, steps: {chosen_steps}, cfg: {chosen_cfg}, sampler: {chosen_sampler}, scheduler: {chosen_scheduler}" 

        if hide_sampler == 0:
            out = (chosen_steps, chosen_cfg, chosen_sampler, sampler_string, chosen_scheduler, scheduler_string, modelname_string, *out[:3], settings)
        
        else:
            out = (chosen_steps, chosen_cfg, sampler_string, scheduler_string, modelname_string, *out[:3], settings)
        return out

# Now you can use chosen_modelname, chosen_steps, chosen_cfg, chosen_sampler, and chosen_scheduler as needed

NODE_CLASS_MAPPINGS = {"WorkflowSettings": WorkflowSettings}
NODE_DISPLAY_NAME_MAPPINGS = {"WorkflowSettings": "👑 WorkflowSettings"}



