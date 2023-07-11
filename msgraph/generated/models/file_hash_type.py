from enum import Enum

class FileHashType(str, Enum):
    Unknown = "unknown",
    Sha1 = "sha1",
    Sha256 = "sha256",
    Md5 = "md5",
    AuthenticodeHash256 = "authenticodeHash256",
    LsHash = "lsHash",
    Ctph = "ctph",
    UnknownFutureValue = "unknownFutureValue",

