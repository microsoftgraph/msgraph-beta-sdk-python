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
    from .....models.identity_governance import workflow_template
    from .....models.o_data_errors import o_data_error
    from .tasks import tasks_request_builder
    from .tasks.item import task_item_request_builder

class WorkflowTemplateItemRequestBuilder():
    """
    Provides operations to manage the workflowTemplates property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkflowTemplateItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/workflowTemplates/{workflowTemplate%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[WorkflowTemplateItemRequestBuilderGetRequestConfiguration] = None) -> Optional[workflow_template.WorkflowTemplate]:
        """
        The workflow templates in the lifecycle workflow instance.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workflow_template.WorkflowTemplate]
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
        from .....models.identity_governance import workflow_template

        return await self.request_adapter.send_async(request_info, workflow_template.WorkflowTemplate, error_mapping)
    
    def tasks_by_id(self,id: str) -> task_item_request_builder.TaskItemRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.identityGovernance.workflowTemplate entity.
        Args:
            id: Unique identifier of the item
        Returns: task_item_request_builder.TaskItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tasks.item import task_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["task%2Did"] = id
        return task_item_request_builder.TaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[WorkflowTemplateItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The workflow templates in the lifecycle workflow instance.
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
    def tasks(self) -> tasks_request_builder.TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.identityGovernance.workflowTemplate entity.
        """
        from .tasks import tasks_request_builder

        return tasks_request_builder.TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkflowTemplateItemRequestBuilderGetQueryParameters():
        """
        The workflow templates in the lifecycle workflow instance.
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
    class WorkflowTemplateItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkflowTemplateItemRequestBuilder.WorkflowTemplateItemRequestBuilderGetQueryParameters] = None

    

