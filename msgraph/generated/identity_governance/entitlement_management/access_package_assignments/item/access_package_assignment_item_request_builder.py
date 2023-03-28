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
    from .....models import access_package_assignment
    from .....models.o_data_errors import o_data_error
    from .access_package import access_package_request_builder
    from .access_package_assignment_policy import access_package_assignment_policy_request_builder
    from .access_package_assignment_requests import access_package_assignment_requests_request_builder
    from .access_package_assignment_requests.item import access_package_assignment_request_item_request_builder
    from .access_package_assignment_resource_roles import access_package_assignment_resource_roles_request_builder
    from .access_package_assignment_resource_roles.item import access_package_assignment_resource_role_item_request_builder
    from .reprocess import reprocess_request_builder
    from .target import target_request_builder

class AccessPackageAssignmentItemRequestBuilder():
    """
    Provides operations to manage the accessPackageAssignments property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageAssignmentItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def access_package_assignment_requests_by_id(self,id: str) -> access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentRequests property of the microsoft.graph.accessPackageAssignment entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_package_assignment_requests.item import access_package_assignment_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentRequest%2Did"] = id
        return access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_package_assignment_resource_roles_by_id(self,id: str) -> access_package_assignment_resource_role_item_request_builder.AccessPackageAssignmentResourceRoleItemRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentResourceRoles property of the microsoft.graph.accessPackageAssignment entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_resource_role_item_request_builder.AccessPackageAssignmentResourceRoleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_package_assignment_resource_roles.item import access_package_assignment_resource_role_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentResourceRole%2Did"] = id
        return access_package_assignment_resource_role_item_request_builder.AccessPackageAssignmentResourceRoleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property accessPackageAssignments for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderGetRequestConfiguration] = None) -> Optional[access_package_assignment.AccessPackageAssignment]:
        """
        The assignment of an access package to a subject for a period of time.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package_assignment.AccessPackageAssignment]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package_assignment

        return await self.request_adapter.send_async(request_info, access_package_assignment.AccessPackageAssignment, error_mapping)
    
    async def patch(self,body: Optional[access_package_assignment.AccessPackageAssignment] = None, request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_package_assignment.AccessPackageAssignment]:
        """
        Update the navigation property accessPackageAssignments in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package_assignment.AccessPackageAssignment]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package_assignment

        return await self.request_adapter.send_async(request_info, access_package_assignment.AccessPackageAssignment, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackageAssignments for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The assignment of an access package to a subject for a period of time.
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
    
    def to_patch_request_information(self,body: Optional[access_package_assignment.AccessPackageAssignment] = None, request_configuration: Optional[AccessPackageAssignmentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackageAssignments in identityGovernance
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
    def access_package(self) -> access_package_request_builder.AccessPackageRequestBuilder:
        """
        Provides operations to manage the accessPackage property of the microsoft.graph.accessPackageAssignment entity.
        """
        from .access_package import access_package_request_builder

        return access_package_request_builder.AccessPackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_assignment_policy(self) -> access_package_assignment_policy_request_builder.AccessPackageAssignmentPolicyRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentPolicy property of the microsoft.graph.accessPackageAssignment entity.
        """
        from .access_package_assignment_policy import access_package_assignment_policy_request_builder

        return access_package_assignment_policy_request_builder.AccessPackageAssignmentPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_assignment_requests(self) -> access_package_assignment_requests_request_builder.AccessPackageAssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentRequests property of the microsoft.graph.accessPackageAssignment entity.
        """
        from .access_package_assignment_requests import access_package_assignment_requests_request_builder

        return access_package_assignment_requests_request_builder.AccessPackageAssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_assignment_resource_roles(self) -> access_package_assignment_resource_roles_request_builder.AccessPackageAssignmentResourceRolesRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentResourceRoles property of the microsoft.graph.accessPackageAssignment entity.
        """
        from .access_package_assignment_resource_roles import access_package_assignment_resource_roles_request_builder

        return access_package_assignment_resource_roles_request_builder.AccessPackageAssignmentResourceRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprocess(self) -> reprocess_request_builder.ReprocessRequestBuilder:
        """
        Provides operations to call the reprocess method.
        """
        from .reprocess import reprocess_request_builder

        return reprocess_request_builder.ReprocessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target(self) -> target_request_builder.TargetRequestBuilder:
        """
        Provides operations to manage the target property of the microsoft.graph.accessPackageAssignment entity.
        """
        from .target import target_request_builder

        return target_request_builder.TargetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackageAssignmentItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageAssignmentItemRequestBuilderGetQueryParameters():
        """
        The assignment of an access package to a subject for a period of time.
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
    class AccessPackageAssignmentItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageAssignmentItemRequestBuilder.AccessPackageAssignmentItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageAssignmentItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

