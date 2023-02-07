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

allowed_values_request_builder = lazy_import('msgraph.generated.directory.custom_security_attribute_definitions.item.allowed_values.allowed_values_request_builder')
allowed_value_item_request_builder = lazy_import('msgraph.generated.directory.custom_security_attribute_definitions.item.allowed_values.item.allowed_value_item_request_builder')
custom_security_attribute_definition = lazy_import('msgraph.generated.models.custom_security_attribute_definition')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CustomSecurityAttributeDefinitionItemRequestBuilder():
    """
    Provides operations to manage the customSecurityAttributeDefinitions property of the microsoft.graph.directory entity.
    """
    @property
    def allowed_values(self) -> allowed_values_request_builder.AllowedValuesRequestBuilder:
        """
        Provides operations to manage the allowedValues property of the microsoft.graph.customSecurityAttributeDefinition entity.
        """
        return allowed_values_request_builder.AllowedValuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def allowed_values_by_id(self,id: str) -> allowed_value_item_request_builder.AllowedValueItemRequestBuilder:
        """
        Provides operations to manage the allowedValues property of the microsoft.graph.customSecurityAttributeDefinition entity.
        Args:
            id: Unique identifier of the item
        Returns: allowed_value_item_request_builder.AllowedValueItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["allowedValue%2Did"] = id
        return allowed_value_item_request_builder.AllowedValueItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CustomSecurityAttributeDefinitionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directory/customSecurityAttributeDefinitions/{customSecurityAttributeDefinition%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property customSecurityAttributeDefinitions for directory
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition]:
        """
        Schema of a custom security attributes (key-value pairs).
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, custom_security_attribute_definition.CustomSecurityAttributeDefinition, error_mapping)
    
    async def patch(self,body: Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition] = None, request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition]:
        """
        Update the navigation property customSecurityAttributeDefinitions in directory
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, custom_security_attribute_definition.CustomSecurityAttributeDefinition, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property customSecurityAttributeDefinitions for directory
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
    
    def to_get_request_information(self,request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Schema of a custom security attributes (key-value pairs).
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
    
    def to_patch_request_information(self,body: Optional[custom_security_attribute_definition.CustomSecurityAttributeDefinition] = None, request_configuration: Optional[CustomSecurityAttributeDefinitionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property customSecurityAttributeDefinitions in directory
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
    
    @dataclass
    class CustomSecurityAttributeDefinitionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CustomSecurityAttributeDefinitionItemRequestBuilderGetQueryParameters():
        """
        Schema of a custom security attributes (key-value pairs).
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
    class CustomSecurityAttributeDefinitionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CustomSecurityAttributeDefinitionItemRequestBuilder.CustomSecurityAttributeDefinitionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CustomSecurityAttributeDefinitionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

