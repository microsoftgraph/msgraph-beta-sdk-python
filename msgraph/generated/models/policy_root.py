from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_policy = lazy_import('msgraph.generated.models.access_review_policy')
activity_based_timeout_policy = lazy_import('msgraph.generated.models.activity_based_timeout_policy')
admin_consent_request_policy = lazy_import('msgraph.generated.models.admin_consent_request_policy')
app_management_policy = lazy_import('msgraph.generated.models.app_management_policy')
authentication_flows_policy = lazy_import('msgraph.generated.models.authentication_flows_policy')
authentication_methods_policy = lazy_import('msgraph.generated.models.authentication_methods_policy')
authentication_strength_policy = lazy_import('msgraph.generated.models.authentication_strength_policy')
authorization_policy = lazy_import('msgraph.generated.models.authorization_policy')
b2c_authentication_methods_policy = lazy_import('msgraph.generated.models.b2c_authentication_methods_policy')
claims_mapping_policy = lazy_import('msgraph.generated.models.claims_mapping_policy')
conditional_access_policy = lazy_import('msgraph.generated.models.conditional_access_policy')
cross_tenant_access_policy = lazy_import('msgraph.generated.models.cross_tenant_access_policy')
device_registration_policy = lazy_import('msgraph.generated.models.device_registration_policy')
directory_role_access_review_policy = lazy_import('msgraph.generated.models.directory_role_access_review_policy')
external_identities_policy = lazy_import('msgraph.generated.models.external_identities_policy')
feature_rollout_policy = lazy_import('msgraph.generated.models.feature_rollout_policy')
home_realm_discovery_policy = lazy_import('msgraph.generated.models.home_realm_discovery_policy')
identity_security_defaults_enforcement_policy = lazy_import('msgraph.generated.models.identity_security_defaults_enforcement_policy')
mobility_management_policy = lazy_import('msgraph.generated.models.mobility_management_policy')
permission_grant_policy = lazy_import('msgraph.generated.models.permission_grant_policy')
service_principal_creation_policy = lazy_import('msgraph.generated.models.service_principal_creation_policy')
tenant_app_management_policy = lazy_import('msgraph.generated.models.tenant_app_management_policy')
token_issuance_policy = lazy_import('msgraph.generated.models.token_issuance_policy')
token_lifetime_policy = lazy_import('msgraph.generated.models.token_lifetime_policy')
unified_role_management_policy = lazy_import('msgraph.generated.models.unified_role_management_policy')
unified_role_management_policy_assignment = lazy_import('msgraph.generated.models.unified_role_management_policy_assignment')

