from enum import Enum

class WindowsManagedAppClipboardSharingLevel(Enum):
    # Org users can paste data from and cut/copy data to any account, document, location or application.
    AnyDestinationAnySource = "anyDestinationAnySource",
    # Org users cannot cut, copy or paste data to or from external accounts, documents, locations or applications from or into the org context.
    None_escaped = "none",

