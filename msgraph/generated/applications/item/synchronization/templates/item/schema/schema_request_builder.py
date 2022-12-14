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

directories_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.schema.directories.directories_request_builder')
directory_definition_item_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.schema.directories.item.directory_definition_item_request_builder')
filter_operators_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.schema.filter_operators.filter_operators_request_builder')
functions_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.schema.functions.functions_request_builder')
parse_expression_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.templates.item.schema.parse_expression.parse_expression_request_builder')
synchronization_schema = lazy_import('msgraph.generated.models.synchronization_schema')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SchemaRequestBuilder():
    """
    Provides operations to manage the schema property of the microsoft.graph.synchronizationTemplate entity.
    """
    @property
    def directories(self) -> directories_request_builder.DirectoriesRequestBuilder:
        """
        Provides operations to manage the directories property of the microsoft.graph.synchronizationSchema entity.
        """
        return directories_request_builder.DirectoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parse_expression(self) -> parse_expression_request_builder.ParseExpressionRequestBuilder:
        """
        Provides operations to call the parseExpression method.
        """
        return parse_expression_request_builder.ParseExpressionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SchemaRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}/synchronization/templates/{synchronizationTemplate%2Did}/schema{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[SchemaRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property schema for applications
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
    
    def create_get_request_information(self,request_configuration: Optional[SchemaRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Default synchronization schema for the jobs based on this template.
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
    
    def create_patch_request_information(self,body: Optional[synchronization_schema.SynchronizationSchema] = None, request_configuration: Optional[SchemaRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property schema in applications
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
    
    async def delete(self,request_configuration: Optional[SchemaRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property schema for applications
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
    
    def directories_by_id(self,id: str) -> directory_definition_item_request_builder.DirectoryDefinitionItemRequestBuilder:
        """
        Provides operations to manage the directories property of the microsoft.graph.synchronizationSchema entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_definition_item_request_builder.DirectoryDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryDefinition%2Did"] = id
        return directory_definition_item_request_builder.DirectoryDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def filter_operators(self,) -> filter_operators_request_builder.FilterOperatorsRequestBuilder:
        """
        Provides operations to call the filterOperators method.
        Returns: filter_operators_request_builder.FilterOperatorsRequestBuilder
        """
        return filter_operators_request_builder.FilterOperatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def functions(self,) -> functions_request_builder.FunctionsRequestBuilder:
        """
        Provides operations to call the functions method.
        Returns: functions_request_builder.FunctionsRequestBuilder
        """
        return functions_request_builder.FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def get(self,request_configuration: Optional[SchemaRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Default synchronization schema for the jobs based on this template.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[synchronization_schema.SynchronizationSchema]
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
        return await self.request_adapter.send_async(request_info, synchronization_schema.SynchronizationSchema, response_handler, error_mapping)
    
    async def patch(self,body: Optional[synchronization_schema.SynchronizationSchema] = None, request_configuration: Optional[SchemaRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Update the navigation property schema in applications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[synchronization_schema.SynchronizationSchema]
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
        return await self.request_adapter.send_async(request_info, synchronization_schema.SynchronizationSchema, response_handler, error_mapping)
    
    @dataclass
    class SchemaRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SchemaRequestBuilderGetQueryParameters():
        """
        Default synchronization schema for the jobs based on this template.
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
    class SchemaRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SchemaRequestBuilder.SchemaRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SchemaRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

