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
    from ...models.exchange_admin import ExchangeAdmin
    from ...models.o_data_errors.o_data_error import ODataError
    from .mailboxes.mailboxes_request_builder import MailboxesRequestBuilder
    from .message_traces.message_traces_request_builder import MessageTracesRequestBuilder

class ExchangeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the exchange property of the microsoft.graph.admin entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExchangeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/exchange{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property exchange for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]] = None) -> Optional[ExchangeAdmin]:
        """
        A container for the Exchange admin functionality. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExchangeAdmin]
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.exchange_admin import ExchangeAdmin

        return await self.request_adapter.send_async(request_info, ExchangeAdmin, error_mapping)
    
    async def patch(self,body: ExchangeAdmin, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ExchangeAdmin]:
        """
        Update the navigation property exchange in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExchangeAdmin]
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.exchange_admin import ExchangeAdmin

        return await self.request_adapter.send_async(request_info, ExchangeAdmin, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property exchange for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A container for the Exchange admin functionality. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ExchangeAdmin, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property exchange in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ExchangeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExchangeRequestBuilder
        """
        warn("Private preview for Import Export APIs as of 2021-08/PrivatePreview:importExport on 2021-08-19 and will be removed 2021-11-15", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExchangeRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def mailboxes(self) -> MailboxesRequestBuilder:
        """
        Provides operations to manage the mailboxes property of the microsoft.graph.exchangeAdmin entity.
        """
        from .mailboxes.mailboxes_request_builder import MailboxesRequestBuilder

        return MailboxesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_traces(self) -> MessageTracesRequestBuilder:
        """
        Provides operations to manage the messageTraces property of the microsoft.graph.exchangeAdmin entity.
        """
        from .message_traces.message_traces_request_builder import MessageTracesRequestBuilder

        return MessageTracesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ExchangeRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExchangeRequestBuilderGetQueryParameters():
        """
        A container for the Exchange admin functionality. Read-only.
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
    class ExchangeRequestBuilderGetRequestConfiguration(RequestConfiguration[ExchangeRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExchangeRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

