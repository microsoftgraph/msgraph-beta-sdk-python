from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import policy_root
    from ..models.o_data_errors import o_data_error
    from .access_review_policy import access_review_policy_request_builder
    from .activity_based_timeout_policies import activity_based_timeout_policies_request_builder
    from .activity_based_timeout_policies.item import activity_based_timeout_policy_item_request_builder
    from .admin_consent_request_policy import admin_consent_request_policy_request_builder
    from .app_management_policies import app_management_policies_request_builder
    from .app_management_policies.item import app_management_policy_item_request_builder
    from .authentication_flows_policy import authentication_flows_policy_request_builder
    from .authentication_methods_policy import authentication_methods_policy_request_builder
    from .authentication_strength_policies import authentication_strength_policies_request_builder
    from .authentication_strength_policies.item import authentication_strength_policy_item_request_builder
    from .authorization_policy import authorization_policy_request_builder
    from .authorization_policy.item import authorization_policy_item_request_builder
    from .b2c_authentication_methods_policy import b2c_authentication_methods_policy_request_builder
    from .claims_mapping_policies import claims_mapping_policies_request_builder
    from .claims_mapping_policies.item import claims_mapping_policy_item_request_builder
    from .conditional_access_policies import conditional_access_policies_request_builder
    from .conditional_access_policies.item import conditional_access_policy_item_request_builder
    from .cross_tenant_access_policy import cross_tenant_access_policy_request_builder
    from .default_app_management_policy import default_app_management_policy_request_builder
    from .device_registration_policy import device_registration_policy_request_builder
    from .directory_role_access_review_policy import directory_role_access_review_policy_request_builder
    from .external_identities_policy import external_identities_policy_request_builder
    from .feature_rollout_policies import feature_rollout_policies_request_builder
    from .feature_rollout_policies.item import feature_rollout_policy_item_request_builder
    from .home_realm_discovery_policies import home_realm_discovery_policies_request_builder
    from .home_realm_discovery_policies.item import home_realm_discovery_policy_item_request_builder
    from .identity_security_defaults_enforcement_policy import identity_security_defaults_enforcement_policy_request_builder
    from .mobile_app_management_policies import mobile_app_management_policies_request_builder
    from .mobile_app_management_policies.item import mobility_management_policy_item_request_builder
    from .mobile_device_management_policies import mobile_device_management_policies_request_builder
    from .mobile_device_management_policies.item import mobility_management_policy_item_request_builder
    from .permission_grant_policies import permission_grant_policies_request_builder
    from .permission_grant_policies.item import permission_grant_policy_item_request_builder
    from .role_management_policies import role_management_policies_request_builder
    from .role_management_policies.item import unified_role_management_policy_item_request_builder
    from .role_management_policy_assignments import role_management_policy_assignments_request_builder
    from .role_management_policy_assignments.item import unified_role_management_policy_assignment_item_request_builder
    from .service_principal_creation_policies import service_principal_creation_policies_request_builder
    from .service_principal_creation_policies.item import service_principal_creation_policy_item_request_builder
    from .token_issuance_policies import token_issuance_policies_request_builder
    from .token_issuance_policies.item import token_issuance_policy_item_request_builder
    from .token_lifetime_policies import token_lifetime_policies_request_builder
    from .token_lifetime_policies.item import token_lifetime_policy_item_request_builder

