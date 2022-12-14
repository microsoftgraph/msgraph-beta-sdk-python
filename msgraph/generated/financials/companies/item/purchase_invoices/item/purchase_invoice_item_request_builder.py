from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

currency_request_builder = lazy_import('msgraph.generated.financials.companies.item.purchase_invoices.item.currency.currency_request_builder')
post_request_builder = lazy_import('msgraph.generated.financials.companies.item.purchase_invoices.item.post.post_request_builder')
purchase_invoice_lines_request_builder = lazy_import('msgraph.generated.financials.companies.item.purchase_invoices.item.purchase_invoice_lines.purchase_invoice_lines_request_builder')
purchase_invoice_line_item_request_builder = lazy_import('msgraph.generated.financials.companies.item.purchase_invoices.item.purchase_invoice_lines.item.purchase_invoice_line_item_request_builder')
vendor_request_builder = lazy_import('msgraph.generated.financials.companies.item.purchase_invoices.item.vendor.vendor_request_builder')
purchase_invoice = lazy_import('msgraph.generated.models.purchase_invoice')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class PurchaseInvoiceItemRequestBuilder():
    """
    Provides operations to manage the purchaseInvoices property of the microsoft.graph.company entity.
    """
    @property
    def currency(self) -> currency_request_builder.CurrencyRequestBuilder:
        """
        Provides operations to manage the currency property of the microsoft.graph.purchaseInvoice entity.
        """
        return currency_request_builder.CurrencyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def post(self) -> post_request_builder.PostRequestBuilder:
        """
        Provides operations to call the post method.
        """
        return post_request_builder.PostRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purchase_invoice_lines(self) -> purchase_invoice_lines_request_builder.PurchaseInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the purchaseInvoiceLines property of the microsoft.graph.purchaseInvoice entity.
        """
        return purchase_invoice_lines_request_builder.PurchaseInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vendor(self) -> vendor_request_builder.VendorRequestBuilder:
        """
        Provides operations to manage the vendor property of the microsoft.graph.purchaseInvoice entity.
        """
        return vendor_request_builder.VendorRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PurchaseInvoiceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/financials/companies/{company%2Did}/purchaseInvoices/{purchaseInvoice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[PurchaseInvoiceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get purchaseInvoices from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[purchase_invoice.PurchaseInvoice] = None, request_configuration: Optional[PurchaseInvoiceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property purchaseInvoices in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[PurchaseInvoiceItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[purchase_invoice.PurchaseInvoice]:
        """
        Get purchaseInvoices from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[purchase_invoice.PurchaseInvoice]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, purchase_invoice.PurchaseInvoice, response_handler, error_mapping)
    
    async def patch(self,body: Optional[purchase_invoice.PurchaseInvoice] = None, request_configuration: Optional[PurchaseInvoiceItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[purchase_invoice.PurchaseInvoice]:
        """
        Update the navigation property purchaseInvoices in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[purchase_invoice.PurchaseInvoice]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, purchase_invoice.PurchaseInvoice, response_handler, error_mapping)
    
    def purchase_invoice_lines_by_id(self,id: str) -> purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder:
        """
        Provides operations to manage the purchaseInvoiceLines property of the microsoft.graph.purchaseInvoice entity.
        Args:
            id: Unique identifier of the item
        Returns: purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["purchaseInvoiceLine%2Did"] = id
        return purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class PurchaseInvoiceItemRequestBuilderGetQueryParameters():
        """
        Get purchaseInvoices from financials
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class PurchaseInvoiceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PurchaseInvoiceItemRequestBuilder.PurchaseInvoiceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PurchaseInvoiceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

