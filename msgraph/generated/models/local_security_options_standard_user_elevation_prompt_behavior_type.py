from enum import Enum

class LocalSecurityOptionsStandardUserElevationPromptBehaviorType(Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Automatically deny elevation requests
    AutomaticallyDenyElevationRequests = "automaticallyDenyElevationRequests",
    # Prompt for credentials on the secure desktop
    PromptForCredentialsOnTheSecureDesktop = "promptForCredentialsOnTheSecureDesktop",
    # Prompt for credentials
    PromptForCredentials = "promptForCredentials",