class PoliciesRequestBuilder():
    """
    Provides operations to manage the policyRoot singleton.
    """
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
    
    def activity_based_timeout_policies_by_id(self,id: str) -> activity_based_timeout_policy_item_request_builder.ActivityBasedTimeoutPolicyItemRequestBuilder:
        """
        Provides operations to manage the activityBasedTimeoutPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: activity_based_timeout_policy_item_request_builder.ActivityBasedTimeoutPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .activity_based_timeout_policies.item import activity_based_timeout_policy_item_request_builder

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
        from .app_management_policies.item import app_management_policy_item_request_builder

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
        from .authentication_strength_policies.item import authentication_strength_policy_item_request_builder

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
        from .authorization_policy.item import authorization_policy_item_request_builder

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
        from .claims_mapping_policies.item import claims_mapping_policy_item_request_builder

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
        from .conditional_access_policies.item import conditional_access_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionalAccessPolicy%2Did"] = id
        return conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def feature_rollout_policies_by_id(self,id: str) -> feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.policyRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .feature_rollout_policies.item import feature_rollout_policy_item_request_builder

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
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import policy_root

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
        from .home_realm_discovery_policies.item import home_realm_discovery_policy_item_request_builder

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
        from .mobile_app_management_policies.item import mobility_management_policy_item_request_builder
        from .mobile_device_management_policies.item import mobility_management_policy_item_request_builder

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
        from .mobile_app_management_policies.item import mobility_management_policy_item_request_builder
        from .mobile_device_management_policies.item import mobility_management_policy_item_request_builder

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
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import policy_root

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
        from .permission_grant_policies.item import permission_grant_policy_item_request_builder

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
        from .role_management_policies.item import unified_role_management_policy_item_request_builder

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
        from .role_management_policy_assignments.item import unified_role_management_policy_assignment_item_request_builder

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
        from .service_principal_creation_policies.item import service_principal_creation_policy_item_request_builder

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
        request_info.headers["Accept"] = ["application/json"]
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
        from .token_issuance_policies.item import token_issuance_policy_item_request_builder

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
        from .token_lifetime_policies.item import token_lifetime_policy_item_request_builder

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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def access_review_policy(self) -> access_review_policy_request_builder.AccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the accessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .access_review_policy import access_review_policy_request_builder

        return access_review_policy_request_builder.AccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def activity_based_timeout_policies(self) -> activity_based_timeout_policies_request_builder.ActivityBasedTimeoutPoliciesRequestBuilder:
        """
        Provides operations to manage the activityBasedTimeoutPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .activity_based_timeout_policies import activity_based_timeout_policies_request_builder

        return activity_based_timeout_policies_request_builder.ActivityBasedTimeoutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin_consent_request_policy(self) -> admin_consent_request_policy_request_builder.AdminConsentRequestPolicyRequestBuilder:
        """
        Provides operations to manage the adminConsentRequestPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .admin_consent_request_policy import admin_consent_request_policy_request_builder

        return admin_consent_request_policy_request_builder.AdminConsentRequestPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_management_policies(self) -> app_management_policies_request_builder.AppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the appManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .app_management_policies import app_management_policies_request_builder

        return app_management_policies_request_builder.AppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_flows_policy(self) -> authentication_flows_policy_request_builder.AuthenticationFlowsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationFlowsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_flows_policy import authentication_flows_policy_request_builder

        return authentication_flows_policy_request_builder.AuthenticationFlowsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_methods_policy import authentication_methods_policy_request_builder

        return authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strength_policies(self) -> authentication_strength_policies_request_builder.AuthenticationStrengthPoliciesRequestBuilder:
        """
        Provides operations to manage the authenticationStrengthPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .authentication_strength_policies import authentication_strength_policies_request_builder

        return authentication_strength_policies_request_builder.AuthenticationStrengthPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authorization_policy(self) -> authorization_policy_request_builder.AuthorizationPolicyRequestBuilder:
        """
        Provides operations to manage the authorizationPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .authorization_policy import authorization_policy_request_builder

        return authorization_policy_request_builder.AuthorizationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2c_authentication_methods_policy(self) -> b2c_authentication_methods_policy_request_builder.B2cAuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the b2cAuthenticationMethodsPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .b2c_authentication_methods_policy import b2c_authentication_methods_policy_request_builder

        return b2c_authentication_methods_policy_request_builder.B2cAuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def claims_mapping_policies(self) -> claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder:
        """
        Provides operations to manage the claimsMappingPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .claims_mapping_policies import claims_mapping_policies_request_builder

        return claims_mapping_policies_request_builder.ClaimsMappingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_policies(self) -> conditional_access_policies_request_builder.ConditionalAccessPoliciesRequestBuilder:
        """
        Provides operations to manage the conditionalAccessPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .conditional_access_policies import conditional_access_policies_request_builder

        return conditional_access_policies_request_builder.ConditionalAccessPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_tenant_access_policy(self) -> cross_tenant_access_policy_request_builder.CrossTenantAccessPolicyRequestBuilder:
        """
        Provides operations to manage the crossTenantAccessPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .cross_tenant_access_policy import cross_tenant_access_policy_request_builder

        return cross_tenant_access_policy_request_builder.CrossTenantAccessPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_app_management_policy(self) -> default_app_management_policy_request_builder.DefaultAppManagementPolicyRequestBuilder:
        """
        Provides operations to manage the defaultAppManagementPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .default_app_management_policy import default_app_management_policy_request_builder

        return default_app_management_policy_request_builder.DefaultAppManagementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_registration_policy(self) -> device_registration_policy_request_builder.DeviceRegistrationPolicyRequestBuilder:
        """
        Provides operations to manage the deviceRegistrationPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .device_registration_policy import device_registration_policy_request_builder

        return device_registration_policy_request_builder.DeviceRegistrationPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_access_review_policy(self) -> directory_role_access_review_policy_request_builder.DirectoryRoleAccessReviewPolicyRequestBuilder:
        """
        Provides operations to manage the directoryRoleAccessReviewPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .directory_role_access_review_policy import directory_role_access_review_policy_request_builder

        return directory_role_access_review_policy_request_builder.DirectoryRoleAccessReviewPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_identities_policy(self) -> external_identities_policy_request_builder.ExternalIdentitiesPolicyRequestBuilder:
        """
        Provides operations to manage the externalIdentitiesPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .external_identities_policy import external_identities_policy_request_builder

        return external_identities_policy_request_builder.ExternalIdentitiesPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feature_rollout_policies(self) -> feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .feature_rollout_policies import feature_rollout_policies_request_builder

        return feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def home_realm_discovery_policies(self) -> home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder:
        """
        Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .home_realm_discovery_policies import home_realm_discovery_policies_request_builder

        return home_realm_discovery_policies_request_builder.HomeRealmDiscoveryPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_security_defaults_enforcement_policy(self) -> identity_security_defaults_enforcement_policy_request_builder.IdentitySecurityDefaultsEnforcementPolicyRequestBuilder:
        """
        Provides operations to manage the identitySecurityDefaultsEnforcementPolicy property of the microsoft.graph.policyRoot entity.
        """
        from .identity_security_defaults_enforcement_policy import identity_security_defaults_enforcement_policy_request_builder

        return identity_security_defaults_enforcement_policy_request_builder.IdentitySecurityDefaultsEnforcementPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_management_policies(self) -> mobile_app_management_policies_request_builder.MobileAppManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileAppManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .mobile_app_management_policies import mobile_app_management_policies_request_builder

        return mobile_app_management_policies_request_builder.MobileAppManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_device_management_policies(self) -> mobile_device_management_policies_request_builder.MobileDeviceManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the mobileDeviceManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .mobile_device_management_policies import mobile_device_management_policies_request_builder

        return mobile_device_management_policies_request_builder.MobileDeviceManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grant_policies(self) -> permission_grant_policies_request_builder.PermissionGrantPoliciesRequestBuilder:
        """
        Provides operations to manage the permissionGrantPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .permission_grant_policies import permission_grant_policies_request_builder

        return permission_grant_policies_request_builder.PermissionGrantPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policies(self) -> role_management_policies_request_builder.RoleManagementPoliciesRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .role_management_policies import role_management_policies_request_builder

        return role_management_policies_request_builder.RoleManagementPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management_policy_assignments(self) -> role_management_policy_assignments_request_builder.RoleManagementPolicyAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleManagementPolicyAssignments property of the microsoft.graph.policyRoot entity.
        """
        from .role_management_policy_assignments import role_management_policy_assignments_request_builder

        return role_management_policy_assignments_request_builder.RoleManagementPolicyAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_creation_policies(self) -> service_principal_creation_policies_request_builder.ServicePrincipalCreationPoliciesRequestBuilder:
        """
        Provides operations to manage the servicePrincipalCreationPolicies property of the microsoft.graph.policyRoot entity.
        """
        from .service_principal_creation_policies import service_principal_creation_policies_request_builder

        return service_principal_creation_policies_request_builder.ServicePrincipalCreationPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_issuance_policies(self) -> token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenIssuancePolicies property of the microsoft.graph.policyRoot entity.
        """
        from .token_issuance_policies import token_issuance_policies_request_builder

        return token_issuance_policies_request_builder.TokenIssuancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def token_lifetime_policies(self) -> token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder:
        """
        Provides operations to manage the tokenLifetimePolicies property of the microsoft.graph.policyRoot entity.
        """
        from .token_lifetime_policies import token_lifetime_policies_request_builder

        return token_lifetime_policies_request_builder.TokenLifetimePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PoliciesRequestBuilderGetQueryParameters():
        """
        Get policies
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class PoliciesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

