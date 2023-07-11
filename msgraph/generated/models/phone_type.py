from enum import Enum

class PhoneType(str, Enum):
    Home = "home",
    Business = "business",
    Mobile = "mobile",
    Other = "other",
    Assistant = "assistant",
    HomeFax = "homeFax",
    BusinessFax = "businessFax",
    OtherFax = "otherFax",
    Pager = "pager",
    Radio = "radio",

