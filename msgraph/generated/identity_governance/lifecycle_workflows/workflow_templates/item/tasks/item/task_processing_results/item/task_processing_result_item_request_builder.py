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
    from .........models.identity_governance import task_processing_result
    from .........models.o_data_errors import o_data_error
    from .identity_governance_resume import identity_governance_resume_request_builder
    from .subject import subject_request_builder
    from .task import task_request_builder

class TaskProcessingResultItemRequestBuilder():
    """
    Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.task entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TaskProcessingResultItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/workflowTemplates/{workflowTemplate%2Did}/tasks/{task%2Did}/taskProcessingResults/{taskProcessingResult%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[TaskProcessingResultItemRequestBuilderGetRequestConfiguration] = None) -> Optional[task_processing_result.TaskProcessingResult]:
        """
        The result of processing the task.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[task_processing_result.TaskProcessingResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.identity_governance import task_processing_result

        return await self.request_adapter.send_async(request_info, task_processing_result.TaskProcessingResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TaskProcessingResultItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The result of processing the task.
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
    
    @property
    def identity_governance_resume(self) -> identity_governance_resume_request_builder.IdentityGovernanceResumeRequestBuilder:
        """
        Provides operations to call the resume method.
        """
        from .identity_governance_resume import identity_governance_resume_request_builder

        return identity_governance_resume_request_builder.IdentityGovernanceResumeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subject(self) -> subject_request_builder.SubjectRequestBuilder:
        """
        Provides operations to manage the subject property of the microsoft.graph.identityGovernance.taskProcessingResult entity.
        """
        from .subject import subject_request_builder

        return subject_request_builder.SubjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task(self) -> task_request_builder.TaskRequestBuilder:
        """
        Provides operations to manage the task property of the microsoft.graph.identityGovernance.taskProcessingResult entity.
        """
        from .task import task_request_builder

        return task_request_builder.TaskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TaskProcessingResultItemRequestBuilderGetQueryParameters():
        """
        The result of processing the task.
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
    class TaskProcessingResultItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TaskProcessingResultItemRequestBuilder.TaskProcessingResultItemRequestBuilderGetQueryParameters] = None

    

