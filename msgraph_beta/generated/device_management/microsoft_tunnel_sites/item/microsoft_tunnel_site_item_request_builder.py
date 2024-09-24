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
    from ....models.microsoft_tunnel_site import MicrosoftTunnelSite
    from ....models.o_data_errors.o_data_error import ODataError
    from .microsoft_tunnel_configuration.microsoft_tunnel_configuration_request_builder import MicrosoftTunnelConfigurationRequestBuilder
    from .microsoft_tunnel_servers.microsoft_tunnel_servers_request_builder import MicrosoftTunnelServersRequestBuilder
    from .request_upgrade.request_upgrade_request_builder import RequestUpgradeRequestBuilder

class MicrosoftTunnelSiteItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the microsoftTunnelSites property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftTunnelSiteItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property microsoftTunnelSites for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MicrosoftTunnelSiteItemRequestBuilderGetQueryParameters]] = None) -> Optional[MicrosoftTunnelSite]:
        """
        Collection of MicrosoftTunnelSite settings associated with account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftTunnelSite]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.microsoft_tunnel_site import MicrosoftTunnelSite

        return await self.request_adapter.send_async(request_info, MicrosoftTunnelSite, error_mapping)
    
    async def patch(self,body: MicrosoftTunnelSite, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MicrosoftTunnelSite]:
        """
        Update the navigation property microsoftTunnelSites in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftTunnelSite]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.microsoft_tunnel_site import MicrosoftTunnelSite

        return await self.request_adapter.send_async(request_info, MicrosoftTunnelSite, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property microsoftTunnelSites for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MicrosoftTunnelSiteItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Collection of MicrosoftTunnelSite settings associated with account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MicrosoftTunnelSite, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property microsoftTunnelSites in deviceManagement
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
    
    def with_url(self,raw_url: str) -> MicrosoftTunnelSiteItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftTunnelSiteItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftTunnelSiteItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def microsoft_tunnel_configuration(self) -> MicrosoftTunnelConfigurationRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelConfiguration property of the microsoft.graph.microsoftTunnelSite entity.
        """
        from .microsoft_tunnel_configuration.microsoft_tunnel_configuration_request_builder import MicrosoftTunnelConfigurationRequestBuilder

        return MicrosoftTunnelConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_tunnel_servers(self) -> MicrosoftTunnelServersRequestBuilder:
        """
        Provides operations to manage the microsoftTunnelServers property of the microsoft.graph.microsoftTunnelSite entity.
        """
        from .microsoft_tunnel_servers.microsoft_tunnel_servers_request_builder import MicrosoftTunnelServersRequestBuilder

        return MicrosoftTunnelServersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_upgrade(self) -> RequestUpgradeRequestBuilder:
        """
        Provides operations to call the requestUpgrade method.
        """
        from .request_upgrade.request_upgrade_request_builder import RequestUpgradeRequestBuilder

        return RequestUpgradeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MicrosoftTunnelSiteItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MicrosoftTunnelSiteItemRequestBuilderGetQueryParameters():
        """
        Collection of MicrosoftTunnelSite settings associated with account.
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
    class MicrosoftTunnelSiteItemRequestBuilderGetRequestConfiguration(RequestConfiguration[MicrosoftTunnelSiteItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MicrosoftTunnelSiteItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

