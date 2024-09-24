from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.sales_invoice import SalesInvoice
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .cancel_and_send.cancel_and_send_request_builder import CancelAndSendRequestBuilder
    from .currency.currency_request_builder import CurrencyRequestBuilder
    from .customer.customer_request_builder import CustomerRequestBuilder
    from .payment_term.payment_term_request_builder import PaymentTermRequestBuilder
    from .post.post_request_builder import PostRequestBuilder
    from .post_and_send.post_and_send_request_builder import PostAndSendRequestBuilder
    from .sales_invoice_lines.sales_invoice_lines_request_builder import SalesInvoiceLinesRequestBuilder
    from .send.send_request_builder import SendRequestBuilder
    from .shipment_method.shipment_method_request_builder import ShipmentMethodRequestBuilder

class SalesInvoiceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the salesInvoices property of the microsoft.graph.company entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SalesInvoiceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesInvoices/{salesInvoice%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SalesInvoiceItemRequestBuilderGetQueryParameters]] = None) -> Optional[SalesInvoice]:
        """
        Get salesInvoices from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalesInvoice]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.sales_invoice import SalesInvoice

        return await self.request_adapter.send_async(request_info, SalesInvoice, error_mapping)
    
    async def patch(self,body: SalesInvoice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SalesInvoice]:
        """
        Update the navigation property salesInvoices in financials
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalesInvoice]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.sales_invoice import SalesInvoice

        return await self.request_adapter.send_async(request_info, SalesInvoice, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SalesInvoiceItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get salesInvoices from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SalesInvoice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property salesInvoices in financials
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SalesInvoiceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SalesInvoiceItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SalesInvoiceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel_and_send(self) -> CancelAndSendRequestBuilder:
        """
        Provides operations to call the cancelAndSend method.
        """
        from .cancel_and_send.cancel_and_send_request_builder import CancelAndSendRequestBuilder

        return CancelAndSendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def currency(self) -> CurrencyRequestBuilder:
        """
        Provides operations to manage the currency property of the microsoft.graph.salesInvoice entity.
        """
        from .currency.currency_request_builder import CurrencyRequestBuilder

        return CurrencyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer(self) -> CustomerRequestBuilder:
        """
        Provides operations to manage the customer property of the microsoft.graph.salesInvoice entity.
        """
        from .customer.customer_request_builder import CustomerRequestBuilder

        return CustomerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_term(self) -> PaymentTermRequestBuilder:
        """
        Provides operations to manage the paymentTerm property of the microsoft.graph.salesInvoice entity.
        """
        from .payment_term.payment_term_request_builder import PaymentTermRequestBuilder

        return PaymentTermRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def post_and_send(self) -> PostAndSendRequestBuilder:
        """
        Provides operations to call the postAndSend method.
        """
        from .post_and_send.post_and_send_request_builder import PostAndSendRequestBuilder

        return PostAndSendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def post_path(self) -> PostRequestBuilder:
        """
        Provides operations to call the post method.
        """
        from .post.post_request_builder import PostRequestBuilder

        return PostRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_invoice_lines(self) -> SalesInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the salesInvoiceLines property of the microsoft.graph.salesInvoice entity.
        """
        from .sales_invoice_lines.sales_invoice_lines_request_builder import SalesInvoiceLinesRequestBuilder

        return SalesInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send(self) -> SendRequestBuilder:
        """
        Provides operations to call the send method.
        """
        from .send.send_request_builder import SendRequestBuilder

        return SendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shipment_method(self) -> ShipmentMethodRequestBuilder:
        """
        Provides operations to manage the shipmentMethod property of the microsoft.graph.salesInvoice entity.
        """
        from .shipment_method.shipment_method_request_builder import ShipmentMethodRequestBuilder

        return ShipmentMethodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SalesInvoiceItemRequestBuilderGetQueryParameters():
        """
        Get salesInvoices from financials
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SalesInvoiceItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SalesInvoiceItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SalesInvoiceItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

