# kudos to efficiency nodes for this one I can't take the credit
# however this is the original one before it was recently changed. As I prefer this one here you go....
# also I updated the x and y offset step to 1 for more precise positioning
# Mokkaboss1 5th May 2024

# ██████╗ ██╗   ██╗███████╗██████╗ ██╗      █████╗ ██╗   ██╗
#██╔═══██╗██║   ██║██╔════╝██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
#██║   ██║██║   ██║█████╗  ██████╔╝██║     ███████║ ╚████╔╝ 
#██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██╔══██║  ╚██╔╝  
#╚██████╔╝ ╚████╔╝ ███████╗██║  ██║███████╗██║  ██║   ██║   
# ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                           
from torch import Tensor
from PIL import Image, ImageOps, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo
import numpy as np
import torch

import ast
from pathlib import Path
from importlib import import_module
import os
import sys
import copy
import subprocess
import json
import psutil

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


# Get the absolute path of various directories
my_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_dir = os.path.abspath(os.path.join(my_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(my_dir, '..', '..'))

# Construct the path to the font file
font_path = os.path.join(my_dir, 'arial.ttf')

# Append comfy_dir to sys.path & import files
sys.path.append(comfy_dir)
from nodes import LatentUpscaleBy, KSampler, KSamplerAdvanced, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, \
    ImageScaleBy, CLIPSetLastLayer, CLIPTextEncode, ControlNetLoader, ControlNetApply, ControlNetApplyAdvanced, \
    PreviewImage, MAX_RESOLUTION
from comfy_extras.nodes_upscale_model import UpscaleModelLoader, ImageUpscaleWithModel
from comfy_extras.nodes_clip_sdxl import CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner
import comfy.sample
import comfy.samplers
import comfy.sd
import comfy.utils
import comfy.latent_formats
sys.path.remove(comfy_dir)

########################################################################################################################
# TSC Image Overlay
class Overlay:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_image": ("IMAGE",),
                "overlay_image": ("IMAGE",),
                "overlay_resize": (["None", "Fit", "Resize by rescale_factor", "Resize to width & heigth"],),
                "resize_method": (["nearest-exact", "bilinear", "area"],),
                "rescale_factor": ("FLOAT", {"default": 1, "min": 0.01, "max": 16.0, "step": 0.1}),
                "width": ("INT", {"default": 512, "min": 0, "max": MAX_RESOLUTION, "step": 64}),
                "height": ("INT", {"default": 512, "min": 0, "max": MAX_RESOLUTION, "step": 64}),
                "x_offset": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 1}),
                "y_offset": ("INT", {"default": 0, "min": -48000, "max": 48000, "step": 1}),
                "rotation": ("INT", {"default": 0, "min": -180, "max": 180, "step": 5}),
                "opacity": ("FLOAT", {"default": 0, "min": 0, "max": 100, "step": 5}),
            },
            "optional": {"optional_mask": ("MASK",),}
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_overlay_image"
    CATEGORY = "Efficiency Nodes/Image"

    def apply_overlay_image(self, base_image, overlay_image, overlay_resize, resize_method, rescale_factor,
                            width, height, x_offset, y_offset, rotation, opacity, optional_mask=None):

        # Pack tuples and assign variables
        size = width, height
        location = x_offset, y_offset
        mask = optional_mask

        # Check for different sizing options
        if overlay_resize != "None":
            #Extract overlay_image size and store in Tuple "overlay_image_size" (WxH)
            overlay_image_size = overlay_image.size()
            overlay_image_size = (overlay_image_size[2], overlay_image_size[1])
            if overlay_resize == "Fit":
                h_ratio = base_image.size()[1] / overlay_image_size[1]
                w_ratio = base_image.size()[2] / overlay_image_size[0]
                ratio = min(h_ratio, w_ratio)
                overlay_image_size = tuple(round(dimension * ratio) for dimension in overlay_image_size)
            elif overlay_resize == "Resize by rescale_factor":
                overlay_image_size = tuple(int(dimension * rescale_factor) for dimension in overlay_image_size)
            elif overlay_resize == "Resize to width & heigth":
                overlay_image_size = (size[0], size[1])

            samples = overlay_image.movedim(-1, 1)
            overlay_image = comfy.utils.common_upscale(samples, overlay_image_size[0], overlay_image_size[1], resize_method, False)
            overlay_image = overlay_image.movedim(1, -1)
            
        overlay_image = tensor2pil(overlay_image)

         # Add Alpha channel to overlay
        overlay_image = overlay_image.convert('RGBA')
        overlay_image.putalpha(Image.new("L", overlay_image.size, 255))

        # If mask connected, check if the overlay_image image has an alpha channel
        if mask is not None:
            # Convert mask to pil and resize
            mask = tensor2pil(mask)
            mask = mask.resize(overlay_image.size)
            # Apply mask as overlay's alpha
            overlay_image.putalpha(ImageOps.invert(mask))

        # Rotate the overlay image
        overlay_image = overlay_image.rotate(rotation, expand=True)

        # Apply opacity on overlay image
        r, g, b, a = overlay_image.split()
        a = a.point(lambda x: max(0, int(x * (1 - opacity / 100))))
        overlay_image.putalpha(a)

        # Split the base_image tensor along the first dimension to get a list of tensors
        base_image_list = torch.unbind(base_image, dim=0)

        # Convert each tensor to a PIL image, apply the overlay, and then convert it back to a tensor
        processed_base_image_list = []
        for tensor in base_image_list:
            # Convert tensor to PIL Image
            image = tensor2pil(tensor)

            # Paste the overlay image onto the base image
            if mask is None:
                image.paste(overlay_image, location)
            else:
                image.paste(overlay_image, location, overlay_image)

            # Convert PIL Image back to tensor
            processed_tensor = pil2tensor(image)

            # Append to list
            processed_base_image_list.append(processed_tensor)

        # Combine the processed images back into a single tensor
        base_image = torch.stack([tensor.squeeze() for tensor in processed_base_image_list])

        # Return the edited base image
        return (base_image,)
        
NODE_CLASS_MAPPINGS = {"Overlay": Overlay}
NODE_DISPLAY_NAME_MAPPINGS = {"Overlay": "👑 Overlay"}
