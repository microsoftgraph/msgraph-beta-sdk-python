from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_root = lazy_import('msgraph.generated.models.policy_root')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
access_review_policy_request_builder = lazy_import('msgraph.generated.policies.access_review_policy.access_review_policy_request_builder')
activity_based_timeout_policies_request_builder = lazy_import('msgraph.generated.policies.activity_based_timeout_policies.activity_based_timeout_policies_request_builder')
activity_based_timeout_policy_item_request_builder = lazy_import('msgraph.generated.policies.activity_based_timeout_policies.item.activity_based_timeout_policy_item_request_builder')
admin_consent_request_policy_request_builder = lazy_import('msgraph.generated.policies.admin_consent_request_policy.admin_consent_request_policy_request_builder')
app_management_policies_request_builder = lazy_import('msgraph.generated.policies.app_management_policies.app_management_policies_request_builder')
app_management_policy_item_request_builder = lazy_import('msgraph.generated.policies.app_management_policies.item.app_management_policy_item_request_builder')
authentication_flows_policy_request_builder = lazy_import('msgraph.generated.policies.authentication_flows_policy.authentication_flows_policy_request_builder')
authentication_methods_policy_request_builder = lazy_import('msgraph.generated.policies.authentication_methods_policy.authentication_methods_policy_request_builder')
authentication_strength_policies_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.authentication_strength_policies_request_builder')
authentication_strength_policy_item_request_builder = lazy_import('msgraph.generated.policies.authentication_strength_policies.item.authentication_strength_policy_item_request_builder')
authorization_policy_request_builder = lazy_import('msgraph.generated.policies.authorization_policy.authorization_policy_request_builder')
authorization_policy_item_request_builder = lazy_import('msgraph.generated.policies.authorization_policy.item.authorization_policy_item_request_builder')
b2c_authentication_methods_policy_request_builder = lazy_import('msgraph.generated.policies.b2c_authentication_methods_policy.b2c_authentication_methods_policy_request_builder')
claims_mapping_policies_request_builder = lazy_import('msgraph.generated.policies.claims_mapping_policies.claims_mapping_policies_request_builder')
claims_mapping_policy_item_request_builder = lazy_import('msgraph.generated.policies.claims_mapping_policies.item.claims_mapping_policy_item_request_builder')
conditional_access_policies_request_builder = lazy_import('msgraph.generated.policies.conditional_access_policies.conditional_access_policies_request_builder')
conditional_access_policy_item_request_builder = lazy_import('msgraph.generated.policies.conditional_access_policies.item.conditional_access_policy_item_request_builder')
cross_tenant_access_policy_request_builder = lazy_import('msgraph.generated.policies.cross_tenant_access_policy.cross_tenant_access_policy_request_builder')
default_app_management_policy_request_builder = lazy_import('msgraph.generated.policies.default_app_management_policy.default_app_management_policy_request_builder')
device_registration_policy_request_builder = lazy_import('msgraph.generated.policies.device_registration_policy.device_registration_policy_request_builder')
directory_role_access_review_policy_request_builder = lazy_import('msgraph.generated.policies.directory_role_access_review_policy.directory_role_access_review_policy_request_builder')
external_identities_policy_request_builder = lazy_import('msgraph.generated.policies.external_identities_policy.external_identities_policy_request_builder')
feature_rollout_policies_request_builder = lazy_import('msgraph.generated.policies.feature_rollout_policies.feature_rollout_policies_request_builder')
feature_rollout_policy_item_request_builder = lazy_import('msgraph.generated.policies.feature_rollout_policies.item.feature_rollout_policy_item_request_builder')
home_realm_discovery_policies_request_builder = lazy_import('msgraph.generated.policies.home_realm_discovery_policies.home_realm_discovery_policies_request_builder')
home_realm_discovery_policy_item_request_builder = lazy_import('msgraph.generated.policies.home_realm_discovery_policies.item.home_realm_discovery_policy_item_request_builder')
identity_security_defaults_enforcement_policy_request_builder = lazy_import('msgraph.generated.policies.identity_security_defaults_enforcement_policy.identity_security_defaults_enforcement_policy_request_builder')
mobile_app_management_policies_request_builder = lazy_import('msgraph.generated.policies.mobile_app_management_policies.mobile_app_management_policies_request_builder')
mobility_management_policy_item_request_builder = lazy_import('msgraph.generated.policies.mobile_app_management_policies.item.mobility_management_policy_item_request_builder')
mobile_device_management_policies_request_builder = lazy_import('msgraph.generated.policies.mobile_device_management_policies.mobile_device_management_policies_request_builder')
mobility_management_policy_item_request_builder = lazy_import('msgraph.generated.policies.mobile_device_management_policies.item.mobility_management_policy_item_request_builder')
permission_grant_policies_request_builder = lazy_import('msgraph.generated.policies.permission_grant_policies.permission_grant_policies_request_builder')
permission_grant_policy_item_request_builder = lazy_import('msgraph.generated.policies.permission_grant_policies.item.permission_grant_policy_item_request_builder')
role_management_policies_request_builder = lazy_import('msgraph.generated.policies.role_management_policies.role_management_policies_request_builder')
unified_role_management_policy_item_request_builder = lazy_import('msgraph.generated.policies.role_management_policies.item.unified_role_management_policy_item_request_builder')
role_management_policy_assignments_request_builder = lazy_import('msgraph.generated.policies.role_management_policy_assignments.role_management_policy_assignments_request_builder')
unified_role_management_policy_assignment_item_request_builder = lazy_import('msgraph.generated.policies.role_management_policy_assignments.item.unified_role_management_policy_assignment_item_request_builder')
service_principal_creation_policies_request_builder = lazy_import('msgraph.generated.policies.service_principal_creation_policies.service_principal_creation_policies_request_builder')
service_principal_creation_policy_item_request_builder = lazy_import('msgraph.generated.policies.service_principal_creation_policies.item.service_principal_creation_policy_item_request_builder')
token_issuance_policies_request_builder = lazy_import('msgraph.generated.policies.token_issuance_policies.token_issuance_policies_request_builder')
token_issuance_policy_item_request_builder = lazy_import('msgraph.generated.policies.token_issuance_policies.item.token_issuance_policy_item_request_builder')
token_lifetime_policies_request_builder = lazy_import('msgraph.generated.policies.token_lifetime_policies.token_lifetime_policies_request_builder')
token_lifetime_policy_item_request_builder = lazy_import('msgraph.generated.policies.token_lifetime_policies.item.token_lifetime_policy_item_request_builder')

