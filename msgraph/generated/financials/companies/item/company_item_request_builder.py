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
    from ....models import company
    from ....models.o_data_errors import o_data_error
    from .accounts import accounts_request_builder
    from .accounts.item import account_item_request_builder
    from .aged_accounts_payable import aged_accounts_payable_request_builder
    from .aged_accounts_payable.item import aged_accounts_payable_item_request_builder
    from .aged_accounts_receivable import aged_accounts_receivable_request_builder
    from .aged_accounts_receivable.item import aged_accounts_receivable_item_request_builder
    from .company_information import company_information_request_builder
    from .company_information.item import company_information_item_request_builder
    from .countries_regions import countries_regions_request_builder
    from .countries_regions.item import country_region_item_request_builder
    from .currencies import currencies_request_builder
    from .currencies.item import currency_item_request_builder
    from .customer_payment_journals import customer_payment_journals_request_builder
    from .customer_payment_journals.item import customer_payment_journal_item_request_builder
    from .customer_payments import customer_payments_request_builder
    from .customer_payments.item import customer_payment_item_request_builder
    from .customers import customers_request_builder
    from .customers.item import customer_item_request_builder
    from .dimensions import dimensions_request_builder
    from .dimensions.item import dimension_item_request_builder
    from .dimension_values import dimension_values_request_builder
    from .dimension_values.item import dimension_value_item_request_builder
    from .employees import employees_request_builder
    from .employees.item import employee_item_request_builder
    from .general_ledger_entries import general_ledger_entries_request_builder
    from .general_ledger_entries.item import general_ledger_entry_item_request_builder
    from .item_categories import item_categories_request_builder
    from .item_categories.item import item_category_item_request_builder
    from .items import items_request_builder
    from .items.item import item_item_request_builder
    from .journal_lines import journal_lines_request_builder
    from .journal_lines.item import journal_line_item_request_builder
    from .journals import journals_request_builder
    from .journals.item import journal_item_request_builder
    from .payment_methods import payment_methods_request_builder
    from .payment_methods.item import payment_method_item_request_builder
    from .payment_terms import payment_terms_request_builder
    from .payment_terms.item import payment_term_item_request_builder
    from .picture import picture_request_builder
    from .picture.item import picture_item_request_builder
    from .purchase_invoice_lines import purchase_invoice_lines_request_builder
    from .purchase_invoice_lines.item import purchase_invoice_line_item_request_builder
    from .purchase_invoices import purchase_invoices_request_builder
    from .purchase_invoices.item import purchase_invoice_item_request_builder
    from .sales_credit_memo_lines import sales_credit_memo_lines_request_builder
    from .sales_credit_memo_lines.item import sales_credit_memo_line_item_request_builder
    from .sales_credit_memos import sales_credit_memos_request_builder
    from .sales_credit_memos.item import sales_credit_memo_item_request_builder
    from .sales_invoice_lines import sales_invoice_lines_request_builder
    from .sales_invoice_lines.item import sales_invoice_line_item_request_builder
    from .sales_invoices import sales_invoices_request_builder
    from .sales_invoices.item import sales_invoice_item_request_builder
    from .sales_order_lines import sales_order_lines_request_builder
    from .sales_order_lines.item import sales_order_line_item_request_builder
    from .sales_orders import sales_orders_request_builder
    from .sales_orders.item import sales_order_item_request_builder
    from .sales_quote_lines import sales_quote_lines_request_builder
    from .sales_quote_lines.item import sales_quote_line_item_request_builder
    from .sales_quotes import sales_quotes_request_builder
    from .sales_quotes.item import sales_quote_item_request_builder
    from .shipment_methods import shipment_methods_request_builder
    from .shipment_methods.item import shipment_method_item_request_builder
    from .tax_areas import tax_areas_request_builder
    from .tax_areas.item import tax_area_item_request_builder
    from .tax_groups import tax_groups_request_builder
    from .tax_groups.item import tax_group_item_request_builder
    from .units_of_measure import units_of_measure_request_builder
    from .units_of_measure.item import unit_of_measure_item_request_builder
    from .vendors import vendors_request_builder
    from .vendors.item import vendor_item_request_builder

