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

category_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.category.category_request_builder')
definition_file_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.definition_file.definition_file_request_builder')
next_version_definition_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.next_version_definition.next_version_definition_request_builder')
presentations_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.presentations.presentations_request_builder')
group_policy_presentation_item_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.presentations.item.group_policy_presentation_item_request_builder')
previous_version_definition_request_builder = lazy_import('msgraph.generated.device_management.group_policy_definitions.item.previous_version_definition.previous_version_definition_request_builder')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class GroupPolicyDefinitionItemRequestBuilder():
    """
    Provides operations to manage the groupPolicyDefinitions property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def category(self) -> category_request_builder.CategoryRequestBuilder:
        """
        Provides operations to manage the category property of the microsoft.graph.groupPolicyDefinition entity.
        """
        return category_request_builder.CategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definition_file(self) -> definition_file_request_builder.DefinitionFileRequestBuilder:
        """
        Provides operations to manage the definitionFile property of the microsoft.graph.groupPolicyDefinition entity.
        """
        return definition_file_request_builder.DefinitionFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def next_version_definition(self) -> next_version_definition_request_builder.NextVersionDefinitionRequestBuilder:
        """
        Provides operations to manage the nextVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
        """
        return next_version_definition_request_builder.NextVersionDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presentations(self) -> presentations_request_builder.PresentationsRequestBuilder:
        """
        Provides operations to manage the presentations property of the microsoft.graph.groupPolicyDefinition entity.
        """
        return presentations_request_builder.PresentationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def previous_version_definition(self) -> previous_version_definition_request_builder.PreviousVersionDefinitionRequestBuilder:
        """
        Provides operations to manage the previousVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
        """
        return previous_version_definition_request_builder.PreviousVersionDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupPolicyDefinitionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/groupPolicyDefinitions/{groupPolicyDefinition%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property groupPolicyDefinitions for deviceManagement
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
    
    async def get(self,request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        The available group policy definitions for this account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
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
        return await self.request_adapter.send_async(request_info, group_policy_definition.GroupPolicyDefinition, error_mapping)
    
    async def patch(self,body: Optional[group_policy_definition.GroupPolicyDefinition] = None, request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        Update the navigation property groupPolicyDefinitions in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
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
        return await self.request_adapter.send_async(request_info, group_policy_definition.GroupPolicyDefinition, error_mapping)
    
    def presentations_by_id(self,id: str) -> group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder:
        """
        Provides operations to manage the presentations property of the microsoft.graph.groupPolicyDefinition entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyPresentation%2Did"] = id
        return group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyDefinitions for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The available group policy definitions for this account.
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
    
    def to_patch_request_information(self,body: Optional[group_policy_definition.GroupPolicyDefinition] = None, request_configuration: Optional[GroupPolicyDefinitionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyDefinitions in deviceManagement
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
    class GroupPolicyDefinitionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupPolicyDefinitionItemRequestBuilderGetQueryParameters():
        """
        The available group policy definitions for this account.
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
    class GroupPolicyDefinitionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupPolicyDefinitionItemRequestBuilder.GroupPolicyDefinitionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupPolicyDefinitionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

