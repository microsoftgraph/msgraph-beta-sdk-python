from enum import Enum

class LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType(Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Administrators
    Administrators = "administrators",
    # Administrators and Power Users
    AdministratorsAndPowerUsers = "administratorsAndPowerUsers",
    # Administrators and Interactive Users 
    AdministratorsAndInteractiveUsers = "administratorsAndInteractiveUsers",