class PolicyRoot(AdditionalDataHolder, Parsable):
    @property
    def access_review_policy(self,) -> Optional[access_review_policy.AccessReviewPolicy]:
        """
        Gets the accessReviewPolicy property value. The policy that contains directory-level access review settings.
        Returns: Optional[access_review_policy.AccessReviewPolicy]
        """
        return self._access_review_policy
    
    @access_review_policy.setter
    def access_review_policy(self,value: Optional[access_review_policy.AccessReviewPolicy] = None) -> None:
        """
        Sets the accessReviewPolicy property value. The policy that contains directory-level access review settings.
        Args:
            value: Value to set for the accessReviewPolicy property.
        """
        self._access_review_policy = value
    
    @property
    def activity_based_timeout_policies(self,) -> Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]]:
        """
        Gets the activityBasedTimeoutPolicies property value. The policy that controls the idle time out for web sessions for applications.
        Returns: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]]
        """
        return self._activity_based_timeout_policies
    
    @activity_based_timeout_policies.setter
    def activity_based_timeout_policies(self,value: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]] = None) -> None:
        """
        Sets the activityBasedTimeoutPolicies property value. The policy that controls the idle time out for web sessions for applications.
        Args:
            value: Value to set for the activityBasedTimeoutPolicies property.
        """
        self._activity_based_timeout_policies = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def admin_consent_request_policy(self,) -> Optional[admin_consent_request_policy.AdminConsentRequestPolicy]:
        """
        Gets the adminConsentRequestPolicy property value. The policy by which consent requests are created and managed for the entire tenant.
        Returns: Optional[admin_consent_request_policy.AdminConsentRequestPolicy]
        """
        return self._admin_consent_request_policy
    
    @admin_consent_request_policy.setter
    def admin_consent_request_policy(self,value: Optional[admin_consent_request_policy.AdminConsentRequestPolicy] = None) -> None:
        """
        Sets the adminConsentRequestPolicy property value. The policy by which consent requests are created and managed for the entire tenant.
        Args:
            value: Value to set for the adminConsentRequestPolicy property.
        """
        self._admin_consent_request_policy = value
    
    @property
    def app_management_policies(self,) -> Optional[List[app_management_policy.AppManagementPolicy]]:
        """
        Gets the appManagementPolicies property value. The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
        Returns: Optional[List[app_management_policy.AppManagementPolicy]]
        """
        return self._app_management_policies
    
    @app_management_policies.setter
    def app_management_policies(self,value: Optional[List[app_management_policy.AppManagementPolicy]] = None) -> None:
        """
        Sets the appManagementPolicies property value. The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
        Args:
            value: Value to set for the appManagementPolicies property.
        """
        self._app_management_policies = value
    
    @property
    def authentication_flows_policy(self,) -> Optional[authentication_flows_policy.AuthenticationFlowsPolicy]:
        """
        Gets the authenticationFlowsPolicy property value. The policy configuration of the self-service sign-up experience of external users.
        Returns: Optional[authentication_flows_policy.AuthenticationFlowsPolicy]
        """
        return self._authentication_flows_policy
    
    @authentication_flows_policy.setter
    def authentication_flows_policy(self,value: Optional[authentication_flows_policy.AuthenticationFlowsPolicy] = None) -> None:
        """
        Sets the authenticationFlowsPolicy property value. The policy configuration of the self-service sign-up experience of external users.
        Args:
            value: Value to set for the authenticationFlowsPolicy property.
        """
        self._authentication_flows_policy = value
    
    @property
    def authentication_methods_policy(self,) -> Optional[authentication_methods_policy.AuthenticationMethodsPolicy]:
        """
        Gets the authenticationMethodsPolicy property value. The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        Returns: Optional[authentication_methods_policy.AuthenticationMethodsPolicy]
        """
        return self._authentication_methods_policy
    
    @authentication_methods_policy.setter
    def authentication_methods_policy(self,value: Optional[authentication_methods_policy.AuthenticationMethodsPolicy] = None) -> None:
        """
        Sets the authenticationMethodsPolicy property value. The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        Args:
            value: Value to set for the authenticationMethodsPolicy property.
        """
        self._authentication_methods_policy = value
    
    @property
    def authentication_strength_policies(self,) -> Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]:
        """
        Gets the authenticationStrengthPolicies property value. The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        Returns: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]
        """
        return self._authentication_strength_policies
    
    @authentication_strength_policies.setter
    def authentication_strength_policies(self,value: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None) -> None:
        """
        Sets the authenticationStrengthPolicies property value. The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        Args:
            value: Value to set for the authenticationStrengthPolicies property.
        """
        self._authentication_strength_policies = value
    
    @property
    def authorization_policy(self,) -> Optional[List[authorization_policy.AuthorizationPolicy]]:
        """
        Gets the authorizationPolicy property value. The policy that controls Azure AD authorization settings.
        Returns: Optional[List[authorization_policy.AuthorizationPolicy]]
        """
        return self._authorization_policy
    
    @authorization_policy.setter
    def authorization_policy(self,value: Optional[List[authorization_policy.AuthorizationPolicy]] = None) -> None:
        """
        Sets the authorizationPolicy property value. The policy that controls Azure AD authorization settings.
        Args:
            value: Value to set for the authorizationPolicy property.
        """
        self._authorization_policy = value
    
    @property
    def b2c_authentication_methods_policy(self,) -> Optional[b2c_authentication_methods_policy.B2cAuthenticationMethodsPolicy]:
        """
        Gets the b2cAuthenticationMethodsPolicy property value. The Azure AD B2C policies that define how end users register via local accounts.
        Returns: Optional[b2c_authentication_methods_policy.B2cAuthenticationMethodsPolicy]
        """
        return self._b2c_authentication_methods_policy
    
    @b2c_authentication_methods_policy.setter
    def b2c_authentication_methods_policy(self,value: Optional[b2c_authentication_methods_policy.B2cAuthenticationMethodsPolicy] = None) -> None:
        """
        Sets the b2cAuthenticationMethodsPolicy property value. The Azure AD B2C policies that define how end users register via local accounts.
        Args:
            value: Value to set for the b2cAuthenticationMethodsPolicy property.
        """
        self._b2c_authentication_methods_policy = value
    
    @property
    def claims_mapping_policies(self,) -> Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]:
        """
        Gets the claimsMappingPolicies property value. The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        Returns: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]
        """
        return self._claims_mapping_policies
    
    @claims_mapping_policies.setter
    def claims_mapping_policies(self,value: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None) -> None:
        """
        Sets the claimsMappingPolicies property value. The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        Args:
            value: Value to set for the claimsMappingPolicies property.
        """
        self._claims_mapping_policies = value
    
    @property
    def conditional_access_policies(self,) -> Optional[List[conditional_access_policy.ConditionalAccessPolicy]]:
        """
        Gets the conditionalAccessPolicies property value. The custom rules that define an access scenario.
        Returns: Optional[List[conditional_access_policy.ConditionalAccessPolicy]]
        """
        return self._conditional_access_policies
    
    @conditional_access_policies.setter
    def conditional_access_policies(self,value: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None) -> None:
        """
        Sets the conditionalAccessPolicies property value. The custom rules that define an access scenario.
        Args:
            value: Value to set for the conditionalAccessPolicies property.
        """
        self._conditional_access_policies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PolicyRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The policy that contains directory-level access review settings.
        self._access_review_policy: Optional[access_review_policy.AccessReviewPolicy] = None
        # The policy that controls the idle time out for web sessions for applications.
        self._activity_based_timeout_policies: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]] = None
        # The policy by which consent requests are created and managed for the entire tenant.
        self._admin_consent_request_policy: Optional[admin_consent_request_policy.AdminConsentRequestPolicy] = None
        # The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
        self._app_management_policies: Optional[List[app_management_policy.AppManagementPolicy]] = None
        # The policy configuration of the self-service sign-up experience of external users.
        self._authentication_flows_policy: Optional[authentication_flows_policy.AuthenticationFlowsPolicy] = None
        # The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        self._authentication_methods_policy: Optional[authentication_methods_policy.AuthenticationMethodsPolicy] = None
        # The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
        self._authentication_strength_policies: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None
        # The policy that controls Azure AD authorization settings.
        self._authorization_policy: Optional[List[authorization_policy.AuthorizationPolicy]] = None
        # The Azure AD B2C policies that define how end users register via local accounts.
        self._b2c_authentication_methods_policy: Optional[b2c_authentication_methods_policy.B2cAuthenticationMethodsPolicy] = None
        # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        self._claims_mapping_policies: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None
        # The custom rules that define an access scenario.
        self._conditional_access_policies: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
        # The custom rules that define an access scenario when interacting with external Azure AD tenants.
        self._cross_tenant_access_policy: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy] = None
        # The tenant-wide policy that enforces app management restrictions for all applications and service principals.
        self._default_app_management_policy: Optional[tenant_app_management_policy.TenantAppManagementPolicy] = None
        # The deviceRegistrationPolicy property
        self._device_registration_policy: Optional[device_registration_policy.DeviceRegistrationPolicy] = None
        # The directoryRoleAccessReviewPolicy property
        self._directory_role_access_review_policy: Optional[directory_role_access_review_policy.DirectoryRoleAccessReviewPolicy] = None
        # Represents the tenant-wide policy that controls whether external users can leave an Azure AD tenant via self-service controls.
        self._external_identities_policy: Optional[external_identities_policy.ExternalIdentitiesPolicy] = None
        # The feature rollout policy associated with a directory object.
        self._feature_rollout_policies: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None
        # The policy to control Azure AD authentication behavior for federated users.
        self._home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
        # The policy that represents the security defaults that protect against common attacks.
        self._identity_security_defaults_enforcement_policy: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy] = None
        # The policy that defines auto-enrollment configuration for a mobility management (MDM or MAM) application.
        self._mobile_app_management_policies: Optional[List[mobility_management_policy.MobilityManagementPolicy]] = None
        # The mobileDeviceManagementPolicies property
        self._mobile_device_management_policies: Optional[List[mobility_management_policy.MobilityManagementPolicy]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policy that specifies the conditions under which consent can be granted.
        self._permission_grant_policies: Optional[List[permission_grant_policy.PermissionGrantPolicy]] = None
        # Represents the role management policies.
        self._role_management_policies: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]] = None
        # Represents the role management policy assignments.
        self._role_management_policy_assignments: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]] = None
        # The servicePrincipalCreationPolicies property
        self._service_principal_creation_policies: Optional[List[service_principal_creation_policy.ServicePrincipalCreationPolicy]] = None
        # The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        self._token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
        # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        self._token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PolicyRoot()
    
    @property
    def cross_tenant_access_policy(self,) -> Optional[cross_tenant_access_policy.CrossTenantAccessPolicy]:
        """
        Gets the crossTenantAccessPolicy property value. The custom rules that define an access scenario when interacting with external Azure AD tenants.
        Returns: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy]
        """
        return self._cross_tenant_access_policy
    
    @cross_tenant_access_policy.setter
    def cross_tenant_access_policy(self,value: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy] = None) -> None:
        """
        Sets the crossTenantAccessPolicy property value. The custom rules that define an access scenario when interacting with external Azure AD tenants.
        Args:
            value: Value to set for the crossTenantAccessPolicy property.
        """
        self._cross_tenant_access_policy = value
    
    @property
    def default_app_management_policy(self,) -> Optional[tenant_app_management_policy.TenantAppManagementPolicy]:
        """
        Gets the defaultAppManagementPolicy property value. The tenant-wide policy that enforces app management restrictions for all applications and service principals.
        Returns: Optional[tenant_app_management_policy.TenantAppManagementPolicy]
        """
        return self._default_app_management_policy
    
    @default_app_management_policy.setter
    def default_app_management_policy(self,value: Optional[tenant_app_management_policy.TenantAppManagementPolicy] = None) -> None:
        """
        Sets the defaultAppManagementPolicy property value. The tenant-wide policy that enforces app management restrictions for all applications and service principals.
        Args:
            value: Value to set for the defaultAppManagementPolicy property.
        """
        self._default_app_management_policy = value
    
    @property
    def device_registration_policy(self,) -> Optional[device_registration_policy.DeviceRegistrationPolicy]:
        """
        Gets the deviceRegistrationPolicy property value. The deviceRegistrationPolicy property
        Returns: Optional[device_registration_policy.DeviceRegistrationPolicy]
        """
        return self._device_registration_policy
    
    @device_registration_policy.setter
    def device_registration_policy(self,value: Optional[device_registration_policy.DeviceRegistrationPolicy] = None) -> None:
        """
        Sets the deviceRegistrationPolicy property value. The deviceRegistrationPolicy property
        Args:
            value: Value to set for the deviceRegistrationPolicy property.
        """
        self._device_registration_policy = value
    
    @property
    def directory_role_access_review_policy(self,) -> Optional[directory_role_access_review_policy.DirectoryRoleAccessReviewPolicy]:
        """
        Gets the directoryRoleAccessReviewPolicy property value. The directoryRoleAccessReviewPolicy property
        Returns: Optional[directory_role_access_review_policy.DirectoryRoleAccessReviewPolicy]
        """
        return self._directory_role_access_review_policy
    
    @directory_role_access_review_policy.setter
    def directory_role_access_review_policy(self,value: Optional[directory_role_access_review_policy.DirectoryRoleAccessReviewPolicy] = None) -> None:
        """
        Sets the directoryRoleAccessReviewPolicy property value. The directoryRoleAccessReviewPolicy property
        Args:
            value: Value to set for the directoryRoleAccessReviewPolicy property.
        """
        self._directory_role_access_review_policy = value
    
    @property
    def external_identities_policy(self,) -> Optional[external_identities_policy.ExternalIdentitiesPolicy]:
        """
        Gets the externalIdentitiesPolicy property value. Represents the tenant-wide policy that controls whether external users can leave an Azure AD tenant via self-service controls.
        Returns: Optional[external_identities_policy.ExternalIdentitiesPolicy]
        """
        return self._external_identities_policy
    
    @external_identities_policy.setter
    def external_identities_policy(self,value: Optional[external_identities_policy.ExternalIdentitiesPolicy] = None) -> None:
        """
        Sets the externalIdentitiesPolicy property value. Represents the tenant-wide policy that controls whether external users can leave an Azure AD tenant via self-service controls.
        Args:
            value: Value to set for the externalIdentitiesPolicy property.
        """
        self._external_identities_policy = value
    
    @property
    def feature_rollout_policies(self,) -> Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]:
        """
        Gets the featureRolloutPolicies property value. The feature rollout policy associated with a directory object.
        Returns: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]
        """
        return self._feature_rollout_policies
    
    @feature_rollout_policies.setter
    def feature_rollout_policies(self,value: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None) -> None:
        """
        Sets the featureRolloutPolicies property value. The feature rollout policy associated with a directory object.
        Args:
            value: Value to set for the featureRolloutPolicies property.
        """
        self._feature_rollout_policies = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_review_policy": lambda n : setattr(self, 'access_review_policy', n.get_object_value(access_review_policy.AccessReviewPolicy)),
            "activity_based_timeout_policies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(activity_based_timeout_policy.ActivityBasedTimeoutPolicy)),
            "admin_consent_request_policy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(admin_consent_request_policy.AdminConsentRequestPolicy)),
            "app_management_policies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(app_management_policy.AppManagementPolicy)),
            "authentication_flows_policy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(authentication_flows_policy.AuthenticationFlowsPolicy)),
            "authentication_methods_policy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(authentication_methods_policy.AuthenticationMethodsPolicy)),
            "authentication_strength_policies": lambda n : setattr(self, 'authentication_strength_policies', n.get_collection_of_object_values(authentication_strength_policy.AuthenticationStrengthPolicy)),
            "authorization_policy": lambda n : setattr(self, 'authorization_policy', n.get_collection_of_object_values(authorization_policy.AuthorizationPolicy)),
            "b2c_authentication_methods_policy": lambda n : setattr(self, 'b2c_authentication_methods_policy', n.get_object_value(b2c_authentication_methods_policy.B2cAuthenticationMethodsPolicy)),
            "claims_mapping_policies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(claims_mapping_policy.ClaimsMappingPolicy)),
            "conditional_access_policies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "cross_tenant_access_policy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(cross_tenant_access_policy.CrossTenantAccessPolicy)),
            "default_app_management_policy": lambda n : setattr(self, 'default_app_management_policy', n.get_object_value(tenant_app_management_policy.TenantAppManagementPolicy)),
            "device_registration_policy": lambda n : setattr(self, 'device_registration_policy', n.get_object_value(device_registration_policy.DeviceRegistrationPolicy)),
            "directory_role_access_review_policy": lambda n : setattr(self, 'directory_role_access_review_policy', n.get_object_value(directory_role_access_review_policy.DirectoryRoleAccessReviewPolicy)),
            "external_identities_policy": lambda n : setattr(self, 'external_identities_policy', n.get_object_value(external_identities_policy.ExternalIdentitiesPolicy)),
            "feature_rollout_policies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(feature_rollout_policy.FeatureRolloutPolicy)),
            "home_realm_discovery_policies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identity_security_defaults_enforcement_policy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy)),
            "mobile_app_management_policies": lambda n : setattr(self, 'mobile_app_management_policies', n.get_collection_of_object_values(mobility_management_policy.MobilityManagementPolicy)),
            "mobile_device_management_policies": lambda n : setattr(self, 'mobile_device_management_policies', n.get_collection_of_object_values(mobility_management_policy.MobilityManagementPolicy)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permission_grant_policies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(permission_grant_policy.PermissionGrantPolicy)),
            "role_management_policies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(unified_role_management_policy.UnifiedRoleManagementPolicy)),
            "role_management_policy_assignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment)),
            "service_principal_creation_policies": lambda n : setattr(self, 'service_principal_creation_policies', n.get_collection_of_object_values(service_principal_creation_policy.ServicePrincipalCreationPolicy)),
            "token_issuance_policies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "token_lifetime_policies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
        }
        return fields
    
    @property
    def home_realm_discovery_policies(self,) -> Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]:
        """
        Gets the homeRealmDiscoveryPolicies property value. The policy to control Azure AD authentication behavior for federated users.
        Returns: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]
        """
        return self._home_realm_discovery_policies
    
    @home_realm_discovery_policies.setter
    def home_realm_discovery_policies(self,value: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None) -> None:
        """
        Sets the homeRealmDiscoveryPolicies property value. The policy to control Azure AD authentication behavior for federated users.
        Args:
            value: Value to set for the homeRealmDiscoveryPolicies property.
        """
        self._home_realm_discovery_policies = value
    
    @property
    def identity_security_defaults_enforcement_policy(self,) -> Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy]:
        """
        Gets the identitySecurityDefaultsEnforcementPolicy property value. The policy that represents the security defaults that protect against common attacks.
        Returns: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy]
        """
        return self._identity_security_defaults_enforcement_policy
    
    @identity_security_defaults_enforcement_policy.setter
    def identity_security_defaults_enforcement_policy(self,value: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy] = None) -> None:
        """
        Sets the identitySecurityDefaultsEnforcementPolicy property value. The policy that represents the security defaults that protect against common attacks.
        Args:
            value: Value to set for the identitySecurityDefaultsEnforcementPolicy property.
        """
        self._identity_security_defaults_enforcement_policy = value
    
    @property
    def mobile_app_management_policies(self,) -> Optional[List[mobility_management_policy.MobilityManagementPolicy]]:
        """
        Gets the mobileAppManagementPolicies property value. The policy that defines auto-enrollment configuration for a mobility management (MDM or MAM) application.
        Returns: Optional[List[mobility_management_policy.MobilityManagementPolicy]]
        """
        return self._mobile_app_management_policies
    
    @mobile_app_management_policies.setter
    def mobile_app_management_policies(self,value: Optional[List[mobility_management_policy.MobilityManagementPolicy]] = None) -> None:
        """
        Sets the mobileAppManagementPolicies property value. The policy that defines auto-enrollment configuration for a mobility management (MDM or MAM) application.
        Args:
            value: Value to set for the mobileAppManagementPolicies property.
        """
        self._mobile_app_management_policies = value
    
    @property
    def mobile_device_management_policies(self,) -> Optional[List[mobility_management_policy.MobilityManagementPolicy]]:
        """
        Gets the mobileDeviceManagementPolicies property value. The mobileDeviceManagementPolicies property
        Returns: Optional[List[mobility_management_policy.MobilityManagementPolicy]]
        """
        return self._mobile_device_management_policies
    
    @mobile_device_management_policies.setter
    def mobile_device_management_policies(self,value: Optional[List[mobility_management_policy.MobilityManagementPolicy]] = None) -> None:
        """
        Sets the mobileDeviceManagementPolicies property value. The mobileDeviceManagementPolicies property
        Args:
            value: Value to set for the mobileDeviceManagementPolicies property.
        """
        self._mobile_device_management_policies = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def permission_grant_policies(self,) -> Optional[List[permission_grant_policy.PermissionGrantPolicy]]:
        """
        Gets the permissionGrantPolicies property value. The policy that specifies the conditions under which consent can be granted.
        Returns: Optional[List[permission_grant_policy.PermissionGrantPolicy]]
        """
        return self._permission_grant_policies
    
    @permission_grant_policies.setter
    def permission_grant_policies(self,value: Optional[List[permission_grant_policy.PermissionGrantPolicy]] = None) -> None:
        """
        Sets the permissionGrantPolicies property value. The policy that specifies the conditions under which consent can be granted.
        Args:
            value: Value to set for the permissionGrantPolicies property.
        """
        self._permission_grant_policies = value
    
    @property
    def role_management_policies(self,) -> Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]]:
        """
        Gets the roleManagementPolicies property value. Represents the role management policies.
        Returns: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]]
        """
        return self._role_management_policies
    
    @role_management_policies.setter
    def role_management_policies(self,value: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]] = None) -> None:
        """
        Sets the roleManagementPolicies property value. Represents the role management policies.
        Args:
            value: Value to set for the roleManagementPolicies property.
        """
        self._role_management_policies = value
    
    @property
    def role_management_policy_assignments(self,) -> Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]]:
        """
        Gets the roleManagementPolicyAssignments property value. Represents the role management policy assignments.
        Returns: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]]
        """
        return self._role_management_policy_assignments
    
    @role_management_policy_assignments.setter
    def role_management_policy_assignments(self,value: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]] = None) -> None:
        """
        Sets the roleManagementPolicyAssignments property value. Represents the role management policy assignments.
        Args:
            value: Value to set for the roleManagementPolicyAssignments property.
        """
        self._role_management_policy_assignments = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("accessReviewPolicy", self.access_review_policy)
        writer.write_collection_of_object_values("activityBasedTimeoutPolicies", self.activity_based_timeout_policies)
        writer.write_object_value("adminConsentRequestPolicy", self.admin_consent_request_policy)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_object_value("authenticationFlowsPolicy", self.authentication_flows_policy)
        writer.write_object_value("authenticationMethodsPolicy", self.authentication_methods_policy)
        writer.write_collection_of_object_values("authenticationStrengthPolicies", self.authentication_strength_policies)
        writer.write_collection_of_object_values("authorizationPolicy", self.authorization_policy)
        writer.write_object_value("b2cAuthenticationMethodsPolicy", self.b2c_authentication_methods_policy)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_object_value("crossTenantAccessPolicy", self.cross_tenant_access_policy)
        writer.write_object_value("defaultAppManagementPolicy", self.default_app_management_policy)
        writer.write_object_value("deviceRegistrationPolicy", self.device_registration_policy)
        writer.write_object_value("directoryRoleAccessReviewPolicy", self.directory_role_access_review_policy)
        writer.write_object_value("externalIdentitiesPolicy", self.external_identities_policy)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("identitySecurityDefaultsEnforcementPolicy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("mobileAppManagementPolicies", self.mobile_app_management_policies)
        writer.write_collection_of_object_values("mobileDeviceManagementPolicies", self.mobile_device_management_policies)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("permissionGrantPolicies", self.permission_grant_policies)
        writer.write_collection_of_object_values("roleManagementPolicies", self.role_management_policies)
        writer.write_collection_of_object_values("roleManagementPolicyAssignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("servicePrincipalCreationPolicies", self.service_principal_creation_policies)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_principal_creation_policies(self,) -> Optional[List[service_principal_creation_policy.ServicePrincipalCreationPolicy]]:
        """
        Gets the servicePrincipalCreationPolicies property value. The servicePrincipalCreationPolicies property
        Returns: Optional[List[service_principal_creation_policy.ServicePrincipalCreationPolicy]]
        """
        return self._service_principal_creation_policies
    
    @service_principal_creation_policies.setter
    def service_principal_creation_policies(self,value: Optional[List[service_principal_creation_policy.ServicePrincipalCreationPolicy]] = None) -> None:
        """
        Sets the servicePrincipalCreationPolicies property value. The servicePrincipalCreationPolicies property
        Args:
            value: Value to set for the servicePrincipalCreationPolicies property.
        """
        self._service_principal_creation_policies = value
    
    @property
    def token_issuance_policies(self,) -> Optional[List[token_issuance_policy.TokenIssuancePolicy]]:
        """
        Gets the tokenIssuancePolicies property value. The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        Returns: Optional[List[token_issuance_policy.TokenIssuancePolicy]]
        """
        return self._token_issuance_policies
    
    @token_issuance_policies.setter
    def token_issuance_policies(self,value: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None) -> None:
        """
        Sets the tokenIssuancePolicies property value. The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        Args:
            value: Value to set for the tokenIssuancePolicies property.
        """
        self._token_issuance_policies = value
    
    @property
    def token_lifetime_policies(self,) -> Optional[List[token_lifetime_policy.TokenLifetimePolicy]]:
        """
        Gets the tokenLifetimePolicies property value. The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        Returns: Optional[List[token_lifetime_policy.TokenLifetimePolicy]]
        """
        return self._token_lifetime_policies
    
    @token_lifetime_policies.setter
    def token_lifetime_policies(self,value: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None) -> None:
        """
        Sets the tokenLifetimePolicies property value. The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        Args:
            value: Value to set for the tokenLifetimePolicies property.
        """
        self._token_lifetime_policies = value
    

