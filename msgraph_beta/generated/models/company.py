from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .account import Account
    from .aged_accounts_payable import AgedAccountsPayable
    from .aged_accounts_receivable import AgedAccountsReceivable
    from .company_information import CompanyInformation
    from .country_region import CountryRegion
    from .currency import Currency
    from .customer import Customer
    from .customer_payment import CustomerPayment
    from .customer_payment_journal import CustomerPaymentJournal
    from .dimension import Dimension
    from .dimension_value import DimensionValue
    from .employee import Employee
    from .general_ledger_entry import GeneralLedgerEntry
    from .item import Item
    from .item_category import ItemCategory
    from .journal import Journal
    from .journal_line import JournalLine
    from .payment_method import PaymentMethod
    from .payment_term import PaymentTerm
    from .picture import Picture
    from .purchase_invoice import PurchaseInvoice
    from .purchase_invoice_line import PurchaseInvoiceLine
    from .sales_credit_memo import SalesCreditMemo
    from .sales_credit_memo_line import SalesCreditMemoLine
    from .sales_invoice import SalesInvoice
    from .sales_invoice_line import SalesInvoiceLine
    from .sales_order import SalesOrder
    from .sales_order_line import SalesOrderLine
    from .sales_quote import SalesQuote
    from .sales_quote_line import SalesQuoteLine
    from .shipment_method import ShipmentMethod
    from .tax_area import TaxArea
    from .tax_group import TaxGroup
    from .unit_of_measure import UnitOfMeasure
    from .vendor import Vendor

