from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.identity_governance.workflow import Workflow
    from .......models.o_data_errors.o_data_error import ODataError

class MicrosoftGraphIdentityGovernanceRestoreRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the restore method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftGraphIdentityGovernanceRestoreRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/microsoft.graph.identityGovernance.restore", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[Workflow]:
        """
        Restore a workflow that has been deleted. You can only restore a workflow that was deleted within the last 30 days before Microsoft Entra ID automatically permanently deletes it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workflow]
        Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-restore?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.identity_governance.workflow import Workflow

        return await self.request_adapter.send_async(request_info, Workflow, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Restore a workflow that has been deleted. You can only restore a workflow that was deleted within the last 30 days before Microsoft Entra ID automatically permanently deletes it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> MicrosoftGraphIdentityGovernanceRestoreRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphIdentityGovernanceRestoreRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphIdentityGovernanceRestoreRequestBuilder(self.request_adapter, raw_url)
    

