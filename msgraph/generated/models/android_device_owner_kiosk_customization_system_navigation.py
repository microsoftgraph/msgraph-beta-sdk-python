from enum import Enum

class AndroidDeviceOwnerKioskCustomizationSystemNavigation(Enum):
    # Not configured; this value defaults to NAVIGATION_DISABLED.
    NotConfigured = "notConfigured",
    # Home and overview buttons are enabled.
    NavigationEnabled = "navigationEnabled",
    #  Only the home button is enabled.
    HomeButtonOnly = "homeButtonOnly",

