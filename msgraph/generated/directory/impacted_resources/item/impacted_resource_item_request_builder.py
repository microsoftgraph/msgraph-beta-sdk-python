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
    from ....models import impacted_resource
    from ....models.o_data_errors import o_data_error
    from .complete import complete_request_builder
    from .dismiss import dismiss_request_builder
    from .postpone import postpone_request_builder
    from .reactivate import reactivate_request_builder

class ImpactedResourceItemRequestBuilder():
    """
    Provides operations to manage the impactedResources property of the microsoft.graph.directory entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ImpactedResourceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directory/impactedResources/{impactedResource%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ImpactedResourceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property impactedResources for directory
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
    
    async def get(self,request_configuration: Optional[ImpactedResourceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[impacted_resource.ImpactedResource]:
        """
        Get impactedResources from directory
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[impacted_resource.ImpactedResource]
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
        from ....models import impacted_resource

        return await self.request_adapter.send_async(request_info, impacted_resource.ImpactedResource, error_mapping)
    
    async def patch(self,body: Optional[impacted_resource.ImpactedResource] = None, request_configuration: Optional[ImpactedResourceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[impacted_resource.ImpactedResource]:
        """
        Update the navigation property impactedResources in directory
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[impacted_resource.ImpactedResource]
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
        from ....models import impacted_resource

        return await self.request_adapter.send_async(request_info, impacted_resource.ImpactedResource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ImpactedResourceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property impactedResources for directory
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
    
    def to_get_request_information(self,request_configuration: Optional[ImpactedResourceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get impactedResources from directory
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
    
    def to_patch_request_information(self,body: Optional[impacted_resource.ImpactedResource] = None, request_configuration: Optional[ImpactedResourceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property impactedResources in directory
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
    def complete(self) -> complete_request_builder.CompleteRequestBuilder:
        """
        Provides operations to call the complete method.
        """
        from .complete import complete_request_builder

        return complete_request_builder.CompleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss(self) -> dismiss_request_builder.DismissRequestBuilder:
        """
        Provides operations to call the dismiss method.
        """
        from .dismiss import dismiss_request_builder

        return dismiss_request_builder.DismissRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def postpone(self) -> postpone_request_builder.PostponeRequestBuilder:
        """
        Provides operations to call the postpone method.
        """
        from .postpone import postpone_request_builder

        return postpone_request_builder.PostponeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reactivate(self) -> reactivate_request_builder.ReactivateRequestBuilder:
        """
        Provides operations to call the reactivate method.
        """
        from .reactivate import reactivate_request_builder

        return reactivate_request_builder.ReactivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ImpactedResourceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ImpactedResourceItemRequestBuilderGetQueryParameters():
        """
        Get impactedResources from directory
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
    class ImpactedResourceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ImpactedResourceItemRequestBuilder.ImpactedResourceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ImpactedResourceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

