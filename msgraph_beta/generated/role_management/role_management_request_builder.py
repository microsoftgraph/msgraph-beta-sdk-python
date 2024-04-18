from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.role_management import RoleManagement
    from .cloud_p_c.cloud_p_c_request_builder import CloudPCRequestBuilder
    from .device_management.device_management_request_builder import DeviceManagementRequestBuilder
    from .directory.directory_request_builder import DirectoryRequestBuilder
    from .enterprise_apps.enterprise_apps_request_builder import EnterpriseAppsRequestBuilder
    from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder
    from .exchange.exchange_request_builder import ExchangeRequestBuilder

class RoleManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the roleManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RoleManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[RoleManagement]:
        """
        Get roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RoleManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.role_management import RoleManagement

        return await self.request_adapter.send_async(request_info, RoleManagement, error_mapping)
    
    async def patch(self,body: Optional[RoleManagement] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[RoleManagement]:
        """
        Update roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RoleManagement]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.role_management import RoleManagement

        return await self.request_adapter.send_async(request_info, RoleManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[RoleManagement] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> RoleManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RoleManagementRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RoleManagementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cloud_p_c(self) -> CloudPCRequestBuilder:
        """
        Provides operations to manage the cloudPC property of the microsoft.graph.roleManagement entity.
        """
        from .cloud_p_c.cloud_p_c_request_builder import CloudPCRequestBuilder

        return CloudPCRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement property of the microsoft.graph.roleManagement entity.
        """
        from .device_management.device_management_request_builder import DeviceManagementRequestBuilder

        return DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory(self) -> DirectoryRequestBuilder:
        """
        Provides operations to manage the directory property of the microsoft.graph.roleManagement entity.
        """
        from .directory.directory_request_builder import DirectoryRequestBuilder

        return DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enterprise_apps(self) -> EnterpriseAppsRequestBuilder:
        """
        Provides operations to manage the enterpriseApps property of the microsoft.graph.roleManagement entity.
        """
        from .enterprise_apps.enterprise_apps_request_builder import EnterpriseAppsRequestBuilder

        return EnterpriseAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entitlement_management(self) -> EntitlementManagementRequestBuilder:
        """
        Provides operations to manage the entitlementManagement property of the microsoft.graph.roleManagement entity.
        """
        from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder

        return EntitlementManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange(self) -> ExchangeRequestBuilder:
        """
        Provides operations to manage the exchange property of the microsoft.graph.roleManagement entity.
        """
        from .exchange.exchange_request_builder import ExchangeRequestBuilder

        return ExchangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RoleManagementRequestBuilderGetQueryParameters():
        """
        Get roleManagement
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

    

