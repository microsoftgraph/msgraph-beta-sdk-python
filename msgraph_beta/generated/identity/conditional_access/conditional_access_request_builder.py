from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_context_class_references.authentication_context_class_references_request_builder import AuthenticationContextClassReferencesRequestBuilder
    from .authentication_strength.authentication_strength_request_builder import AuthenticationStrengthRequestBuilder
    from .authentication_strengths.authentication_strengths_request_builder import AuthenticationStrengthsRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder

class ConditionalAccessRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /identity/conditionalAccess
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConditionalAccessRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/conditionalAccess", path_parameters)
    
    @property
    def authentication_context_class_references(self) -> AuthenticationContextClassReferencesRequestBuilder:
        """
        Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .authentication_context_class_references.authentication_context_class_references_request_builder import AuthenticationContextClassReferencesRequestBuilder

        return AuthenticationContextClassReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strength(self) -> AuthenticationStrengthRequestBuilder:
        """
        Provides operations to manage the authenticationStrength property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .authentication_strength.authentication_strength_request_builder import AuthenticationStrengthRequestBuilder

        return AuthenticationStrengthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strengths(self) -> AuthenticationStrengthsRequestBuilder:
        """
        Provides operations to manage the authenticationStrengths property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .authentication_strengths.authentication_strengths_request_builder import AuthenticationStrengthsRequestBuilder

        return AuthenticationStrengthsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    

