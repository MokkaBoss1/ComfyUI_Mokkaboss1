#---------------------------------------------------------------------------------------------------------------------#
import torch
import numpy as np
import os
import sys
import csv
import comfy.sd
import json
import folder_paths
import typing as tg
import datetime
import io
from server import PromptServer, BinaryEventTypes
#from nodes import common_ksampler
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from pathlib import Path


#---------------------------------------------------------------------------------------------------------------------#
# Core Nodes
#---------------------------------------------------------------------------------------------------------------------#

class DoubleConditioningMixer:

    @classmethod
    def INPUT_TYPES(cls):
        mix_methods = ["Combine", "Average", "Concatenate"]
        return {"required":
                    {"conditioning_1a": ("CONDITIONING", ),
                     "conditioning_1b": ("CONDITIONING", ),
                     "conditioning_2a": ("CONDITIONING", ),
                     "conditioning_2b": ("CONDITIONING", ),
                     "mix_method": (mix_methods, ),
                     "average_strength": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                    }
               }

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "STRING", )
    RETURN_NAMES = ("CONDITIONING_1", "CONDITIONING_2", "show_help", )
    FUNCTION = "conditioning"
    CATEGORY = "👑 MokkaBoss1/Text"

    def conditioning(self, mix_method, conditioning_1a, conditioning_1b, conditioning_2a, conditioning_2b, average_strength):
        def mix_conditionings(cond_from, cond_to, method, strength):
            if method == "Combine":
                return cond_from + cond_to
            
            if method == "Average":
                out = []
                if len(cond_from) > 1:
                    print("Warning: ConditioningAverage cond_from contains more than 1 cond, only the first one will be applied.")

                base_cond = cond_from[0][0]
                pooled_output_from = cond_from[0][1].get("pooled_output", None)

                for i in range(len(cond_to)):
                    target_cond = cond_to[i][0]
                    pooled_output_to = cond_to[i][1].get("pooled_output", pooled_output_from)
                    truncated_base = base_cond[:, :target_cond.shape[1]]
                    if truncated_base.shape[1] < target_cond.shape[1]:
                        truncated_base = torch.cat([truncated_base] + [torch.zeros((1, (target_cond.shape[1] - truncated_base.shape[1]), target_cond.shape[2]))], dim=1)

                    blended = torch.mul(target_cond, strength) + torch.mul(truncated_base, (1.0 - strength))
                    updated_meta = cond_to[i][1].copy()

                    if pooled_output_from is not None and pooled_output_to is not None:
                        updated_meta["pooled_output"] = torch.mul(pooled_output_to, strength) + torch.mul(pooled_output_from, (1.0 - strength))
                    elif pooled_output_from is not None:
                        updated_meta["pooled_output"] = pooled_output_from

                    out.append([blended, updated_meta])
                return out

            if method == "Concatenate":
                out = []
                if len(cond_from) > 1:
                    print("Warning: ConditioningConcat cond_from contains more than 1 cond, only the first one will be applied.")

                base_cond = cond_from[0][0]

                for i in range(len(cond_to)):
                    target_cond = cond_to[i][0]
                    concatenated = torch.cat((target_cond, base_cond), 1)
                    updated_meta = cond_to[i][1].copy()
                    out.append([concatenated, updated_meta])
                return out

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-conditioning-mixer"

        output_1 = mix_conditionings(conditioning_1a, conditioning_1b, mix_method, average_strength)
        output_2 = mix_conditionings(conditioning_2a, conditioning_2b, mix_method, average_strength)

        return (output_1, output_2, show_help)

NODE_CLASS_MAPPINGS = {"DoubleConditioningMixer": DoubleConditioningMixer}
NODE_DISPLAY_NAME_MAPPINGS = {"DoubleConditioningMixer": "👑 DoubleConditioningMixer"}
