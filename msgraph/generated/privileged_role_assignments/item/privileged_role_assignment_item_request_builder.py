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

privileged_role_assignment = lazy_import('msgraph.generated.models.privileged_role_assignment')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
make_eligible_request_builder = lazy_import('msgraph.generated.privileged_role_assignments.item.make_eligible.make_eligible_request_builder')
make_permanent_request_builder = lazy_import('msgraph.generated.privileged_role_assignments.item.make_permanent.make_permanent_request_builder')
role_info_request_builder = lazy_import('msgraph.generated.privileged_role_assignments.item.role_info.role_info_request_builder')

class PrivilegedRoleAssignmentItemRequestBuilder():
    """
    Provides operations to manage the collection of privilegedRoleAssignment entities.
    """
    @property
    def make_eligible(self) -> make_eligible_request_builder.MakeEligibleRequestBuilder:
        """
        Provides operations to call the makeEligible method.
        """
        return make_eligible_request_builder.MakeEligibleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def make_permanent(self) -> make_permanent_request_builder.MakePermanentRequestBuilder:
        """
        Provides operations to call the makePermanent method.
        """
        return make_permanent_request_builder.MakePermanentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_info(self) -> role_info_request_builder.RoleInfoRequestBuilder:
        """
        Provides operations to manage the roleInfo property of the microsoft.graph.privilegedRoleAssignment entity.
        """
        return role_info_request_builder.RoleInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrivilegedRoleAssignmentItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/privilegedRoleAssignments/{privilegedRoleAssignment%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete privilegedRoleAssignment.
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
    
    def create_get_request_information(self,request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of privilegedRoleAssignment object.
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
    
    def create_patch_request_information(self,body: Optional[privileged_role_assignment.PrivilegedRoleAssignment] = None, request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in privilegedRoleAssignments
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
    
    async def delete(self,request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete privilegedRoleAssignment.
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
    
    async def get(self,request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_role_assignment.PrivilegedRoleAssignment]:
        """
        Retrieve the properties and relationships of privilegedRoleAssignment object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_role_assignment.PrivilegedRoleAssignment]
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
        return await self.request_adapter.send_async(request_info, privileged_role_assignment.PrivilegedRoleAssignment, response_handler, error_mapping)
    
    async def patch(self,body: Optional[privileged_role_assignment.PrivilegedRoleAssignment] = None, request_configuration: Optional[PrivilegedRoleAssignmentItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_role_assignment.PrivilegedRoleAssignment]:
        """
        Update entity in privilegedRoleAssignments
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_role_assignment.PrivilegedRoleAssignment]
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
        return await self.request_adapter.send_async(request_info, privileged_role_assignment.PrivilegedRoleAssignment, response_handler, error_mapping)
    
    @dataclass
    class PrivilegedRoleAssignmentItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrivilegedRoleAssignmentItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of privilegedRoleAssignment object.
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
    class PrivilegedRoleAssignmentItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrivilegedRoleAssignmentItemRequestBuilder.PrivilegedRoleAssignmentItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrivilegedRoleAssignmentItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

