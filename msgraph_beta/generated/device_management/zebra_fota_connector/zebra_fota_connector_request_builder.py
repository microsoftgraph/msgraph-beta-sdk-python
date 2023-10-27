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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.zebra_fota_connector import ZebraFotaConnector
    from .approve_fota_apps.approve_fota_apps_request_builder import ApproveFotaAppsRequestBuilder
    from .connect.connect_request_builder import ConnectRequestBuilder
    from .disconnect.disconnect_request_builder import DisconnectRequestBuilder
    from .has_active_deployments.has_active_deployments_request_builder import HasActiveDeploymentsRequestBuilder

class ZebraFotaConnectorRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the zebraFotaConnector property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ZebraFotaConnectorRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/zebraFotaConnector{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property zebraFotaConnector for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderGetRequestConfiguration] = None) -> Optional[ZebraFotaConnector]:
        """
        The singleton ZebraFotaConnector associated with account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ZebraFotaConnector]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.zebra_fota_connector import ZebraFotaConnector

        return await self.request_adapter.send_async(request_info, ZebraFotaConnector, error_mapping)
    
    async def patch(self,body: Optional[ZebraFotaConnector] = None, request_configuration: Optional[ZebraFotaConnectorRequestBuilderPatchRequestConfiguration] = None) -> Optional[ZebraFotaConnector]:
        """
        Update the navigation property zebraFotaConnector in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ZebraFotaConnector]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.zebra_fota_connector import ZebraFotaConnector

        return await self.request_adapter.send_async(request_info, ZebraFotaConnector, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property zebraFotaConnector for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The singleton ZebraFotaConnector associated with account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ZebraFotaConnector] = None, request_configuration: Optional[ZebraFotaConnectorRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property zebraFotaConnector in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ZebraFotaConnectorRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ZebraFotaConnectorRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ZebraFotaConnectorRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def approve_fota_apps(self) -> ApproveFotaAppsRequestBuilder:
        """
        Provides operations to call the approveFotaApps method.
        """
        from .approve_fota_apps.approve_fota_apps_request_builder import ApproveFotaAppsRequestBuilder

        return ApproveFotaAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connect(self) -> ConnectRequestBuilder:
        """
        Provides operations to call the connect method.
        """
        from .connect.connect_request_builder import ConnectRequestBuilder

        return ConnectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disconnect(self) -> DisconnectRequestBuilder:
        """
        Provides operations to call the disconnect method.
        """
        from .disconnect.disconnect_request_builder import DisconnectRequestBuilder

        return DisconnectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def has_active_deployments(self) -> HasActiveDeploymentsRequestBuilder:
        """
        Provides operations to call the hasActiveDeployments method.
        """
        from .has_active_deployments.has_active_deployments_request_builder import HasActiveDeploymentsRequestBuilder

        return HasActiveDeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ZebraFotaConnectorRequestBuilderGetQueryParameters():
        """
        The singleton ZebraFotaConnector associated with account.
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
    class ZebraFotaConnectorRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ZebraFotaConnectorRequestBuilder.ZebraFotaConnectorRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ZebraFotaConnectorRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

