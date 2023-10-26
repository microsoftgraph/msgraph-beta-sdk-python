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
    from ......models.device_management_template import DeviceManagementTemplate
    from ......models.o_data_errors.o_data_error import ODataError
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .compare_with_template_id.compare_with_template_id_request_builder import CompareWithTemplateIdRequestBuilder
    from .create_instance.create_instance_request_builder import CreateInstanceRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class DeviceManagementTemplateItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the migratableTo property of the microsoft.graph.deviceManagementTemplate entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementTemplateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}/migratableTo/{deviceManagementTemplate%2Did1}{?%24select,%24expand}", path_parameters)
    
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
    
    async def delete(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property migratableTo for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceManagementTemplate]:
        """
        Collection of templates this template can migrate to
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementTemplate]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.device_management_template import DeviceManagementTemplate

        return await self.request_adapter.send_async(request_info, DeviceManagementTemplate, error_mapping)
    
    async def patch(self,body: Optional[DeviceManagementTemplate] = None, request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DeviceManagementTemplate]:
        """
        Update the navigation property migratableTo in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementTemplate]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.device_management_template import DeviceManagementTemplate

        return await self.request_adapter.send_async(request_info, DeviceManagementTemplate, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property migratableTo for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Collection of templates this template can migrate to
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
    
    def to_patch_request_information(self,body: Optional[DeviceManagementTemplate] = None, request_configuration: Optional[DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property migratableTo in deviceManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DeviceManagementTemplateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceManagementTemplateItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DeviceManagementTemplateItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.deviceManagementTemplate entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_instance(self) -> CreateInstanceRequestBuilder:
        """
        Provides operations to call the createInstance method.
        """
        from .create_instance.create_instance_request_builder import CreateInstanceRequestBuilder

        return CreateInstanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.deviceManagementTemplate entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementTemplateItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DeviceManagementTemplateItemRequestBuilderGetQueryParameters():
        """
        Collection of templates this template can migrate to
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
    class DeviceManagementTemplateItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeviceManagementTemplateItemRequestBuilder.DeviceManagementTemplateItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementTemplateItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