@dataclass
class Company(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accounts property
    accounts: Optional[List[Account]] = None
    # The agedAccountsPayable property
    aged_accounts_payable: Optional[List[AgedAccountsPayable]] = None
    # The agedAccountsReceivable property
    aged_accounts_receivable: Optional[List[AgedAccountsReceivable]] = None
    # The businessProfileId property
    business_profile_id: Optional[str] = None
    # The companyInformation property
    company_information: Optional[List[CompanyInformation]] = None
    # The countriesRegions property
    countries_regions: Optional[List[CountryRegion]] = None
    # The currencies property
    currencies: Optional[List[Currency]] = None
    # The customerPaymentJournals property
    customer_payment_journals: Optional[List[CustomerPaymentJournal]] = None
    # The customerPayments property
    customer_payments: Optional[List[CustomerPayment]] = None
    # The customers property
    customers: Optional[List[Customer]] = None
    # The dimensionValues property
    dimension_values: Optional[List[DimensionValue]] = None
    # The dimensions property
    dimensions: Optional[List[Dimension]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The employees property
    employees: Optional[List[Employee]] = None
    # The generalLedgerEntries property
    general_ledger_entries: Optional[List[GeneralLedgerEntry]] = None
    # The id property
    id: Optional[UUID] = None
    # The itemCategories property
    item_categories: Optional[List[ItemCategory]] = None
    # The items property
    items: Optional[List[Item]] = None
    # The journalLines property
    journal_lines: Optional[List[JournalLine]] = None
    # The journals property
    journals: Optional[List[Journal]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The paymentMethods property
    payment_methods: Optional[List[PaymentMethod]] = None
    # The paymentTerms property
    payment_terms: Optional[List[PaymentTerm]] = None
    # The picture property
    picture: Optional[List[Picture]] = None
    # The purchaseInvoiceLines property
    purchase_invoice_lines: Optional[List[PurchaseInvoiceLine]] = None
    # The purchaseInvoices property
    purchase_invoices: Optional[List[PurchaseInvoice]] = None
    # The salesCreditMemoLines property
    sales_credit_memo_lines: Optional[List[SalesCreditMemoLine]] = None
    # The salesCreditMemos property
    sales_credit_memos: Optional[List[SalesCreditMemo]] = None
    # The salesInvoiceLines property
    sales_invoice_lines: Optional[List[SalesInvoiceLine]] = None
    # The salesInvoices property
    sales_invoices: Optional[List[SalesInvoice]] = None
    # The salesOrderLines property
    sales_order_lines: Optional[List[SalesOrderLine]] = None
    # The salesOrders property
    sales_orders: Optional[List[SalesOrder]] = None
    # The salesQuoteLines property
    sales_quote_lines: Optional[List[SalesQuoteLine]] = None
    # The salesQuotes property
    sales_quotes: Optional[List[SalesQuote]] = None
    # The shipmentMethods property
    shipment_methods: Optional[List[ShipmentMethod]] = None
    # The systemVersion property
    system_version: Optional[str] = None
    # The taxAreas property
    tax_areas: Optional[List[TaxArea]] = None
    # The taxGroups property
    tax_groups: Optional[List[TaxGroup]] = None
    # The unitsOfMeasure property
    units_of_measure: Optional[List[UnitOfMeasure]] = None
    # The vendors property
    vendors: Optional[List[Vendor]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Company:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Company
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Company()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account import Account
        from .aged_accounts_payable import AgedAccountsPayable
        from .aged_accounts_receivable import AgedAccountsReceivable
        from .company_information import CompanyInformation
        from .country_region import CountryRegion
        from .currency import Currency
        from .customer import Customer
        from .customer_payment import CustomerPayment
        from .customer_payment_journal import CustomerPaymentJournal
        from .dimension import Dimension
        from .dimension_value import DimensionValue
        from .employee import Employee
        from .general_ledger_entry import GeneralLedgerEntry
        from .item import Item
        from .item_category import ItemCategory
        from .journal import Journal
        from .journal_line import JournalLine
        from .payment_method import PaymentMethod
        from .payment_term import PaymentTerm
        from .picture import Picture
        from .purchase_invoice import PurchaseInvoice
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .sales_credit_memo import SalesCreditMemo
        from .sales_credit_memo_line import SalesCreditMemoLine
        from .sales_invoice import SalesInvoice
        from .sales_invoice_line import SalesInvoiceLine
        from .sales_order import SalesOrder
        from .sales_order_line import SalesOrderLine
        from .sales_quote import SalesQuote
        from .sales_quote_line import SalesQuoteLine
        from .shipment_method import ShipmentMethod
        from .tax_area import TaxArea
        from .tax_group import TaxGroup
        from .unit_of_measure import UnitOfMeasure
        from .vendor import Vendor

        from .account import Account
        from .aged_accounts_payable import AgedAccountsPayable
        from .aged_accounts_receivable import AgedAccountsReceivable
        from .company_information import CompanyInformation
        from .country_region import CountryRegion
        from .currency import Currency
        from .customer import Customer
        from .customer_payment import CustomerPayment
        from .customer_payment_journal import CustomerPaymentJournal
        from .dimension import Dimension
        from .dimension_value import DimensionValue
        from .employee import Employee
        from .general_ledger_entry import GeneralLedgerEntry
        from .item import Item
        from .item_category import ItemCategory
        from .journal import Journal
        from .journal_line import JournalLine
        from .payment_method import PaymentMethod
        from .payment_term import PaymentTerm
        from .picture import Picture
        from .purchase_invoice import PurchaseInvoice
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .sales_credit_memo import SalesCreditMemo
        from .sales_credit_memo_line import SalesCreditMemoLine
        from .sales_invoice import SalesInvoice
        from .sales_invoice_line import SalesInvoiceLine
        from .sales_order import SalesOrder
        from .sales_order_line import SalesOrderLine
        from .sales_quote import SalesQuote
        from .sales_quote_line import SalesQuoteLine
        from .shipment_method import ShipmentMethod
        from .tax_area import TaxArea
        from .tax_group import TaxGroup
        from .unit_of_measure import UnitOfMeasure
        from .vendor import Vendor

        fields: Dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(Account)),
            "agedAccountsPayable": lambda n : setattr(self, 'aged_accounts_payable', n.get_collection_of_object_values(AgedAccountsPayable)),
            "agedAccountsReceivable": lambda n : setattr(self, 'aged_accounts_receivable', n.get_collection_of_object_values(AgedAccountsReceivable)),
            "businessProfileId": lambda n : setattr(self, 'business_profile_id', n.get_str_value()),
            "companyInformation": lambda n : setattr(self, 'company_information', n.get_collection_of_object_values(CompanyInformation)),
            "countriesRegions": lambda n : setattr(self, 'countries_regions', n.get_collection_of_object_values(CountryRegion)),
            "currencies": lambda n : setattr(self, 'currencies', n.get_collection_of_object_values(Currency)),
            "customerPaymentJournals": lambda n : setattr(self, 'customer_payment_journals', n.get_collection_of_object_values(CustomerPaymentJournal)),
            "customerPayments": lambda n : setattr(self, 'customer_payments', n.get_collection_of_object_values(CustomerPayment)),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(Customer)),
            "dimensionValues": lambda n : setattr(self, 'dimension_values', n.get_collection_of_object_values(DimensionValue)),
            "dimensions": lambda n : setattr(self, 'dimensions', n.get_collection_of_object_values(Dimension)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(Employee)),
            "generalLedgerEntries": lambda n : setattr(self, 'general_ledger_entries', n.get_collection_of_object_values(GeneralLedgerEntry)),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "itemCategories": lambda n : setattr(self, 'item_categories', n.get_collection_of_object_values(ItemCategory)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(Item)),
            "journalLines": lambda n : setattr(self, 'journal_lines', n.get_collection_of_object_values(JournalLine)),
            "journals": lambda n : setattr(self, 'journals', n.get_collection_of_object_values(Journal)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "paymentMethods": lambda n : setattr(self, 'payment_methods', n.get_collection_of_object_values(PaymentMethod)),
            "paymentTerms": lambda n : setattr(self, 'payment_terms', n.get_collection_of_object_values(PaymentTerm)),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(Picture)),
            "purchaseInvoiceLines": lambda n : setattr(self, 'purchase_invoice_lines', n.get_collection_of_object_values(PurchaseInvoiceLine)),
            "purchaseInvoices": lambda n : setattr(self, 'purchase_invoices', n.get_collection_of_object_values(PurchaseInvoice)),
            "salesCreditMemoLines": lambda n : setattr(self, 'sales_credit_memo_lines', n.get_collection_of_object_values(SalesCreditMemoLine)),
            "salesCreditMemos": lambda n : setattr(self, 'sales_credit_memos', n.get_collection_of_object_values(SalesCreditMemo)),
            "salesInvoiceLines": lambda n : setattr(self, 'sales_invoice_lines', n.get_collection_of_object_values(SalesInvoiceLine)),
            "salesInvoices": lambda n : setattr(self, 'sales_invoices', n.get_collection_of_object_values(SalesInvoice)),
            "salesOrderLines": lambda n : setattr(self, 'sales_order_lines', n.get_collection_of_object_values(SalesOrderLine)),
            "salesOrders": lambda n : setattr(self, 'sales_orders', n.get_collection_of_object_values(SalesOrder)),
            "salesQuoteLines": lambda n : setattr(self, 'sales_quote_lines', n.get_collection_of_object_values(SalesQuoteLine)),
            "salesQuotes": lambda n : setattr(self, 'sales_quotes', n.get_collection_of_object_values(SalesQuote)),
            "shipmentMethods": lambda n : setattr(self, 'shipment_methods', n.get_collection_of_object_values(ShipmentMethod)),
            "systemVersion": lambda n : setattr(self, 'system_version', n.get_str_value()),
            "taxAreas": lambda n : setattr(self, 'tax_areas', n.get_collection_of_object_values(TaxArea)),
            "taxGroups": lambda n : setattr(self, 'tax_groups', n.get_collection_of_object_values(TaxGroup)),
            "unitsOfMeasure": lambda n : setattr(self, 'units_of_measure', n.get_collection_of_object_values(UnitOfMeasure)),
            "vendors": lambda n : setattr(self, 'vendors', n.get_collection_of_object_values(Vendor)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_collection_of_object_values("agedAccountsPayable", self.aged_accounts_payable)
        writer.write_collection_of_object_values("agedAccountsReceivable", self.aged_accounts_receivable)
        writer.write_str_value("businessProfileId", self.business_profile_id)
        writer.write_collection_of_object_values("companyInformation", self.company_information)
        writer.write_collection_of_object_values("countriesRegions", self.countries_regions)
        writer.write_collection_of_object_values("currencies", self.currencies)
        writer.write_collection_of_object_values("customerPaymentJournals", self.customer_payment_journals)
        writer.write_collection_of_object_values("customerPayments", self.customer_payments)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_collection_of_object_values("dimensionValues", self.dimension_values)
        writer.write_collection_of_object_values("dimensions", self.dimensions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_collection_of_object_values("generalLedgerEntries", self.general_ledger_entries)
        writer.write_uuid_value("id", self.id)
        writer.write_collection_of_object_values("itemCategories", self.item_categories)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_collection_of_object_values("journalLines", self.journal_lines)
        writer.write_collection_of_object_values("journals", self.journals)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("paymentMethods", self.payment_methods)
        writer.write_collection_of_object_values("paymentTerms", self.payment_terms)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_collection_of_object_values("purchaseInvoiceLines", self.purchase_invoice_lines)
        writer.write_collection_of_object_values("purchaseInvoices", self.purchase_invoices)
        writer.write_collection_of_object_values("salesCreditMemoLines", self.sales_credit_memo_lines)
        writer.write_collection_of_object_values("salesCreditMemos", self.sales_credit_memos)
        writer.write_collection_of_object_values("salesInvoiceLines", self.sales_invoice_lines)
        writer.write_collection_of_object_values("salesInvoices", self.sales_invoices)
        writer.write_collection_of_object_values("salesOrderLines", self.sales_order_lines)
        writer.write_collection_of_object_values("salesOrders", self.sales_orders)
        writer.write_collection_of_object_values("salesQuoteLines", self.sales_quote_lines)
        writer.write_collection_of_object_values("salesQuotes", self.sales_quotes)
        writer.write_collection_of_object_values("shipmentMethods", self.shipment_methods)
        writer.write_str_value("systemVersion", self.system_version)
        writer.write_collection_of_object_values("taxAreas", self.tax_areas)
        writer.write_collection_of_object_values("taxGroups", self.tax_groups)
        writer.write_collection_of_object_values("unitsOfMeasure", self.units_of_measure)
        writer.write_collection_of_object_values("vendors", self.vendors)
        writer.write_additional_data_value(self.additional_data)
    

