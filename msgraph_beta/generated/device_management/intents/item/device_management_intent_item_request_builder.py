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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementIntentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}{?%24select,%24expand}", path_parameters)
    
    def compare_with_template_id(self,template_id: Optional[str] = None) -> CompareWithTemplateIdRequestBuilder:
        """
        Provides operations to call the compare method.
        param template_id: Usage: templateId='{templateId}'
        Returns: CompareWithTemplateIdRequestBuilder
        """
        if not template_id:
            raise TypeError("template_id cannot be null.")
        from .compare_with_template_id.compare_with_template_id_request_builder import CompareWithTemplateIdRequestBuilder

        return CompareWithTemplateIdRequestBuilder(self.request_adapter, self.path_parameters, template_id)
    
    async def delete(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property intents for deviceManagement
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
    
    async def get(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceManagementIntent]:
        """
        The device management intents
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementIntent]
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
        from ....models.device_management_intent import DeviceManagementIntent

        return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)
    
    async def patch(self,body: Optional[DeviceManagementIntent] = None, request_configuration: Optional[DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DeviceManagementIntent]:
        """
        Update the navigation property intents in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementIntent]
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
        from ....models.device_management_intent import DeviceManagementIntent

        return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property intents for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The device management intents
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
    
    def to_patch_request_information(self,body: Optional[DeviceManagementIntent] = None, request_configuration: Optional[DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property intents in deviceManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DeviceManagementIntentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceManagementIntentItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderGetQueryParameters():
        """
        The device management intents
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
    class DeviceManagementIntentItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeviceManagementIntentItemRequestBuilder.DeviceManagementIntentItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

