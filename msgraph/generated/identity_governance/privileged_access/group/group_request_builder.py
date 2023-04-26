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
    from ....models import privileged_access_group
    from ....models.o_data_errors import o_data_error
    from .assignment_approvals import assignment_approvals_request_builder
    from .assignment_schedule_instances import assignment_schedule_instances_request_builder
    from .assignment_schedule_requests import assignment_schedule_requests_request_builder
    from .assignment_schedules import assignment_schedules_request_builder
    from .eligibility_schedule_instances import eligibility_schedule_instances_request_builder
    from .eligibility_schedule_requests import eligibility_schedule_requests_request_builder
    from .eligibility_schedules import eligibility_schedules_request_builder

class GroupRequestBuilder():
    """
    Provides operations to manage the group property of the microsoft.graph.privilegedAccessRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/privilegedAccess/group{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GroupRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property group for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[GroupRequestBuilderGetRequestConfiguration] = None) -> Optional[privileged_access_group.PrivilegedAccessGroup]:
        """
        Get group from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[privileged_access_group.PrivilegedAccessGroup]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import privileged_access_group

        return await self.request_adapter.send_async(request_info, privileged_access_group.PrivilegedAccessGroup, error_mapping)
    
    async def patch(self,body: Optional[privileged_access_group.PrivilegedAccessGroup] = None, request_configuration: Optional[GroupRequestBuilderPatchRequestConfiguration] = None) -> Optional[privileged_access_group.PrivilegedAccessGroup]:
        """
        Update the navigation property group in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[privileged_access_group.PrivilegedAccessGroup]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import privileged_access_group

        return await self.request_adapter.send_async(request_info, privileged_access_group.PrivilegedAccessGroup, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property group for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[GroupRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get group from identityGovernance
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
    
    def to_patch_request_information(self,body: Optional[privileged_access_group.PrivilegedAccessGroup] = None, request_configuration: Optional[GroupRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property group in identityGovernance
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
    def assignment_approvals(self) -> assignment_approvals_request_builder.AssignmentApprovalsRequestBuilder:
        """
        Provides operations to manage the assignmentApprovals property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .assignment_approvals import assignment_approvals_request_builder

        return assignment_approvals_request_builder.AssignmentApprovalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_schedule_instances(self) -> assignment_schedule_instances_request_builder.AssignmentScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .assignment_schedule_instances import assignment_schedule_instances_request_builder

        return assignment_schedule_instances_request_builder.AssignmentScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_schedule_requests(self) -> assignment_schedule_requests_request_builder.AssignmentScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .assignment_schedule_requests import assignment_schedule_requests_request_builder

        return assignment_schedule_requests_request_builder.AssignmentScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_schedules(self) -> assignment_schedules_request_builder.AssignmentSchedulesRequestBuilder:
        """
        Provides operations to manage the assignmentSchedules property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .assignment_schedules import assignment_schedules_request_builder

        return assignment_schedules_request_builder.AssignmentSchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedule_instances(self) -> eligibility_schedule_instances_request_builder.EligibilityScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .eligibility_schedule_instances import eligibility_schedule_instances_request_builder

        return eligibility_schedule_instances_request_builder.EligibilityScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedule_requests(self) -> eligibility_schedule_requests_request_builder.EligibilityScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .eligibility_schedule_requests import eligibility_schedule_requests_request_builder

        return eligibility_schedule_requests_request_builder.EligibilityScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedules(self) -> eligibility_schedules_request_builder.EligibilitySchedulesRequestBuilder:
        """
        Provides operations to manage the eligibilitySchedules property of the microsoft.graph.privilegedAccessGroup entity.
        """
        from .eligibility_schedules import eligibility_schedules_request_builder

        return eligibility_schedules_request_builder.EligibilitySchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupRequestBuilderGetQueryParameters():
        """
        Get group from identityGovernance
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
    class GroupRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupRequestBuilder.GroupRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

