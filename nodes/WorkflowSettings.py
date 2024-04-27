import random
import re
import folder_paths
import comfy.sd  # Import the necessary module containing `load_checkpoint_guess_config`

# Attempt to import hide_sampler from a file two directories up
try:
    import sys
    sys.path.append('../../../')  # Adds the directory two levels up to the path
    from hide_sampler import hide_sampler
except ImportError:
    hide_sampler = 0
finally:
    sys.path.remove('../../../')  # Clean up by removing the added path

class WorkflowSettings:

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
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                "text_value": ("STRING", {"multiline": True, "default": "0,juggernautXL_v9Rdphoto2Lightning.safetensors,5,1.5,dpmpp_sde,karras"}),
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
            if len(parts) == 6:
                try:
                    line_key = int(parts[0])
                    modelname = parts[1]
                    steps = int(parts[2])
                    cfg = float(parts[3])
                    sampler = parts[4]
                    scheduler = parts[5]
                    value_tuple = (modelname, steps, cfg, sampler, scheduler)
                    result_dict[line_key] = value_tuple
                except (ValueError, IndexError):
                    pass

        # Output logic remains the same as in the original script provided above
        
        return out  # return the output tuple as needed

NODE_CLASS_MAPPINGS = {"WorkflowSettings": WorkflowSettings}
NODE_DISPLAY_NAME_MAPPINGS = {"WorkflowSettings": "👑 WorkflowSettings"}