class PoliciesRequestBuilder():
    """
    Provides operations to manage the policyRoot singleton.
    """
    @property
    def access_review_policy(self) -> access_review_policy_request_builder.AccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the accessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        return access_review_policy_request_builder.AccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activity_based_timeout_policies(self) -> activity_based_timeout_policies_request_builder.ActivityBasedTimeoutPoliciesRequestBuilder:
        """
        Provides operations to manage the activityBasedTimeoutPolicies property of the microsoft.graph.policyRoot entity.
        """
        return activity_based_timeout_policies_request_builder.ActivityBasedTimeoutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin_consent_request_policy(self) -> admin_consent_request_policy_request_builder.AdminConsentRequestPolicyRequestBuilder:
        """
        Provides operations to manage the adminConsentRequestPolicy property of the microsoft.graph.policyRoot entity.
        """
        return admin_consent_request_policy_request_builder.AdminConsentRequestPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_management_policies(self) -> app_management_policies_request_builder.AppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        return app_management_policies_request_builder.AppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_flows_policy(self) -> authentication_flows_policy_request_builder.AuthenticationFlowsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationFlowsPolicy property of the microsoft.graph.policyRoot entity.
        """
        return authentication_flows_policy_request_builder.AuthenticationFlowsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        return authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strength_policies(self) -> authentication_strength_policies_request_builder.AuthenticationStrengthPoliciesRequestBuilder:
        """
        Provides operations to manage the authenticationStrengthPolicies property of the microsoft.graph.policyRoot entity.
        """
        return authentication_strength_policies_request_builder.AuthenticationStrengthPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authorization_policy(self) -> authorization_policy_request_builder.AuthorizationPolicyRequestBuilder:
        """
        Provides operations to manage the authorizationPolicy property of the microsoft.graph.policyRoot entity.
        """
        return authorization_policy_request_builder.AuthorizationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2c_authentication_methods_policy(self) -> b2c_authentication_methods_policy_request_builder.B2cAuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the b2cAuthenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        return b2c_authentication_methods_policy_request_builder.B2cAuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def claims_mapping_policies(self) -> claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.policyRoot entity.
        """
        return claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_policies(self) -> conditional_access_policies_request_builder.ConditionalAccessPoliciesRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicies property of the microsoft.graph.policyRoot entity.
        """
        return conditional_access_policies_request_builder.ConditionalAccessPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_tenant_access_policy(self) -> cross_tenant_access_policy_request_builder.CrossTenantAccessPolicyRequestBuilder:
        """
        Provides operations to manage the crossTenantAccessPolicy property of the microsoft.graph.policyRoot entity.
        """
        return cross_tenant_access_policy_request_builder.CrossTenantAccessPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_app_management_policy(self) -> default_app_management_policy_request_builder.DefaultAppManagementPolicyRequestBuilder:
        """
        Provides operations to manage the defaultAppManagementPolicy property of the microsoft.graph.policyRoot entity.
        """
        return default_app_management_policy_request_builder.DefaultAppManagementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_registration_policy(self) -> device_registration_policy_request_builder.DeviceRegistrationPolicyRequestBuilder:
        """
        Provides operations to manage the deviceRegistrationPolicy property of the microsoft.graph.policyRoot entity.
        """
        return device_registration_policy_request_builder.DeviceRegistrationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_access_review_policy(self) -> directory_role_access_review_policy_request_builder.DirectoryRoleAccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the directoryRoleAccessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        return directory_role_access_review_policy_request_builder.DirectoryRoleAccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_identities_policy(self) -> external_identities_policy_request_builder.ExternalIdentitiesPolicyRequestBuilder:
        """
        Provides operations to manage the externalIdentitiesPolicy property of the microsoft.graph.policyRoot entity.
        """
        return external_identities_policy_request_builder.ExternalIdentitiesPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feature_rollout_policies(self) -> feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.policyRoot entity.
        """
        return feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def home_realm_discovery_policies(self) -> home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.policyRoot entity.
        """
        return home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_security_defaults_enforcement_policy(self) -> identity_security_defaults_enforcement_policy_request_builder.IdentitySecurityDefaultsEnforcementPolicyRequestBuilder:
        """
        Provides operations to manage the identitySecurityDefaultsEnforcementPolicy property of the microsoft.graph.policyRoot entity.
        """
        return identity_security_defaults_enforcement_policy_request_builder.IdentitySecurityDefaultsEnforcementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_management_policies(self) -> mobile_app_management_policies_request_builder.MobileAppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileAppManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        return mobile_app_management_policies_request_builder.MobileAppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_device_management_policies(self) -> mobile_device_management_policies_request_builder.MobileDeviceManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileDeviceManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        return mobile_device_management_policies_request_builder.MobileDeviceManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grant_policies(self) -> permission_grant_policies_request_builder.PermissionGrantPoliciesRequestBuilder:
        """
        Provides operations to manage the permissionGrantPolicies property of the microsoft.graph.policyRoot entity.
        """
        return permission_grant_policies_request_builder.PermissionGrantPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policies(self) -> role_management_policies_request_builder.RoleManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        return role_management_policies_request_builder.RoleManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policy_assignments(self) -> role_management_policy_assignments_request_builder.RoleManagementPolicyAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicyAssignments property of the microsoft.graph.policyRoot entity.
        """
        return role_management_policy_assignments_request_builder.RoleManagementPolicyAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_creation_policies(self) -> service_principal_creation_policies_request_builder.ServicePrincipalCreationPoliciesRequestBuilder:
        """
        Provides operations to manage the servicePrincipalCreationPolicies property of the microsoft.graph.policyRoot entity.
        """
        return service_principal_creation_policies_request_builder.ServicePrincipalCreationPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_issuance_policies(self) -> token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.policyRoot entity.
        """
        return token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_lifetime_policies(self) -> token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.policyRoot entity.
        """
        return token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def activity_based_timeout_policies_by_id(self,id: str) -> activity_based_timeout_policy_item_request_builder.ActivityBasedTimeoutPolicyItemRequestBuilder:
        """
        Provides operations to manage the activityBasedTimeoutPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: activity_based_timeout_policy_item_request_builder.ActivityBasedTimeoutPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["activityBasedTimeoutPolicy%2Did"] = id
        return activity_based_timeout_policy_item_request_builder.ActivityBasedTimeoutPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def app_management_policies_by_id(self,id: str) -> app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appManagementPolicy%2Did"] = id
        return app_management_policy_item_request_builder.AppManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def authentication_strength_policies_by_id(self,id: str) -> authentication_strength_policy_item_request_builder.AuthenticationStrengthPolicyItemRequestBuilder:
        """
        Provides operations to manage the authenticationStrengthPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: authentication_strength_policy_item_request_builder.AuthenticationStrengthPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationStrengthPolicy%2Did"] = id
        return authentication_strength_policy_item_request_builder.AuthenticationStrengthPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def authorization_policy_by_id(self,id: str) -> authorization_policy_item_request_builder.AuthorizationPolicyItemRequestBuilder:
        """
        Provides operations to manage the authorizationPolicy property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: authorization_policy_item_request_builder.AuthorizationPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authorizationPolicy%2Did"] = id
        return authorization_policy_item_request_builder.AuthorizationPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def claims_mapping_policies_by_id(self,id: str) -> claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["claimsMappingPolicy%2Did"] = id
        return claims_mapping_policy_item_request_builder.ClaimsMappingPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def conditional_access_policies_by_id(self,id: str) -> conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionalAccessPolicy%2Did"] = id
        return conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PoliciesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/policies{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def feature_rollout_policies_by_id(self,id: str) -> feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["featureRolloutPolicy%2Did"] = id
        return feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[PoliciesRequestBuilderGetRequestConfiguration] = None) -> Optional[policy_root.PolicyRoot]:
        """
        Get policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[policy_root.PolicyRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, policy_root.PolicyRoot, error_mapping)
    
    def home_realm_discovery_policies_by_id(self,id: str) -> home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["homeRealmDiscoveryPolicy%2Did"] = id
        return home_realm_discovery_policy_item_request_builder.HomeRealmDiscoveryPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_management_policies_by_id(self,id: str) -> mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the mobileAppManagementPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobilityManagementPolicy%2Did"] = id
        return mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_device_management_policies_by_id(self,id: str) -> mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the mobileDeviceManagementPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobilityManagementPolicy%2Did"] = id
        return mobility_management_policy_item_request_builder.MobilityManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[policy_root.PolicyRoot] = None, request_configuration: Optional[PoliciesRequestBuilderPatchRequestConfiguration] = None) -> Optional[policy_root.PolicyRoot]:
        """
        Update policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[policy_root.PolicyRoot]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, policy_root.PolicyRoot, error_mapping)
    
    def permission_grant_policies_by_id(self,id: str) -> permission_grant_policy_item_request_builder.PermissionGrantPolicyItemRequestBuilder:
        """
        Provides operations to manage the permissionGrantPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: permission_grant_policy_item_request_builder.PermissionGrantPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["permissionGrantPolicy%2Did"] = id
        return permission_grant_policy_item_request_builder.PermissionGrantPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_management_policies_by_id(self,id: str) -> unified_role_management_policy_item_request_builder.UnifiedRoleManagementPolicyItemRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_item_request_builder.UnifiedRoleManagementPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicy%2Did"] = id
        return unified_role_management_policy_item_request_builder.UnifiedRoleManagementPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_management_policy_assignments_by_id(self,id: str) -> unified_role_management_policy_assignment_item_request_builder.UnifiedRoleManagementPolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicyAssignments property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_management_policy_assignment_item_request_builder.UnifiedRoleManagementPolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleManagementPolicyAssignment%2Did"] = id
        return unified_role_management_policy_assignment_item_request_builder.UnifiedRoleManagementPolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def service_principal_creation_policies_by_id(self,id: str) -> service_principal_creation_policy_item_request_builder.ServicePrincipalCreationPolicyItemRequestBuilder:
        """
        Provides operations to manage the servicePrincipalCreationPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: service_principal_creation_policy_item_request_builder.ServicePrincipalCreationPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["servicePrincipalCreationPolicy%2Did"] = id
        return service_principal_creation_policy_item_request_builder.ServicePrincipalCreationPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[PoliciesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def token_issuance_policies_by_id(self,id: str) -> token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenIssuancePolicy%2Did"] = id
        return token_issuance_policy_item_request_builder.TokenIssuancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def token_lifetime_policies_by_id(self,id: str) -> token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tokenLifetimePolicy%2Did"] = id
        return token_lifetime_policy_item_request_builder.TokenLifetimePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_patch_request_information(self,body: Optional[policy_root.PolicyRoot] = None, request_configuration: Optional[PoliciesRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class PoliciesRequestBuilderGetQueryParameters():
        """
        Get policies
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class PoliciesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PoliciesRequestBuilder.PoliciesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PoliciesRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

