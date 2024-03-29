# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
import random
import re
import folder_paths
import comfy.sd  # Import the necessary module containing `load_checkpoint_guess_config`

multi_field_list = [
    [0, 'devlishphotorealism_sdxl15.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [1, 'sdxlUnstableDiffusers_v8HEAVENSWRATH.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [2, 'lovexlAllInOneMega_v20.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [3, 'juggernautXL_v9Rdphoto2Lightning.safetensors', 5, 1.5, 'dpmpp_sde', 'karras'],
    [4, 'dreamshaperXL_v21TurboDPMSDE.safetensors', 6, 2.0, 'dpmpp_sde', 'karras'],
    [5, 'devlish LoveXL 050.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [6, 'sdxlUnstableDiffusers_v11.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [7, 'DEVLISH LIGHTNING.safetensors', 5, 1.5, 'dpmpp_sde', 'karras'],
    [8, 'sdxlUnstableDiffusers_nihilmania.safetensors', 30, 4.0, 'dpmpp_2m_sde', 'karras'],
    [9, 'realvisxlV40_v40Bakedvae.safetensors', 30, 4.0, 'dpmpp_2m', 'karras'],
    [10, 'realvisxlV40_v40LightningBakedvae.safetensors', 5, 1.5, 'dpmpp_sde', 'karras'],
    [11, 'juggernautXL_v8Rundiffusion.safetensors', 30, 4.0, 'dpmpp_2m', 'karras']
    
    # Add more rows as needed
]

class seveninabox:

    def __init__(self):
        pass

    RETURN_TYPES = ("INT", "FLOAT", comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "MODEL", "CLIP", "VAE", "STRING",)
    RETURN_NAMES = ("Steps", "cfg", "sampler", "scheduler", "MODEL", "CLIP", "VAE", "settings")
    FUNCTION = "load_checkpoint"

    CATEGORY = "👑 MokkaBoss1"

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
NODE_DISPLAY_NAME_MAPPINGS = {"seveninabox": "👑 7 in a box"}
