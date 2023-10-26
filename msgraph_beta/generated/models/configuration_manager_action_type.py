from enum import Enum

class ConfigurationManagerActionType(str, Enum):
    # Refresh machine policy on Configuration Manager client
    RefreshMachinePolicy = "refreshMachinePolicy",
    # Refresh user policy on Configuration Manager client
    RefreshUserPolicy = "refreshUserPolicy",
    # Wake up Configuration Manager client
    WakeUpClient = "wakeUpClient",
    # Evaluation application policy on Configuration Manager client
    AppEvaluation = "appEvaluation",
    # Evaluation application policy on Configuration Manager client
    QuickScan = "quickScan",
    # Evaluation application policy on Configuration Manager client
    FullScan = "fullScan",
    # Evaluation application policy on Configuration Manager client
    WindowsDefenderUpdateSignatures = "windowsDefenderUpdateSignatures",

