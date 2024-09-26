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
    from ......models.sales_quote import SalesQuote
    from .currency.currency_request_builder import CurrencyRequestBuilder
    from .customer.customer_request_builder import CustomerRequestBuilder
    from .make_invoice.make_invoice_request_builder import MakeInvoiceRequestBuilder
    from .payment_term.payment_term_request_builder import PaymentTermRequestBuilder
    from .sales_quote_lines.sales_quote_lines_request_builder import SalesQuoteLinesRequestBuilder
    from .send.send_request_builder import SendRequestBuilder
    from .shipment_method.shipment_method_request_builder import ShipmentMethodRequestBuilder

class SalesQuoteItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the salesQuotes property of the microsoft.graph.company entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SalesQuoteItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesQuotes/{salesQuote%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SalesQuoteItemRequestBuilderGetQueryParameters]] = None) -> Optional[SalesQuote]:
        """
        Get salesQuotes from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalesQuote]
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
        from ......models.sales_quote import SalesQuote

        return await self.request_adapter.send_async(request_info, SalesQuote, error_mapping)
    
    async def patch(self,body: SalesQuote, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SalesQuote]:
        """
        Update the navigation property salesQuotes in financials
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SalesQuote]
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
        from ......models.sales_quote import SalesQuote

        return await self.request_adapter.send_async(request_info, SalesQuote, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SalesQuoteItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get salesQuotes from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SalesQuote, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property salesQuotes in financials
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
    
    def with_url(self,raw_url: str) -> SalesQuoteItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SalesQuoteItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SalesQuoteItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def currency(self) -> CurrencyRequestBuilder:
        """
        Provides operations to manage the currency property of the microsoft.graph.salesQuote entity.
        """
        from .currency.currency_request_builder import CurrencyRequestBuilder

        return CurrencyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer(self) -> CustomerRequestBuilder:
        """
        Provides operations to manage the customer property of the microsoft.graph.salesQuote entity.
        """
        from .customer.customer_request_builder import CustomerRequestBuilder

        return CustomerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def make_invoice(self) -> MakeInvoiceRequestBuilder:
        """
        Provides operations to call the makeInvoice method.
        """
        from .make_invoice.make_invoice_request_builder import MakeInvoiceRequestBuilder

        return MakeInvoiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_term(self) -> PaymentTermRequestBuilder:
        """
        Provides operations to manage the paymentTerm property of the microsoft.graph.salesQuote entity.
        """
        from .payment_term.payment_term_request_builder import PaymentTermRequestBuilder

        return PaymentTermRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quote_lines(self) -> SalesQuoteLinesRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.salesQuote entity.
        """
        from .sales_quote_lines.sales_quote_lines_request_builder import SalesQuoteLinesRequestBuilder

        return SalesQuoteLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
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
        Provides operations to manage the shipmentMethod property of the microsoft.graph.salesQuote entity.
        """
        from .shipment_method.shipment_method_request_builder import ShipmentMethodRequestBuilder

        return ShipmentMethodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SalesQuoteItemRequestBuilderGetQueryParameters():
        """
        Get salesQuotes from financials
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
    class SalesQuoteItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SalesQuoteItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SalesQuoteItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

