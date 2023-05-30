from enum import Enum

class UserDefaultAuthenticationMethodType(Enum):
    Push = "push",
    Oath = "oath",
    VoiceMobile = "voiceMobile",
    VoiceAlternateMobile = "voiceAlternateMobile",
    VoiceOffice = "voiceOffice",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