class CompanyItemRequestBuilder():
    """
    Provides operations to manage the companies property of the microsoft.graph.financials entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CompanyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/financials/companies/{company%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def accounts_by_id(self,id: str) -> account_item_request_builder.AccountItemRequestBuilder:
        """
        Provides operations to manage the accounts property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: account_item_request_builder.AccountItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .accounts.item import account_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["account%2Did"] = id
        return account_item_request_builder.AccountItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def aged_accounts_payable_by_id(self,id: str) -> aged_accounts_payable_item_request_builder.AgedAccountsPayableItemRequestBuilder:
        """
        Provides operations to manage the agedAccountsPayable property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: aged_accounts_payable_item_request_builder.AgedAccountsPayableItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .aged_accounts_payable.item import aged_accounts_payable_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agedAccountsPayable%2Did"] = id
        return aged_accounts_payable_item_request_builder.AgedAccountsPayableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def aged_accounts_receivable_by_id(self,id: str) -> aged_accounts_receivable_item_request_builder.AgedAccountsReceivableItemRequestBuilder:
        """
        Provides operations to manage the agedAccountsReceivable property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: aged_accounts_receivable_item_request_builder.AgedAccountsReceivableItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .aged_accounts_receivable.item import aged_accounts_receivable_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agedAccountsReceivable%2Did"] = id
        return aged_accounts_receivable_item_request_builder.AgedAccountsReceivableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def company_information_by_id(self,id: str) -> company_information_item_request_builder.CompanyInformationItemRequestBuilder:
        """
        Provides operations to manage the companyInformation property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: company_information_item_request_builder.CompanyInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .company_information.item import company_information_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["companyInformation%2Did"] = id
        return company_information_item_request_builder.CompanyInformationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def countries_regions_by_id(self,id: str) -> country_region_item_request_builder.CountryRegionItemRequestBuilder:
        """
        Provides operations to manage the countriesRegions property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: country_region_item_request_builder.CountryRegionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .countries_regions.item import country_region_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["countryRegion%2Did"] = id
        return country_region_item_request_builder.CountryRegionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def currencies_by_id(self,id: str) -> currency_item_request_builder.CurrencyItemRequestBuilder:
        """
        Provides operations to manage the currencies property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: currency_item_request_builder.CurrencyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .currencies.item import currency_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["currency%2Did"] = id
        return currency_item_request_builder.CurrencyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def customer_payment_journals_by_id(self,id: str) -> customer_payment_journal_item_request_builder.CustomerPaymentJournalItemRequestBuilder:
        """
        Provides operations to manage the customerPaymentJournals property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: customer_payment_journal_item_request_builder.CustomerPaymentJournalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .customer_payment_journals.item import customer_payment_journal_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["customerPaymentJournal%2Did"] = id
        return customer_payment_journal_item_request_builder.CustomerPaymentJournalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def customer_payments_by_id(self,id: str) -> customer_payment_item_request_builder.CustomerPaymentItemRequestBuilder:
        """
        Provides operations to manage the customerPayments property of the microsoft.graph.company entity.
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
    
    def customers_by_id(self,id: str) -> customer_item_request_builder.CustomerItemRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: customer_item_request_builder.CustomerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .customers.item import customer_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["customer%2Did"] = id
        return customer_item_request_builder.CustomerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def dimensions_by_id(self,id: str) -> dimension_item_request_builder.DimensionItemRequestBuilder:
        """
        Provides operations to manage the dimensions property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: dimension_item_request_builder.DimensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .dimensions.item import dimension_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dimension%2Did"] = id
        return dimension_item_request_builder.DimensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def dimension_values_by_id(self,id: str) -> dimension_value_item_request_builder.DimensionValueItemRequestBuilder:
        """
        Provides operations to manage the dimensionValues property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: dimension_value_item_request_builder.DimensionValueItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .dimension_values.item import dimension_value_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dimensionValue%2Did"] = id
        return dimension_value_item_request_builder.DimensionValueItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def employees_by_id(self,id: str) -> employee_item_request_builder.EmployeeItemRequestBuilder:
        """
        Provides operations to manage the employees property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: employee_item_request_builder.EmployeeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .employees.item import employee_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employee%2Did"] = id
        return employee_item_request_builder.EmployeeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def general_ledger_entries_by_id(self,id: str) -> general_ledger_entry_item_request_builder.GeneralLedgerEntryItemRequestBuilder:
        """
        Provides operations to manage the generalLedgerEntries property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: general_ledger_entry_item_request_builder.GeneralLedgerEntryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .general_ledger_entries.item import general_ledger_entry_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["generalLedgerEntry%2Did"] = id
        return general_ledger_entry_item_request_builder.GeneralLedgerEntryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[CompanyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[company.Company]:
        """
        Get companies from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[company.Company]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import company

        return await self.request_adapter.send_async(request_info, company.Company, error_mapping)
    
    def item_categories_by_id(self,id: str) -> item_category_item_request_builder.ItemCategoryItemRequestBuilder:
        """
        Provides operations to manage the itemCategories property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: item_category_item_request_builder.ItemCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .item_categories.item import item_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemCategory%2Did"] = id
        return item_category_item_request_builder.ItemCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def items_by_id(self,id: str) -> item_item_request_builder.ItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: item_item_request_builder.ItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .items.item import item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["item%2Did"] = id
        return item_item_request_builder.ItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def journal_lines_by_id(self,id: str) -> journal_line_item_request_builder.JournalLineItemRequestBuilder:
        """
        Provides operations to manage the journalLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: journal_line_item_request_builder.JournalLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .journal_lines.item import journal_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["journalLine%2Did"] = id
        return journal_line_item_request_builder.JournalLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def journals_by_id(self,id: str) -> journal_item_request_builder.JournalItemRequestBuilder:
        """
        Provides operations to manage the journals property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: journal_item_request_builder.JournalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .journals.item import journal_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["journal%2Did"] = id
        return journal_item_request_builder.JournalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def payment_methods_by_id(self,id: str) -> payment_method_item_request_builder.PaymentMethodItemRequestBuilder:
        """
        Provides operations to manage the paymentMethods property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: payment_method_item_request_builder.PaymentMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .payment_methods.item import payment_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["paymentMethod%2Did"] = id
        return payment_method_item_request_builder.PaymentMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def payment_terms_by_id(self,id: str) -> payment_term_item_request_builder.PaymentTermItemRequestBuilder:
        """
        Provides operations to manage the paymentTerms property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: payment_term_item_request_builder.PaymentTermItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .payment_terms.item import payment_term_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["paymentTerm%2Did"] = id
        return payment_term_item_request_builder.PaymentTermItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def picture_by_id(self,id: str) -> picture_item_request_builder.PictureItemRequestBuilder:
        """
        Provides operations to manage the picture property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: picture_item_request_builder.PictureItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .picture.item import picture_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["picture%2Did"] = id
        return picture_item_request_builder.PictureItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def purchase_invoice_lines_by_id(self,id: str) -> purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder:
        """
        Provides operations to manage the purchaseInvoiceLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .purchase_invoice_lines.item import purchase_invoice_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["purchaseInvoiceLine%2Did"] = id
        return purchase_invoice_line_item_request_builder.PurchaseInvoiceLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def purchase_invoices_by_id(self,id: str) -> purchase_invoice_item_request_builder.PurchaseInvoiceItemRequestBuilder:
        """
        Provides operations to manage the purchaseInvoices property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: purchase_invoice_item_request_builder.PurchaseInvoiceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .purchase_invoices.item import purchase_invoice_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["purchaseInvoice%2Did"] = id
        return purchase_invoice_item_request_builder.PurchaseInvoiceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_credit_memo_lines_by_id(self,id: str) -> sales_credit_memo_line_item_request_builder.SalesCreditMemoLineItemRequestBuilder:
        """
        Provides operations to manage the salesCreditMemoLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_credit_memo_line_item_request_builder.SalesCreditMemoLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_credit_memo_lines.item import sales_credit_memo_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesCreditMemoLine%2Did"] = id
        return sales_credit_memo_line_item_request_builder.SalesCreditMemoLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_credit_memos_by_id(self,id: str) -> sales_credit_memo_item_request_builder.SalesCreditMemoItemRequestBuilder:
        """
        Provides operations to manage the salesCreditMemos property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_credit_memo_item_request_builder.SalesCreditMemoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_credit_memos.item import sales_credit_memo_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesCreditMemo%2Did"] = id
        return sales_credit_memo_item_request_builder.SalesCreditMemoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_invoice_lines_by_id(self,id: str) -> sales_invoice_line_item_request_builder.SalesInvoiceLineItemRequestBuilder:
        """
        Provides operations to manage the salesInvoiceLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_invoice_line_item_request_builder.SalesInvoiceLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_invoice_lines.item import sales_invoice_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesInvoiceLine%2Did"] = id
        return sales_invoice_line_item_request_builder.SalesInvoiceLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_invoices_by_id(self,id: str) -> sales_invoice_item_request_builder.SalesInvoiceItemRequestBuilder:
        """
        Provides operations to manage the salesInvoices property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_invoice_item_request_builder.SalesInvoiceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_invoices.item import sales_invoice_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesInvoice%2Did"] = id
        return sales_invoice_item_request_builder.SalesInvoiceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_order_lines_by_id(self,id: str) -> sales_order_line_item_request_builder.SalesOrderLineItemRequestBuilder:
        """
        Provides operations to manage the salesOrderLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_order_line_item_request_builder.SalesOrderLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_order_lines.item import sales_order_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesOrderLine%2Did"] = id
        return sales_order_line_item_request_builder.SalesOrderLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_orders_by_id(self,id: str) -> sales_order_item_request_builder.SalesOrderItemRequestBuilder:
        """
        Provides operations to manage the salesOrders property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_order_item_request_builder.SalesOrderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_orders.item import sales_order_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesOrder%2Did"] = id
        return sales_order_item_request_builder.SalesOrderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_quote_lines_by_id(self,id: str) -> sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_quote_lines.item import sales_quote_line_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesQuoteLine%2Did"] = id
        return sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sales_quotes_by_id(self,id: str) -> sales_quote_item_request_builder.SalesQuoteItemRequestBuilder:
        """
        Provides operations to manage the salesQuotes property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_quote_item_request_builder.SalesQuoteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .sales_quotes.item import sales_quote_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesQuote%2Did"] = id
        return sales_quote_item_request_builder.SalesQuoteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shipment_methods_by_id(self,id: str) -> shipment_method_item_request_builder.ShipmentMethodItemRequestBuilder:
        """
        Provides operations to manage the shipmentMethods property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: shipment_method_item_request_builder.ShipmentMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .shipment_methods.item import shipment_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["shipmentMethod%2Did"] = id
        return shipment_method_item_request_builder.ShipmentMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tax_areas_by_id(self,id: str) -> tax_area_item_request_builder.TaxAreaItemRequestBuilder:
        """
        Provides operations to manage the taxAreas property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: tax_area_item_request_builder.TaxAreaItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tax_areas.item import tax_area_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taxArea%2Did"] = id
        return tax_area_item_request_builder.TaxAreaItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tax_groups_by_id(self,id: str) -> tax_group_item_request_builder.TaxGroupItemRequestBuilder:
        """
        Provides operations to manage the taxGroups property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: tax_group_item_request_builder.TaxGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tax_groups.item import tax_group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taxGroup%2Did"] = id
        return tax_group_item_request_builder.TaxGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[CompanyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get companies from financials
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
    
    def units_of_measure_by_id(self,id: str) -> unit_of_measure_item_request_builder.UnitOfMeasureItemRequestBuilder:
        """
        Provides operations to manage the unitsOfMeasure property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: unit_of_measure_item_request_builder.UnitOfMeasureItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .units_of_measure.item import unit_of_measure_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unitOfMeasure%2Did"] = id
        return unit_of_measure_item_request_builder.UnitOfMeasureItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def vendors_by_id(self,id: str) -> vendor_item_request_builder.VendorItemRequestBuilder:
        """
        Provides operations to manage the vendors property of the microsoft.graph.company entity.
        Args:
            id: Unique identifier of the item
        Returns: vendor_item_request_builder.VendorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .vendors.item import vendor_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["vendor%2Did"] = id
        return vendor_item_request_builder.VendorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def accounts(self) -> accounts_request_builder.AccountsRequestBuilder:
        """
        Provides operations to manage the accounts property of the microsoft.graph.company entity.
        """
        from .accounts import accounts_request_builder

        return accounts_request_builder.AccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def aged_accounts_payable(self) -> aged_accounts_payable_request_builder.AgedAccountsPayableRequestBuilder:
        """
        Provides operations to manage the agedAccountsPayable property of the microsoft.graph.company entity.
        """
        from .aged_accounts_payable import aged_accounts_payable_request_builder

        return aged_accounts_payable_request_builder.AgedAccountsPayableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def aged_accounts_receivable(self) -> aged_accounts_receivable_request_builder.AgedAccountsReceivableRequestBuilder:
        """
        Provides operations to manage the agedAccountsReceivable property of the microsoft.graph.company entity.
        """
        from .aged_accounts_receivable import aged_accounts_receivable_request_builder

        return aged_accounts_receivable_request_builder.AgedAccountsReceivableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_information(self) -> company_information_request_builder.CompanyInformationRequestBuilder:
        """
        Provides operations to manage the companyInformation property of the microsoft.graph.company entity.
        """
        from .company_information import company_information_request_builder

        return company_information_request_builder.CompanyInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def countries_regions(self) -> countries_regions_request_builder.CountriesRegionsRequestBuilder:
        """
        Provides operations to manage the countriesRegions property of the microsoft.graph.company entity.
        """
        from .countries_regions import countries_regions_request_builder

        return countries_regions_request_builder.CountriesRegionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def currencies(self) -> currencies_request_builder.CurrenciesRequestBuilder:
        """
        Provides operations to manage the currencies property of the microsoft.graph.company entity.
        """
        from .currencies import currencies_request_builder

        return currencies_request_builder.CurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_payment_journals(self) -> customer_payment_journals_request_builder.CustomerPaymentJournalsRequestBuilder:
        """
        Provides operations to manage the customerPaymentJournals property of the microsoft.graph.company entity.
        """
        from .customer_payment_journals import customer_payment_journals_request_builder

        return customer_payment_journals_request_builder.CustomerPaymentJournalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_payments(self) -> customer_payments_request_builder.CustomerPaymentsRequestBuilder:
        """
        Provides operations to manage the customerPayments property of the microsoft.graph.company entity.
        """
        from .customer_payments import customer_payments_request_builder

        return customer_payments_request_builder.CustomerPaymentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> customers_request_builder.CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.company entity.
        """
        from .customers import customers_request_builder

        return customers_request_builder.CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dimensions(self) -> dimensions_request_builder.DimensionsRequestBuilder:
        """
        Provides operations to manage the dimensions property of the microsoft.graph.company entity.
        """
        from .dimensions import dimensions_request_builder

        return dimensions_request_builder.DimensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dimension_values(self) -> dimension_values_request_builder.DimensionValuesRequestBuilder:
        """
        Provides operations to manage the dimensionValues property of the microsoft.graph.company entity.
        """
        from .dimension_values import dimension_values_request_builder

        return dimension_values_request_builder.DimensionValuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> employees_request_builder.EmployeesRequestBuilder:
        """
        Provides operations to manage the employees property of the microsoft.graph.company entity.
        """
        from .employees import employees_request_builder

        return employees_request_builder.EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def general_ledger_entries(self) -> general_ledger_entries_request_builder.GeneralLedgerEntriesRequestBuilder:
        """
        Provides operations to manage the generalLedgerEntries property of the microsoft.graph.company entity.
        """
        from .general_ledger_entries import general_ledger_entries_request_builder

        return general_ledger_entries_request_builder.GeneralLedgerEntriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_categories(self) -> item_categories_request_builder.ItemCategoriesRequestBuilder:
        """
        Provides operations to manage the itemCategories property of the microsoft.graph.company entity.
        """
        from .item_categories import item_categories_request_builder

        return item_categories_request_builder.ItemCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.company entity.
        """
        from .items import items_request_builder

        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def journal_lines(self) -> journal_lines_request_builder.JournalLinesRequestBuilder:
        """
        Provides operations to manage the journalLines property of the microsoft.graph.company entity.
        """
        from .journal_lines import journal_lines_request_builder

        return journal_lines_request_builder.JournalLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def journals(self) -> journals_request_builder.JournalsRequestBuilder:
        """
        Provides operations to manage the journals property of the microsoft.graph.company entity.
        """
        from .journals import journals_request_builder

        return journals_request_builder.JournalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_methods(self) -> payment_methods_request_builder.PaymentMethodsRequestBuilder:
        """
        Provides operations to manage the paymentMethods property of the microsoft.graph.company entity.
        """
        from .payment_methods import payment_methods_request_builder

        return payment_methods_request_builder.PaymentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_terms(self) -> payment_terms_request_builder.PaymentTermsRequestBuilder:
        """
        Provides operations to manage the paymentTerms property of the microsoft.graph.company entity.
        """
        from .payment_terms import payment_terms_request_builder

        return payment_terms_request_builder.PaymentTermsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def picture(self) -> picture_request_builder.PictureRequestBuilder:
        """
        Provides operations to manage the picture property of the microsoft.graph.company entity.
        """
        from .picture import picture_request_builder

        return picture_request_builder.PictureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purchase_invoice_lines(self) -> purchase_invoice_lines_request_builder.PurchaseInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the purchaseInvoiceLines property of the microsoft.graph.company entity.
        """
        from .purchase_invoice_lines import purchase_invoice_lines_request_builder

        return purchase_invoice_lines_request_builder.PurchaseInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def purchase_invoices(self) -> purchase_invoices_request_builder.PurchaseInvoicesRequestBuilder:
        """
        Provides operations to manage the purchaseInvoices property of the microsoft.graph.company entity.
        """
        from .purchase_invoices import purchase_invoices_request_builder

        return purchase_invoices_request_builder.PurchaseInvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_credit_memo_lines(self) -> sales_credit_memo_lines_request_builder.SalesCreditMemoLinesRequestBuilder:
        """
        Provides operations to manage the salesCreditMemoLines property of the microsoft.graph.company entity.
        """
        from .sales_credit_memo_lines import sales_credit_memo_lines_request_builder

        return sales_credit_memo_lines_request_builder.SalesCreditMemoLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_credit_memos(self) -> sales_credit_memos_request_builder.SalesCreditMemosRequestBuilder:
        """
        Provides operations to manage the salesCreditMemos property of the microsoft.graph.company entity.
        """
        from .sales_credit_memos import sales_credit_memos_request_builder

        return sales_credit_memos_request_builder.SalesCreditMemosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_invoice_lines(self) -> sales_invoice_lines_request_builder.SalesInvoiceLinesRequestBuilder:
        """
        Provides operations to manage the salesInvoiceLines property of the microsoft.graph.company entity.
        """
        from .sales_invoice_lines import sales_invoice_lines_request_builder

        return sales_invoice_lines_request_builder.SalesInvoiceLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_invoices(self) -> sales_invoices_request_builder.SalesInvoicesRequestBuilder:
        """
        Provides operations to manage the salesInvoices property of the microsoft.graph.company entity.
        """
        from .sales_invoices import sales_invoices_request_builder

        return sales_invoices_request_builder.SalesInvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_order_lines(self) -> sales_order_lines_request_builder.SalesOrderLinesRequestBuilder:
        """
        Provides operations to manage the salesOrderLines property of the microsoft.graph.company entity.
        """
        from .sales_order_lines import sales_order_lines_request_builder

        return sales_order_lines_request_builder.SalesOrderLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_orders(self) -> sales_orders_request_builder.SalesOrdersRequestBuilder:
        """
        Provides operations to manage the salesOrders property of the microsoft.graph.company entity.
        """
        from .sales_orders import sales_orders_request_builder

        return sales_orders_request_builder.SalesOrdersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quote_lines(self) -> sales_quote_lines_request_builder.SalesQuoteLinesRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.company entity.
        """
        from .sales_quote_lines import sales_quote_lines_request_builder

        return sales_quote_lines_request_builder.SalesQuoteLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quotes(self) -> sales_quotes_request_builder.SalesQuotesRequestBuilder:
        """
        Provides operations to manage the salesQuotes property of the microsoft.graph.company entity.
        """
        from .sales_quotes import sales_quotes_request_builder

        return sales_quotes_request_builder.SalesQuotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shipment_methods(self) -> shipment_methods_request_builder.ShipmentMethodsRequestBuilder:
        """
        Provides operations to manage the shipmentMethods property of the microsoft.graph.company entity.
        """
        from .shipment_methods import shipment_methods_request_builder

        return shipment_methods_request_builder.ShipmentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tax_areas(self) -> tax_areas_request_builder.TaxAreasRequestBuilder:
        """
        Provides operations to manage the taxAreas property of the microsoft.graph.company entity.
        """
        from .tax_areas import tax_areas_request_builder

        return tax_areas_request_builder.TaxAreasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tax_groups(self) -> tax_groups_request_builder.TaxGroupsRequestBuilder:
        """
        Provides operations to manage the taxGroups property of the microsoft.graph.company entity.
        """
        from .tax_groups import tax_groups_request_builder

        return tax_groups_request_builder.TaxGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def units_of_measure(self) -> units_of_measure_request_builder.UnitsOfMeasureRequestBuilder:
        """
        Provides operations to manage the unitsOfMeasure property of the microsoft.graph.company entity.
        """
        from .units_of_measure import units_of_measure_request_builder

        return units_of_measure_request_builder.UnitsOfMeasureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vendors(self) -> vendors_request_builder.VendorsRequestBuilder:
        """
        Provides operations to manage the vendors property of the microsoft.graph.company entity.
        """
        from .vendors import vendors_request_builder

        return vendors_request_builder.VendorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CompanyItemRequestBuilderGetQueryParameters():
        """
        Get companies from financials
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
    class CompanyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CompanyItemRequestBuilder.CompanyItemRequestBuilderGetQueryParameters] = None

    

