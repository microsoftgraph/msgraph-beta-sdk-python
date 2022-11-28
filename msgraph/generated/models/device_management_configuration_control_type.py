from enum import Enum

class DeviceManagementConfigurationControlType(Enum):
    # Don’t override default
    Default = "default",
    # Display Choice in dropdown
    Dropdown = "dropdown",
    # Display text input in small text input
    SmallTextBox = "smallTextBox",
    # Display text input in large text input
    LargeTextBox = "largeTextBox",
    # Allow for toggle control type
    Toggle = "toggle",
    # Allow for multiheader grid control type
    MultiheaderGrid = "multiheaderGrid",
    # Allow for context pane control type
    ContextPane = "contextPane",

