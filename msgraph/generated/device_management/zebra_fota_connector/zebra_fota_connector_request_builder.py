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

approve_fota_apps_request_builder = lazy_import('msgraph.generated.device_management.zebra_fota_connector.approve_fota_apps.approve_fota_apps_request_builder')
connect_request_builder = lazy_import('msgraph.generated.device_management.zebra_fota_connector.connect.connect_request_builder')
disconnect_request_builder = lazy_import('msgraph.generated.device_management.zebra_fota_connector.disconnect.disconnect_request_builder')
has_active_deployments_request_builder = lazy_import('msgraph.generated.device_management.zebra_fota_connector.has_active_deployments.has_active_deployments_request_builder')
zebra_fota_connector = lazy_import('msgraph.generated.models.zebra_fota_connector')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ZebraFotaConnectorRequestBuilder():
    """
    Provides operations to manage the zebraFotaConnector property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def approve_fota_apps(self) -> approve_fota_apps_request_builder.ApproveFotaAppsRequestBuilder:
        """
        Provides operations to call the approveFotaApps method.
        """
        return approve_fota_apps_request_builder.ApproveFotaAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connect(self) -> connect_request_builder.ConnectRequestBuilder:
        """
        Provides operations to call the connect method.
        """
        return connect_request_builder.ConnectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disconnect(self) -> disconnect_request_builder.DisconnectRequestBuilder:
        """
        Provides operations to call the disconnect method.
        """
        return disconnect_request_builder.DisconnectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def has_active_deployments(self) -> has_active_deployments_request_builder.HasActiveDeploymentsRequestBuilder:
        """
        Provides operations to call the hasActiveDeployments method.
        """
        return has_active_deployments_request_builder.HasActiveDeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ZebraFotaConnectorRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/zebraFotaConnector{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property zebraFotaConnector for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def create_get_request_information(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The singleton ZebraFotaConnector associated with account.
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
    
    def create_patch_request_information(self,body: Optional[zebra_fota_connector.ZebraFotaConnector] = None, request_configuration: Optional[ZebraFotaConnectorRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property zebraFotaConnector in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property zebraFotaConnector for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[ZebraFotaConnectorRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[zebra_fota_connector.ZebraFotaConnector]:
        """
        The singleton ZebraFotaConnector associated with account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[zebra_fota_connector.ZebraFotaConnector]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, zebra_fota_connector.ZebraFotaConnector, response_handler, error_mapping)
    
    async def patch(self,body: Optional[zebra_fota_connector.ZebraFotaConnector] = None, request_configuration: Optional[ZebraFotaConnectorRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[zebra_fota_connector.ZebraFotaConnector]:
        """
        Update the navigation property zebraFotaConnector in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[zebra_fota_connector.ZebraFotaConnector]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, zebra_fota_connector.ZebraFotaConnector, response_handler, error_mapping)
    
    @dataclass
    class ZebraFotaConnectorRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ZebraFotaConnectorRequestBuilderGetQueryParameters():
        """
        The singleton ZebraFotaConnector associated with account.
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
    class ZebraFotaConnectorRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ZebraFotaConnectorRequestBuilder.ZebraFotaConnectorRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ZebraFotaConnectorRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

