# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ███╗   ███╗ ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███████╗███████╗ ██╗    ██╗███╗   ██╗██╗████████╗
# ████╗ ████║██╔═══██╗██║ ██╔╝██║ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝███║    ██║████╗  ██║██║╚══██╔══╝
# ██╔████╔██║██║   ██║█████╔╝ █████╔╝ ███████║██████╔╝██║   ██║███████╗███████╗╚██║    ██║██╔██╗ ██║██║   ██║   
# ██║╚██╔╝██║██║   ██║██╔═██╗ ██╔═██╗ ██╔══██║██╔══██╗██║   ██║╚════██║╚════██║ ██║    ██║██║╚██╗██║██║   ██║   
# ██║ ╚═╝ ██║╚██████╔╝██║  ██╗██║  ██╗██║  ██║██████╔╝╚██████╔╝███████║███████║ ██║    ██║██║ ╚████║██║   ██║   
# ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝ ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   
                                                                                                              
from ComfyUI_Mokkaboss1.nodes.DoubleClipTextEncode import DoubleClipTextEncode
from ComfyUI_Mokkaboss1.nodes.HashText import HashText
from ComfyUI_Mokkaboss1.nodes.IndoorBackgrounds import IndoorBackgrounds
from ComfyUI_Mokkaboss1.nodes.LandscapeBackgrounds import LandscapeBackgrounds
from ComfyUI_Mokkaboss1.nodes.OptimalCrop import OptimalCrop
from ComfyUI_Mokkaboss1.nodes.X_In_a_Dress import X_In_a_Dress
from ComfyUI_Mokkaboss1.nodes.X_In_a_Suit import X_In_a_Suit
from ComfyUI_Mokkaboss1.nodes.WrapText import WrapText
from ComfyUI_Mokkaboss1.nodes.AspectRatioCondition import AspectRatioCondition
from ComfyUI_Mokkaboss1.nodes.SDXLEmptyLatent import SDXLEmptyLatent
from ComfyUI_Mokkaboss1.nodes.ZoomCrop import ZoomCrop
from ComfyUI_Mokkaboss1.nodes.IntFloatDict import IntFloatDict
from ComfyUI_Mokkaboss1.nodes.WorkflowSettings import WorkflowSettings
from ComfyUI_Mokkaboss1.nodes.IntStringDict import IntStringDict
from ComfyUI_Mokkaboss1.nodes.ConnectImage import ConnectImage
from ComfyUI_Mokkaboss1.nodes.ConnectString import ConnectString
from ComfyUI_Mokkaboss1.nodes.ConnectInteger import ConnectInteger
from ComfyUI_Mokkaboss1.nodes.ConnectFloat import ConnectFloat
from ComfyUI_Mokkaboss1.nodes.ConnectLatent import ConnectLatent
from ComfyUI_Mokkaboss1.nodes.TimeStamp import TimeStamp
from ComfyUI_Mokkaboss1.nodes.SaveWithMetaData import SaveWithMetaData
from ComfyUI_Mokkaboss1.nodes.SaveWithMetaData2 import SaveWithMetaData2
from ComfyUI_Mokkaboss1.nodes.TricolorComposition import TricolorComposition
from ComfyUI_Mokkaboss1.nodes.Colors import Colors
from ComfyUI_Mokkaboss1.nodes.HueSatLum import HueSatLum
from ComfyUI_Mokkaboss1.nodes.EmbeddingLoader import EmbeddingLoader
from ComfyUI_Mokkaboss1.nodes.ImageDimensions import ImageDimensions
from ComfyUI_Mokkaboss1.nodes.SimplePrompts import SimplePrompts
from ComfyUI_Mokkaboss1.nodes.IntEvaluate import IntEvaluate
from ComfyUI_Mokkaboss1.nodes.ImageResizeLong import ImageResizeLong
from ComfyUI_Mokkaboss1.nodes.PhotomontageA import PhotomontageA
from ComfyUI_Mokkaboss1.nodes.PhotomontageB import PhotomontageB
from ComfyUI_Mokkaboss1.nodes.PhotomontageC import PhotomontageC
from ComfyUI_Mokkaboss1.nodes.PostSamplerCrop import PostSamplerCrop
from ComfyUI_Mokkaboss1.nodes.Mbsampler import Mbsampler
from ComfyUI_Mokkaboss1.nodes.Overlay import Overlay
from ComfyUI_Mokkaboss1.nodes.HueShift import HueShift
from ComfyUI_Mokkaboss1.nodes.FuseImages import FuseImages
from ComfyUI_Mokkaboss1.nodes.FuseImages2 import FuseImages2
from ComfyUI_Mokkaboss1.nodes.StringJoin import StringJoin
from ComfyUI_Mokkaboss1.nodes.SearchReplace import SearchReplace
from ComfyUI_Mokkaboss1.nodes.SavePrompt import SavePrompt
from ComfyUI_Mokkaboss1.nodes.PresetSave import PresetSave
from ComfyUI_Mokkaboss1.nodes.PresetLoad import PresetLoad
from ComfyUI_Mokkaboss1.nodes.PresetRemove import PresetRemove
from ComfyUI_Mokkaboss1.nodes.RandomString import RandomString
from ComfyUI_Mokkaboss1.nodes.JsonSearch import JsonSearch
from ComfyUI_Mokkaboss1.nodes.PromptSwitcher import PromptSwitcher
from ComfyUI_Mokkaboss1.nodes.imageborder import imageborder
from ComfyUI_Mokkaboss1.nodes.StopWorkflow import StopWorkflow

