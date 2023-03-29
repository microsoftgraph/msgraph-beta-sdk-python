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
    from ..models import directory
    from ..models.o_data_errors import o_data_error
    from .administrative_units import administrative_units_request_builder
    from .administrative_units.item import administrative_unit_item_request_builder
    from .attribute_sets import attribute_sets_request_builder
    from .attribute_sets.item import attribute_set_item_request_builder
    from .custom_security_attribute_definitions import custom_security_attribute_definitions_request_builder
    from .custom_security_attribute_definitions.item import custom_security_attribute_definition_item_request_builder
    from .deleted_items import deleted_items_request_builder
    from .deleted_items.item import directory_object_item_request_builder
    from .feature_rollout_policies import feature_rollout_policies_request_builder
    from .feature_rollout_policies.item import feature_rollout_policy_item_request_builder
    from .federation_configurations import federation_configurations_request_builder
    from .federation_configurations.item import identity_provider_base_item_request_builder
    from .impacted_resources import impacted_resources_request_builder
    from .impacted_resources.item import impacted_resource_item_request_builder
    from .inbound_shared_user_profiles import inbound_shared_user_profiles_request_builder
    from .inbound_shared_user_profiles.item import inbound_shared_user_profile_user_item_request_builder
    from .on_premises_synchronization import on_premises_synchronization_request_builder
    from .on_premises_synchronization.item import on_premises_directory_synchronization_item_request_builder
    from .outbound_shared_user_profiles import outbound_shared_user_profiles_request_builder
    from .outbound_shared_user_profiles.item import outbound_shared_user_profile_user_item_request_builder
    from .recommendations import recommendations_request_builder
    from .recommendations.item import recommendation_item_request_builder
    from .shared_email_domains import shared_email_domains_request_builder
    from .shared_email_domains.item import shared_email_domain_item_request_builder

