from __future__ import annotations
from dataclasses import dataclass, field
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
    from ...models.operation_approval_request import OperationApprovalRequest
    from ...models.operation_approval_request_collection_response import OperationApprovalRequestCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .cancel_my_request.cancel_my_request_request_builder import CancelMyRequestRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .item.operation_approval_request_item_request_builder import OperationApprovalRequestItemRequestBuilder
    from .retrieve_my_requests.retrieve_my_requests_request_builder import RetrieveMyRequestsRequestBuilder
    from .retrieve_my_request_by_id_with_id.retrieve_my_request_by_id_with_id_request_builder import RetrieveMyRequestByIdWithIdRequestBuilder
    from .retrieve_request_status.retrieve_request_status_request_builder import RetrieveRequestStatusRequestBuilder

class OperationApprovalRequestsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the operationApprovalRequests property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OperationApprovalRequestsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/operationApprovalRequests{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_operation_approval_request_id(self,operation_approval_request_id: str) -> OperationApprovalRequestItemRequestBuilder:
        """
        Provides operations to manage the operationApprovalRequests property of the microsoft.graph.deviceManagement entity.
        param operation_approval_request_id: The unique identifier of operationApprovalRequest
        Returns: OperationApprovalRequestItemRequestBuilder
        """
        if not operation_approval_request_id:
            raise TypeError("operation_approval_request_id cannot be null.")
        from .item.operation_approval_request_item_request_builder import OperationApprovalRequestItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["operationApprovalRequest%2Did"] = operation_approval_request_id
        return OperationApprovalRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[OperationApprovalRequestCollectionResponse]:
        """
        The Operation Approval Requests
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OperationApprovalRequestCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.operation_approval_request_collection_response import OperationApprovalRequestCollectionResponse

        return await self.request_adapter.send_async(request_info, OperationApprovalRequestCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[OperationApprovalRequest] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[OperationApprovalRequest]:
        """
        Create new navigation property to operationApprovalRequests for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OperationApprovalRequest]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.operation_approval_request import OperationApprovalRequest

        return await self.request_adapter.send_async(request_info, OperationApprovalRequest, error_mapping)
    
    def retrieve_my_request_by_id_with_id(self,id: Optional[str] = None) -> RetrieveMyRequestByIdWithIdRequestBuilder:
        """
        Provides operations to call the retrieveMyRequestById method.
        param id: Usage: id='{id}'
        Returns: RetrieveMyRequestByIdWithIdRequestBuilder
        """
        if not id:
            raise TypeError("id cannot be null.")
        from .retrieve_my_request_by_id_with_id.retrieve_my_request_by_id_with_id_request_builder import RetrieveMyRequestByIdWithIdRequestBuilder

        return RetrieveMyRequestByIdWithIdRequestBuilder(self.request_adapter, self.path_parameters, id)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The Operation Approval Requests
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[OperationApprovalRequest] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to operationApprovalRequests for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> OperationApprovalRequestsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OperationApprovalRequestsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OperationApprovalRequestsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel_my_request(self) -> CancelMyRequestRequestBuilder:
        """
        Provides operations to call the cancelMyRequest method.
        """
        from .cancel_my_request.cancel_my_request_request_builder import CancelMyRequestRequestBuilder

        return CancelMyRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_my_requests(self) -> RetrieveMyRequestsRequestBuilder:
        """
        Provides operations to call the retrieveMyRequests method.
        """
        from .retrieve_my_requests.retrieve_my_requests_request_builder import RetrieveMyRequestsRequestBuilder

        return RetrieveMyRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_request_status(self) -> RetrieveRequestStatusRequestBuilder:
        """
        Provides operations to call the retrieveRequestStatus method.
        """
        from .retrieve_request_status.retrieve_request_status_request_builder import RetrieveRequestStatusRequestBuilder

        return RetrieveRequestStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OperationApprovalRequestsRequestBuilderGetQueryParameters():
        """
        The Operation Approval Requests
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    

