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
from ComfyUI_Mokkaboss1.nodes.TricolorComposition import TricolorComposition
from ComfyUI_Mokkaboss1.nodes.Colors import Colors
from ComfyUI_Mokkaboss1.nodes.HueSatLum import HueSatLum
from ComfyUI_Mokkaboss1.nodes.EmbeddingLoader import EmbeddingLoader
from ComfyUI_Mokkaboss1.nodes.ImageDimensions import ImageDimensions
from ComfyUI_Mokkaboss1.nodes.SimplePrompts import SimplePrompts

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
    "TricolorComposition": TricolorComposition,
    "Colors": Colors,
    "HueSatLum": HueSatLum,
    "EmbeddingLoader": EmbeddingLoader,
    "ImageDimensions": ImageDimensions,
    "SimplePrompts": SimplePrompts,
    
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
    "TricolorComposition": "👑 TricolorComposition",
    "Colors":"👑 Colors",
    "HueSatLum": "👑 HueSatLum",
    "EmbeddingLoader": "👑 EmbeddingLoader",
    "ImageDimensions": "👑 ImageDimensions",
    "SimplePrompts": "👑 SimplePrompts",
}
print ("👑 Mokkaboss1 27 Custom Nodes: Loaded")
