from enum import Enum

class UserEmailSource(Enum):
    # User principal name.
    UserPrincipalName = "userPrincipalName",
    # Primary SMTP address.
    PrimarySmtpAddress = "primarySmtpAddress",

