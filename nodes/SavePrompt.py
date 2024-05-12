# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ███████╗ █████╗ ██╗   ██╗███████╗██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
# ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
# ███████╗███████║██║   ██║█████╗  ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║   
# ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║   
# ███████║██║  ██║ ╚████╔╝ ███████╗██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║   
# ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   
                                                                                      
from datetime import datetime
import os
import folder_paths  # Ensure this module is correctly defined and available

def date_string(format):        
    now = datetime.now()
    return now.strftime(format)

def save_text_to_file(file_path, text):
    """
    Save the given text to a file at the specified path.
    Ensure the directory exists before saving.
    
    :param file_path: Path of the file where the text will be saved.
    :param text: The text content to be saved in the file.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if they don't exist
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text has been successfully saved to {file_path}.")
    except FileNotFoundError:
        print(f"Error: The directory {os.path.dirname(file_path)} does not exist.")
    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class SavePrompt:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "positive_prompt": ("STRING", {"default": "", "ForceInput": True}),
            "negative_prompt": ("STRING", {"default": "", "ForceInput": True}),
            "model_name": ("STRING", {"default": "", "ForceInput": True}),
            "sampler_name": ("STRING", {"default": "", "ForceInput": True}),
            "scheduler_name": ("STRING", {"default": "", "ForceInput": True}),
            "steps": ("INT", {"ForceInput": True}),
            "cfg": ("FLOAT", {"ForceInput": True}),
            "width": ("INT", {"ForceInput": True}),
            "height": ("INT", {"ForceInput": True}),
            "seed": ("INT", {"ForceInput": True}),
        }}

    RETURN_TYPES = ("STRING")
    RETURN_NAMES = ("save_string")
    FUNCTION = "SavePrompt"
    CATEGORY = "👑 MokkaBoss1/Other"

    def SavePrompt(self, positive_prompt, negative_prompt, model_name, sampler_name, scheduler_name, steps, cfg, width, height, seed): 
        ar = round(float(width) / float(height), 3)
        mp = round(float(width) * float(height) / (1024 * 1024), 3)
        part1 = f"Positive Prompt\n{positive_prompt}\n\nNegative Prompt\n{negative_prompt}\n\n"
        part2 = f"Dimensions\nWidth: {width}\nHeight: {height}\nAspect Ratio: {ar}\nMegapixels: {mp}\n\n"
        part3 = f"Generation Parameters\nModel Name: {model_name}\nSampler Name: {sampler_name}\nScheduler: {scheduler_name}\nSteps: {steps}\nCfg: {cfg}\nSeed: {seed}"
        save_string = part1 + part2 + part3

        format1 = "(%Y-%m-%d)(%H-%M-%S)"
        format2 = "(%Y-%m-%d)"
        
        path_initial = folder_paths.output_directory
        
        filename = date_string(format1)
        path = os.path.join(path_initial, date_string(format2), f"{date_string(format2)}_txt", f"{filename}.txt")
                        
        save_text_to_file(path, save_string)
        
        return (save_string, )

NODE_CLASS_MAPPINGS = {"SavePrompt": SavePrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"SavePrompt": "👑 SavePrompt"}

