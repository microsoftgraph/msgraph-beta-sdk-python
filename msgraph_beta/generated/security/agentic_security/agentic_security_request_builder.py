from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .playbook_definitions.playbook_definitions_request_builder import PlaybookDefinitionsRequestBuilder
    from .sessions.sessions_request_builder import SessionsRequestBuilder

class AgenticSecurityRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /security/agenticSecurity
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgenticSecurityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/agenticSecurity", path_parameters)
    
    @property
    def playbook_definitions(self) -> PlaybookDefinitionsRequestBuilder:
        """
        Provides operations to manage the playbookDefinitions property of the microsoft.graph.agenticSecurityRoot entity.
        """
        from .playbook_definitions.playbook_definitions_request_builder import PlaybookDefinitionsRequestBuilder

        return PlaybookDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sessions(self) -> SessionsRequestBuilder:
        """
        Provides operations to manage the sessions property of the microsoft.graph.agenticSecurityRoot entity.
        """
        from .sessions.sessions_request_builder import SessionsRequestBuilder

        return SessionsRequestBuilder(self.request_adapter, self.path_parameters)
    

