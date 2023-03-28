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
    from .....models.identity_governance import workflow
    from .....models.o_data_errors import o_data_error
    from .execution_scope import execution_scope_request_builder
    from .execution_scope.item import user_item_request_builder
    from .identity_governance_activate import identity_governance_activate_request_builder
    from .identity_governance_create_new_version import identity_governance_create_new_version_request_builder
    from .identity_governance_restore import identity_governance_restore_request_builder
    from .runs import runs_request_builder
    from .runs.item import run_item_request_builder
    from .task_reports import task_reports_request_builder
    from .task_reports.item import task_report_item_request_builder
    from .user_processing_results import user_processing_results_request_builder
    from .user_processing_results.item import user_processing_result_item_request_builder
    from .versions import versions_request_builder
    from .versions.item import workflow_version_version_number_item_request_builder

class WorkflowItemRequestBuilder():
    """
    Provides operations to manage the workflows property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkflowItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WorkflowItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property workflows for identityGovernance
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
    
    def execution_scope_by_id(self,id: str) -> user_item_request_builder.UserItemRequestBuilder:
        """
        Provides operations to manage the executionScope property of the microsoft.graph.identityGovernance.workflow entity.
        Args:
            id: Unique identifier of the item
        Returns: user_item_request_builder.UserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .execution_scope.item import user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[WorkflowItemRequestBuilderGetRequestConfiguration] = None) -> Optional[workflow.Workflow]:
        """
        The workflows in the lifecycle workflows instance.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workflow.Workflow]
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
        from .....models.identity_governance import workflow

        return await self.request_adapter.send_async(request_info, workflow.Workflow, error_mapping)
    
    async def patch(self,body: Optional[workflow.Workflow] = None, request_configuration: Optional[WorkflowItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[workflow.Workflow]:
        """
        Update the navigation property workflows in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workflow.Workflow]
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
        from .....models.identity_governance import workflow

        return await self.request_adapter.send_async(request_info, workflow.Workflow, error_mapping)
    
    def runs_by_id(self,id: str) -> run_item_request_builder.RunItemRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.identityGovernance.workflow entity.
        Args:
            id: Unique identifier of the item
        Returns: run_item_request_builder.RunItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .runs.item import run_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["run%2Did"] = id
        return run_item_request_builder.RunItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def task_reports_by_id(self,id: str) -> task_report_item_request_builder.TaskReportItemRequestBuilder:
        """
        Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
        Args:
            id: Unique identifier of the item
        Returns: task_report_item_request_builder.TaskReportItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .task_reports.item import task_report_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taskReport%2Did"] = id
        return task_report_item_request_builder.TaskReportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkflowItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property workflows for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkflowItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The workflows in the lifecycle workflows instance.
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
    
    def to_patch_request_information(self,body: Optional[workflow.Workflow] = None, request_configuration: Optional[WorkflowItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property workflows in identityGovernance
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
    
    def user_processing_results_by_id(self,id: str) -> user_processing_result_item_request_builder.UserProcessingResultItemRequestBuilder:
        """
        Provides operations to manage the userProcessingResults property of the microsoft.graph.identityGovernance.workflow entity.
        Args:
            id: Unique identifier of the item
        Returns: user_processing_result_item_request_builder.UserProcessingResultItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_processing_results.item import user_processing_result_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userProcessingResult%2Did"] = id
        return user_processing_result_item_request_builder.UserProcessingResultItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def versions_by_id(self,id: str) -> workflow_version_version_number_item_request_builder.WorkflowVersionVersionNumberItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.identityGovernance.workflow entity.
        Args:
            id: Unique identifier of the item
        Returns: workflow_version_version_number_item_request_builder.WorkflowVersionVersionNumberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .versions.item import workflow_version_version_number_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workflowVersion%2DversionNumber"] = id
        return workflow_version_version_number_item_request_builder.WorkflowVersionVersionNumberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def execution_scope(self) -> execution_scope_request_builder.ExecutionScopeRequestBuilder:
        """
        Provides operations to manage the executionScope property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .execution_scope import execution_scope_request_builder

        return execution_scope_request_builder.ExecutionScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance_activate(self) -> identity_governance_activate_request_builder.IdentityGovernanceActivateRequestBuilder:
        """
        Provides operations to call the activate method.
        """
        from .identity_governance_activate import identity_governance_activate_request_builder

        return identity_governance_activate_request_builder.IdentityGovernanceActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance_create_new_version(self) -> identity_governance_create_new_version_request_builder.IdentityGovernanceCreateNewVersionRequestBuilder:
        """
        Provides operations to call the createNewVersion method.
        """
        from .identity_governance_create_new_version import identity_governance_create_new_version_request_builder

        return identity_governance_create_new_version_request_builder.IdentityGovernanceCreateNewVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance_restore(self) -> identity_governance_restore_request_builder.IdentityGovernanceRestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .identity_governance_restore import identity_governance_restore_request_builder

        return identity_governance_restore_request_builder.IdentityGovernanceRestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def runs(self) -> runs_request_builder.RunsRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .runs import runs_request_builder

        return runs_request_builder.RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_reports(self) -> task_reports_request_builder.TaskReportsRequestBuilder:
        """
        Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .task_reports import task_reports_request_builder

        return task_reports_request_builder.TaskReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_processing_results(self) -> user_processing_results_request_builder.UserProcessingResultsRequestBuilder:
        """
        Provides operations to manage the userProcessingResults property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .user_processing_results import user_processing_results_request_builder

        return user_processing_results_request_builder.UserProcessingResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .versions import versions_request_builder

        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkflowItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkflowItemRequestBuilderGetQueryParameters():
        """
        The workflows in the lifecycle workflows instance.
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
    class WorkflowItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkflowItemRequestBuilder.WorkflowItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WorkflowItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

