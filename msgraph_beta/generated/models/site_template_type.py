from enum import Enum

class SiteTemplateType(str, Enum):
    Sitepagepublishing = "sitepagepublishing",
    Group = "group",
    Sts = "sts",
    UnknownFutureValue = "unknownFutureValue",

