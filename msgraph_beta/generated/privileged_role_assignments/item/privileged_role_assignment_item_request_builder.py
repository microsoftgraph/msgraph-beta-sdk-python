from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.privileged_role_assignment import PrivilegedRoleAssignment
    from .make_eligible.make_eligible_request_builder import MakeEligibleRequestBuilder
    from .make_permanent.make_permanent_request_builder import MakePermanentRequestBuilder
    from .role_info.role_info_request_builder import RoleInfoRequestBuilder

class PrivilegedRoleAssignmentItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of privilegedRoleAssignment entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PrivilegedRoleAssignmentItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/privilegedRoleAssignments/{privilegedRoleAssignment%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete entity from privilegedRoleAssignments
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[PrivilegedRoleAssignment]:
        """
        Get entity from privilegedRoleAssignments by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrivilegedRoleAssignment]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.privileged_role_assignment import PrivilegedRoleAssignment

        return await self.request_adapter.send_async(request_info, PrivilegedRoleAssignment, error_mapping)
    
    async def patch(self,body: Optional[PrivilegedRoleAssignment] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[PrivilegedRoleAssignment]:
        """
        Update entity in privilegedRoleAssignments
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrivilegedRoleAssignment]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.privileged_role_assignment import PrivilegedRoleAssignment

        return await self.request_adapter.send_async(request_info, PrivilegedRoleAssignment, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from privilegedRoleAssignments
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from privilegedRoleAssignments by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PrivilegedRoleAssignment] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in privilegedRoleAssignments
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PrivilegedRoleAssignmentItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrivilegedRoleAssignmentItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PrivilegedRoleAssignmentItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def make_eligible(self) -> MakeEligibleRequestBuilder:
        """
        Provides operations to call the makeEligible method.
        """
        from .make_eligible.make_eligible_request_builder import MakeEligibleRequestBuilder

        return MakeEligibleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def make_permanent(self) -> MakePermanentRequestBuilder:
        """
        Provides operations to call the makePermanent method.
        """
        from .make_permanent.make_permanent_request_builder import MakePermanentRequestBuilder

        return MakePermanentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_info(self) -> RoleInfoRequestBuilder:
        """
        Provides operations to manage the roleInfo property of the microsoft.graph.privilegedRoleAssignment entity.
        """
        from .role_info.role_info_request_builder import RoleInfoRequestBuilder

        return RoleInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrivilegedRoleAssignmentItemRequestBuilderGetQueryParameters():
        """
        Get entity from privilegedRoleAssignments by key
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    

