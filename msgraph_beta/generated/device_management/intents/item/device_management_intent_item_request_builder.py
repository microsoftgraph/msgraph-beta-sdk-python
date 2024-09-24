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
    from ....models.device_management_intent import DeviceManagementIntent
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign.assign_request_builder import AssignRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .compare_with_template_id.compare_with_template_id_request_builder import CompareWithTemplateIdRequestBuilder
    from .create_copy.create_copy_request_builder import CreateCopyRequestBuilder
    from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder
    from .device_states.device_states_request_builder import DeviceStatesRequestBuilder
    from .device_state_summary.device_state_summary_request_builder import DeviceStateSummaryRequestBuilder
    from .get_customized_settings.get_customized_settings_request_builder import GetCustomizedSettingsRequestBuilder
    from .migrate_to_template.migrate_to_template_request_builder import MigrateToTemplateRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .update_settings.update_settings_request_builder import UpdateSettingsRequestBuilder
    from .user_states.user_states_request_builder import UserStatesRequestBuilder
    from .user_state_summary.user_state_summary_request_builder import UserStateSummaryRequestBuilder

class DeviceManagementIntentItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the intents property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceManagementIntentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}{?%24expand,%24select}", path_parameters)
    
    def compare_with_template_id(self,template_id: str) -> CompareWithTemplateIdRequestBuilder:
        """
        Provides operations to call the compare method.
        param template_id: Usage: templateId='{templateId}'
        Returns: CompareWithTemplateIdRequestBuilder
        """
        if template_id is None:
            raise TypeError("template_id cannot be null.")
        from .compare_with_template_id.compare_with_template_id_request_builder import CompareWithTemplateIdRequestBuilder

        return CompareWithTemplateIdRequestBuilder(self.request_adapter, self.path_parameters, template_id)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property intents for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceManagementIntentItemRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceManagementIntent]:
        """
        The device management intents
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementIntent]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.device_management_intent import DeviceManagementIntent

        return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)
    
    async def patch(self,body: DeviceManagementIntent, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceManagementIntent]:
        """
        Update the navigation property intents in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementIntent]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.device_management_intent import DeviceManagementIntent

        return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property intents for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceManagementIntentItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The device management intents
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceManagementIntent, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property intents in deviceManagement
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
    
    def with_url(self,raw_url: str) -> DeviceManagementIntentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceManagementIntentItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceManagementIntentItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assign(self) -> AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign.assign_request_builder import AssignRequestBuilder

        return AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_copy(self) -> CreateCopyRequestBuilder:
        """
        Provides operations to call the createCopy method.
        """
        from .create_copy.create_copy_request_builder import CreateCopyRequestBuilder

        return CreateCopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_setting_state_summaries(self) -> DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder

        return DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_state_summary(self) -> DeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceStateSummary property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_state_summary.device_state_summary_request_builder import DeviceStateSummaryRequestBuilder

        return DeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_states(self) -> DeviceStatesRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_states.device_states_request_builder import DeviceStatesRequestBuilder

        return DeviceStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_customized_settings(self) -> GetCustomizedSettingsRequestBuilder:
        """
        Provides operations to call the getCustomizedSettings method.
        """
        from .get_customized_settings.get_customized_settings_request_builder import GetCustomizedSettingsRequestBuilder

        return GetCustomizedSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migrate_to_template(self) -> MigrateToTemplateRequestBuilder:
        """
        Provides operations to call the migrateToTemplate method.
        """
        from .migrate_to_template.migrate_to_template_request_builder import MigrateToTemplateRequestBuilder

        return MigrateToTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_settings(self) -> UpdateSettingsRequestBuilder:
        """
        Provides operations to call the updateSettings method.
        """
        from .update_settings.update_settings_request_builder import UpdateSettingsRequestBuilder

        return UpdateSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_state_summary(self) -> UserStateSummaryRequestBuilder:
        """
        Provides operations to manage the userStateSummary property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .user_state_summary.user_state_summary_request_builder import UserStateSummaryRequestBuilder

        return UserStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_states(self) -> UserStatesRequestBuilder:
        """
        Provides operations to manage the userStates property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .user_states.user_states_request_builder import UserStatesRequestBuilder

        return UserStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderGetQueryParameters():
        """
        The device management intents
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
    class DeviceManagementIntentItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceManagementIntentItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

