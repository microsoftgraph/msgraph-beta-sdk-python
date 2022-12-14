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

complete_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.complete.complete_request_builder')
dismiss_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.dismiss.dismiss_request_builder')
impacted_resources_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.impacted_resources.impacted_resources_request_builder')
recommendation_resource_item_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.impacted_resources.item.recommendation_resource_item_request_builder')
postpone_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.postpone.postpone_request_builder')
reactivate_request_builder = lazy_import('msgraph.generated.directory.recommendations.item.reactivate.reactivate_request_builder')
recommendation = lazy_import('msgraph.generated.models.recommendation')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class RecommendationItemRequestBuilder():
    """
    Provides operations to manage the recommendations property of the microsoft.graph.directory entity.
    """
    @property
    def complete(self) -> complete_request_builder.CompleteRequestBuilder:
        """
        Provides operations to call the complete method.
        """
        return complete_request_builder.CompleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss(self) -> dismiss_request_builder.DismissRequestBuilder:
        """
        Provides operations to call the dismiss method.
        """
        return dismiss_request_builder.DismissRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def impacted_resources(self) -> impacted_resources_request_builder.ImpactedResourcesRequestBuilder:
        """
        Provides operations to manage the impactedResources property of the microsoft.graph.recommendation entity.
        """
        return impacted_resources_request_builder.ImpactedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def postpone(self) -> postpone_request_builder.PostponeRequestBuilder:
        """
        Provides operations to call the postpone method.
        """
        return postpone_request_builder.PostponeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reactivate(self) -> reactivate_request_builder.ReactivateRequestBuilder:
        """
        Provides operations to call the reactivate method.
        """
        return reactivate_request_builder.ReactivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RecommendationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directory/recommendations/{recommendation%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[RecommendationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property recommendations for directory
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
    
    def create_get_request_information(self,request_configuration: Optional[RecommendationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get recommendations from directory
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
    
    def create_patch_request_information(self,body: Optional[recommendation.Recommendation] = None, request_configuration: Optional[RecommendationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property recommendations in directory
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
    
    async def delete(self,request_configuration: Optional[RecommendationItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property recommendations for directory
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
    
    async def get(self,request_configuration: Optional[RecommendationItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[recommendation.Recommendation]:
        """
        Get recommendations from directory
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[recommendation.Recommendation]
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
        return await self.request_adapter.send_async(request_info, recommendation.Recommendation, response_handler, error_mapping)
    
    def impacted_resources_by_id(self,id: str) -> recommendation_resource_item_request_builder.RecommendationResourceItemRequestBuilder:
        """
        Provides operations to manage the impactedResources property of the microsoft.graph.recommendation entity.
        Args:
            id: Unique identifier of the item
        Returns: recommendation_resource_item_request_builder.RecommendationResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["recommendationResource%2Did"] = id
        return recommendation_resource_item_request_builder.RecommendationResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[recommendation.Recommendation] = None, request_configuration: Optional[RecommendationItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[recommendation.Recommendation]:
        """
        Update the navigation property recommendations in directory
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[recommendation.Recommendation]
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
        return await self.request_adapter.send_async(request_info, recommendation.Recommendation, response_handler, error_mapping)
    
    @dataclass
    class RecommendationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class RecommendationItemRequestBuilderGetQueryParameters():
        """
        Get recommendations from directory
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
    class RecommendationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[RecommendationItemRequestBuilder.RecommendationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class RecommendationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

