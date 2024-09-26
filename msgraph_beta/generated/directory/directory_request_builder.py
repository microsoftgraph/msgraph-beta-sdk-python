from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.directory import Directory
    from ..models.o_data_errors.o_data_error import ODataError
    from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder
    from .attribute_sets.attribute_sets_request_builder import AttributeSetsRequestBuilder
    from .certificate_authorities.certificate_authorities_request_builder import CertificateAuthoritiesRequestBuilder
    from .custom_security_attribute_definitions.custom_security_attribute_definitions_request_builder import CustomSecurityAttributeDefinitionsRequestBuilder
    from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder
    from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder
    from .external_user_profiles.external_user_profiles_request_builder import ExternalUserProfilesRequestBuilder
    from .feature_rollout_policies.feature_rollout_policies_request_builder import FeatureRolloutPoliciesRequestBuilder
    from .federation_configurations.federation_configurations_request_builder import FederationConfigurationsRequestBuilder
    from .impacted_resources.impacted_resources_request_builder import ImpactedResourcesRequestBuilder
    from .inbound_shared_user_profiles.inbound_shared_user_profiles_request_builder import InboundSharedUserProfilesRequestBuilder
    from .on_premises_synchronization.on_premises_synchronization_request_builder import OnPremisesSynchronizationRequestBuilder
    from .outbound_shared_user_profiles.outbound_shared_user_profiles_request_builder import OutboundSharedUserProfilesRequestBuilder
    from .pending_external_user_profiles.pending_external_user_profiles_request_builder import PendingExternalUserProfilesRequestBuilder
    from .recommendations.recommendations_request_builder import RecommendationsRequestBuilder
    from .shared_email_domains.shared_email_domains_request_builder import SharedEmailDomainsRequestBuilder
    from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder
    from .subscriptions_with_commerce_subscription_id.subscriptions_with_commerce_subscription_id_request_builder import SubscriptionsWithCommerceSubscriptionIdRequestBuilder
    from .subscriptions_with_ocp_subscription_id.subscriptions_with_ocp_subscription_id_request_builder import SubscriptionsWithOcpSubscriptionIdRequestBuilder

class DirectoryRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the directory singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DirectoryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]] = None) -> Optional[Directory]:
        """
        Get directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Directory]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.directory import Directory

        return await self.request_adapter.send_async(request_info, Directory, error_mapping)
    
    async def patch(self,body: Directory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Directory]:
        """
        Update directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Directory]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.directory import Directory

        return await self.request_adapter.send_async(request_info, Directory, error_mapping)
    
    def subscriptions_with_commerce_subscription_id(self,commerce_subscription_id: str) -> SubscriptionsWithCommerceSubscriptionIdRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.directory entity.
        param commerce_subscription_id: Alternate key of companySubscription
        Returns: SubscriptionsWithCommerceSubscriptionIdRequestBuilder
        """
        if commerce_subscription_id is None:
            raise TypeError("commerce_subscription_id cannot be null.")
        from .subscriptions_with_commerce_subscription_id.subscriptions_with_commerce_subscription_id_request_builder import SubscriptionsWithCommerceSubscriptionIdRequestBuilder

        return SubscriptionsWithCommerceSubscriptionIdRequestBuilder(self.request_adapter, self.path_parameters, commerce_subscription_id)
    
    def subscriptions_with_ocp_subscription_id(self,ocp_subscription_id: str) -> SubscriptionsWithOcpSubscriptionIdRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.directory entity.
        param ocp_subscription_id: Alternate key of companySubscription
        Returns: SubscriptionsWithOcpSubscriptionIdRequestBuilder
        """
        if ocp_subscription_id is None:
            raise TypeError("ocp_subscription_id cannot be null.")
        from .subscriptions_with_ocp_subscription_id.subscriptions_with_ocp_subscription_id_request_builder import SubscriptionsWithOcpSubscriptionIdRequestBuilder

        return SubscriptionsWithOcpSubscriptionIdRequestBuilder(self.request_adapter, self.path_parameters, ocp_subscription_id)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Directory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DirectoryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DirectoryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DirectoryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def administrative_units(self) -> AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        """
        from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder

        return AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attribute_sets(self) -> AttributeSetsRequestBuilder:
        """
        Provides operations to manage the attributeSets property of the microsoft.graph.directory entity.
        """
        from .attribute_sets.attribute_sets_request_builder import AttributeSetsRequestBuilder

        return AttributeSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_authorities(self) -> CertificateAuthoritiesRequestBuilder:
        """
        Provides operations to manage the certificateAuthorities property of the microsoft.graph.directory entity.
        """
        from .certificate_authorities.certificate_authorities_request_builder import CertificateAuthoritiesRequestBuilder

        return CertificateAuthoritiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_security_attribute_definitions(self) -> CustomSecurityAttributeDefinitionsRequestBuilder:
        """
        Provides operations to manage the customSecurityAttributeDefinitions property of the microsoft.graph.directory entity.
        """
        from .custom_security_attribute_definitions.custom_security_attribute_definitions_request_builder import CustomSecurityAttributeDefinitionsRequestBuilder

        return CustomSecurityAttributeDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_items(self) -> DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        """
        from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder

        return DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_local_credentials(self) -> DeviceLocalCredentialsRequestBuilder:
        """
        Provides operations to manage the deviceLocalCredentials property of the microsoft.graph.directory entity.
        """
        from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder

        return DeviceLocalCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_user_profiles(self) -> ExternalUserProfilesRequestBuilder:
        """
        Provides operations to manage the externalUserProfiles property of the microsoft.graph.directory entity.
        """
        from .external_user_profiles.external_user_profiles_request_builder import ExternalUserProfilesRequestBuilder

        return ExternalUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feature_rollout_policies(self) -> FeatureRolloutPoliciesRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.directory entity.
        """
        from .feature_rollout_policies.feature_rollout_policies_request_builder import FeatureRolloutPoliciesRequestBuilder

        return FeatureRolloutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federation_configurations(self) -> FederationConfigurationsRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        """
        from .federation_configurations.federation_configurations_request_builder import FederationConfigurationsRequestBuilder

        return FederationConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def impacted_resources(self) -> ImpactedResourcesRequestBuilder:
        """
        Provides operations to manage the impactedResources property of the microsoft.graph.directory entity.
        """
        from .impacted_resources.impacted_resources_request_builder import ImpactedResourcesRequestBuilder

        return ImpactedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inbound_shared_user_profiles(self) -> InboundSharedUserProfilesRequestBuilder:
        """
        Provides operations to manage the inboundSharedUserProfiles property of the microsoft.graph.directory entity.
        """
        from .inbound_shared_user_profiles.inbound_shared_user_profiles_request_builder import InboundSharedUserProfilesRequestBuilder

        return InboundSharedUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_synchronization(self) -> OnPremisesSynchronizationRequestBuilder:
        """
        Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
        """
        from .on_premises_synchronization.on_premises_synchronization_request_builder import OnPremisesSynchronizationRequestBuilder

        return OnPremisesSynchronizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbound_shared_user_profiles(self) -> OutboundSharedUserProfilesRequestBuilder:
        """
        Provides operations to manage the outboundSharedUserProfiles property of the microsoft.graph.directory entity.
        """
        from .outbound_shared_user_profiles.outbound_shared_user_profiles_request_builder import OutboundSharedUserProfilesRequestBuilder

        return OutboundSharedUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pending_external_user_profiles(self) -> PendingExternalUserProfilesRequestBuilder:
        """
        Provides operations to manage the pendingExternalUserProfiles property of the microsoft.graph.directory entity.
        """
        from .pending_external_user_profiles.pending_external_user_profiles_request_builder import PendingExternalUserProfilesRequestBuilder

        return PendingExternalUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recommendations(self) -> RecommendationsRequestBuilder:
        """
        Provides operations to manage the recommendations property of the microsoft.graph.directory entity.
        """
        from .recommendations.recommendations_request_builder import RecommendationsRequestBuilder

        return RecommendationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_email_domains(self) -> SharedEmailDomainsRequestBuilder:
        """
        Provides operations to manage the sharedEmailDomains property of the microsoft.graph.directory entity.
        """
        from .shared_email_domains.shared_email_domains_request_builder import SharedEmailDomainsRequestBuilder

        return SharedEmailDomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.directory entity.
        """
        from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder

        return SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DirectoryRequestBuilderGetQueryParameters():
        """
        Get directory
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
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
    class DirectoryRequestBuilderGetRequestConfiguration(RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DirectoryRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

