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
    from ....models import managed_device_mobile_app_configuration
    from ....models.o_data_errors import o_data_error
    from .assign import assign_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import managed_device_mobile_app_configuration_assignment_item_request_builder
    from .device_statuses import device_statuses_request_builder
    from .device_statuses.item import managed_device_mobile_app_configuration_device_status_item_request_builder
    from .device_status_summary import device_status_summary_request_builder
    from .user_statuses import user_statuses_request_builder
    from .user_statuses.item import managed_device_mobile_app_configuration_user_status_item_request_builder
    from .user_status_summary import user_status_summary_request_builder

class ManagedDeviceMobileAppConfigurationItemRequestBuilder():
    """
    Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedDeviceMobileAppConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/mobileAppConfigurations/{managedDeviceMobileAppConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignments_by_id(self,id: str) -> managed_device_mobile_app_configuration_assignment_item_request_builder.ManagedDeviceMobileAppConfigurationAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_mobile_app_configuration_assignment_item_request_builder.ManagedDeviceMobileAppConfigurationAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import managed_device_mobile_app_configuration_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceMobileAppConfigurationAssignment%2Did"] = id
        return managed_device_mobile_app_configuration_assignment_item_request_builder.ManagedDeviceMobileAppConfigurationAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property mobileAppConfigurations for deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def device_statuses_by_id(self,id: str) -> managed_device_mobile_app_configuration_device_status_item_request_builder.ManagedDeviceMobileAppConfigurationDeviceStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_mobile_app_configuration_device_status_item_request_builder.ManagedDeviceMobileAppConfigurationDeviceStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_statuses.item import managed_device_mobile_app_configuration_device_status_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceMobileAppConfigurationDeviceStatus%2Did"] = id
        return managed_device_mobile_app_configuration_device_status_item_request_builder.ManagedDeviceMobileAppConfigurationDeviceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]:
        """
        The Managed Device Mobile Application Configurations.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_device_mobile_app_configuration

        return await self.request_adapter.send_async(request_info, managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration, error_mapping)
    
    async def patch(self,body: Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration] = None, request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]:
        """
        Update the navigation property mobileAppConfigurations in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_device_mobile_app_configuration

        return await self.request_adapter.send_async(request_info, managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property mobileAppConfigurations for deviceAppManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Managed Device Mobile Application Configurations.
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
    
    def to_patch_request_information(self,body: Optional[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration] = None, request_configuration: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property mobileAppConfigurations in deviceAppManagement
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
    
    def user_statuses_by_id(self,id: str) -> managed_device_mobile_app_configuration_user_status_item_request_builder.ManagedDeviceMobileAppConfigurationUserStatusItemRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_mobile_app_configuration_user_status_item_request_builder.ManagedDeviceMobileAppConfigurationUserStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_statuses.item import managed_device_mobile_app_configuration_user_status_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceMobileAppConfigurationUserStatus%2Did"] = id
        return managed_device_mobile_app_configuration_user_status_item_request_builder.ManagedDeviceMobileAppConfigurationUserStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign import assign_request_builder

        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> device_statuses_request_builder.DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .device_statuses import device_statuses_request_builder

        return device_statuses_request_builder.DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_status_summary(self) -> device_status_summary_request_builder.DeviceStatusSummaryRequestBuilder:
        """
        Provides operations to manage the deviceStatusSummary property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .device_status_summary import device_status_summary_request_builder

        return device_status_summary_request_builder.DeviceStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> user_statuses_request_builder.UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .user_statuses import user_statuses_request_builder

        return user_statuses_request_builder.UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_status_summary(self) -> user_status_summary_request_builder.UserStatusSummaryRequestBuilder:
        """
        Provides operations to manage the userStatusSummary property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .user_status_summary import user_status_summary_request_builder

        return user_status_summary_request_builder.UserStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters():
        """
        The Managed Device Mobile Application Configurations.
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
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedDeviceMobileAppConfigurationItemRequestBuilder.ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

