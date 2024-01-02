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
    from ......models.education_module import EducationModule
    from ......models.o_data_errors.o_data_error import ODataError
    from .pin.pin_request_builder import PinRequestBuilder
    from .publish.publish_request_builder import PublishRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .set_up_resources_folder.set_up_resources_folder_request_builder import SetUpResourcesFolderRequestBuilder
    from .unpin.unpin_request_builder import UnpinRequestBuilder

class EducationModuleItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the modules property of the microsoft.graph.educationClass entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationModuleItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/modules/{educationModule%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EducationModuleItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an existing module in a class. Only teachers within a class can delete modules.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationmodule-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[EducationModuleItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EducationModule]:
        """
        Get the properties and relationships of a module. Only teachers, students, and applications with application permissions can perform this operation. Students can only see published modules; teachers and applications with application permissions can see all modules in a class.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationModule]
        Find more info here: https://learn.microsoft.com/graph/api/educationmodule-get?view=graph-rest-1.0
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
        from ......models.education_module import EducationModule

        return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)
    
    async def patch(self,body: Optional[EducationModule] = None, request_configuration: Optional[EducationModuleItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EducationModule]:
        """
        Update an educationModule object in a class. Only teachers in the class can perform this operation. Note that you can't use a PATCH request to change the status of a module. Use the publish action to change the module status.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationModule]
        Find more info here: https://learn.microsoft.com/graph/api/educationmodule-update?view=graph-rest-1.0
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
        from ......models.education_module import EducationModule

        return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EducationModuleItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an existing module in a class. Only teachers within a class can delete modules.
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
    
    def to_get_request_information(self,request_configuration: Optional[EducationModuleItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a module. Only teachers, students, and applications with application permissions can perform this operation. Students can only see published modules; teachers and applications with application permissions can see all modules in a class.
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
    
    def to_patch_request_information(self,body: Optional[EducationModule] = None, request_configuration: Optional[EducationModuleItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update an educationModule object in a class. Only teachers in the class can perform this operation. Note that you can't use a PATCH request to change the status of a module. Use the publish action to change the module status.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> EducationModuleItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationModuleItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EducationModuleItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def pin(self) -> PinRequestBuilder:
        """
        Provides operations to call the pin method.
        """
        from .pin.pin_request_builder import PinRequestBuilder

        return PinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        from .publish.publish_request_builder import PublishRequestBuilder

        return PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationModule entity.
        """
        from .resources.resources_request_builder import ResourcesRequestBuilder

        return ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_up_resources_folder(self) -> SetUpResourcesFolderRequestBuilder:
        """
        Provides operations to call the setUpResourcesFolder method.
        """
        from .set_up_resources_folder.set_up_resources_folder_request_builder import SetUpResourcesFolderRequestBuilder

        return SetUpResourcesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpin(self) -> UnpinRequestBuilder:
        """
        Provides operations to call the unpin method.
        """
        from .unpin.unpin_request_builder import UnpinRequestBuilder

        return UnpinRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationModuleItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EducationModuleItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a module. Only teachers, students, and applications with application permissions can perform this operation. Students can only see published modules; teachers and applications with application permissions can see all modules in a class.
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
    class EducationModuleItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EducationModuleItemRequestBuilder.EducationModuleItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationModuleItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

