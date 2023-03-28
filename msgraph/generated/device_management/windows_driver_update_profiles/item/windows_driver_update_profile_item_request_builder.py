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
    from ....models import windows_driver_update_profile
    from ....models.o_data_errors import o_data_error
    from .assign import assign_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import windows_driver_update_profile_assignment_item_request_builder
    from .driver_inventories import driver_inventories_request_builder
    from .driver_inventories.item import windows_driver_update_inventory_item_request_builder
    from .execute_action import execute_action_request_builder
    from .sync_inventory import sync_inventory_request_builder

class WindowsDriverUpdateProfileItemRequestBuilder():
    """
    Provides operations to manage the windowsDriverUpdateProfiles property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WindowsDriverUpdateProfileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/windowsDriverUpdateProfiles/{windowsDriverUpdateProfile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignments_by_id(self,id: str) -> windows_driver_update_profile_assignment_item_request_builder.WindowsDriverUpdateProfileAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsDriverUpdateProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_driver_update_profile_assignment_item_request_builder.WindowsDriverUpdateProfileAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import windows_driver_update_profile_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDriverUpdateProfileAssignment%2Did"] = id
        return windows_driver_update_profile_assignment_item_request_builder.WindowsDriverUpdateProfileAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property windowsDriverUpdateProfiles for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def driver_inventories_by_id(self,id: str) -> windows_driver_update_inventory_item_request_builder.WindowsDriverUpdateInventoryItemRequestBuilder:
        """
        Provides operations to manage the driverInventories property of the microsoft.graph.windowsDriverUpdateProfile entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_driver_update_inventory_item_request_builder.WindowsDriverUpdateInventoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .driver_inventories.item import windows_driver_update_inventory_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDriverUpdateInventory%2Did"] = id
        return windows_driver_update_inventory_item_request_builder.WindowsDriverUpdateInventoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[windows_driver_update_profile.WindowsDriverUpdateProfile]:
        """
        A collection of windows driver update profiles
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_driver_update_profile.WindowsDriverUpdateProfile]
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
        from ....models import windows_driver_update_profile

        return await self.request_adapter.send_async(request_info, windows_driver_update_profile.WindowsDriverUpdateProfile, error_mapping)
    
    async def patch(self,body: Optional[windows_driver_update_profile.WindowsDriverUpdateProfile] = None, request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[windows_driver_update_profile.WindowsDriverUpdateProfile]:
        """
        Update the navigation property windowsDriverUpdateProfiles in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_driver_update_profile.WindowsDriverUpdateProfile]
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
        from ....models import windows_driver_update_profile

        return await self.request_adapter.send_async(request_info, windows_driver_update_profile.WindowsDriverUpdateProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property windowsDriverUpdateProfiles for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of windows driver update profiles
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
    
    def to_patch_request_information(self,body: Optional[windows_driver_update_profile.WindowsDriverUpdateProfile] = None, request_configuration: Optional[WindowsDriverUpdateProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property windowsDriverUpdateProfiles in deviceManagement
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
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign import assign_request_builder

        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsDriverUpdateProfile entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def driver_inventories(self) -> driver_inventories_request_builder.DriverInventoriesRequestBuilder:
        """
        Provides operations to manage the driverInventories property of the microsoft.graph.windowsDriverUpdateProfile entity.
        """
        from .driver_inventories import driver_inventories_request_builder

        return driver_inventories_request_builder.DriverInventoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def execute_action(self) -> execute_action_request_builder.ExecuteActionRequestBuilder:
        """
        Provides operations to call the executeAction method.
        """
        from .execute_action import execute_action_request_builder

        return execute_action_request_builder.ExecuteActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_inventory(self) -> sync_inventory_request_builder.SyncInventoryRequestBuilder:
        """
        Provides operations to call the syncInventory method.
        """
        from .sync_inventory import sync_inventory_request_builder

        return sync_inventory_request_builder.SyncInventoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WindowsDriverUpdateProfileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WindowsDriverUpdateProfileItemRequestBuilderGetQueryParameters():
        """
        A collection of windows driver update profiles
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
    class WindowsDriverUpdateProfileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WindowsDriverUpdateProfileItemRequestBuilder.WindowsDriverUpdateProfileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WindowsDriverUpdateProfileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

