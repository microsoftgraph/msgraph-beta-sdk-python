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

categories_request_builder = lazy_import('msgraph.generated.device_management.templates.item.categories.categories_request_builder')
device_management_template_setting_category_item_request_builder = lazy_import('msgraph.generated.device_management.templates.item.categories.item.device_management_template_setting_category_item_request_builder')
compare_with_template_id_request_builder = lazy_import('msgraph.generated.device_management.templates.item.compare_with_template_id.compare_with_template_id_request_builder')
create_instance_request_builder = lazy_import('msgraph.generated.device_management.templates.item.create_instance.create_instance_request_builder')
migratable_to_request_builder = lazy_import('msgraph.generated.device_management.templates.item.migratable_to.migratable_to_request_builder')
device_management_template_item_request_builder = lazy_import('msgraph.generated.device_management.templates.item.migratable_to.item.device_management_template_item_request_builder')
settings_request_builder = lazy_import('msgraph.generated.device_management.templates.item.settings.settings_request_builder')
device_management_setting_instance_item_request_builder = lazy_import('msgraph.generated.device_management.templates.item.settings.item.device_management_setting_instance_item_request_builder')
device_management_template = lazy_import('msgraph.generated.models.device_management_template')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceManagementTemplateItemRequestBuilder():
    """
    Provides operations to manage the templates property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementTemplate entity.
        """
        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_instance(self) -> create_instance_request_builder.CreateInstanceRequestBuilder:
        """
        Provides operations to call the createInstance method.
        """
        return create_instance_request_builder.CreateInstanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migratable_to(self) -> migratable_to_request_builder.MigratableToRequestBuilder:
        """
        Provides operations to manage the migratableTo property of the microsoft.graph.deviceManagementTemplate entity.
        """
        return migratable_to_request_builder.MigratableToRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementTemplate entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def categories_by_id(self,id: str) -> device_management_template_setting_category_item_request_builder.DeviceManagementTemplateSettingCategoryItemRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementTemplate entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_template_setting_category_item_request_builder.DeviceManagementTemplateSettingCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTemplateSettingCategory%2Did"] = id
        return device_management_template_setting_category_item_request_builder.DeviceManagementTemplateSettingCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def compare_with_template_id(self,template_id: Optional[str] = None) -> compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder:
        """
        Provides operations to call the compare method.
        Args:
            templateId: Usage: templateId='{templateId}'
        Returns: compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder
        """
        if template_id is None:
            raise Exception("template_id cannot be undefined")
        return compare_with_template_id_request_builder.CompareWithTemplateIdRequestBuilder(self.request_adapter, self.path_parameters, templateId)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementTemplateItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property templates for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The available templates
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
    
    def create_patch_request_information(self,body: Optional[device_management_template.DeviceManagementTemplate] = None, request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property templates in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property templates for deviceManagement
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
    
    async def get(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_template.DeviceManagementTemplate]:
        """
        The available templates
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_template.DeviceManagementTemplate]
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
        return await self.request_adapter.send_async(request_info, device_management_template.DeviceManagementTemplate, response_handler, error_mapping)
    
    def migratable_to_by_id(self,id: str) -> DeviceManagementTemplateItemRequestBuilder:
        """
        Provides operations to manage the migratableTo property of the microsoft.graph.deviceManagementTemplate entity.
        Args:
            id: Unique identifier of the item
        Returns: DeviceManagementTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTemplate%2Did1"] = id
        return DeviceManagementTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device_management_template.DeviceManagementTemplate] = None, request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_template.DeviceManagementTemplate]:
        """
        Update the navigation property templates in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_template.DeviceManagementTemplate]
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
        return await self.request_adapter.send_async(request_info, device_management_template.DeviceManagementTemplate, response_handler, error_mapping)
    
    def settings_by_id(self,id: str) -> device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementTemplate entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementSettingInstance%2Did"] = id
        return device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceManagementTemplateItemRequestBuilderGetQueryParameters():
        """
        The available templates
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
    class DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementTemplateItemRequestBuilder.DeviceManagementTemplateItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

