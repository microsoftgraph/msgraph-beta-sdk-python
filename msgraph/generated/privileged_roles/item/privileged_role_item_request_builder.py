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
    from ...models import privileged_role
    from ...models.o_data_errors import o_data_error
    from .assignments import assignments_request_builder
    from .assignments.item import privileged_role_assignment_item_request_builder
    from .self_activate import self_activate_request_builder
    from .self_deactivate import self_deactivate_request_builder
    from .settings import settings_request_builder
    from .summary import summary_request_builder

class PrivilegedRoleItemRequestBuilder():
    """
    Provides operations to manage the collection of privilegedRole entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrivilegedRoleItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/privilegedRoles/{privilegedRole%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignments_by_id(self,id: str) -> privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.privilegedRole entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import privileged_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedRoleAssignment%2Did"] = id
        return privileged_role_assignment_item_request_builder.PrivilegedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[PrivilegedRoleItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from privilegedRoles
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PrivilegedRoleItemRequestBuilderGetRequestConfiguration] = None) -> Optional[privileged_role.PrivilegedRole]:
        """
        Retrieve the properties and relationships of privilegedRole object. 
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[privileged_role.PrivilegedRole]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import privileged_role

        return await self.request_adapter.send_async(request_info, privileged_role.PrivilegedRole, error_mapping)
    
    async def patch(self,body: Optional[privileged_role.PrivilegedRole] = None, request_configuration: Optional[PrivilegedRoleItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[privileged_role.PrivilegedRole]:
        """
        Update entity in privilegedRoles
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[privileged_role.PrivilegedRole]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import privileged_role

        return await self.request_adapter.send_async(request_info, privileged_role.PrivilegedRole, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrivilegedRoleItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from privilegedRoles
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
    
    def to_get_request_information(self,request_configuration: Optional[PrivilegedRoleItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of privilegedRole object. 
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
    
    def to_patch_request_information(self,body: Optional[privileged_role.PrivilegedRole] = None, request_configuration: Optional[PrivilegedRoleItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in privilegedRoles
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
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.privilegedRole entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def self_activate(self) -> self_activate_request_builder.SelfActivateRequestBuilder:
        """
        Provides operations to call the selfActivate method.
        """
        from .self_activate import self_activate_request_builder

        return self_activate_request_builder.SelfActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def self_deactivate(self) -> self_deactivate_request_builder.SelfDeactivateRequestBuilder:
        """
        Provides operations to call the selfDeactivate method.
        """
        from .self_deactivate import self_deactivate_request_builder

        return self_deactivate_request_builder.SelfDeactivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.privilegedRole entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def summary(self) -> summary_request_builder.SummaryRequestBuilder:
        """
        Provides operations to manage the summary property of the microsoft.graph.privilegedRole entity.
        """
        from .summary import summary_request_builder

        return summary_request_builder.SummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrivilegedRoleItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrivilegedRoleItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of privilegedRole object. 
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
    class PrivilegedRoleItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrivilegedRoleItemRequestBuilder.PrivilegedRoleItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrivilegedRoleItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

