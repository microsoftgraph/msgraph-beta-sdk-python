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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
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
    Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WindowsAutopilotDeviceIdentityItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsAutopilotDeviceIdentities/{windowsAutopilotDeviceIdentity%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property windowsAutopilotDeviceIdentities for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration] = None) -> Optional[WindowsAutopilotDeviceIdentity]:
        """
        The Windows autopilot device identities contained collection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsAutopilotDeviceIdentity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

        return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)
    
    async def patch(self,body: Optional[WindowsAutopilotDeviceIdentity] = None, request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[WindowsAutopilotDeviceIdentity]:
        """
        Update the navigation property windowsAutopilotDeviceIdentities in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WindowsAutopilotDeviceIdentity]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

        return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property windowsAutopilotDeviceIdentities for deviceManagement
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Windows autopilot device identities contained collection.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[WindowsAutopilotDeviceIdentity] = None, request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property windowsAutopilotDeviceIdentities in deviceManagement
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
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> WindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters():
        """
        The Windows autopilot device identities contained collection.
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
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilder.WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

