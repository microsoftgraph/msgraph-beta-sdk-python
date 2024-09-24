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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .allow_next_enrollment.allow_next_enrollment_request_builder import AllowNextEnrollmentRequestBuilder
    from .assign_resource_account_to_device.assign_resource_account_to_device_request_builder import AssignResourceAccountToDeviceRequestBuilder
    from .assign_user_to_device.assign_user_to_device_request_builder import AssignUserToDeviceRequestBuilder
    from .deployment_profile.deployment_profile_request_builder import DeploymentProfileRequestBuilder
    from .intended_deployment_profile.intended_deployment_profile_request_builder import IntendedDeploymentProfileRequestBuilder
    from .unassign_resource_account_from_device.unassign_resource_account_from_device_request_builder import UnassignResourceAccountFromDeviceRequestBuilder
    from .unassign_user_from_device.unassign_user_from_device_request_builder import UnassignUserFromDeviceRequestBuilder
    from .update_device_properties.update_device_properties_request_builder import UpdateDevicePropertiesRequestBuilder

class WindowsAutopilotDeviceIdentityItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignedDevices property of the microsoft.graph.windowsAutopilotDeploymentProfile entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WindowsAutopilotDeviceIdentityItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsAutopilotDeploymentProfiles/{windowsAutopilotDeploymentProfile%2Did}/assignedDevices/{windowsAutopilotDeviceIdentity%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property assignedDevices for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters]] = None) -> Optional[WindowsAutopilotDeviceIdentity]:
        """
        The list of assigned devices for the profile.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsAutopilotDeviceIdentity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

        return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)
    
    async def patch(self,body: WindowsAutopilotDeviceIdentity, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WindowsAutopilotDeviceIdentity]:
        """
        Update the navigation property assignedDevices in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsAutopilotDeviceIdentity]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

        return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property assignedDevices for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The list of assigned devices for the profile.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WindowsAutopilotDeviceIdentity, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property assignedDevices in deviceManagement
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
    
    def with_url(self,raw_url: str) -> WindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WindowsAutopilotDeviceIdentityItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def allow_next_enrollment(self) -> AllowNextEnrollmentRequestBuilder:
        """
        Provides operations to call the allowNextEnrollment method.
        """
        from .allow_next_enrollment.allow_next_enrollment_request_builder import AllowNextEnrollmentRequestBuilder

        return AllowNextEnrollmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_resource_account_to_device(self) -> AssignResourceAccountToDeviceRequestBuilder:
        """
        Provides operations to call the assignResourceAccountToDevice method.
        """
        from .assign_resource_account_to_device.assign_resource_account_to_device_request_builder import AssignResourceAccountToDeviceRequestBuilder

        return AssignResourceAccountToDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_user_to_device(self) -> AssignUserToDeviceRequestBuilder:
        """
        Provides operations to call the assignUserToDevice method.
        """
        from .assign_user_to_device.assign_user_to_device_request_builder import AssignUserToDeviceRequestBuilder

        return AssignUserToDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_profile(self) -> DeploymentProfileRequestBuilder:
        """
        Provides operations to manage the deploymentProfile property of the microsoft.graph.windowsAutopilotDeviceIdentity entity.
        """
        from .deployment_profile.deployment_profile_request_builder import DeploymentProfileRequestBuilder

        return DeploymentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intended_deployment_profile(self) -> IntendedDeploymentProfileRequestBuilder:
        """
        Provides operations to manage the intendedDeploymentProfile property of the microsoft.graph.windowsAutopilotDeviceIdentity entity.
        """
        from .intended_deployment_profile.intended_deployment_profile_request_builder import IntendedDeploymentProfileRequestBuilder

        return IntendedDeploymentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unassign_resource_account_from_device(self) -> UnassignResourceAccountFromDeviceRequestBuilder:
        """
        Provides operations to call the unassignResourceAccountFromDevice method.
        """
        from .unassign_resource_account_from_device.unassign_resource_account_from_device_request_builder import UnassignResourceAccountFromDeviceRequestBuilder

        return UnassignResourceAccountFromDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unassign_user_from_device(self) -> UnassignUserFromDeviceRequestBuilder:
        """
        Provides operations to call the unassignUserFromDevice method.
        """
        from .unassign_user_from_device.unassign_user_from_device_request_builder import UnassignUserFromDeviceRequestBuilder

        return UnassignUserFromDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_device_properties(self) -> UpdateDevicePropertiesRequestBuilder:
        """
        Provides operations to call the updateDeviceProperties method.
        """
        from .update_device_properties.update_device_properties_request_builder import UpdateDevicePropertiesRequestBuilder

        return UpdateDevicePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters():
        """
        The list of assigned devices for the profile.
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
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

