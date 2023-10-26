from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.governance_role_assignment import GovernanceRoleAssignment
    from ....models.o_data_errors.o_data_error import ODataError

class LinkedEligibleRoleAssignmentRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the linkedEligibleRoleAssignment property of the microsoft.graph.governanceRoleAssignment entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new LinkedEligibleRoleAssignmentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/governanceRoleAssignments/{governanceRoleAssignment%2Did}/linkedEligibleRoleAssignment{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[LinkedEligibleRoleAssignmentRequestBuilderGetRequestConfiguration] = None) -> Optional[GovernanceRoleAssignment]:
        """
        Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GovernanceRoleAssignment]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.governance_role_assignment import GovernanceRoleAssignment

        return await self.request_adapter.send_async(request_info, GovernanceRoleAssignment, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[LinkedEligibleRoleAssignmentRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> LinkedEligibleRoleAssignmentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LinkedEligibleRoleAssignmentRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return LinkedEligibleRoleAssignmentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LinkedEligibleRoleAssignmentRequestBuilderGetQueryParameters():
        """
        Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class LinkedEligibleRoleAssignmentRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[LinkedEligibleRoleAssignmentRequestBuilder.LinkedEligibleRoleAssignmentRequestBuilderGetQueryParameters] = None

    

