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
    from ...models import managed_device, managed_device_collection_response
    from ...models.o_data_errors import o_data_error
    from .app_diagnostics_with_upn import app_diagnostics_with_upn_request_builder
    from .bulk_reprovision_cloud_pc import bulk_reprovision_cloud_pc_request_builder
    from .bulk_restore_cloud_pc import bulk_restore_cloud_pc_request_builder
    from .bulk_set_cloud_pc_review_status import bulk_set_cloud_pc_review_status_request_builder
    from .count import count_request_builder
    from .download_app_diagnostics import download_app_diagnostics_request_builder
    from .execute_action import execute_action_request_builder
    from .item import managed_device_item_request_builder
    from .move_devices_to_o_u import move_devices_to_o_u_request_builder

class ComanagedDevicesRequestBuilder():
    """
    Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ComanagedDevicesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/comanagedDevices{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def app_diagnostics_with_upn(self,upn: Optional[str] = None) -> app_diagnostics_with_upn_request_builder.AppDiagnosticsWithUpnRequestBuilder:
        """
        Provides operations to call the appDiagnostics method.
        Args:
            upn: Usage: upn='{upn}'
        Returns: app_diagnostics_with_upn_request_builder.AppDiagnosticsWithUpnRequestBuilder
        """
        if upn is None:
            raise Exception("upn cannot be undefined")
        from .app_diagnostics_with_upn import app_diagnostics_with_upn_request_builder

        return app_diagnostics_with_upn_request_builder.AppDiagnosticsWithUpnRequestBuilder(self.request_adapter, self.path_parameters, upn)
    
    def by_managed_device_id(self,managed_device_id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the comanagedDevices property of the microsoft.graph.deviceManagement entity.
        Args:
            managed_device_id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if managed_device_id is None:
            raise Exception("managed_device_id cannot be undefined")
        from .item import managed_device_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = managed_device_id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ComanagedDevicesRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device_collection_response.ManagedDeviceCollectionResponse]:
        """
        The list of co-managed devices report
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device_collection_response.ManagedDeviceCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import managed_device_collection_response

        return await self.request_adapter.send_async(request_info, managed_device_collection_response.ManagedDeviceCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ComanagedDevicesRequestBuilderPostRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Create new navigation property to comanagedDevices for deviceManagement
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
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import managed_device

        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ComanagedDevicesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of co-managed devices report
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
    
    def to_post_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ComanagedDevicesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to comanagedDevices for deviceManagement
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def bulk_reprovision_cloud_pc(self) -> bulk_reprovision_cloud_pc_request_builder.BulkReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the bulkReprovisionCloudPc method.
        """
        from .bulk_reprovision_cloud_pc import bulk_reprovision_cloud_pc_request_builder

        return bulk_reprovision_cloud_pc_request_builder.BulkReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bulk_restore_cloud_pc(self) -> bulk_restore_cloud_pc_request_builder.BulkRestoreCloudPcRequestBuilder:
        """
        Provides operations to call the bulkRestoreCloudPc method.
        """
        from .bulk_restore_cloud_pc import bulk_restore_cloud_pc_request_builder

        return bulk_restore_cloud_pc_request_builder.BulkRestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bulk_set_cloud_pc_review_status(self) -> bulk_set_cloud_pc_review_status_request_builder.BulkSetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the bulkSetCloudPcReviewStatus method.
        """
        from .bulk_set_cloud_pc_review_status import bulk_set_cloud_pc_review_status_request_builder

        return bulk_set_cloud_pc_review_status_request_builder.BulkSetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def download_app_diagnostics(self) -> download_app_diagnostics_request_builder.DownloadAppDiagnosticsRequestBuilder:
        """
        Provides operations to call the downloadAppDiagnostics method.
        """
        from .download_app_diagnostics import download_app_diagnostics_request_builder

        return download_app_diagnostics_request_builder.DownloadAppDiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def execute_action(self) -> execute_action_request_builder.ExecuteActionRequestBuilder:
        """
        Provides operations to call the executeAction method.
        """
        from .execute_action import execute_action_request_builder

        return execute_action_request_builder.ExecuteActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move_devices_to_o_u(self) -> move_devices_to_o_u_request_builder.MoveDevicesToOURequestBuilder:
        """
        Provides operations to call the moveDevicesToOU method.
        """
        from .move_devices_to_o_u import move_devices_to_o_u_request_builder

        return move_devices_to_o_u_request_builder.MoveDevicesToOURequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ComanagedDevicesRequestBuilderGetQueryParameters():
        """
        The list of co-managed devices report
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
    class ComanagedDevicesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ComanagedDevicesRequestBuilder.ComanagedDevicesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ComanagedDevicesRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

