import random
import re
import folder_paths
import comfy.sd  # Import the necessary module containing `load_checkpoint_guess_config`
from ..model_settings.model_data import multi_field_list  # Import multi_field_list

class seveninabox:

    def __init__(self):
        pass

    RETURN_TYPES = ("INT", "FLOAT", comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "MODEL", "CLIP", "VAE", "STRING",)
    RETURN_NAMES = ("Steps", "cfg", "sampler", "scheduler", "MODEL", "CLIP", "VAE", "settings")
    FUNCTION = "load_checkpoint"

    CATEGORY = "👑 MokkaBoss1/Other"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),}}
    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))

        # add checkpoint name to the output tuple (without the ClipVisionModel)
        model = ckpt_name
        index = None
        for i, row in enumerate(multi_field_list):
            if model == row[1]:  
                index = i
                break
        
        if index is not None:
            print(f"Model '{model}' found at index {index}.")
            # Print out the fields of the found row
            print("Fields in the found row:")
            print("ID:", multi_field_list[index][0])
            print("Model:", multi_field_list[index][1])
            print("Steps:", multi_field_list[index][2])
            print("cfg:", multi_field_list[index][3])
            print("sampler:", multi_field_list[index][4])
            print("scheduler:", multi_field_list[index][5])
            
            steps = multi_field_list[index][2]
            cfg = multi_field_list[index][3]
            sampler = multi_field_list[index][4]
            scheduler = multi_field_list[index][5]
            ckpt_name = f"settings found and will be applied. Steps: {steps}, cfg: {cfg}, sampler: {sampler}, scheduler: {scheduler}"
            
        else:
               
            steps = int(20)
            cfg = float(7.0)
            sampler = "euler"
            scheduler = "normal"
            ckpt_name = f"settings not found - standrd settings will be applied. Steps 20, cfg 7, sampler euler, scheduler normal"
            
        out = (steps, cfg, sampler, scheduler, *out[:3], ckpt_name)
        return out

NODE_CLASS_MAPPINGS = {"seveninabox": seveninabox}
NODE_DISPLAY_NAME_MAPPINGS = {"seveninabox": "👑 7inabox(deprecated)"}
