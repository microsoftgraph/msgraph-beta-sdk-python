from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

currency = lazy_import('msgraph.generated.models.currency')
entity = lazy_import('msgraph.generated.models.entity')
postal_address_type = lazy_import('msgraph.generated.models.postal_address_type')
purchase_invoice_line = lazy_import('msgraph.generated.models.purchase_invoice_line')
vendor = lazy_import('msgraph.generated.models.vendor')

class PurchaseInvoice(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def buy_from_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the buyFromAddress property value. The buyFromAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._buy_from_address
    
    @buy_from_address.setter
    def buy_from_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the buyFromAddress property value. The buyFromAddress property
        Args:
            value: Value to set for the buyFromAddress property.
        """
        self._buy_from_address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new purchaseInvoice and sets the default values.
        """
        super().__init__()
        # The buyFromAddress property
        self._buy_from_address: Optional[postal_address_type.PostalAddressType] = None
        # The currency property
        self._currency: Optional[currency.Currency] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currencyId property
        self._currency_id: Optional[Guid] = None
        # The discountAmount property
        self._discount_amount: Optional[float] = None
        # The discountAppliedBeforeTax property
        self._discount_applied_before_tax: Optional[bool] = None
        # The dueDate property
        self._due_date: Optional[Date] = None
        # The invoiceDate property
        self._invoice_date: Optional[Date] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The payToAddress property
        self._pay_to_address: Optional[postal_address_type.PostalAddressType] = None
        # The payToContact property
        self._pay_to_contact: Optional[str] = None
        # The payToName property
        self._pay_to_name: Optional[str] = None
        # The payToVendorId property
        self._pay_to_vendor_id: Optional[Guid] = None
        # The payToVendorNumber property
        self._pay_to_vendor_number: Optional[str] = None
        # The pricesIncludeTax property
        self._prices_include_tax: Optional[bool] = None
        # The purchaseInvoiceLines property
        self._purchase_invoice_lines: Optional[List[purchase_invoice_line.PurchaseInvoiceLine]] = None
        # The shipToAddress property
        self._ship_to_address: Optional[postal_address_type.PostalAddressType] = None
        # The shipToContact property
        self._ship_to_contact: Optional[str] = None
        # The shipToName property
        self._ship_to_name: Optional[str] = None
        # The status property
        self._status: Optional[str] = None
        # The totalAmountExcludingTax property
        self._total_amount_excluding_tax: Optional[float] = None
        # The totalAmountIncludingTax property
        self._total_amount_including_tax: Optional[float] = None
        # The totalTaxAmount property
        self._total_tax_amount: Optional[float] = None
        # The vendor property
        self._vendor: Optional[vendor.Vendor] = None
        # The vendorId property
        self._vendor_id: Optional[Guid] = None
        # The vendorInvoiceNumber property
        self._vendor_invoice_number: Optional[str] = None
        # The vendorName property
        self._vendor_name: Optional[str] = None
        # The vendorNumber property
        self._vendor_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PurchaseInvoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PurchaseInvoice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PurchaseInvoice()
    
    @property
    def currency(self,) -> Optional[currency.Currency]:
        """
        Gets the currency property value. The currency property
        Returns: Optional[currency.Currency]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[currency.Currency] = None) -> None:
        """
        Sets the currency property value. The currency property
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
    @property
    def currency_code(self,) -> Optional[str]:
        """
        Gets the currencyCode property value. The currencyCode property
        Returns: Optional[str]
        """
        return self._currency_code
    
    @currency_code.setter
    def currency_code(self,value: Optional[str] = None) -> None:
        """
        Sets the currencyCode property value. The currencyCode property
        Args:
            value: Value to set for the currencyCode property.
        """
        self._currency_code = value
    
    @property
    def currency_id(self,) -> Optional[Guid]:
        """
        Gets the currencyId property value. The currencyId property
        Returns: Optional[Guid]
        """
        return self._currency_id
    
    @currency_id.setter
    def currency_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the currencyId property value. The currencyId property
        Args:
            value: Value to set for the currencyId property.
        """
        self._currency_id = value
    
    @property
    def discount_amount(self,) -> Optional[float]:
        """
        Gets the discountAmount property value. The discountAmount property
        Returns: Optional[float]
        """
        return self._discount_amount
    
    @discount_amount.setter
    def discount_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the discountAmount property value. The discountAmount property
        Args:
            value: Value to set for the discountAmount property.
        """
        self._discount_amount = value
    
    @property
    def discount_applied_before_tax(self,) -> Optional[bool]:
        """
        Gets the discountAppliedBeforeTax property value. The discountAppliedBeforeTax property
        Returns: Optional[bool]
        """
        return self._discount_applied_before_tax
    
    @discount_applied_before_tax.setter
    def discount_applied_before_tax(self,value: Optional[bool] = None) -> None:
        """
        Sets the discountAppliedBeforeTax property value. The discountAppliedBeforeTax property
        Args:
            value: Value to set for the discountAppliedBeforeTax property.
        """
        self._discount_applied_before_tax = value
    
    @property
    def due_date(self,) -> Optional[Date]:
        """
        Gets the dueDate property value. The dueDate property
        Returns: Optional[Date]
        """
        return self._due_date
    
    @due_date.setter
    def due_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the dueDate property value. The dueDate property
        Args:
            value: Value to set for the dueDate property.
        """
        self._due_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "buy_from_address": lambda n : setattr(self, 'buy_from_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency.Currency)),
            "currency_code": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currency_id": lambda n : setattr(self, 'currency_id', n.get_object_value(Guid)),
            "discount_amount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discount_applied_before_tax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "due_date": lambda n : setattr(self, 'due_date', n.get_object_value(Date)),
            "invoice_date": lambda n : setattr(self, 'invoice_date', n.get_object_value(Date)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "pay_to_address": lambda n : setattr(self, 'pay_to_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "pay_to_contact": lambda n : setattr(self, 'pay_to_contact', n.get_str_value()),
            "pay_to_name": lambda n : setattr(self, 'pay_to_name', n.get_str_value()),
            "pay_to_vendor_id": lambda n : setattr(self, 'pay_to_vendor_id', n.get_object_value(Guid)),
            "pay_to_vendor_number": lambda n : setattr(self, 'pay_to_vendor_number', n.get_str_value()),
            "prices_include_tax": lambda n : setattr(self, 'prices_include_tax', n.get_bool_value()),
            "purchase_invoice_lines": lambda n : setattr(self, 'purchase_invoice_lines', n.get_collection_of_object_values(purchase_invoice_line.PurchaseInvoiceLine)),
            "ship_to_address": lambda n : setattr(self, 'ship_to_address', n.get_object_value(postal_address_type.PostalAddressType)),
            "ship_to_contact": lambda n : setattr(self, 'ship_to_contact', n.get_str_value()),
            "ship_to_name": lambda n : setattr(self, 'ship_to_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "total_amount_excluding_tax": lambda n : setattr(self, 'total_amount_excluding_tax', n.get_float_value()),
            "total_amount_including_tax": lambda n : setattr(self, 'total_amount_including_tax', n.get_float_value()),
            "total_tax_amount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_object_value(vendor.Vendor)),
            "vendor_id": lambda n : setattr(self, 'vendor_id', n.get_object_value(Guid)),
            "vendor_invoice_number": lambda n : setattr(self, 'vendor_invoice_number', n.get_str_value()),
            "vendor_name": lambda n : setattr(self, 'vendor_name', n.get_str_value()),
            "vendor_number": lambda n : setattr(self, 'vendor_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invoice_date(self,) -> Optional[Date]:
        """
        Gets the invoiceDate property value. The invoiceDate property
        Returns: Optional[Date]
        """
        return self._invoice_date
    
    @invoice_date.setter
    def invoice_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the invoiceDate property value. The invoiceDate property
        Args:
            value: Value to set for the invoiceDate property.
        """
        self._invoice_date = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The number property
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def pay_to_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the payToAddress property value. The payToAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._pay_to_address
    
    @pay_to_address.setter
    def pay_to_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the payToAddress property value. The payToAddress property
        Args:
            value: Value to set for the payToAddress property.
        """
        self._pay_to_address = value
    
    @property
    def pay_to_contact(self,) -> Optional[str]:
        """
        Gets the payToContact property value. The payToContact property
        Returns: Optional[str]
        """
        return self._pay_to_contact
    
    @pay_to_contact.setter
    def pay_to_contact(self,value: Optional[str] = None) -> None:
        """
        Sets the payToContact property value. The payToContact property
        Args:
            value: Value to set for the payToContact property.
        """
        self._pay_to_contact = value
    
    @property
    def pay_to_name(self,) -> Optional[str]:
        """
        Gets the payToName property value. The payToName property
        Returns: Optional[str]
        """
        return self._pay_to_name
    
    @pay_to_name.setter
    def pay_to_name(self,value: Optional[str] = None) -> None:
        """
        Sets the payToName property value. The payToName property
        Args:
            value: Value to set for the payToName property.
        """
        self._pay_to_name = value
    
    @property
    def pay_to_vendor_id(self,) -> Optional[Guid]:
        """
        Gets the payToVendorId property value. The payToVendorId property
        Returns: Optional[Guid]
        """
        return self._pay_to_vendor_id
    
    @pay_to_vendor_id.setter
    def pay_to_vendor_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the payToVendorId property value. The payToVendorId property
        Args:
            value: Value to set for the payToVendorId property.
        """
        self._pay_to_vendor_id = value
    
    @property
    def pay_to_vendor_number(self,) -> Optional[str]:
        """
        Gets the payToVendorNumber property value. The payToVendorNumber property
        Returns: Optional[str]
        """
        return self._pay_to_vendor_number
    
    @pay_to_vendor_number.setter
    def pay_to_vendor_number(self,value: Optional[str] = None) -> None:
        """
        Sets the payToVendorNumber property value. The payToVendorNumber property
        Args:
            value: Value to set for the payToVendorNumber property.
        """
        self._pay_to_vendor_number = value
    
    @property
    def prices_include_tax(self,) -> Optional[bool]:
        """
        Gets the pricesIncludeTax property value. The pricesIncludeTax property
        Returns: Optional[bool]
        """
        return self._prices_include_tax
    
    @prices_include_tax.setter
    def prices_include_tax(self,value: Optional[bool] = None) -> None:
        """
        Sets the pricesIncludeTax property value. The pricesIncludeTax property
        Args:
            value: Value to set for the pricesIncludeTax property.
        """
        self._prices_include_tax = value
    
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
            value: Value to set for the purchaseInvoiceLines property.
        """
        self._purchase_invoice_lines = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("buyFromAddress", self.buy_from_address)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_object_value("currencyId", self.currency_id)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_object_value("dueDate", self.due_date)
        writer.write_object_value("invoiceDate", self.invoice_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_object_value("payToAddress", self.pay_to_address)
        writer.write_str_value("payToContact", self.pay_to_contact)
        writer.write_str_value("payToName", self.pay_to_name)
        writer.write_object_value("payToVendorId", self.pay_to_vendor_id)
        writer.write_str_value("payToVendorNumber", self.pay_to_vendor_number)
        writer.write_bool_value("pricesIncludeTax", self.prices_include_tax)
        writer.write_collection_of_object_values("purchaseInvoiceLines", self.purchase_invoice_lines)
        writer.write_object_value("shipToAddress", self.ship_to_address)
        writer.write_str_value("shipToContact", self.ship_to_contact)
        writer.write_str_value("shipToName", self.ship_to_name)
        writer.write_str_value("status", self.status)
        writer.write_float_value("totalAmountExcludingTax", self.total_amount_excluding_tax)
        writer.write_float_value("totalAmountIncludingTax", self.total_amount_including_tax)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
        writer.write_object_value("vendor", self.vendor)
        writer.write_object_value("vendorId", self.vendor_id)
        writer.write_str_value("vendorInvoiceNumber", self.vendor_invoice_number)
        writer.write_str_value("vendorName", self.vendor_name)
        writer.write_str_value("vendorNumber", self.vendor_number)
    
    @property
    def ship_to_address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the shipToAddress property value. The shipToAddress property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._ship_to_address
    
    @ship_to_address.setter
    def ship_to_address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the shipToAddress property value. The shipToAddress property
        Args:
            value: Value to set for the shipToAddress property.
        """
        self._ship_to_address = value
    
    @property
    def ship_to_contact(self,) -> Optional[str]:
        """
        Gets the shipToContact property value. The shipToContact property
        Returns: Optional[str]
        """
        return self._ship_to_contact
    
    @ship_to_contact.setter
    def ship_to_contact(self,value: Optional[str] = None) -> None:
        """
        Sets the shipToContact property value. The shipToContact property
        Args:
            value: Value to set for the shipToContact property.
        """
        self._ship_to_contact = value
    
    @property
    def ship_to_name(self,) -> Optional[str]:
        """
        Gets the shipToName property value. The shipToName property
        Returns: Optional[str]
        """
        return self._ship_to_name
    
    @ship_to_name.setter
    def ship_to_name(self,value: Optional[str] = None) -> None:
        """
        Sets the shipToName property value. The shipToName property
        Args:
            value: Value to set for the shipToName property.
        """
        self._ship_to_name = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def total_amount_excluding_tax(self,) -> Optional[float]:
        """
        Gets the totalAmountExcludingTax property value. The totalAmountExcludingTax property
        Returns: Optional[float]
        """
        return self._total_amount_excluding_tax
    
    @total_amount_excluding_tax.setter
    def total_amount_excluding_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the totalAmountExcludingTax property value. The totalAmountExcludingTax property
        Args:
            value: Value to set for the totalAmountExcludingTax property.
        """
        self._total_amount_excluding_tax = value
    
    @property
    def total_amount_including_tax(self,) -> Optional[float]:
        """
        Gets the totalAmountIncludingTax property value. The totalAmountIncludingTax property
        Returns: Optional[float]
        """
        return self._total_amount_including_tax
    
    @total_amount_including_tax.setter
    def total_amount_including_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the totalAmountIncludingTax property value. The totalAmountIncludingTax property
        Args:
            value: Value to set for the totalAmountIncludingTax property.
        """
        self._total_amount_including_tax = value
    
    @property
    def total_tax_amount(self,) -> Optional[float]:
        """
        Gets the totalTaxAmount property value. The totalTaxAmount property
        Returns: Optional[float]
        """
        return self._total_tax_amount
    
    @total_tax_amount.setter
    def total_tax_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the totalTaxAmount property value. The totalTaxAmount property
        Args:
            value: Value to set for the totalTaxAmount property.
        """
        self._total_tax_amount = value
    
    @property
    def vendor(self,) -> Optional[vendor.Vendor]:
        """
        Gets the vendor property value. The vendor property
        Returns: Optional[vendor.Vendor]
        """
        return self._vendor
    
    @vendor.setter
    def vendor(self,value: Optional[vendor.Vendor] = None) -> None:
        """
        Sets the vendor property value. The vendor property
        Args:
            value: Value to set for the vendor property.
        """
        self._vendor = value
    
    @property
    def vendor_id(self,) -> Optional[Guid]:
        """
        Gets the vendorId property value. The vendorId property
        Returns: Optional[Guid]
        """
        return self._vendor_id
    
    @vendor_id.setter
    def vendor_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the vendorId property value. The vendorId property
        Args:
            value: Value to set for the vendorId property.
        """
        self._vendor_id = value
    
    @property
    def vendor_invoice_number(self,) -> Optional[str]:
        """
        Gets the vendorInvoiceNumber property value. The vendorInvoiceNumber property
        Returns: Optional[str]
        """
        return self._vendor_invoice_number
    
    @vendor_invoice_number.setter
    def vendor_invoice_number(self,value: Optional[str] = None) -> None:
        """
        Sets the vendorInvoiceNumber property value. The vendorInvoiceNumber property
        Args:
            value: Value to set for the vendorInvoiceNumber property.
        """
        self._vendor_invoice_number = value
    
    @property
    def vendor_name(self,) -> Optional[str]:
        """
        Gets the vendorName property value. The vendorName property
        Returns: Optional[str]
        """
        return self._vendor_name
    
    @vendor_name.setter
    def vendor_name(self,value: Optional[str] = None) -> None:
        """
        Sets the vendorName property value. The vendorName property
        Args:
            value: Value to set for the vendorName property.
        """
        self._vendor_name = value
    
    @property
    def vendor_number(self,) -> Optional[str]:
        """
        Gets the vendorNumber property value. The vendorNumber property
        Returns: Optional[str]
        """
        return self._vendor_number
    
    @vendor_number.setter
    def vendor_number(self,value: Optional[str] = None) -> None:
        """
        Sets the vendorNumber property value. The vendorNumber property
        Args:
            value: Value to set for the vendorNumber property.
        """
        self._vendor_number = value
    

