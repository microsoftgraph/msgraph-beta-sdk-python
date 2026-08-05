from enum import Enum

class ContentModality(str, Enum):
    Audio = "audio",
    Video = "video",
    Image = "image",
    Text = "text",
    Multimodal = "multimodal",
    UnknownFutureValue = "unknownFutureValue",

