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
    from ......models import customer_payment_journal
    from ......models.o_data_errors import o_data_error
    from .account import account_request_builder
    from .customer_payments import customer_payments_request_builder
    from .customer_payments.item import customer_payment_item_request_builder

class CustomerPaymentJournalItemRequestBuilder():
    """
    Provides operations to manage the customerPaymentJournals property of the microsoft.graph.company entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CustomerPaymentJournalItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/financials/companies/{company%2Did}/customerPaymentJournals/{customerPaymentJournal%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def customer_payments_by_id(self,id: str) -> customer_payment_item_request_builder.CustomerPaymentItemRequestBuilder:
        """
        Provides operations to manage the customerPayments property of the microsoft.graph.customerPaymentJournal entity.
        Args:
            id: Unique identifier of the item
        Returns: customer_payment_item_request_builder.CustomerPaymentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .customer_payments.item import customer_payment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["customerPayment%2Did"] = id
        return customer_payment_item_request_builder.CustomerPaymentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property customerPaymentJournals for financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderGetRequestConfiguration] = None) -> Optional[customer_payment_journal.CustomerPaymentJournal]:
        """
        Get customerPaymentJournals from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[customer_payment_journal.CustomerPaymentJournal]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import customer_payment_journal

        return await self.request_adapter.send_async(request_info, customer_payment_journal.CustomerPaymentJournal, error_mapping)
    
    async def patch(self,body: Optional[customer_payment_journal.CustomerPaymentJournal] = None, request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[customer_payment_journal.CustomerPaymentJournal]:
        """
        Update the navigation property customerPaymentJournals in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[customer_payment_journal.CustomerPaymentJournal]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import customer_payment_journal

        return await self.request_adapter.send_async(request_info, customer_payment_journal.CustomerPaymentJournal, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property customerPaymentJournals for financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get customerPaymentJournals from financials
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
    
    def to_patch_request_information(self,body: Optional[customer_payment_journal.CustomerPaymentJournal] = None, request_configuration: Optional[CustomerPaymentJournalItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property customerPaymentJournals in financials
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def account(self) -> account_request_builder.AccountRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.customerPaymentJournal entity.
        """
        from .account import account_request_builder

        return account_request_builder.AccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_payments(self) -> customer_payments_request_builder.CustomerPaymentsRequestBuilder:
        """
        Provides operations to manage the customerPayments property of the microsoft.graph.customerPaymentJournal entity.
        """
        from .customer_payments import customer_payments_request_builder

        return customer_payments_request_builder.CustomerPaymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CustomerPaymentJournalItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CustomerPaymentJournalItemRequestBuilderGetQueryParameters():
        """
        Get customerPaymentJournals from financials
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
    class CustomerPaymentJournalItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CustomerPaymentJournalItemRequestBuilder.CustomerPaymentJournalItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CustomerPaymentJournalItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

