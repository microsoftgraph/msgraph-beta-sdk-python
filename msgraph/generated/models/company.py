from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account, aged_accounts_payable, aged_accounts_receivable, company_information, country_region, currency, customer, customer_payment, customer_payment_journal, dimension, dimension_value, employee, entity, general_ledger_entry, item, item_category, journal, journal_line, payment_method, payment_term, picture, purchase_invoice, purchase_invoice_line, sales_credit_memo, sales_credit_memo_line, sales_invoice, sales_invoice_line, sales_order, sales_order_line, sales_quote, sales_quote_line, shipment_method, tax_area, tax_group, unit_of_measure, vendor

from . import entity

class Company(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Company and sets the default values.
        """
        super().__init__()
        # The accounts property
        self._accounts: Optional[List[account.Account]] = None
        # The agedAccountsPayable property
        self._aged_accounts_payable: Optional[List[aged_accounts_payable.AgedAccountsPayable]] = None
        # The agedAccountsReceivable property
        self._aged_accounts_receivable: Optional[List[aged_accounts_receivable.AgedAccountsReceivable]] = None
        # The businessProfileId property
        self._business_profile_id: Optional[str] = None
        # The companyInformation property
        self._company_information: Optional[List[company_information.CompanyInformation]] = None
        # The countriesRegions property
        self._countries_regions: Optional[List[country_region.CountryRegion]] = None
        # The currencies property
        self._currencies: Optional[List[currency.Currency]] = None
        # The customerPaymentJournals property
        self._customer_payment_journals: Optional[List[customer_payment_journal.CustomerPaymentJournal]] = None
        # The customerPayments property
        self._customer_payments: Optional[List[customer_payment.CustomerPayment]] = None
        # The customers property
        self._customers: Optional[List[customer.Customer]] = None
        # The dimensionValues property
        self._dimension_values: Optional[List[dimension_value.DimensionValue]] = None
        # The dimensions property
        self._dimensions: Optional[List[dimension.Dimension]] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The employees property
        self._employees: Optional[List[employee.Employee]] = None
        # The generalLedgerEntries property
        self._general_ledger_entries: Optional[List[general_ledger_entry.GeneralLedgerEntry]] = None
        # The itemCategories property
        self._item_categories: Optional[List[item_category.ItemCategory]] = None
        # The items property
        self._items: Optional[List[item.Item]] = None
        # The journalLines property
        self._journal_lines: Optional[List[journal_line.JournalLine]] = None
        # The journals property
        self._journals: Optional[List[journal.Journal]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The paymentMethods property
        self._payment_methods: Optional[List[payment_method.PaymentMethod]] = None
        # The paymentTerms property
        self._payment_terms: Optional[List[payment_term.PaymentTerm]] = None
        # The picture property
        self._picture: Optional[List[picture.Picture]] = None
        # The purchaseInvoiceLines property
        self._purchase_invoice_lines: Optional[List[purchase_invoice_line.PurchaseInvoiceLine]] = None
        # The purchaseInvoices property
        self._purchase_invoices: Optional[List[purchase_invoice.PurchaseInvoice]] = None
        # The salesCreditMemoLines property
        self._sales_credit_memo_lines: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None
        # The salesCreditMemos property
        self._sales_credit_memos: Optional[List[sales_credit_memo.SalesCreditMemo]] = None
        # The salesInvoiceLines property
        self._sales_invoice_lines: Optional[List[sales_invoice_line.SalesInvoiceLine]] = None
        # The salesInvoices property
        self._sales_invoices: Optional[List[sales_invoice.SalesInvoice]] = None
        # The salesOrderLines property
        self._sales_order_lines: Optional[List[sales_order_line.SalesOrderLine]] = None
        # The salesOrders property
        self._sales_orders: Optional[List[sales_order.SalesOrder]] = None
        # The salesQuoteLines property
        self._sales_quote_lines: Optional[List[sales_quote_line.SalesQuoteLine]] = None
        # The salesQuotes property
        self._sales_quotes: Optional[List[sales_quote.SalesQuote]] = None
        # The shipmentMethods property
        self._shipment_methods: Optional[List[shipment_method.ShipmentMethod]] = None
        # The systemVersion property
        self._system_version: Optional[str] = None
        # The taxAreas property
        self._tax_areas: Optional[List[tax_area.TaxArea]] = None
        # The taxGroups property
        self._tax_groups: Optional[List[tax_group.TaxGroup]] = None
        # The unitsOfMeasure property
        self._units_of_measure: Optional[List[unit_of_measure.UnitOfMeasure]] = None
        # The vendors property
        self._vendors: Optional[List[vendor.Vendor]] = None
    
    @property
    def accounts(self,) -> Optional[List[account.Account]]:
        """
        Gets the accounts property value. The accounts property
        Returns: Optional[List[account.Account]]
        """
        return self._accounts
    
    @accounts.setter
    def accounts(self,value: Optional[List[account.Account]] = None) -> None:
        """
        Sets the accounts property value. The accounts property
        Args:
            value: Value to set for the accounts property.
        """
        self._accounts = value
    
    @property
    def aged_accounts_payable(self,) -> Optional[List[aged_accounts_payable.AgedAccountsPayable]]:
        """
        Gets the agedAccountsPayable property value. The agedAccountsPayable property
        Returns: Optional[List[aged_accounts_payable.AgedAccountsPayable]]
        """
        return self._aged_accounts_payable
    
    @aged_accounts_payable.setter
    def aged_accounts_payable(self,value: Optional[List[aged_accounts_payable.AgedAccountsPayable]] = None) -> None:
        """
        Sets the agedAccountsPayable property value. The agedAccountsPayable property
        Args:
            value: Value to set for the aged_accounts_payable property.
        """
        self._aged_accounts_payable = value
    
    @property
    def aged_accounts_receivable(self,) -> Optional[List[aged_accounts_receivable.AgedAccountsReceivable]]:
        """
        Gets the agedAccountsReceivable property value. The agedAccountsReceivable property
        Returns: Optional[List[aged_accounts_receivable.AgedAccountsReceivable]]
        """
        return self._aged_accounts_receivable
    
    @aged_accounts_receivable.setter
    def aged_accounts_receivable(self,value: Optional[List[aged_accounts_receivable.AgedAccountsReceivable]] = None) -> None:
        """
        Sets the agedAccountsReceivable property value. The agedAccountsReceivable property
        Args:
            value: Value to set for the aged_accounts_receivable property.
        """
        self._aged_accounts_receivable = value
    
    @property
    def business_profile_id(self,) -> Optional[str]:
        """
        Gets the businessProfileId property value. The businessProfileId property
        Returns: Optional[str]
        """
        return self._business_profile_id
    
    @business_profile_id.setter
    def business_profile_id(self,value: Optional[str] = None) -> None:
        """
        Sets the businessProfileId property value. The businessProfileId property
        Args:
            value: Value to set for the business_profile_id property.
        """
        self._business_profile_id = value
    
    @property
    def company_information(self,) -> Optional[List[company_information.CompanyInformation]]:
        """
        Gets the companyInformation property value. The companyInformation property
        Returns: Optional[List[company_information.CompanyInformation]]
        """
        return self._company_information
    
    @company_information.setter
    def company_information(self,value: Optional[List[company_information.CompanyInformation]] = None) -> None:
        """
        Sets the companyInformation property value. The companyInformation property
        Args:
            value: Value to set for the company_information property.
        """
        self._company_information = value
    
    @property
    def countries_regions(self,) -> Optional[List[country_region.CountryRegion]]:
        """
        Gets the countriesRegions property value. The countriesRegions property
        Returns: Optional[List[country_region.CountryRegion]]
        """
        return self._countries_regions
    
    @countries_regions.setter
    def countries_regions(self,value: Optional[List[country_region.CountryRegion]] = None) -> None:
        """
        Sets the countriesRegions property value. The countriesRegions property
        Args:
            value: Value to set for the countries_regions property.
        """
        self._countries_regions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Company:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Company
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Company()
    
    @property
    def currencies(self,) -> Optional[List[currency.Currency]]:
        """
        Gets the currencies property value. The currencies property
        Returns: Optional[List[currency.Currency]]
        """
        return self._currencies
    
    @currencies.setter
    def currencies(self,value: Optional[List[currency.Currency]] = None) -> None:
        """
        Sets the currencies property value. The currencies property
        Args:
            value: Value to set for the currencies property.
        """
        self._currencies = value
    
    @property
    def customer_payment_journals(self,) -> Optional[List[customer_payment_journal.CustomerPaymentJournal]]:
        """
        Gets the customerPaymentJournals property value. The customerPaymentJournals property
        Returns: Optional[List[customer_payment_journal.CustomerPaymentJournal]]
        """
        return self._customer_payment_journals
    
    @customer_payment_journals.setter
    def customer_payment_journals(self,value: Optional[List[customer_payment_journal.CustomerPaymentJournal]] = None) -> None:
        """
        Sets the customerPaymentJournals property value. The customerPaymentJournals property
        Args:
            value: Value to set for the customer_payment_journals property.
        """
        self._customer_payment_journals = value
    
    @property
    def customer_payments(self,) -> Optional[List[customer_payment.CustomerPayment]]:
        """
        Gets the customerPayments property value. The customerPayments property
        Returns: Optional[List[customer_payment.CustomerPayment]]
        """
        return self._customer_payments
    
    @customer_payments.setter
    def customer_payments(self,value: Optional[List[customer_payment.CustomerPayment]] = None) -> None:
        """
        Sets the customerPayments property value. The customerPayments property
        Args:
            value: Value to set for the customer_payments property.
        """
        self._customer_payments = value
    
    @property
    def customers(self,) -> Optional[List[customer.Customer]]:
        """
        Gets the customers property value. The customers property
        Returns: Optional[List[customer.Customer]]
        """
        return self._customers
    
    @customers.setter
    def customers(self,value: Optional[List[customer.Customer]] = None) -> None:
        """
        Sets the customers property value. The customers property
        Args:
            value: Value to set for the customers property.
        """
        self._customers = value
    
    @property
    def dimension_values(self,) -> Optional[List[dimension_value.DimensionValue]]:
        """
        Gets the dimensionValues property value. The dimensionValues property
        Returns: Optional[List[dimension_value.DimensionValue]]
        """
        return self._dimension_values
    
    @dimension_values.setter
    def dimension_values(self,value: Optional[List[dimension_value.DimensionValue]] = None) -> None:
        """
        Sets the dimensionValues property value. The dimensionValues property
        Args:
            value: Value to set for the dimension_values property.
        """
        self._dimension_values = value
    
    @property
    def dimensions(self,) -> Optional[List[dimension.Dimension]]:
        """
        Gets the dimensions property value. The dimensions property
        Returns: Optional[List[dimension.Dimension]]
        """
        return self._dimensions
    
    @dimensions.setter
    def dimensions(self,value: Optional[List[dimension.Dimension]] = None) -> None:
        """
        Sets the dimensions property value. The dimensions property
        Args:
            value: Value to set for the dimensions property.
        """
        self._dimensions = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def employees(self,) -> Optional[List[employee.Employee]]:
        """
        Gets the employees property value. The employees property
        Returns: Optional[List[employee.Employee]]
        """
        return self._employees
    
    @employees.setter
    def employees(self,value: Optional[List[employee.Employee]] = None) -> None:
        """
        Sets the employees property value. The employees property
        Args:
            value: Value to set for the employees property.
        """
        self._employees = value
    
    @property
    def general_ledger_entries(self,) -> Optional[List[general_ledger_entry.GeneralLedgerEntry]]:
        """
        Gets the generalLedgerEntries property value. The generalLedgerEntries property
        Returns: Optional[List[general_ledger_entry.GeneralLedgerEntry]]
        """
        return self._general_ledger_entries
    
    @general_ledger_entries.setter
    def general_ledger_entries(self,value: Optional[List[general_ledger_entry.GeneralLedgerEntry]] = None) -> None:
        """
        Sets the generalLedgerEntries property value. The generalLedgerEntries property
        Args:
            value: Value to set for the general_ledger_entries property.
        """
        self._general_ledger_entries = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account, aged_accounts_payable, aged_accounts_receivable, company_information, country_region, currency, customer, customer_payment, customer_payment_journal, dimension, dimension_value, employee, entity, general_ledger_entry, item, item_category, journal, journal_line, payment_method, payment_term, picture, purchase_invoice, purchase_invoice_line, sales_credit_memo, sales_credit_memo_line, sales_invoice, sales_invoice_line, sales_order, sales_order_line, sales_quote, sales_quote_line, shipment_method, tax_area, tax_group, unit_of_measure, vendor

        fields: Dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(account.Account)),
            "agedAccountsPayable": lambda n : setattr(self, 'aged_accounts_payable', n.get_collection_of_object_values(aged_accounts_payable.AgedAccountsPayable)),
            "agedAccountsReceivable": lambda n : setattr(self, 'aged_accounts_receivable', n.get_collection_of_object_values(aged_accounts_receivable.AgedAccountsReceivable)),
            "businessProfileId": lambda n : setattr(self, 'business_profile_id', n.get_str_value()),
            "companyInformation": lambda n : setattr(self, 'company_information', n.get_collection_of_object_values(company_information.CompanyInformation)),
            "countriesRegions": lambda n : setattr(self, 'countries_regions', n.get_collection_of_object_values(country_region.CountryRegion)),
            "currencies": lambda n : setattr(self, 'currencies', n.get_collection_of_object_values(currency.Currency)),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(customer.Customer)),
            "customerPayments": lambda n : setattr(self, 'customer_payments', n.get_collection_of_object_values(customer_payment.CustomerPayment)),
            "customerPaymentJournals": lambda n : setattr(self, 'customer_payment_journals', n.get_collection_of_object_values(customer_payment_journal.CustomerPaymentJournal)),
            "dimensions": lambda n : setattr(self, 'dimensions', n.get_collection_of_object_values(dimension.Dimension)),
            "dimensionValues": lambda n : setattr(self, 'dimension_values', n.get_collection_of_object_values(dimension_value.DimensionValue)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(employee.Employee)),
            "generalLedgerEntries": lambda n : setattr(self, 'general_ledger_entries', n.get_collection_of_object_values(general_ledger_entry.GeneralLedgerEntry)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(item.Item)),
            "itemCategories": lambda n : setattr(self, 'item_categories', n.get_collection_of_object_values(item_category.ItemCategory)),
            "journals": lambda n : setattr(self, 'journals', n.get_collection_of_object_values(journal.Journal)),
            "journalLines": lambda n : setattr(self, 'journal_lines', n.get_collection_of_object_values(journal_line.JournalLine)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "paymentMethods": lambda n : setattr(self, 'payment_methods', n.get_collection_of_object_values(payment_method.PaymentMethod)),
            "paymentTerms": lambda n : setattr(self, 'payment_terms', n.get_collection_of_object_values(payment_term.PaymentTerm)),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(picture.Picture)),
            "purchaseInvoices": lambda n : setattr(self, 'purchase_invoices', n.get_collection_of_object_values(purchase_invoice.PurchaseInvoice)),
            "purchaseInvoiceLines": lambda n : setattr(self, 'purchase_invoice_lines', n.get_collection_of_object_values(purchase_invoice_line.PurchaseInvoiceLine)),
            "salesCreditMemos": lambda n : setattr(self, 'sales_credit_memos', n.get_collection_of_object_values(sales_credit_memo.SalesCreditMemo)),
            "salesCreditMemoLines": lambda n : setattr(self, 'sales_credit_memo_lines', n.get_collection_of_object_values(sales_credit_memo_line.SalesCreditMemoLine)),
            "salesInvoices": lambda n : setattr(self, 'sales_invoices', n.get_collection_of_object_values(sales_invoice.SalesInvoice)),
            "salesInvoiceLines": lambda n : setattr(self, 'sales_invoice_lines', n.get_collection_of_object_values(sales_invoice_line.SalesInvoiceLine)),
            "salesOrders": lambda n : setattr(self, 'sales_orders', n.get_collection_of_object_values(sales_order.SalesOrder)),
            "salesOrderLines": lambda n : setattr(self, 'sales_order_lines', n.get_collection_of_object_values(sales_order_line.SalesOrderLine)),
            "salesQuotes": lambda n : setattr(self, 'sales_quotes', n.get_collection_of_object_values(sales_quote.SalesQuote)),
            "salesQuoteLines": lambda n : setattr(self, 'sales_quote_lines', n.get_collection_of_object_values(sales_quote_line.SalesQuoteLine)),
            "shipmentMethods": lambda n : setattr(self, 'shipment_methods', n.get_collection_of_object_values(shipment_method.ShipmentMethod)),
            "systemVersion": lambda n : setattr(self, 'system_version', n.get_str_value()),
            "taxAreas": lambda n : setattr(self, 'tax_areas', n.get_collection_of_object_values(tax_area.TaxArea)),
            "taxGroups": lambda n : setattr(self, 'tax_groups', n.get_collection_of_object_values(tax_group.TaxGroup)),
            "unitsOfMeasure": lambda n : setattr(self, 'units_of_measure', n.get_collection_of_object_values(unit_of_measure.UnitOfMeasure)),
            "vendors": lambda n : setattr(self, 'vendors', n.get_collection_of_object_values(vendor.Vendor)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item_categories(self,) -> Optional[List[item_category.ItemCategory]]:
        """
        Gets the itemCategories property value. The itemCategories property
        Returns: Optional[List[item_category.ItemCategory]]
        """
        return self._item_categories
    
    @item_categories.setter
    def item_categories(self,value: Optional[List[item_category.ItemCategory]] = None) -> None:
        """
        Sets the itemCategories property value. The itemCategories property
        Args:
            value: Value to set for the item_categories property.
        """
        self._item_categories = value
    
    @property
    def items(self,) -> Optional[List[item.Item]]:
        """
        Gets the items property value. The items property
        Returns: Optional[List[item.Item]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[item.Item]] = None) -> None:
        """
        Sets the items property value. The items property
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def journal_lines(self,) -> Optional[List[journal_line.JournalLine]]:
        """
        Gets the journalLines property value. The journalLines property
        Returns: Optional[List[journal_line.JournalLine]]
        """
        return self._journal_lines
    
    @journal_lines.setter
    def journal_lines(self,value: Optional[List[journal_line.JournalLine]] = None) -> None:
        """
        Sets the journalLines property value. The journalLines property
        Args:
            value: Value to set for the journal_lines property.
        """
        self._journal_lines = value
    
    @property
    def journals(self,) -> Optional[List[journal.Journal]]:
        """
        Gets the journals property value. The journals property
        Returns: Optional[List[journal.Journal]]
        """
        return self._journals
    
    @journals.setter
    def journals(self,value: Optional[List[journal.Journal]] = None) -> None:
        """
        Sets the journals property value. The journals property
        Args:
            value: Value to set for the journals property.
        """
        self._journals = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def payment_methods(self,) -> Optional[List[payment_method.PaymentMethod]]:
        """
        Gets the paymentMethods property value. The paymentMethods property
        Returns: Optional[List[payment_method.PaymentMethod]]
        """
        return self._payment_methods
    
    @payment_methods.setter
    def payment_methods(self,value: Optional[List[payment_method.PaymentMethod]] = None) -> None:
        """
        Sets the paymentMethods property value. The paymentMethods property
        Args:
            value: Value to set for the payment_methods property.
        """
        self._payment_methods = value
    
    @property
    def payment_terms(self,) -> Optional[List[payment_term.PaymentTerm]]:
        """
        Gets the paymentTerms property value. The paymentTerms property
        Returns: Optional[List[payment_term.PaymentTerm]]
        """
        return self._payment_terms
    
    @payment_terms.setter
    def payment_terms(self,value: Optional[List[payment_term.PaymentTerm]] = None) -> None:
        """
        Sets the paymentTerms property value. The paymentTerms property
        Args:
            value: Value to set for the payment_terms property.
        """
        self._payment_terms = value
    
    @property
    def picture(self,) -> Optional[List[picture.Picture]]:
        """
        Gets the picture property value. The picture property
        Returns: Optional[List[picture.Picture]]
        """
        return self._picture
    
    @picture.setter
    def picture(self,value: Optional[List[picture.Picture]] = None) -> None:
        """
        Sets the picture property value. The picture property
        Args:
            value: Value to set for the picture property.
        """
        self._picture = value
    
    @property
    def purchase_invoice_lines(self,) -> Optional[List[purchase_invoice_line.PurchaseInvoiceLine]]:
        """
        Gets the purchaseInvoiceLines property value. The purchaseInvoiceLines property
        Returns: Optional[List[purchase_invoice_line.PurchaseInvoiceLine]]
        """
        return self._purchase_invoice_lines
    
    @purchase_invoice_lines.setter
    def purchase_invoice_lines(self,value: Optional[List[purchase_invoice_line.PurchaseInvoiceLine]] = None) -> None:
        """
        Sets the purchaseInvoiceLines property value. The purchaseInvoiceLines property
        Args:
            value: Value to set for the purchase_invoice_lines property.
        """
        self._purchase_invoice_lines = value
    
    @property
    def purchase_invoices(self,) -> Optional[List[purchase_invoice.PurchaseInvoice]]:
        """
        Gets the purchaseInvoices property value. The purchaseInvoices property
        Returns: Optional[List[purchase_invoice.PurchaseInvoice]]
        """
        return self._purchase_invoices
    
    @purchase_invoices.setter
    def purchase_invoices(self,value: Optional[List[purchase_invoice.PurchaseInvoice]] = None) -> None:
        """
        Sets the purchaseInvoices property value. The purchaseInvoices property
        Args:
            value: Value to set for the purchase_invoices property.
        """
        self._purchase_invoices = value
    
    @property
    def sales_credit_memo_lines(self,) -> Optional[List[sales_credit_memo_line.SalesCreditMemoLine]]:
        """
        Gets the salesCreditMemoLines property value. The salesCreditMemoLines property
        Returns: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]]
        """
        return self._sales_credit_memo_lines
    
    @sales_credit_memo_lines.setter
    def sales_credit_memo_lines(self,value: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None) -> None:
        """
        Sets the salesCreditMemoLines property value. The salesCreditMemoLines property
        Args:
            value: Value to set for the sales_credit_memo_lines property.
        """
        self._sales_credit_memo_lines = value
    
    @property
    def sales_credit_memos(self,) -> Optional[List[sales_credit_memo.SalesCreditMemo]]:
        """
        Gets the salesCreditMemos property value. The salesCreditMemos property
        Returns: Optional[List[sales_credit_memo.SalesCreditMemo]]
        """
        return self._sales_credit_memos
    
    @sales_credit_memos.setter
    def sales_credit_memos(self,value: Optional[List[sales_credit_memo.SalesCreditMemo]] = None) -> None:
        """
        Sets the salesCreditMemos property value. The salesCreditMemos property
        Args:
            value: Value to set for the sales_credit_memos property.
        """
        self._sales_credit_memos = value
    
    @property
    def sales_invoice_lines(self,) -> Optional[List[sales_invoice_line.SalesInvoiceLine]]:
        """
        Gets the salesInvoiceLines property value. The salesInvoiceLines property
        Returns: Optional[List[sales_invoice_line.SalesInvoiceLine]]
        """
        return self._sales_invoice_lines
    
    @sales_invoice_lines.setter
    def sales_invoice_lines(self,value: Optional[List[sales_invoice_line.SalesInvoiceLine]] = None) -> None:
        """
        Sets the salesInvoiceLines property value. The salesInvoiceLines property
        Args:
            value: Value to set for the sales_invoice_lines property.
        """
        self._sales_invoice_lines = value
    
    @property
    def sales_invoices(self,) -> Optional[List[sales_invoice.SalesInvoice]]:
        """
        Gets the salesInvoices property value. The salesInvoices property
        Returns: Optional[List[sales_invoice.SalesInvoice]]
        """
        return self._sales_invoices
    
    @sales_invoices.setter
    def sales_invoices(self,value: Optional[List[sales_invoice.SalesInvoice]] = None) -> None:
        """
        Sets the salesInvoices property value. The salesInvoices property
        Args:
            value: Value to set for the sales_invoices property.
        """
        self._sales_invoices = value
    
    @property
    def sales_order_lines(self,) -> Optional[List[sales_order_line.SalesOrderLine]]:
        """
        Gets the salesOrderLines property value. The salesOrderLines property
        Returns: Optional[List[sales_order_line.SalesOrderLine]]
        """
        return self._sales_order_lines
    
    @sales_order_lines.setter
    def sales_order_lines(self,value: Optional[List[sales_order_line.SalesOrderLine]] = None) -> None:
        """
        Sets the salesOrderLines property value. The salesOrderLines property
        Args:
            value: Value to set for the sales_order_lines property.
        """
        self._sales_order_lines = value
    
    @property
    def sales_orders(self,) -> Optional[List[sales_order.SalesOrder]]:
        """
        Gets the salesOrders property value. The salesOrders property
        Returns: Optional[List[sales_order.SalesOrder]]
        """
        return self._sales_orders
    
    @sales_orders.setter
    def sales_orders(self,value: Optional[List[sales_order.SalesOrder]] = None) -> None:
        """
        Sets the salesOrders property value. The salesOrders property
        Args:
            value: Value to set for the sales_orders property.
        """
        self._sales_orders = value
    
    @property
    def sales_quote_lines(self,) -> Optional[List[sales_quote_line.SalesQuoteLine]]:
        """
        Gets the salesQuoteLines property value. The salesQuoteLines property
        Returns: Optional[List[sales_quote_line.SalesQuoteLine]]
        """
        return self._sales_quote_lines
    
    @sales_quote_lines.setter
    def sales_quote_lines(self,value: Optional[List[sales_quote_line.SalesQuoteLine]] = None) -> None:
        """
        Sets the salesQuoteLines property value. The salesQuoteLines property
        Args:
            value: Value to set for the sales_quote_lines property.
        """
        self._sales_quote_lines = value
    
    @property
    def sales_quotes(self,) -> Optional[List[sales_quote.SalesQuote]]:
        """
        Gets the salesQuotes property value. The salesQuotes property
        Returns: Optional[List[sales_quote.SalesQuote]]
        """
        return self._sales_quotes
    
    @sales_quotes.setter
    def sales_quotes(self,value: Optional[List[sales_quote.SalesQuote]] = None) -> None:
        """
        Sets the salesQuotes property value. The salesQuotes property
        Args:
            value: Value to set for the sales_quotes property.
        """
        self._sales_quotes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_collection_of_object_values("agedAccountsPayable", self.aged_accounts_payable)
        writer.write_collection_of_object_values("agedAccountsReceivable", self.aged_accounts_receivable)
        writer.write_str_value("businessProfileId", self.business_profile_id)
        writer.write_collection_of_object_values("companyInformation", self.company_information)
        writer.write_collection_of_object_values("countriesRegions", self.countries_regions)
        writer.write_collection_of_object_values("currencies", self.currencies)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_collection_of_object_values("customerPayments", self.customer_payments)
        writer.write_collection_of_object_values("customerPaymentJournals", self.customer_payment_journals)
        writer.write_collection_of_object_values("dimensions", self.dimensions)
        writer.write_collection_of_object_values("dimensionValues", self.dimension_values)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_collection_of_object_values("generalLedgerEntries", self.general_ledger_entries)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_collection_of_object_values("itemCategories", self.item_categories)
        writer.write_collection_of_object_values("journals", self.journals)
        writer.write_collection_of_object_values("journalLines", self.journal_lines)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("paymentMethods", self.payment_methods)
        writer.write_collection_of_object_values("paymentTerms", self.payment_terms)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_collection_of_object_values("purchaseInvoices", self.purchase_invoices)
        writer.write_collection_of_object_values("purchaseInvoiceLines", self.purchase_invoice_lines)
        writer.write_collection_of_object_values("salesCreditMemos", self.sales_credit_memos)
        writer.write_collection_of_object_values("salesCreditMemoLines", self.sales_credit_memo_lines)
        writer.write_collection_of_object_values("salesInvoices", self.sales_invoices)
        writer.write_collection_of_object_values("salesInvoiceLines", self.sales_invoice_lines)
        writer.write_collection_of_object_values("salesOrders", self.sales_orders)
        writer.write_collection_of_object_values("salesOrderLines", self.sales_order_lines)
        writer.write_collection_of_object_values("salesQuotes", self.sales_quotes)
        writer.write_collection_of_object_values("salesQuoteLines", self.sales_quote_lines)
        writer.write_collection_of_object_values("shipmentMethods", self.shipment_methods)
        writer.write_str_value("systemVersion", self.system_version)
        writer.write_collection_of_object_values("taxAreas", self.tax_areas)
        writer.write_collection_of_object_values("taxGroups", self.tax_groups)
        writer.write_collection_of_object_values("unitsOfMeasure", self.units_of_measure)
        writer.write_collection_of_object_values("vendors", self.vendors)
    
    @property
    def shipment_methods(self,) -> Optional[List[shipment_method.ShipmentMethod]]:
        """
        Gets the shipmentMethods property value. The shipmentMethods property
        Returns: Optional[List[shipment_method.ShipmentMethod]]
        """
        return self._shipment_methods
    
    @shipment_methods.setter
    def shipment_methods(self,value: Optional[List[shipment_method.ShipmentMethod]] = None) -> None:
        """
        Sets the shipmentMethods property value. The shipmentMethods property
        Args:
            value: Value to set for the shipment_methods property.
        """
        self._shipment_methods = value
    
    @property
    def system_version(self,) -> Optional[str]:
        """
        Gets the systemVersion property value. The systemVersion property
        Returns: Optional[str]
        """
        return self._system_version
    
    @system_version.setter
    def system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the systemVersion property value. The systemVersion property
        Args:
            value: Value to set for the system_version property.
        """
        self._system_version = value
    
    @property
    def tax_areas(self,) -> Optional[List[tax_area.TaxArea]]:
        """
        Gets the taxAreas property value. The taxAreas property
        Returns: Optional[List[tax_area.TaxArea]]
        """
        return self._tax_areas
    
    @tax_areas.setter
    def tax_areas(self,value: Optional[List[tax_area.TaxArea]] = None) -> None:
        """
        Sets the taxAreas property value. The taxAreas property
        Args:
            value: Value to set for the tax_areas property.
        """
        self._tax_areas = value
    
    @property
    def tax_groups(self,) -> Optional[List[tax_group.TaxGroup]]:
        """
        Gets the taxGroups property value. The taxGroups property
        Returns: Optional[List[tax_group.TaxGroup]]
        """
        return self._tax_groups
    
    @tax_groups.setter
    def tax_groups(self,value: Optional[List[tax_group.TaxGroup]] = None) -> None:
        """
        Sets the taxGroups property value. The taxGroups property
        Args:
            value: Value to set for the tax_groups property.
        """
        self._tax_groups = value
    
    @property
    def units_of_measure(self,) -> Optional[List[unit_of_measure.UnitOfMeasure]]:
        """
        Gets the unitsOfMeasure property value. The unitsOfMeasure property
        Returns: Optional[List[unit_of_measure.UnitOfMeasure]]
        """
        return self._units_of_measure
    
    @units_of_measure.setter
    def units_of_measure(self,value: Optional[List[unit_of_measure.UnitOfMeasure]] = None) -> None:
        """
        Sets the unitsOfMeasure property value. The unitsOfMeasure property
        Args:
            value: Value to set for the units_of_measure property.
        """
        self._units_of_measure = value
    
    @property
    def vendors(self,) -> Optional[List[vendor.Vendor]]:
        """
        Gets the vendors property value. The vendors property
        Returns: Optional[List[vendor.Vendor]]
        """
        return self._vendors
    
    @vendors.setter
    def vendors(self,value: Optional[List[vendor.Vendor]] = None) -> None:
        """
        Sets the vendors property value. The vendors property
        Args:
            value: Value to set for the vendors property.
        """
        self._vendors = value
    

