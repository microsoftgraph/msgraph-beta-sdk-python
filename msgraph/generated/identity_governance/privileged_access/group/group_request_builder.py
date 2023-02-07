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

assignment_schedule_instances_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedule_instances.assignment_schedule_instances_request_builder')
privileged_access_group_assignment_schedule_instance_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedule_instances.item.privileged_access_group_assignment_schedule_instance_item_request_builder')
assignment_schedule_requests_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedule_requests.assignment_schedule_requests_request_builder')
privileged_access_group_assignment_schedule_request_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedule_requests.item.privileged_access_group_assignment_schedule_request_item_request_builder')
assignment_schedules_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedules.assignment_schedules_request_builder')
privileged_access_group_assignment_schedule_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.assignment_schedules.item.privileged_access_group_assignment_schedule_item_request_builder')
eligibility_schedule_instances_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_instances.eligibility_schedule_instances_request_builder')
privileged_access_group_eligibility_schedule_instance_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_instances.item.privileged_access_group_eligibility_schedule_instance_item_request_builder')
eligibility_schedule_requests_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.eligibility_schedule_requests_request_builder')
privileged_access_group_eligibility_schedule_request_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.item.privileged_access_group_eligibility_schedule_request_item_request_builder')
eligibility_schedules_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedules.eligibility_schedules_request_builder')
privileged_access_group_eligibility_schedule_item_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedules.item.privileged_access_group_eligibility_schedule_item_request_builder')
privileged_access_group = lazy_import('msgraph.generated.models.privileged_access_group')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class GroupRequestBuilder():
    """
    Provides operations to manage the group property of the microsoft.graph.privilegedAccessRoot entity.
    """
    @property
    def assignment_schedule_instances(self) -> assignment_schedule_instances_request_builder.AssignmentScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return assignment_schedule_instances_request_builder.AssignmentScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_schedule_requests(self) -> assignment_schedule_requests_request_builder.AssignmentScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return assignment_schedule_requests_request_builder.AssignmentScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_schedules(self) -> assignment_schedules_request_builder.AssignmentSchedulesRequestBuilder:
        """
        Provides operations to manage the assignmentSchedules property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return assignment_schedules_request_builder.AssignmentSchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedule_instances(self) -> eligibility_schedule_instances_request_builder.EligibilityScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return eligibility_schedule_instances_request_builder.EligibilityScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedule_requests(self) -> eligibility_schedule_requests_request_builder.EligibilityScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return eligibility_schedule_requests_request_builder.EligibilityScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eligibility_schedules(self) -> eligibility_schedules_request_builder.EligibilitySchedulesRequestBuilder:
        """
        Provides operations to manage the eligibilitySchedules property of the microsoft.graph.privilegedAccessGroup entity.
        """
        return eligibility_schedules_request_builder.EligibilitySchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignment_schedule_instances_by_id(self,id: str) -> privileged_access_group_assignment_schedule_instance_item_request_builder.PrivilegedAccessGroupAssignmentScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_assignment_schedule_instance_item_request_builder.PrivilegedAccessGroupAssignmentScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupAssignmentScheduleInstance%2Did"] = id
        return privileged_access_group_assignment_schedule_instance_item_request_builder.PrivilegedAccessGroupAssignmentScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_schedule_requests_by_id(self,id: str) -> privileged_access_group_assignment_schedule_request_item_request_builder.PrivilegedAccessGroupAssignmentScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the assignmentScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_assignment_schedule_request_item_request_builder.PrivilegedAccessGroupAssignmentScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupAssignmentScheduleRequest%2Did"] = id
        return privileged_access_group_assignment_schedule_request_item_request_builder.PrivilegedAccessGroupAssignmentScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_schedules_by_id(self,id: str) -> privileged_access_group_assignment_schedule_item_request_builder.PrivilegedAccessGroupAssignmentScheduleItemRequestBuilder:
        """
        Provides operations to manage the assignmentSchedules property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_assignment_schedule_item_request_builder.PrivilegedAccessGroupAssignmentScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupAssignmentSchedule%2Did"] = id
        return privileged_access_group_assignment_schedule_item_request_builder.PrivilegedAccessGroupAssignmentScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def eligibility_schedule_instances_by_id(self,id: str) -> privileged_access_group_eligibility_schedule_instance_item_request_builder.PrivilegedAccessGroupEligibilityScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleInstances property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_eligibility_schedule_instance_item_request_builder.PrivilegedAccessGroupEligibilityScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupEligibilityScheduleInstance%2Did"] = id
        return privileged_access_group_eligibility_schedule_instance_item_request_builder.PrivilegedAccessGroupEligibilityScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def eligibility_schedule_requests_by_id(self,id: str) -> privileged_access_group_eligibility_schedule_request_item_request_builder.PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the eligibilityScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_eligibility_schedule_request_item_request_builder.PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupEligibilityScheduleRequest%2Did"] = id
        return privileged_access_group_eligibility_schedule_request_item_request_builder.PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def eligibility_schedules_by_id(self,id: str) -> privileged_access_group_eligibility_schedule_item_request_builder.PrivilegedAccessGroupEligibilityScheduleItemRequestBuilder:
        """
        Provides operations to manage the eligibilitySchedules property of the microsoft.graph.privilegedAccessGroup entity.
        Args:
            id: Unique identifier of the item
        Returns: privileged_access_group_eligibility_schedule_item_request_builder.PrivilegedAccessGroupEligibilityScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["privilegedAccessGroupEligibilitySchedule%2Did"] = id
        return privileged_access_group_eligibility_schedule_item_request_builder.PrivilegedAccessGroupEligibilityScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
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
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
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
        request_info.headers["Accept"] = "application/json"
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class GroupRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupRequestBuilderGetQueryParameters():
        """
        Get group from identityGovernance
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
    class GroupRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

