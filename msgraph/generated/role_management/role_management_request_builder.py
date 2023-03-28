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
    from ..models import role_management
    from ..models.o_data_errors import o_data_error
    from .cloud_p_c import cloud_p_c_request_builder
    from .device_management import device_management_request_builder
    from .directory import directory_request_builder
    from .entitlement_management import entitlement_management_request_builder
    from .exchange import exchange_request_builder

class RoleManagementRequestBuilder():
    """
    Provides operations to manage the roleManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RoleManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[RoleManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[role_management.RoleManagement]:
        """
        Get roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[role_management.RoleManagement]
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
        from ..models import role_management

        return await self.request_adapter.send_async(request_info, role_management.RoleManagement, error_mapping)
    
    async def patch(self,body: Optional[role_management.RoleManagement] = None, request_configuration: Optional[RoleManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[role_management.RoleManagement]:
        """
        Update roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[role_management.RoleManagement]
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
        from ..models import role_management

        return await self.request_adapter.send_async(request_info, role_management.RoleManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RoleManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get roleManagement
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
    
    def to_patch_request_information(self,body: Optional[role_management.RoleManagement] = None, request_configuration: Optional[RoleManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update roleManagement
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
    def cloud_p_c(self) -> cloud_p_c_request_builder.CloudPCRequestBuilder:
        """
        Provides operations to manage the cloudPC property of the microsoft.graph.roleManagement entity.
        """
        from .cloud_p_c import cloud_p_c_request_builder

        return cloud_p_c_request_builder.CloudPCRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> device_management_request_builder.DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement property of the microsoft.graph.roleManagement entity.
        """
        from .device_management import device_management_request_builder

        return device_management_request_builder.DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory(self) -> directory_request_builder.DirectoryRequestBuilder:
        """
        Provides operations to manage the directory property of the microsoft.graph.roleManagement entity.
        """
        from .directory import directory_request_builder

        return directory_request_builder.DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entitlement_management(self) -> entitlement_management_request_builder.EntitlementManagementRequestBuilder:
        """
        Provides operations to manage the entitlementManagement property of the microsoft.graph.roleManagement entity.
        """
        from .entitlement_management import entitlement_management_request_builder

        return entitlement_management_request_builder.EntitlementManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange(self) -> exchange_request_builder.ExchangeRequestBuilder:
        """
        Provides operations to manage the exchange property of the microsoft.graph.roleManagement entity.
        """
        from .exchange import exchange_request_builder

        return exchange_request_builder.ExchangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RoleManagementRequestBuilderGetQueryParameters():
        """
        Get roleManagement
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
    class RoleManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[RoleManagementRequestBuilder.RoleManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class RoleManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