class DirectoryRequestBuilder():
    """
    Provides operations to manage the directory singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directory{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def administrative_units_by_id(self,id: str) -> administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .administrative_units.item import administrative_unit_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["administrativeUnit%2Did"] = id
        return administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def attribute_sets_by_id(self,id: str) -> attribute_set_item_request_builder.AttributeSetItemRequestBuilder:
        """
        Provides operations to manage the attributeSets property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: attribute_set_item_request_builder.AttributeSetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .attribute_sets.item import attribute_set_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attributeSet%2Did"] = id
        return attribute_set_item_request_builder.AttributeSetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def custom_security_attribute_definitions_by_id(self,id: str) -> custom_security_attribute_definition_item_request_builder.CustomSecurityAttributeDefinitionItemRequestBuilder:
        """
        Provides operations to manage the customSecurityAttributeDefinitions property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: custom_security_attribute_definition_item_request_builder.CustomSecurityAttributeDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .custom_security_attribute_definitions.item import custom_security_attribute_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["customSecurityAttributeDefinition%2Did"] = id
        return custom_security_attribute_definition_item_request_builder.CustomSecurityAttributeDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def deleted_items_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .deleted_items.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def feature_rollout_policies_by_id(self,id: str) -> feature_rollout_policy_item_request_builder.FeatureRolloutPolicyItemRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.directory entity.
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
    
    def federation_configurations_by_id(self,id: str) -> identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .federation_configurations.item import identity_provider_base_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProviderBase%2Did"] = id
        return identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None) -> Optional[directory.Directory]:
        """
        Get directory
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[directory.Directory]
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
        from ..models import directory

        return await self.request_adapter.send_async(request_info, directory.Directory, error_mapping)
    
    def impacted_resources_by_id(self,id: str) -> impacted_resource_item_request_builder.ImpactedResourceItemRequestBuilder:
        """
        Provides operations to manage the impactedResources property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: impacted_resource_item_request_builder.ImpactedResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .impacted_resources.item import impacted_resource_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["impactedResource%2Did"] = id
        return impacted_resource_item_request_builder.ImpactedResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def inbound_shared_user_profiles_by_id(self,id: str) -> inbound_shared_user_profile_user_item_request_builder.InboundSharedUserProfileUserItemRequestBuilder:
        """
        Provides operations to manage the inboundSharedUserProfiles property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: inbound_shared_user_profile_user_item_request_builder.InboundSharedUserProfileUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .inbound_shared_user_profiles.item import inbound_shared_user_profile_user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["inboundSharedUserProfile%2DuserId"] = id
        return inbound_shared_user_profile_user_item_request_builder.InboundSharedUserProfileUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def on_premises_synchronization_by_id(self,id: str) -> on_premises_directory_synchronization_item_request_builder.OnPremisesDirectorySynchronizationItemRequestBuilder:
        """
        Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: on_premises_directory_synchronization_item_request_builder.OnPremisesDirectorySynchronizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .on_premises_synchronization.item import on_premises_directory_synchronization_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onPremisesDirectorySynchronization%2Did"] = id
        return on_premises_directory_synchronization_item_request_builder.OnPremisesDirectorySynchronizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def outbound_shared_user_profiles_by_id(self,id: str) -> outbound_shared_user_profile_user_item_request_builder.OutboundSharedUserProfileUserItemRequestBuilder:
        """
        Provides operations to manage the outboundSharedUserProfiles property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: outbound_shared_user_profile_user_item_request_builder.OutboundSharedUserProfileUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .outbound_shared_user_profiles.item import outbound_shared_user_profile_user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["outboundSharedUserProfile%2DuserId"] = id
        return outbound_shared_user_profile_user_item_request_builder.OutboundSharedUserProfileUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[directory.Directory] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None) -> Optional[directory.Directory]:
        """
        Update directory
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[directory.Directory]
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
        from ..models import directory

        return await self.request_adapter.send_async(request_info, directory.Directory, error_mapping)
    
    def recommendations_by_id(self,id: str) -> recommendation_item_request_builder.RecommendationItemRequestBuilder:
        """
        Provides operations to manage the recommendations property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: recommendation_item_request_builder.RecommendationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .recommendations.item import recommendation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["recommendation%2Did"] = id
        return recommendation_item_request_builder.RecommendationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shared_email_domains_by_id(self,id: str) -> shared_email_domain_item_request_builder.SharedEmailDomainItemRequestBuilder:
        """
        Provides operations to manage the sharedEmailDomains property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: shared_email_domain_item_request_builder.SharedEmailDomainItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .shared_email_domains.item import shared_email_domain_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharedEmailDomain%2Did"] = id
        return shared_email_domain_item_request_builder.SharedEmailDomainItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get directory
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
    
    def to_patch_request_information(self,body: Optional[directory.Directory] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update directory
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
    def administrative_units(self) -> administrative_units_request_builder.AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        """
        from .administrative_units import administrative_units_request_builder

        return administrative_units_request_builder.AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attribute_sets(self) -> attribute_sets_request_builder.AttributeSetsRequestBuilder:
        """
        Provides operations to manage the attributeSets property of the microsoft.graph.directory entity.
        """
        from .attribute_sets import attribute_sets_request_builder

        return attribute_sets_request_builder.AttributeSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_security_attribute_definitions(self) -> custom_security_attribute_definitions_request_builder.CustomSecurityAttributeDefinitionsRequestBuilder:
        """
        Provides operations to manage the customSecurityAttributeDefinitions property of the microsoft.graph.directory entity.
        """
        from .custom_security_attribute_definitions import custom_security_attribute_definitions_request_builder

        return custom_security_attribute_definitions_request_builder.CustomSecurityAttributeDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_items(self) -> deleted_items_request_builder.DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        """
        from .deleted_items import deleted_items_request_builder

        return deleted_items_request_builder.DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def feature_rollout_policies(self) -> feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder:
        """
        Provides operations to manage the featureRolloutPolicies property of the microsoft.graph.directory entity.
        """
        from .feature_rollout_policies import feature_rollout_policies_request_builder

        return feature_rollout_policies_request_builder.FeatureRolloutPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federation_configurations(self) -> federation_configurations_request_builder.FederationConfigurationsRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        """
        from .federation_configurations import federation_configurations_request_builder

        return federation_configurations_request_builder.FederationConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def impacted_resources(self) -> impacted_resources_request_builder.ImpactedResourcesRequestBuilder:
        """
        Provides operations to manage the impactedResources property of the microsoft.graph.directory entity.
        """
        from .impacted_resources import impacted_resources_request_builder

        return impacted_resources_request_builder.ImpactedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inbound_shared_user_profiles(self) -> inbound_shared_user_profiles_request_builder.InboundSharedUserProfilesRequestBuilder:
        """
        Provides operations to manage the inboundSharedUserProfiles property of the microsoft.graph.directory entity.
        """
        from .inbound_shared_user_profiles import inbound_shared_user_profiles_request_builder

        return inbound_shared_user_profiles_request_builder.InboundSharedUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_synchronization(self) -> on_premises_synchronization_request_builder.OnPremisesSynchronizationRequestBuilder:
        """
        Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
        """
        from .on_premises_synchronization import on_premises_synchronization_request_builder

        return on_premises_synchronization_request_builder.OnPremisesSynchronizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbound_shared_user_profiles(self) -> outbound_shared_user_profiles_request_builder.OutboundSharedUserProfilesRequestBuilder:
        """
        Provides operations to manage the outboundSharedUserProfiles property of the microsoft.graph.directory entity.
        """
        from .outbound_shared_user_profiles import outbound_shared_user_profiles_request_builder

        return outbound_shared_user_profiles_request_builder.OutboundSharedUserProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recommendations(self) -> recommendations_request_builder.RecommendationsRequestBuilder:
        """
        Provides operations to manage the recommendations property of the microsoft.graph.directory entity.
        """
        from .recommendations import recommendations_request_builder

        return recommendations_request_builder.RecommendationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_email_domains(self) -> shared_email_domains_request_builder.SharedEmailDomainsRequestBuilder:
        """
        Provides operations to manage the sharedEmailDomains property of the microsoft.graph.directory entity.
        """
        from .shared_email_domains import shared_email_domains_request_builder

        return shared_email_domains_request_builder.SharedEmailDomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DirectoryRequestBuilderGetQueryParameters():
        """
        Get directory
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
    class DirectoryRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DirectoryRequestBuilder.DirectoryRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DirectoryRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

