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

children_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.children.children_request_builder')
group_policy_category_item_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.children.item.group_policy_category_item_request_builder')
definition_file_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.definition_file.definition_file_request_builder')
definitions_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.definitions.definitions_request_builder')
group_policy_definition_item_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.definitions.item.group_policy_definition_item_request_builder')
parent_request_builder = lazy_import('msgraph.generated.device_management.group_policy_categories.item.parent.parent_request_builder')
group_policy_category = lazy_import('msgraph.generated.models.group_policy_category')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class GroupPolicyCategoryItemRequestBuilder():
    """
    Provides operations to manage the groupPolicyCategories property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.groupPolicyCategory entity.
        """
        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definition_file(self) -> definition_file_request_builder.DefinitionFileRequestBuilder:
        """
        Provides operations to manage the definitionFile property of the microsoft.graph.groupPolicyCategory entity.
        """
        return definition_file_request_builder.DefinitionFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definitions(self) -> definitions_request_builder.DefinitionsRequestBuilder:
        """
        Provides operations to manage the definitions property of the microsoft.graph.groupPolicyCategory entity.
        """
        return definitions_request_builder.DefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent(self) -> parent_request_builder.ParentRequestBuilder:
        """
        Provides operations to manage the parent property of the microsoft.graph.groupPolicyCategory entity.
        """
        return parent_request_builder.ParentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def children_by_id(self,id: str) -> GroupPolicyCategoryItemRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.groupPolicyCategory entity.
        Args:
            id: Unique identifier of the item
        Returns: GroupPolicyCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyCategory%2Did1"] = id
        return GroupPolicyCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupPolicyCategoryItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/groupPolicyCategories/{groupPolicyCategory%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyCategories for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The available group policy categories for this account.
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
    
    def create_patch_request_information(self,body: Optional[group_policy_category.GroupPolicyCategory] = None, request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyCategories in deviceManagement
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
    
    def definitions_by_id(self,id: str) -> group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder:
        """
        Provides operations to manage the definitions property of the microsoft.graph.groupPolicyCategory entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyDefinition%2Did"] = id
        return group_policy_definition_item_request_builder.GroupPolicyDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property groupPolicyCategories for deviceManagement
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
    
    async def get(self,request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[group_policy_category.GroupPolicyCategory]:
        """
        The available group policy categories for this account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[group_policy_category.GroupPolicyCategory]
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
        return await self.request_adapter.send_async(request_info, group_policy_category.GroupPolicyCategory, response_handler, error_mapping)
    
    async def patch(self,body: Optional[group_policy_category.GroupPolicyCategory] = None, request_configuration: Optional[GroupPolicyCategoryItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[group_policy_category.GroupPolicyCategory]:
        """
        Update the navigation property groupPolicyCategories in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[group_policy_category.GroupPolicyCategory]
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
        return await self.request_adapter.send_async(request_info, group_policy_category.GroupPolicyCategory, response_handler, error_mapping)
    
    @dataclass
    class GroupPolicyCategoryItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupPolicyCategoryItemRequestBuilderGetQueryParameters():
        """
        The available group policy categories for this account.
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
    class GroupPolicyCategoryItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupPolicyCategoryItemRequestBuilder.GroupPolicyCategoryItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupPolicyCategoryItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

