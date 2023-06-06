from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account, aged_accounts_payable, aged_accounts_receivable, company_information, country_region, currency, customer, customer_payment, customer_payment_journal, dimension, dimension_value, employee, entity, general_ledger_entry, item, item_category, journal, journal_line, payment_method, payment_term, picture, purchase_invoice, purchase_invoice_line, sales_credit_memo, sales_credit_memo_line, sales_invoice, sales_invoice_line, sales_order, sales_order_line, sales_quote, sales_quote_line, shipment_method, tax_area, tax_group, unit_of_measure, vendor

from . import entity

@dataclass
class Company(entity.Entity):
    # The accounts property
    accounts: Optional[List[account.Account]] = None
    # The agedAccountsPayable property
    aged_accounts_payable: Optional[List[aged_accounts_payable.AgedAccountsPayable]] = None
    # The agedAccountsReceivable property
    aged_accounts_receivable: Optional[List[aged_accounts_receivable.AgedAccountsReceivable]] = None
    # The businessProfileId property
    business_profile_id: Optional[str] = None
    # The companyInformation property
    company_information: Optional[List[company_information.CompanyInformation]] = None
    # The countriesRegions property
    countries_regions: Optional[List[country_region.CountryRegion]] = None
    # The currencies property
    currencies: Optional[List[currency.Currency]] = None
    # The customerPaymentJournals property
    customer_payment_journals: Optional[List[customer_payment_journal.CustomerPaymentJournal]] = None
    # The customerPayments property
    customer_payments: Optional[List[customer_payment.CustomerPayment]] = None
    # The customers property
    customers: Optional[List[customer.Customer]] = None
    # The dimensionValues property
    dimension_values: Optional[List[dimension_value.DimensionValue]] = None
    # The dimensions property
    dimensions: Optional[List[dimension.Dimension]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The employees property
    employees: Optional[List[employee.Employee]] = None
    # The generalLedgerEntries property
    general_ledger_entries: Optional[List[general_ledger_entry.GeneralLedgerEntry]] = None
    # The itemCategories property
    item_categories: Optional[List[item_category.ItemCategory]] = None
    # The items property
    items: Optional[List[item.Item]] = None
    # The journalLines property
    journal_lines: Optional[List[journal_line.JournalLine]] = None
    # The journals property
    journals: Optional[List[journal.Journal]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The paymentMethods property
    payment_methods: Optional[List[payment_method.PaymentMethod]] = None
    # The paymentTerms property
    payment_terms: Optional[List[payment_term.PaymentTerm]] = None
    # The picture property
    picture: Optional[List[picture.Picture]] = None
    # The purchaseInvoiceLines property
    purchase_invoice_lines: Optional[List[purchase_invoice_line.PurchaseInvoiceLine]] = None
    # The purchaseInvoices property
    purchase_invoices: Optional[List[purchase_invoice.PurchaseInvoice]] = None
    # The salesCreditMemoLines property
    sales_credit_memo_lines: Optional[List[sales_credit_memo_line.SalesCreditMemoLine]] = None
    # The salesCreditMemos property
    sales_credit_memos: Optional[List[sales_credit_memo.SalesCreditMemo]] = None
    # The salesInvoiceLines property
    sales_invoice_lines: Optional[List[sales_invoice_line.SalesInvoiceLine]] = None
    # The salesInvoices property
    sales_invoices: Optional[List[sales_invoice.SalesInvoice]] = None
    # The salesOrderLines property
    sales_order_lines: Optional[List[sales_order_line.SalesOrderLine]] = None
    # The salesOrders property
    sales_orders: Optional[List[sales_order.SalesOrder]] = None
    # The salesQuoteLines property
    sales_quote_lines: Optional[List[sales_quote_line.SalesQuoteLine]] = None
    # The salesQuotes property
    sales_quotes: Optional[List[sales_quote.SalesQuote]] = None
    # The shipmentMethods property
    shipment_methods: Optional[List[shipment_method.ShipmentMethod]] = None
    # The systemVersion property
    system_version: Optional[str] = None
    # The taxAreas property
    tax_areas: Optional[List[tax_area.TaxArea]] = None
    # The taxGroups property
    tax_groups: Optional[List[tax_group.TaxGroup]] = None
    # The unitsOfMeasure property
    units_of_measure: Optional[List[unit_of_measure.UnitOfMeasure]] = None
    # The vendors property
    vendors: Optional[List[vendor.Vendor]] = None
    
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
    

