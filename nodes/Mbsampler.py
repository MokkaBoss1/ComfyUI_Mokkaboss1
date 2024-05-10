
# ███╗   ███╗██████╗ ███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
# ████╗ ████║██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
# ██╔████╔██║██████╔╝███████╗███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
# ██║╚██╔╝██║██╔══██╗╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██╗
# ██║ ╚═╝ ██║██████╔╝███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║
# ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                              



import torch
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

import comfy.samplers
import comfy.sample
import comfy.model_management
import comfy.utils
import latent_preview

def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0,
                    disable_noise=False, start_step=None, last_step=None, force_full_denoise=False,
                    preview_latent=True, disable_pbar=False, custom=None):
    device = comfy.model_management.get_torch_device()

    if isinstance(latent, dict):
        samples_tensor = latent.get("samples")
        noise_mask = latent.get("noise_mask")
    else:
        raise TypeError(f"Expected 'latent' to be a dictionary, but got type {type(latent).__name__}")

    preview_format = "JPEG"
    if preview_format not in ["JPEG", "PNG"]:
        preview_format = "JPEG"

    previewer = False
    if preview_latent:
        previewer = latent_preview.get_previewer(device, model.model.latent_format)

    pbar = comfy.utils.ProgressBar(steps)

    def callback(step, x0, x, total_steps):
        preview_bytes = None
        if previewer:
            preview_bytes = previewer.decode_latent_to_preview_image(preview_format, x0)
        pbar.update_absolute(step + 1, total_steps, preview_bytes)

    if custom is not None:
        guider = custom['guider'] if 'guider' in custom else None
        sampler = custom['sampler'] if 'sampler' in custom else None
        sigmas = custom['sigmas'] if 'sigmas' in custom else None
        noise = custom['noise'] if 'noise' in custom else None
        samples = guider.sample(noise.generate_noise(samples_tensor), samples_tensor, sampler, sigmas,
                                denoise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar,
                                seed=noise.seed)
        samples = samples.to(comfy.model_management.intermediate_device())
    else:
        if disable_noise:
            noise = torch.zeros(samples_tensor.size(), dtype=samples_tensor.dtype, layout=samples_tensor.layout, device="cpu")
        else:
            batch_inds = latent.get("batch_index")
            noise = comfy.sample.prepare_noise(samples_tensor, seed, batch_inds)

        samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative,
                                      samples_tensor, denoise=denoise, disable_noise=disable_noise, start_step=start_step,
                                      last_step=last_step, force_full_denoise=force_full_denoise, noise_mask=noise_mask,
                                      callback=callback, disable_pbar=disable_pbar, seed=seed)

    latent["samples"] = samples
    return latent

class Mbsampler:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"model": ("MODEL",),
                             "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                             "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "forceInput":True}),
                             "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step": 0.1, "round": 0.01, "forceInput":True}),
                             "sampler_string": ("STRING", {"default": '', "multiline": False, "forceInput":True}),
                             "scheduler_string": ("STRING", {"default": '', "multiline": False, "forceInput":True}),
                             "positive": ("CONDITIONING",),
                             "negative": ("CONDITIONING",),
                             "latent": ("LATENT",),
                             "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01})}}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "👑 MokkaBoss1/Other"

    @classmethod
    def sample(cls, model, seed, steps, cfg, sampler_string, scheduler_string, positive, negative, latent, denoise=1.0):
        
        if sampler_string != "":
            #check if sampler_string is an allowed value within the sampler list
            is_in_samplers = sampler_string in comfy.samplers.KSampler.SAMPLERS

            if is_in_samplers:
                #print(f"{sampler_string} is in the list of samplers.")
                sampler_name = sampler_string
            #else:
                #print(f"{sampler_string} is not in the list of samplers.")
                
        if scheduler_string != "":
            #check if scheduler_string is an allowed value within the scheduler list
            is_in_schedulers = scheduler_string in comfy.samplers.KSampler.SCHEDULERS

            if is_in_schedulers:
                #print(f"{scheduler_string} is in the list of schedulers.")
                scheduler = scheduler_string
            #else:
                #print(f"{scheduler_string} is not in the list of schedulers.")
        
        #print (f"The sampler applied is: {sampler_name}. The scheduler applied is: {scheduler}")
            
        common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=denoise)
    
        return (latent,)
    
NODE_CLASS_MAPPINGS = {"Mbsampler": Mbsampler}
NODE_DISPLAY_NAME_MAPPINGS = {"Mbsampler": "👑 MB Sampler"}
