from enum import Enum

class ManagedDeviceRemoteAction(str, Enum):
    # Name of the retire action.
    Retire = "retire",
    # Name of the delete action.
    Delete = "delete",
    # Name of the full Scan action.
    FullScan = "fullScan",
    # Name of the Quick Scan action.
    QuickScan = "quickScan",
    # Signature Update action
    SignatureUpdate = "signatureUpdate",
    # Name of the wipe action.
    Wipe = "wipe",
    # Name of the Custom Text Notification action.
    CustomTextNotification = "customTextNotification",
    # Name of the reboot now action.
    RebootNow = "rebootNow",
    # Set Device Name action.
    SetDeviceName = "setDeviceName",
    # Sync Device action.
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
    # Name of action to initiate On Demand Proactive Remediation
    InitiateOnDemandProactiveRemediation = "initiateOnDemandProactiveRemediation",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",
    # Indicates remote device action to intiate Mobile Device Management (MDM) attestation if device is capable for it
    InitiateDeviceAttestation = "initiateDeviceAttestation",

