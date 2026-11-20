from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.investigation_session import InvestigationSession
    from .....models.o_data_errors.o_data_error import ODataError
    from .agent_runs.agent_runs_request_builder import AgentRunsRequestBuilder
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .inputs.inputs_request_builder import InputsRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .outputs.outputs_request_builder import OutputsRequestBuilder
    from .playbook_definition.playbook_definition_request_builder import PlaybookDefinitionRequestBuilder

class InvestigationSessionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sessions property of the microsoft.graph.agenticSecurityRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InvestigationSessionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/agenticSecurity/sessions/{investigationSession%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InvestigationSessionItemRequestBuilderGetQueryParameters]] = None) -> Optional[InvestigationSession]:
        """
        Get an agentic session and poll its processing status. This operation uses the agentic session resource.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InvestigationSession]
        Find more info here: https://learn.microsoft.com/graph/api/investigationsession-get?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.investigation_session import InvestigationSession

        return await self.request_adapter.send_async(request_info, InvestigationSession, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InvestigationSessionItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get an agentic session and poll its processing status. This operation uses the agentic session resource.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> InvestigationSessionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InvestigationSessionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InvestigationSessionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def agent_runs(self) -> AgentRunsRequestBuilder:
        """
        Provides operations to manage the agentRuns property of the microsoft.graph.investigationSession entity.
        """
        from .agent_runs.agent_runs_request_builder import AgentRunsRequestBuilder

        return AgentRunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inputs(self) -> InputsRequestBuilder:
        """
        Provides operations to manage the inputs property of the microsoft.graph.investigationSession entity.
        """
        from .inputs.inputs_request_builder import InputsRequestBuilder

        return InputsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.investigationSession entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outputs(self) -> OutputsRequestBuilder:
        """
        Provides operations to manage the outputs property of the microsoft.graph.investigationSession entity.
        """
        from .outputs.outputs_request_builder import OutputsRequestBuilder

        return OutputsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def playbook_definition(self) -> PlaybookDefinitionRequestBuilder:
        """
        Provides operations to manage the playbookDefinition property of the microsoft.graph.investigationSession entity.
        """
        from .playbook_definition.playbook_definition_request_builder import PlaybookDefinitionRequestBuilder

        return PlaybookDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InvestigationSessionItemRequestBuilderGetQueryParameters():
        """
        Get an agentic session and poll its processing status. This operation uses the agentic session resource.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class InvestigationSessionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[InvestigationSessionItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

