from enum import Enum

class ManagedDeviceRemoteAction(Enum):
    Retire = "retire",
    Delete = "delete",
    FullScan = "fullScan",
    QuickScan = "quickScan",
    SignatureUpdate = "signatureUpdate",
    Wipe = "wipe",
    CustomTextNotification = "customTextNotification",
    RebootNow = "rebootNow",
    SetDeviceName = "setDeviceName",
    SyncDevice = "syncDevice",
    # Name of the deprovision action.
    Deprovision = "deprovision",
    # Name of the disable action.
    Disable = "disable",
    # Name of the reenable action.
    Reenable = "reenable",
    # Name of the moveDevicesToOU action.
    MoveDeviceToOrganizationalUnit = "moveDeviceToOrganizationalUnit",
    # Name of action to Activate eSIM on the device.
    ActivateDeviceEsim = "activateDeviceEsim",
    # Name of the collectDiagnostics action.
    CollectDiagnostics = "collectDiagnostics",
    # Name of action to initiate MDM key recovery
    InitiateMobileDeviceManagementKeyRecovery = "initiateMobileDeviceManagementKeyRecovery",

