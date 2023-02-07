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

managed_device = lazy_import('msgraph.generated.models.managed_device')
managed_device_collection_response = lazy_import('msgraph.generated.models.managed_device_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
count_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.count.count_request_builder')
microsoft_graph_app_diagnostics_with_upn_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_app_diagnostics_with_upn.microsoft_graph_app_diagnostics_with_upn_request_builder')
microsoft_graph_bulk_reprovision_cloud_pc_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_bulk_reprovision_cloud_pc.microsoft_graph_bulk_reprovision_cloud_pc_request_builder')
microsoft_graph_bulk_restore_cloud_pc_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_bulk_restore_cloud_pc.microsoft_graph_bulk_restore_cloud_pc_request_builder')
microsoft_graph_bulk_set_cloud_pc_review_status_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_bulk_set_cloud_pc_review_status.microsoft_graph_bulk_set_cloud_pc_review_status_request_builder')
microsoft_graph_download_app_diagnostics_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_download_app_diagnostics.microsoft_graph_download_app_diagnostics_request_builder')
microsoft_graph_execute_action_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_execute_action.microsoft_graph_execute_action_request_builder')
microsoft_graph_move_devices_to_o_u_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.microsoft_graph_move_devices_to_o_u.microsoft_graph_move_devices_to_o_u_request_builder')

class ManagedDevicesRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_bulk_reprovision_cloud_pc(self) -> microsoft_graph_bulk_reprovision_cloud_pc_request_builder.MicrosoftGraphBulkReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the bulkReprovisionCloudPc method.
        """
        return microsoft_graph_bulk_reprovision_cloud_pc_request_builder.MicrosoftGraphBulkReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_bulk_restore_cloud_pc(self) -> microsoft_graph_bulk_restore_cloud_pc_request_builder.MicrosoftGraphBulkRestoreCloudPcRequestBuilder:
        """
        Provides operations to call the bulkRestoreCloudPc method.
        """
        return microsoft_graph_bulk_restore_cloud_pc_request_builder.MicrosoftGraphBulkRestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_bulk_set_cloud_pc_review_status(self) -> microsoft_graph_bulk_set_cloud_pc_review_status_request_builder.MicrosoftGraphBulkSetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the bulkSetCloudPcReviewStatus method.
        """
        return microsoft_graph_bulk_set_cloud_pc_review_status_request_builder.MicrosoftGraphBulkSetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_download_app_diagnostics(self) -> microsoft_graph_download_app_diagnostics_request_builder.MicrosoftGraphDownloadAppDiagnosticsRequestBuilder:
        """
        Provides operations to call the downloadAppDiagnostics method.
        """
        return microsoft_graph_download_app_diagnostics_request_builder.MicrosoftGraphDownloadAppDiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_execute_action(self) -> microsoft_graph_execute_action_request_builder.MicrosoftGraphExecuteActionRequestBuilder:
        """
        Provides operations to call the executeAction method.
        """
        return microsoft_graph_execute_action_request_builder.MicrosoftGraphExecuteActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_move_devices_to_o_u(self) -> microsoft_graph_move_devices_to_o_u_request_builder.MicrosoftGraphMoveDevicesToOURequestBuilder:
        """
        Provides operations to call the moveDevicesToOU method.
        """
        return microsoft_graph_move_devices_to_o_u_request_builder.MicrosoftGraphMoveDevicesToOURequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedDevicesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/managedDevices{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[ManagedDevicesRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device_collection_response.ManagedDeviceCollectionResponse]:
        """
        The managed devices associated with the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device_collection_response.ManagedDeviceCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device_collection_response.ManagedDeviceCollectionResponse, error_mapping)
    
    def microsoft_graph_app_diagnostics_with_upn(self,upn: Optional[str] = None) -> microsoft_graph_app_diagnostics_with_upn_request_builder.MicrosoftGraphAppDiagnosticsWithUpnRequestBuilder:
        """
        Provides operations to call the appDiagnostics method.
        Args:
            upn: Usage: upn='{upn}'
        Returns: microsoft_graph_app_diagnostics_with_upn_request_builder.MicrosoftGraphAppDiagnosticsWithUpnRequestBuilder
        """
        if upn is None:
            raise Exception("upn cannot be undefined")
        return microsoft_graph_app_diagnostics_with_upn_request_builder.MicrosoftGraphAppDiagnosticsWithUpnRequestBuilder(self.request_adapter, self.path_parameters, upn)
    
    async def post(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDevicesRequestBuilderPostRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Create new navigation property to managedDevices for users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDevicesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The managed devices associated with the user.
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
    
    def to_post_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDevicesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to managedDevices for users
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class ManagedDevicesRequestBuilderGetQueryParameters():
        """
        The managed devices associated with the user.
        """
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

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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
        
    
    @dataclass
    class ManagedDevicesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedDevicesRequestBuilder.ManagedDevicesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedDevicesRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

