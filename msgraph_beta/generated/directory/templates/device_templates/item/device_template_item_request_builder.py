from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.device_template import DeviceTemplate
    from .....models.o_data_errors.o_data_error import ODataError
    from .create_device_from_template.create_device_from_template_request_builder import CreateDeviceFromTemplateRequestBuilder
    from .device_instances.device_instances_request_builder import DeviceInstancesRequestBuilder
    from .device_instances_with_device_id.device_instances_with_device_id_request_builder import DeviceInstancesWithDeviceIdRequestBuilder
    from .owners.owners_request_builder import OwnersRequestBuilder

class DeviceTemplateItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceTemplates property of the microsoft.graph.template entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceTemplateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/templates/deviceTemplates/{deviceTemplate%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a registered deviceTemplate. You must first delete all devices linked to the template before deleting the template itself. Only registered owners of the template can perform this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/devicetemplate-delete?view=graph-rest-beta
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def device_instances_with_device_id(self,device_id: str) -> DeviceInstancesWithDeviceIdRequestBuilder:
        """
        Provides operations to manage the deviceInstances property of the microsoft.graph.deviceTemplate entity.
        param device_id: Alternate key of device
        Returns: DeviceInstancesWithDeviceIdRequestBuilder
        """
        if device_id is None:
            raise TypeError("device_id cannot be null.")
        from .device_instances_with_device_id.device_instances_with_device_id_request_builder import DeviceInstancesWithDeviceIdRequestBuilder

        return DeviceInstancesWithDeviceIdRequestBuilder(self.request_adapter, self.path_parameters, device_id)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceTemplateItemRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceTemplate]:
        """
        Get the properties and relationships of a deviceTemplate object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceTemplate]
        Find more info here: https://learn.microsoft.com/graph/api/devicetemplate-get?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.device_template import DeviceTemplate

        return await self.request_adapter.send_async(request_info, DeviceTemplate, error_mapping)
    
    async def patch(self,body: DeviceTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceTemplate]:
        """
        Update the navigation property deviceTemplates in directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceTemplate]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.device_template import DeviceTemplate

        return await self.request_adapter.send_async(request_info, DeviceTemplate, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a registered deviceTemplate. You must first delete all devices linked to the template before deleting the template itself. Only registered owners of the template can perform this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceTemplateItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the properties and relationships of a deviceTemplate object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property deviceTemplates in directory
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
    
    def with_url(self,raw_url: str) -> DeviceTemplateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceTemplateItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceTemplateItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def create_device_from_template(self) -> CreateDeviceFromTemplateRequestBuilder:
        """
        Provides operations to call the createDeviceFromTemplate method.
        """
        from .create_device_from_template.create_device_from_template_request_builder import CreateDeviceFromTemplateRequestBuilder

        return CreateDeviceFromTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_instances(self) -> DeviceInstancesRequestBuilder:
        """
        Provides operations to manage the deviceInstances property of the microsoft.graph.deviceTemplate entity.
        """
        from .device_instances.device_instances_request_builder import DeviceInstancesRequestBuilder

        return DeviceInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.deviceTemplate entity.
        """
        from .owners.owners_request_builder import OwnersRequestBuilder

        return OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceTemplateItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceTemplateItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a deviceTemplate object.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class DeviceTemplateItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceTemplateItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceTemplateItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

