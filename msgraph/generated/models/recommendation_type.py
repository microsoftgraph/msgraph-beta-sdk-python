from enum import Enum

class RecommendationType(Enum):
    AdfsAppsMigration = "adfsAppsMigration",
    EnableDesktopSSO = "enableDesktopSSO",
    EnablePHS = "enablePHS",
    EnableProvisioning = "enableProvisioning",
    SwitchFromPerUserMFA = "switchFromPerUserMFA",
    TenantMFA = "tenantMFA",
    ThirdPartyApps = "thirdPartyApps",
    TurnOffPerUserMFA = "turnOffPerUserMFA",
    UseAuthenticatorApp = "useAuthenticatorApp",
    UseMyApps = "useMyApps",
    StaleApps = "staleApps",
    StaleAppCreds = "staleAppCreds",
    ApplicationCredentialExpiry = "applicationCredentialExpiry",
    ServicePrincipalKeyExpiry = "servicePrincipalKeyExpiry",
    AdminMFAV2 = "adminMFAV2",
    BlockLegacyAuthentication = "blockLegacyAuthentication",
    IntegratedApps = "integratedApps",
    MfaRegistrationV2 = "mfaRegistrationV2",
    PwagePolicyNew = "pwagePolicyNew",
    PasswordHashSync = "passwordHashSync",
    OneAdmin = "oneAdmin",
    RoleOverlap = "roleOverlap",
    SelfServicePasswordReset = "selfServicePasswordReset",
    SigninRiskPolicy = "signinRiskPolicy",
    UserRiskPolicy = "userRiskPolicy",
    VerifyAppPublisher = "verifyAppPublisher",
    PrivateLinkForAAD = "privateLinkForAAD",
    AppRoleAssignmentsGroups = "appRoleAssignmentsGroups",
    AppRoleAssignmentsUsers = "appRoleAssignmentsUsers",
    ManagedIdentity = "managedIdentity",
    OverprivilegedApps = "overprivilegedApps",
    UnknownFutureValue = "unknownFutureValue",
