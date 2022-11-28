from enum import Enum

class DeviceManagementConfigurationStringFormat(Enum):
    None_escaped = "none",
    Email = "email",
    Guid = "guid",
    Ip = "ip",
    Base64 = "base64",
    Url = "url",
    Version = "version",
    Xml = "xml",
    Date = "date",
    Time = "time",
    Binary = "binary",
    RegEx = "regEx",
    Json = "json",
    DateTime = "dateTime",
    SurfaceHub = "surfaceHub",

