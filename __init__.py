# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ███╗   ███╗ ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███████╗███████╗ ██╗    ██╗███╗   ██╗██╗████████╗
# ████╗ ████║██╔═══██╗██║ ██╔╝██║ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝███║    ██║████╗  ██║██║╚══██╔══╝
# ██╔████╔██║██║   ██║█████╔╝ █████╔╝ ███████║██████╔╝██║   ██║███████╗███████╗╚██║    ██║██╔██╗ ██║██║   ██║   
# ██║╚██╔╝██║██║   ██║██╔═██╗ ██╔═██╗ ██╔══██║██╔══██╗██║   ██║╚════██║╚════██║ ██║    ██║██║╚██╗██║██║   ██║   
# ██║ ╚═╝ ██║╚██████╔╝██║  ██╗██║  ██╗██║  ██║██████╔╝╚██████╔╝███████║███████║ ██║    ██║██║ ╚████║██║   ██║   
# ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝ ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   
                                                                                                               
from .nodes.DoubleClipTextEncode import DoubleClipTextEncode
from .nodes.HashText import HashText
from .nodes.IndoorBackgrounds import IndoorBackgrounds
from .nodes.LandscapeBackgrounds import LandscapeBackgrounds
from .nodes.OptimalCrop import OptimalCrop
from .nodes.X_In_a_Dress import X_In_a_Dress
from .nodes.X_In_a_Suit import X_In_a_Suit
from .nodes.WrapText import WrapText
from .nodes.AspectRatioCondition import AspectRatioCondition
from .nodes.SDXLEmptyLatent import SDXLEmptyLatent
from .nodes.ZoomCrop import ZoomCrop
from .nodes.IntFloatDict import IntFloatDict
from .nodes.WorkflowSettings import WorkflowSettings
from .nodes.IntStringDict import IntStringDict
from .nodes.ConnectImage import ConnectImage
from .nodes.ConnectString import ConnectString
from .nodes.ConnectInteger import ConnectInteger
from .nodes.ConnectFloat import ConnectFloat
from .nodes.ConnectLatent import ConnectLatent
from .nodes.TimeStamp import TimeStamp
from .nodes.SaveWithMetaData import SaveWithMetaData
from .nodes.SaveWithMetaData2 import SaveWithMetaData2
from .nodes.TricolorComposition import TricolorComposition
from .nodes.Colors import Colors
from .nodes.HueSatLum import HueSatLum
from .nodes.EmbeddingLoader import EmbeddingLoader
from .nodes.ImageDimensions import ImageDimensions
from .nodes.SimplePrompts import SimplePrompts
from .nodes.IntEvaluate import IntEvaluate
from .nodes.ImageResizeLong import ImageResizeLong
from .nodes.PhotomontageA import PhotomontageA
from .nodes.PhotomontageB import PhotomontageB
from .nodes.PhotomontageC import PhotomontageC
from .nodes.PostSamplerCrop import PostSamplerCrop
from .nodes.Mbsampler import Mbsampler
from .nodes.Overlay import Overlay
from .nodes.HueShift import HueShift
from .nodes.FuseImages import FuseImages
from .nodes.FuseImages2 import FuseImages2
from .nodes.StringJoin import StringJoin
from .nodes.SearchReplace import SearchReplace
from .nodes.SavePrompt import SavePrompt
from .nodes.PresetSave import PresetSave
from .nodes.PresetLoad import PresetLoad
from .nodes.PresetRemove import PresetRemove
from .nodes.RandomString import RandomString
from .nodes.JsonSearch import JsonSearch
from .nodes.PromptSwitcher import PromptSwitcher
from .nodes.imageborder import imageborder
from .nodes.KillWorkflow import KillWorkflow
from .nodes.SplitImages import SplitImages
from .nodes.ImageZigzag import ImageZigzag
from .nodes.CombinedCrop import CombinedCrop
from .nodes.ImageOverlayResized import ImageOverlayResized
from .nodes.TintnShift import TintnShift
from .nodes.ImageDimensionsBatch import ImageDimensionsBatch
from .nodes.ChooseImage import ChooseImage
from .nodes.ConnectInteger2 import ConnectInteger2
from .nodes.CycleInteger import CycleInteger
from .nodes.FlexEmptyLatent import FlexEmptyLatent
from .nodes.FloatEvaluate import FloatEvaluate
from .nodes.LinEqEval import LinEqEval
from .nodes.QuadClipTextEncode import QuadClipTextEncode
from .nodes.DoubleConditioningMixer import DoubleConditioningMixer

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
    "KillWorkflow": KillWorkflow,
    "SplitImages": SplitImages,
    "ImageZigzag": ImageZigzag,
    "CombinedCrop": CombinedCrop,
    "ImageOverlayResized": ImageOverlayResized,
    "TintnShift": TintnShift,
    "ImageDimensionsBatch": ImageDimensionsBatch,
    "ChooseImage": ChooseImage,
    "ConnectInteger2": ConnectInteger2,
    "CycleInteger": CycleInteger,
    "FlexEmptyLatent": FlexEmptyLatent,
    "FloatEvaluate": FloatEvaluate,
    "LinEqEval": LinEqEval,
    "QuadClipTextEncode": QuadClipTextEncode,
    "DoubleConditioningMixer": DoubleConditioningMixer,
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
    "KillWorkflow": "👑 KillWorkflow",
    "SplitImages": "👑 SplitImages",
    "ImageZigzag": "👑 ImageZigzag",
    "CombinedCrop": "👑 CombinedCrop",
    "ImageOverlayResized": "👑 ImageOverlayResized",
    "TintnShift": "👑 TintnShift",
    "ImageDimensionsBatch": "👑 ImageDimensionsBatch",
    "ChooseImage": "👑 ChooseImage",
    "ConnectInteger2": "👑 ConnectInteger2",
    "CycleInteger": "👑 CycleInteger",
    "FlexEmptyLatent": "👑 FlexEmptyLatent",
    "FloatEvaluate": "👑 FloatEvaluate",
    "LinEqEval": "👑 LinEqEval",
    "QuadClipTextEncode": "👑 QuadClipTextEncode",
    "DoubleConditioningMixer": "👑 DoubleConditioningMixer",
}
print ("👑 Mokkaboss1 59 Custom Nodes: Loaded")

