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
    from ....models import device_management_intent
    from ....models.o_data_errors import o_data_error
    from .assign import assign_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import device_management_intent_assignment_item_request_builder
    from .categories import categories_request_builder
    from .categories.item import device_management_intent_setting_category_item_request_builder
    from .compare_with_template_id import compare_with_template_id_request_builder
    from .create_copy import create_copy_request_builder
    from .device_setting_state_summaries import device_setting_state_summaries_request_builder
    from .device_setting_state_summaries.item import device_management_intent_device_setting_state_summary_item_request_builder
    from .device_states import device_states_request_builder
    from .device_states.item import device_management_intent_device_state_item_request_builder
    from .device_state_summary import device_state_summary_request_builder
    from .get_customized_settings import get_customized_settings_request_builder
    from .migrate_to_template import migrate_to_template_request_builder
    from .settings import settings_request_builder
    from .settings.item import device_management_setting_instance_item_request_builder
    from .update_settings import update_settings_request_builder
    from .user_states import user_states_request_builder
    from .user_states.item import device_management_intent_user_state_item_request_builder
    from .user_state_summary import user_state_summary_request_builder

class DeviceManagementIntentItemRequestBuilder():
    """
    Provides operations to manage the intents property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementIntentItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignments_by_id(self,id: str) -> device_management_intent_assignment_item_request_builder.DeviceManagementIntentAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_assignment_item_request_builder.DeviceManagementIntentAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import device_management_intent_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntentAssignment%2Did"] = id
        return device_management_intent_assignment_item_request_builder.DeviceManagementIntentAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def categories_by_id(self,id: str) -> device_management_intent_setting_category_item_request_builder.DeviceManagementIntentSettingCategoryItemRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_setting_category_item_request_builder.DeviceManagementIntentSettingCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .categories.item import device_management_intent_setting_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntentSettingCategory%2Did"] = id
        return device_management_intent_setting_category_item_request_builder.DeviceManagementIntentSettingCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compare_with_template_id(self,template_id: Optional[str] = None) -> compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder:
        """
        Provides operations to call the compare method.
        Args:
            templateId: Usage: templateId='{templateId}'
        Returns: compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder
        """
        if template_id is None:
            raise Exception("template_id cannot be undefined")
        from .compare_with_template_id import compare_with_template_id_request_builder

        return compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder(self.request_adapter, self.path_parameters, template_id)
    
    async def delete(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property intents for deviceManagement
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
    
    def device_setting_state_summaries_by_id(self,id: str) -> device_management_intent_device_setting_state_summary_item_request_builder.DeviceManagementIntentDeviceSettingStateSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_device_setting_state_summary_item_request_builder.DeviceManagementIntentDeviceSettingStateSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_setting_state_summaries.item import device_management_intent_device_setting_state_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntentDeviceSettingStateSummary%2Did"] = id
        return device_management_intent_device_setting_state_summary_item_request_builder.DeviceManagementIntentDeviceSettingStateSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_states_by_id(self,id: str) -> device_management_intent_device_state_item_request_builder.DeviceManagementIntentDeviceStateItemRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_device_state_item_request_builder.DeviceManagementIntentDeviceStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_states.item import device_management_intent_device_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntentDeviceState%2Did"] = id
        return device_management_intent_device_state_item_request_builder.DeviceManagementIntentDeviceStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_intent.DeviceManagementIntent]:
        """
        The device management intents
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_intent.DeviceManagementIntent]
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
        from ....models import device_management_intent

        return await self.request_adapter.send_async(request_info, device_management_intent.DeviceManagementIntent, error_mapping)
    
    async def patch(self,body: Optional[device_management_intent.DeviceManagementIntent] = None, request_configuration: Optional[DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_intent.DeviceManagementIntent]:
        """
        Update the navigation property intents in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_intent.DeviceManagementIntent]
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
        from ....models import device_management_intent

        return await self.request_adapter.send_async(request_info, device_management_intent.DeviceManagementIntent, error_mapping)
    
    def settings_by_id(self,id: str) -> device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .settings.item import device_management_setting_instance_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementSettingInstance%2Did"] = id
        return device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property intents for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementIntentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The device management intents
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
    
    def to_patch_request_information(self,body: Optional[device_management_intent.DeviceManagementIntent] = None, request_configuration: Optional[DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property intents in deviceManagement
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
    
    def user_states_by_id(self,id: str) -> device_management_intent_user_state_item_request_builder.DeviceManagementIntentUserStateItemRequestBuilder:
        """
        Provides operations to manage the userStates property of the microsoft.graph.deviceManagementIntent entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_intent_user_state_item_request_builder.DeviceManagementIntentUserStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_states.item import device_management_intent_user_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementIntentUserState%2Did"] = id
        return device_management_intent_user_state_item_request_builder.DeviceManagementIntentUserStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .categories import categories_request_builder

        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_copy(self) -> create_copy_request_builder.CreateCopyRequestBuilder:
        """
        Provides operations to call the createCopy method.
        """
        from .create_copy import create_copy_request_builder

        return create_copy_request_builder.CreateCopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_setting_state_summaries(self) -> device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_setting_state_summaries import device_setting_state_summaries_request_builder

        return device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_states(self) -> device_states_request_builder.DeviceStatesRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_states import device_states_request_builder

        return device_states_request_builder.DeviceStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_state_summary(self) -> device_state_summary_request_builder.DeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceStateSummary property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .device_state_summary import device_state_summary_request_builder

        return device_state_summary_request_builder.DeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_customized_settings(self) -> get_customized_settings_request_builder.GetCustomizedSettingsRequestBuilder:
        """
        Provides operations to call the getCustomizedSettings method.
        """
        from .get_customized_settings import get_customized_settings_request_builder

        return get_customized_settings_request_builder.GetCustomizedSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migrate_to_template(self) -> migrate_to_template_request_builder.MigrateToTemplateRequestBuilder:
        """
        Provides operations to call the migrateToTemplate method.
        """
        from .migrate_to_template import migrate_to_template_request_builder

        return migrate_to_template_request_builder.MigrateToTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_settings(self) -> update_settings_request_builder.UpdateSettingsRequestBuilder:
        """
        Provides operations to call the updateSettings method.
        """
        from .update_settings import update_settings_request_builder

        return update_settings_request_builder.UpdateSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_states(self) -> user_states_request_builder.UserStatesRequestBuilder:
        """
        Provides operations to manage the userStates property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .user_states import user_states_request_builder

        return user_states_request_builder.UserStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_state_summary(self) -> user_state_summary_request_builder.UserStateSummaryRequestBuilder:
        """
        Provides operations to manage the userStateSummary property of the microsoft.graph.deviceManagementIntent entity.
        """
        from .user_state_summary import user_state_summary_request_builder

        return user_state_summary_request_builder.UserStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderGetQueryParameters():
        """
        The device management intents
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
    class DeviceManagementIntentItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementIntentItemRequestBuilder.DeviceManagementIntentItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementIntentItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

