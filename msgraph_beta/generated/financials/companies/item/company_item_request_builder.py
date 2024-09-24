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
    from ....models.company import Company
    from ....models.o_data_errors.o_data_error import ODataError
    from .accounts.accounts_request_builder import AccountsRequestBuilder
    from .aged_accounts_payable.aged_accounts_payable_request_builder import AgedAccountsPayableRequestBuilder
    from .aged_accounts_receivable.aged_accounts_receivable_request_builder import AgedAccountsReceivableRequestBuilder
    from .company_information.company_information_request_builder import CompanyInformationRequestBuilder
    from .countries_regions.countries_regions_request_builder import CountriesRegionsRequestBuilder
    from .currencies.currencies_request_builder import CurrenciesRequestBuilder
    from .customers.customers_request_builder import CustomersRequestBuilder
    from .customer_payments.customer_payments_request_builder import CustomerPaymentsRequestBuilder
    from .customer_payment_journals.customer_payment_journals_request_builder import CustomerPaymentJournalsRequestBuilder
    from .dimensions.dimensions_request_builder import DimensionsRequestBuilder
    from .dimension_values.dimension_values_request_builder import DimensionValuesRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .general_ledger_entries.general_ledger_entries_request_builder import GeneralLedgerEntriesRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .item_categories.item_categories_request_builder import ItemCategoriesRequestBuilder
    from .journals.journals_request_builder import JournalsRequestBuilder
    from .journal_lines.journal_lines_request_builder import JournalLinesRequestBuilder
    from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder
    from .payment_terms.payment_terms_request_builder import PaymentTermsRequestBuilder
    from .picture.picture_request_builder import PictureRequestBuilder
    from .purchase_invoices.purchase_invoices_request_builder import PurchaseInvoicesRequestBuilder
    from .purchase_invoice_lines.purchase_invoice_lines_request_builder import PurchaseInvoiceLinesRequestBuilder
    from .sales_credit_memos.sales_credit_memos_request_builder import SalesCreditMemosRequestBuilder
    from .sales_credit_memo_lines.sales_credit_memo_lines_request_builder import SalesCreditMemoLinesRequestBuilder
    from .sales_invoices.sales_invoices_request_builder import SalesInvoicesRequestBuilder
    from .sales_invoice_lines.sales_invoice_lines_request_builder import SalesInvoiceLinesRequestBuilder
    from .sales_orders.sales_orders_request_builder import SalesOrdersRequestBuilder
    from .sales_order_lines.sales_order_lines_request_builder import SalesOrderLinesRequestBuilder
    from .sales_quotes.sales_quotes_request_builder import SalesQuotesRequestBuilder
    from .sales_quote_lines.sales_quote_lines_request_builder import SalesQuoteLinesRequestBuilder
    from .shipment_methods.shipment_methods_request_builder import ShipmentMethodsRequestBuilder
    from .tax_areas.tax_areas_request_builder import TaxAreasRequestBuilder
    from .tax_groups.tax_groups_request_builder import TaxGroupsRequestBuilder
    from .units_of_measure.units_of_measure_request_builder import UnitsOfMeasureRequestBuilder
    from .vendors.vendors_request_builder import VendorsRequestBuilder

class CompanyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the companies property of the microsoft.graph.financials entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CompanyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CompanyItemRequestBuilderGetQueryParameters]] = None) -> Optional[Company]:
        """
        Get companies from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Company]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.company import Company

        return await self.request_adapter.send_async(request_info, Company, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CompanyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get companies from financials
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CompanyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CompanyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CompanyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def accounts(self) -> AccountsRequestBuilder:
        """
        Provides operations to manage the accounts property of the microsoft.graph.company entity.
        """
        from .accounts.accounts_request_builder import AccountsRequestBuilder

        return AccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def aged_accounts_payable(self) -> AgedAccountsPayableRequestBuilder:
        """
        Provides operations to manage the agedAccountsPayable property of the microsoft.graph.company entity.
        """
        from .aged_accounts_payable.aged_accounts_payable_request_builder import AgedAccountsPayableRequestBuilder

        return AgedAccountsPayableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def aged_accounts_receivable(self) -> AgedAccountsReceivableRequestBuilder:
        """
        Provides operations to manage the agedAccountsReceivable property of the microsoft.graph.company entity.
        """
        from .aged_accounts_receivable.aged_accounts_receivable_request_builder import AgedAccountsReceivableRequestBuilder

        return AgedAccountsReceivableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_information(self) -> CompanyInformationRequestBuilder:
        """
        Provides operations to manage the companyInformation property of the microsoft.graph.company entity.
        """
        from .company_information.company_information_request_builder import CompanyInformationRequestBuilder

        return CompanyInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def countries_regions(self) -> CountriesRegionsRequestBuilder:
        """
        Provides operations to manage the countriesRegions property of the microsoft.graph.company entity.
        """
        from .countries_regions.countries_regions_request_builder import CountriesRegionsRequestBuilder

        return CountriesRegionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def currencies(self) -> CurrenciesRequestBuilder:
        """
        Provides operations to manage the currencies property of the microsoft.graph.company entity.
        """
        from .currencies.currencies_request_builder import CurrenciesRequestBuilder

        return CurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_payment_journals(self) -> CustomerPaymentJournalsRequestBuilder:
        """
        Provides operations to manage the customerPaymentJournals property of the microsoft.graph.company entity.
        """
        from .customer_payment_journals.customer_payment_journals_request_builder import CustomerPaymentJournalsRequestBuilder

        return CustomerPaymentJournalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_payments(self) -> CustomerPaymentsRequestBuilder:
        """
        Provides operations to manage the customerPayments property of the microsoft.graph.company entity.
        """
        from .customer_payments.customer_payments_request_builder import CustomerPaymentsRequestBuilder

        return CustomerPaymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.company entity.
        """
        from .customers.customers_request_builder import CustomersRequestBuilder

        return CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dimension_values(self) -> DimensionValuesRequestBuilder:
        """
        Provides operations to manage the dimensionValues property of the microsoft.graph.company entity.
        """
        from .dimension_values.dimension_values_request_builder import DimensionValuesRequestBuilder

        return DimensionValuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dimensions(self) -> DimensionsRequestBuilder:
        """
        Provides operations to manage the dimensions property of the microsoft.graph.company entity.
        """
        from .dimensions.dimensions_request_builder import DimensionsRequestBuilder

        return DimensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        Provides operations to manage the employees property of the microsoft.graph.company entity.
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def general_ledger_entries(self) -> GeneralLedgerEntriesRequestBuilder:
        """
        Provides operations to manage the generalLedgerEntries property of the microsoft.graph.company entity.
        """
        from .general_ledger_entries.general_ledger_entries_request_builder import GeneralLedgerEntriesRequestBuilder

        return GeneralLedgerEntriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_categories(self) -> ItemCategoriesRequestBuilder:
        """
        Provides operations to manage the itemCategories property of the microsoft.graph.company entity.
        """
        from .item_categories.item_categories_request_builder import ItemCategoriesRequestBuilder

        return ItemCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.company entity.
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def journal_lines(self) -> JournalLinesRequestBuilder:
        """
        Provides operations to manage the journalLines property of the microsoft.graph.company entity.
        """
        from .journal_lines.journal_lines_request_builder import JournalLinesRequestBuilder

        return JournalLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def journals(self) -> JournalsRequestBuilder:
        """
        Provides operations to manage the journals property of the microsoft.graph.company entity.
        """
        from .journals.journals_request_builder import JournalsRequestBuilder

        return JournalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_methods(self) -> PaymentMethodsRequestBuilder:
        """
        Provides operations to manage the paymentMethods property of the microsoft.graph.company entity.
        """
        from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder

        return PaymentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_terms(self) -> PaymentTermsRequestBuilder:
        """
        Provides operations to manage the paymentTerms property of the microsoft.graph.company entity.
        """
        from .payment_terms.payment_terms_request_builder import PaymentTermsRequestBuilder

        return PaymentTermsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def picture(self) -> PictureRequestBuilder:
        """
        Provides operations to manage the picture property of the microsoft.graph.company entity.
        """
        from .picture.picture_request_builder import PictureRequestBuilder

        return PictureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purchase_invoice_lines(self) -> PurchaseInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the purchaseInvoiceLines property of the microsoft.graph.company entity.
        """
        from .purchase_invoice_lines.purchase_invoice_lines_request_builder import PurchaseInvoiceLinesRequestBuilder

        return PurchaseInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purchase_invoices(self) -> PurchaseInvoicesRequestBuilder:
        """
        Provides operations to manage the purchaseInvoices property of the microsoft.graph.company entity.
        """
        from .purchase_invoices.purchase_invoices_request_builder import PurchaseInvoicesRequestBuilder

        return PurchaseInvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_credit_memo_lines(self) -> SalesCreditMemoLinesRequestBuilder:
        """
        Provides operations to manage the salesCreditMemoLines property of the microsoft.graph.company entity.
        """
        from .sales_credit_memo_lines.sales_credit_memo_lines_request_builder import SalesCreditMemoLinesRequestBuilder

        return SalesCreditMemoLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_credit_memos(self) -> SalesCreditMemosRequestBuilder:
        """
        Provides operations to manage the salesCreditMemos property of the microsoft.graph.company entity.
        """
        from .sales_credit_memos.sales_credit_memos_request_builder import SalesCreditMemosRequestBuilder

        return SalesCreditMemosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_invoice_lines(self) -> SalesInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the salesInvoiceLines property of the microsoft.graph.company entity.
        """
        from .sales_invoice_lines.sales_invoice_lines_request_builder import SalesInvoiceLinesRequestBuilder

        return SalesInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_invoices(self) -> SalesInvoicesRequestBuilder:
        """
        Provides operations to manage the salesInvoices property of the microsoft.graph.company entity.
        """
        from .sales_invoices.sales_invoices_request_builder import SalesInvoicesRequestBuilder

        return SalesInvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_order_lines(self) -> SalesOrderLinesRequestBuilder:
        """
        Provides operations to manage the salesOrderLines property of the microsoft.graph.company entity.
        """
        from .sales_order_lines.sales_order_lines_request_builder import SalesOrderLinesRequestBuilder

        return SalesOrderLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_orders(self) -> SalesOrdersRequestBuilder:
        """
        Provides operations to manage the salesOrders property of the microsoft.graph.company entity.
        """
        from .sales_orders.sales_orders_request_builder import SalesOrdersRequestBuilder

        return SalesOrdersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quote_lines(self) -> SalesQuoteLinesRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.company entity.
        """
        from .sales_quote_lines.sales_quote_lines_request_builder import SalesQuoteLinesRequestBuilder

        return SalesQuoteLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quotes(self) -> SalesQuotesRequestBuilder:
        """
        Provides operations to manage the salesQuotes property of the microsoft.graph.company entity.
        """
        from .sales_quotes.sales_quotes_request_builder import SalesQuotesRequestBuilder

        return SalesQuotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shipment_methods(self) -> ShipmentMethodsRequestBuilder:
        """
        Provides operations to manage the shipmentMethods property of the microsoft.graph.company entity.
        """
        from .shipment_methods.shipment_methods_request_builder import ShipmentMethodsRequestBuilder

        return ShipmentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tax_areas(self) -> TaxAreasRequestBuilder:
        """
        Provides operations to manage the taxAreas property of the microsoft.graph.company entity.
        """
        from .tax_areas.tax_areas_request_builder import TaxAreasRequestBuilder

        return TaxAreasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tax_groups(self) -> TaxGroupsRequestBuilder:
        """
        Provides operations to manage the taxGroups property of the microsoft.graph.company entity.
        """
        from .tax_groups.tax_groups_request_builder import TaxGroupsRequestBuilder

        return TaxGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def units_of_measure(self) -> UnitsOfMeasureRequestBuilder:
        """
        Provides operations to manage the unitsOfMeasure property of the microsoft.graph.company entity.
        """
        from .units_of_measure.units_of_measure_request_builder import UnitsOfMeasureRequestBuilder

        return UnitsOfMeasureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vendors(self) -> VendorsRequestBuilder:
        """
        Provides operations to manage the vendors property of the microsoft.graph.company entity.
        """
        from .vendors.vendors_request_builder import VendorsRequestBuilder

        return VendorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CompanyItemRequestBuilderGetQueryParameters():
        """
        Get companies from financials
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
    class CompanyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CompanyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

