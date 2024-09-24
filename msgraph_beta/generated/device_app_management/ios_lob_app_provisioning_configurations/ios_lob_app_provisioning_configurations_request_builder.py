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
    from ...models.ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
    from ...models.ios_lob_app_provisioning_configuration_collection_response import IosLobAppProvisioningConfigurationCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .has_payload_links.has_payload_links_request_builder import HasPayloadLinksRequestBuilder
    from .item.ios_lob_app_provisioning_configuration_item_request_builder import IosLobAppProvisioningConfigurationItemRequestBuilder

class IosLobAppProvisioningConfigurationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new IosLobAppProvisioningConfigurationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/iosLobAppProvisioningConfigurations{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_ios_lob_app_provisioning_configuration_id(self,ios_lob_app_provisioning_configuration_id: str) -> IosLobAppProvisioningConfigurationItemRequestBuilder:
        """
        Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
        param ios_lob_app_provisioning_configuration_id: The unique identifier of iosLobAppProvisioningConfiguration
        Returns: IosLobAppProvisioningConfigurationItemRequestBuilder
        """
        if ios_lob_app_provisioning_configuration_id is None:
            raise TypeError("ios_lob_app_provisioning_configuration_id cannot be null.")
        from .item.ios_lob_app_provisioning_configuration_item_request_builder import IosLobAppProvisioningConfigurationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["iosLobAppProvisioningConfiguration%2Did"] = ios_lob_app_provisioning_configuration_id
        return IosLobAppProvisioningConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IosLobAppProvisioningConfigurationsRequestBuilderGetQueryParameters]] = None) -> Optional[IosLobAppProvisioningConfigurationCollectionResponse]:
        """
        The IOS Lob App Provisioning Configurations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IosLobAppProvisioningConfigurationCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.ios_lob_app_provisioning_configuration_collection_response import IosLobAppProvisioningConfigurationCollectionResponse

        return await self.request_adapter.send_async(request_info, IosLobAppProvisioningConfigurationCollectionResponse, error_mapping)
    
    async def post(self,body: IosLobAppProvisioningConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IosLobAppProvisioningConfiguration]:
        """
        Create new navigation property to iosLobAppProvisioningConfigurations for deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IosLobAppProvisioningConfiguration]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration

        return await self.request_adapter.send_async(request_info, IosLobAppProvisioningConfiguration, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IosLobAppProvisioningConfigurationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The IOS Lob App Provisioning Configurations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: IosLobAppProvisioningConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to iosLobAppProvisioningConfigurations for deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> IosLobAppProvisioningConfigurationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IosLobAppProvisioningConfigurationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IosLobAppProvisioningConfigurationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def has_payload_links(self) -> HasPayloadLinksRequestBuilder:
        """
        Provides operations to call the hasPayloadLinks method.
        """
        from .has_payload_links.has_payload_links_request_builder import HasPayloadLinksRequestBuilder

        return HasPayloadLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IosLobAppProvisioningConfigurationsRequestBuilderGetQueryParameters():
        """
        The IOS Lob App Provisioning Configurations.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class IosLobAppProvisioningConfigurationsRequestBuilderGetRequestConfiguration(RequestConfiguration[IosLobAppProvisioningConfigurationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IosLobAppProvisioningConfigurationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

