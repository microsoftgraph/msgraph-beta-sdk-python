from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.networkaccess.branch_connectivity_configuration import BranchConnectivityConfiguration
    from ......models.o_data_errors.o_data_error import ODataError
    from .links.links_request_builder import LinksRequestBuilder

class ConnectivityConfigurationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the connectivityConfiguration property of the microsoft.graph.networkaccess.branchSite entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ConnectivityConfigurationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/connectivityConfiguration{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ConnectivityConfigurationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property connectivityConfiguration for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ConnectivityConfigurationRequestBuilderGetRequestConfiguration] = None) -> Optional[BranchConnectivityConfiguration]:
        """
        Get connectivityConfiguration from networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BranchConnectivityConfiguration]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.networkaccess.branch_connectivity_configuration import BranchConnectivityConfiguration

        return await self.request_adapter.send_async(request_info, BranchConnectivityConfiguration, error_mapping)
    
    async def patch(self,body: Optional[BranchConnectivityConfiguration] = None, request_configuration: Optional[ConnectivityConfigurationRequestBuilderPatchRequestConfiguration] = None) -> Optional[BranchConnectivityConfiguration]:
        """
        Update the navigation property connectivityConfiguration in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BranchConnectivityConfiguration]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.networkaccess.branch_connectivity_configuration import BranchConnectivityConfiguration

        return await self.request_adapter.send_async(request_info, BranchConnectivityConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ConnectivityConfigurationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property connectivityConfiguration for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ConnectivityConfigurationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get connectivityConfiguration from networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[BranchConnectivityConfiguration] = None, request_configuration: Optional[ConnectivityConfigurationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property connectivityConfiguration in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def links(self) -> LinksRequestBuilder:
        """
        Provides operations to manage the links property of the microsoft.graph.networkaccess.branchConnectivityConfiguration entity.
        """
        from .links.links_request_builder import LinksRequestBuilder

        return LinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ConnectivityConfigurationRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ConnectivityConfigurationRequestBuilderGetQueryParameters():
        """
        Get connectivityConfiguration from networkAccess
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ConnectivityConfigurationRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ConnectivityConfigurationRequestBuilder.ConnectivityConfigurationRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ConnectivityConfigurationRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

