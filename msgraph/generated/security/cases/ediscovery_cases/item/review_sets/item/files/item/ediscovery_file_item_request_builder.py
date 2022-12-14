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

o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
ediscovery_file = lazy_import('msgraph.generated.models.security.ediscovery_file')
content_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.files.item.content.content_request_builder')
custodian_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.files.item.custodian.custodian_request_builder')
extracted_text_content_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.files.item.extracted_text_content.extracted_text_content_request_builder')
tags_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.files.item.tags.tags_request_builder')
ediscovery_review_tag_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.files.item.tags.item.ediscovery_review_tag_item_request_builder')

class EdiscoveryFileItemRequestBuilder():
    """
    Provides operations to manage the files property of the microsoft.graph.security.ediscoveryReviewSet entity.
    """
    @property
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the security entity.
        """
        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custodian(self) -> custodian_request_builder.CustodianRequestBuilder:
        """
        Provides operations to manage the custodian property of the microsoft.graph.security.ediscoveryFile entity.
        """
        return custodian_request_builder.CustodianRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extracted_text_content(self) -> extracted_text_content_request_builder.ExtractedTextContentRequestBuilder:
        """
        Provides operations to manage the media for the security entity.
        """
        return extracted_text_content_request_builder.ExtractedTextContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> tags_request_builder.TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryFile entity.
        """
        return tags_request_builder.TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoveryFileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/reviewSets/{ediscoveryReviewSet%2Did}/files/{ediscoveryFile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EdiscoveryFileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property files for security
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
    
    def create_get_request_information(self,request_configuration: Optional[EdiscoveryFileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents files within the review set.
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
    
    def create_patch_request_information(self,body: Optional[ediscovery_file.EdiscoveryFile] = None, request_configuration: Optional[EdiscoveryFileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property files in security
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
    
    async def delete(self,request_configuration: Optional[EdiscoveryFileItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property files for security
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
    
    async def get(self,request_configuration: Optional[EdiscoveryFileItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ediscovery_file.EdiscoveryFile]:
        """
        Represents files within the review set.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ediscovery_file.EdiscoveryFile]
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
        return await self.request_adapter.send_async(request_info, ediscovery_file.EdiscoveryFile, response_handler, error_mapping)
    
    async def patch(self,body: Optional[ediscovery_file.EdiscoveryFile] = None, request_configuration: Optional[EdiscoveryFileItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ediscovery_file.EdiscoveryFile]:
        """
        Update the navigation property files in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ediscovery_file.EdiscoveryFile]
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
        return await self.request_adapter.send_async(request_info, ediscovery_file.EdiscoveryFile, response_handler, error_mapping)
    
    def tags_by_id(self,id: str) -> ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryFile entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryReviewTag%2Did"] = id
        return ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EdiscoveryFileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EdiscoveryFileItemRequestBuilderGetQueryParameters():
        """
        Represents files within the review set.
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
    class EdiscoveryFileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EdiscoveryFileItemRequestBuilder.EdiscoveryFileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EdiscoveryFileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