NODE_CLASS_MAPPINGS = {
    "DoubleClipTextEncode": DoubleClipTextEncode,
    "HashText": HashText,
    "IndoorBackgrounds": IndoorBackgrounds,   
    "LandscapeBackgrounds": LandscapeBackgrounds,
    "OptimalCrop": OptimalCrop,
    "X_In_a_Dress": X_In_a_Dress,
    "X_In_a_Suit": X_In_a_Suit,
    "WrapText": WrapText,
    "AspectRatioCondition": AspectRatioCondition,
    "SDXLEmptyLatent": SDXLEmptyLatent,
    "ZoomCrop": ZoomCrop,
    "IntFloatDict": IntFloatDict,
    "WorkflowSettings": WorkflowSettings,
    "IntStringDict": IntStringDict,
    "ConnectImage": ConnectImage,
    "ConnectInteger": ConnectInteger,
    "ConnectString": ConnectString,
    "ConnectFloat": ConnectFloat,
    "ConnectLatent": ConnectLatent,
    "TimeStamp": TimeStamp,
    "SaveWithMetaData": SaveWithMetaData,
    "SaveWithMetaData2": SaveWithMetaData2,
    "TricolorComposition": TricolorComposition,
    "Colors": Colors,
    "HueSatLum": HueSatLum,
    "EmbeddingLoader": EmbeddingLoader,
    "ImageDimensions": ImageDimensions,
    "SimplePrompts": SimplePrompts,
    "IntEvaluate": IntEvaluate,
    "ImageResizeLong": ImageResizeLong,
    "PhotomontageA": PhotomontageA,
    "PhotomontageB": PhotomontageB,
    "PhotomontageC": PhotomontageC,
    "PostSamplerCrop": PostSamplerCrop,
    "Mbsampler": Mbsampler,
    "Overlay": Overlay,
    "HueShift": HueShift,
    "FuseImages": FuseImages,
    "FuseImages2": FuseImages2,
    "StringJoin": StringJoin,
    "SearchReplace": SearchReplace,
    "SavePrompt": SavePrompt,
    "PresetSave": PresetSave,
    "PresetLoad": PresetLoad,
    "PresetRemove": PresetRemove,
    "JsonSearch": JsonSearch,
    "RandomString": RandomString,
    "PromptSwitcher": PromptSwitcher,
    "imageborder": imageborder,
    "StopWorkflow": StopWorkflow,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DoubleClipTextEncode": "👑 DoubleClipTextEncode",
    "HashText": "👑 HashText",
    "IndoorBackgrounds": "👑 IndoorBackgrounds",
    "LandscapeBackgrounds": "👑 LandscapeBackgrounds",
    "OptimalCrop": "👑 OptimalCrop",
    "X_In_a_Dress": "👑 X_In_a_Dress",
    "X_In_a_Suit": "👑 X_In_a_Suit",
    "WrapText": "👑 WrapText",
    "AspectRatioCondition": "👑 AspectRatioCondition",
    "SDXLEmptyLatent": "👑 SDXLEmptyLatent",
    "ZoomCrop": "👑 ZoomCrop",
    "IntFloatDict": "👑 IntFloatDict",
    "WorkflowSettings": "👑 WorkflowSettings",
    "IntStringDict": "👑 IntStringDict",
    "ConnectImage": "👑 ConnectImage",
    "ConnectInteger": "👑 ConnectInteger",
    "ConnectString": "👑 ConnectString",
    "ConnectFloat": "👑 ConnectFloat",
    "ConnectLatent": "👑 ConnectLatent",
    "TimeStamp": "👑 TimeStamp",
    "SaveWithMetaData": "👑 SaveWithMetaData",
    "SaveWithMetaData2": "👑 SaveWithMetaData2",
    "TricolorComposition": "👑 TricolorComposition",
    "Colors":"👑 Colors",
    "HueSatLum": "👑 HueSatLum",
    "EmbeddingLoader": "👑 EmbeddingLoader",
    "ImageDimensions": "👑 ImageDimensions",
    "SimplePrompts": "👑 SimplePrompts",
    "IntEvaluate": "👑 IntEvaluate",
    "ImageResizeLong": "👑 ImageResizeLong",
    "PhotomontageA": "👑 PhotomontageA",
    "PhotomontageB": "👑 PhotomontageB",
    "PhotomontageC": "👑 PhotomontageC",
    "PostSamplerCrop": "👑 PostSamplerCrop",
    "Mbsampler": "👑 Mbsampler",
    "Overlay": "👑 Overlay",
    "HueShift": "👑 HueShift",
    "FuseImages": "👑 FuseImages",
    "FuseImages2": "👑 FuseImages2",
    "StringJoin": "👑 StringJoin",
    "SearchReplace": "👑 SearchReplace",
    "SavePrompt": "👑 SavePrompt",
    "PresetSave": "👑 PresetSave",
    "PresetLoad": "👑 PresetLoad",
    "PresetRemove": "👑 PresetRemove",
    "JsonSearch": "👑 JsonSearch",
    "RandomString": "👑 RandomString",
    "PromptSwitcher": "👑 PromptSwitcher",
    "imageborder": "👑 imageborder",
    "StopWorkflow": "👑 StopWorkflow",
}
print ("👑 Mokkaboss1 47 Custom Nodes: Loaded")
