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

acquire_access_token_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.acquire_access_token.acquire_access_token_request_builder')
jobs_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.jobs_request_builder')
synchronization_job_item_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.synchronization_job_item_request_builder')
ping_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.ping.ping_request_builder')
templates_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.templates_request_builder')
synchronization_template_item_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.synchronization_template_item_request_builder')
synchronization = lazy_import('msgraph.generated.models.synchronization')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SynchronizationRequestBuilder():
    """
    Provides operations to manage the synchronization property of the microsoft.graph.application entity.
    """
    @property
    def acquire_access_token(self) -> acquire_access_token_request_builder.AcquireAccessTokenRequestBuilder:
        """
        Provides operations to call the acquireAccessToken method.
        """
        return acquire_access_token_request_builder.AcquireAccessTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> jobs_request_builder.JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
        """
        return jobs_request_builder.JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> templates_request_builder.TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.synchronization entity.
        """
        return templates_request_builder.TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SynchronizationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}/synchronization{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[SynchronizationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property synchronization for applications
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
    
    def create_get_request_information(self,request_configuration: Optional[SynchronizationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get synchronization from applications
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
    
    def create_patch_request_information(self,body: Optional[synchronization.Synchronization] = None, request_configuration: Optional[SynchronizationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property synchronization in applications
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
    
    async def delete(self,request_configuration: Optional[SynchronizationRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property synchronization for applications
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
    
    async def get(self,request_configuration: Optional[SynchronizationRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[synchronization.Synchronization]:
        """
        Get synchronization from applications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[synchronization.Synchronization]
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
        return await self.request_adapter.send_async(request_info, synchronization.Synchronization, response_handler, error_mapping)
    
    def jobs_by_id(self,id: str) -> synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
        Args:
            id: Unique identifier of the item
        Returns: synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["synchronizationJob%2Did"] = id
        return synchronization_job_item_request_builder.SynchronizationJobItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[synchronization.Synchronization] = None, request_configuration: Optional[SynchronizationRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[synchronization.Synchronization]:
        """
        Update the navigation property synchronization in applications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[synchronization.Synchronization]
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
        return await self.request_adapter.send_async(request_info, synchronization.Synchronization, response_handler, error_mapping)
    
    def ping(self,) -> ping_request_builder.PingRequestBuilder:
        """
        Provides operations to call the Ping method.
        Returns: ping_request_builder.PingRequestBuilder
        """
        return ping_request_builder.PingRequestBuilder(self.request_adapter, self.path_parameters)
    
    def templates_by_id(self,id: str) -> synchronization_template_item_request_builder.SynchronizationTemplateItemRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.synchronization entity.
        Args:
            id: Unique identifier of the item
        Returns: synchronization_template_item_request_builder.SynchronizationTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["synchronizationTemplate%2Did"] = id
        return synchronization_template_item_request_builder.SynchronizationTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class SynchronizationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SynchronizationRequestBuilderGetQueryParameters():
        """
        Get synchronization from applications
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
    class SynchronizationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SynchronizationRequestBuilder.SynchronizationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SynchronizationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

