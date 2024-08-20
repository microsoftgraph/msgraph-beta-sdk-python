from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .currency import Currency
    from .postal_address_type import PostalAddressType
    from .purchase_invoice_line import PurchaseInvoiceLine
    from .vendor import Vendor

@dataclass
class PurchaseInvoice(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The buyFromAddress property
    buy_from_address: Optional[PostalAddressType] = None
    # The currency property
    currency: Optional[Currency] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currencyId property
    currency_id: Optional[UUID] = None
    # The discountAmount property
    discount_amount: Optional[float] = None
    # The discountAppliedBeforeTax property
    discount_applied_before_tax: Optional[bool] = None
    # The dueDate property
    due_date: Optional[datetime.date] = None
    # The id property
    id: Optional[UUID] = None
    # The invoiceDate property
    invoice_date: Optional[datetime.date] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The number property
    number: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The payToAddress property
    pay_to_address: Optional[PostalAddressType] = None
    # The payToContact property
    pay_to_contact: Optional[str] = None
    # The payToName property
    pay_to_name: Optional[str] = None
    # The payToVendorId property
    pay_to_vendor_id: Optional[UUID] = None
    # The payToVendorNumber property
    pay_to_vendor_number: Optional[str] = None
    # The pricesIncludeTax property
    prices_include_tax: Optional[bool] = None
    # The purchaseInvoiceLines property
    purchase_invoice_lines: Optional[List[PurchaseInvoiceLine]] = None
    # The shipToAddress property
    ship_to_address: Optional[PostalAddressType] = None
    # The shipToContact property
    ship_to_contact: Optional[str] = None
    # The shipToName property
    ship_to_name: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The totalAmountExcludingTax property
    total_amount_excluding_tax: Optional[float] = None
    # The totalAmountIncludingTax property
    total_amount_including_tax: Optional[float] = None
    # The totalTaxAmount property
    total_tax_amount: Optional[float] = None
    # The vendor property
    vendor: Optional[Vendor] = None
    # The vendorId property
    vendor_id: Optional[UUID] = None
    # The vendorInvoiceNumber property
    vendor_invoice_number: Optional[str] = None
    # The vendorName property
    vendor_name: Optional[str] = None
    # The vendorNumber property
    vendor_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PurchaseInvoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PurchaseInvoice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PurchaseInvoice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .currency import Currency
        from .postal_address_type import PostalAddressType
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .vendor import Vendor

        from .currency import Currency
        from .postal_address_type import PostalAddressType
        from .purchase_invoice_line import PurchaseInvoiceLine
        from .vendor import Vendor

        fields: Dict[str, Callable[[Any], None]] = {
            "buyFromAddress": lambda n : setattr(self, 'buy_from_address', n.get_object_value(PostalAddressType)),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(Currency)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currencyId": lambda n : setattr(self, 'currency_id', n.get_uuid_value()),
            "discountAmount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discountAppliedBeforeTax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_date_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "invoiceDate": lambda n : setattr(self, 'invoice_date', n.get_date_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payToAddress": lambda n : setattr(self, 'pay_to_address', n.get_object_value(PostalAddressType)),
            "payToContact": lambda n : setattr(self, 'pay_to_contact', n.get_str_value()),
            "payToName": lambda n : setattr(self, 'pay_to_name', n.get_str_value()),
            "payToVendorId": lambda n : setattr(self, 'pay_to_vendor_id', n.get_uuid_value()),
            "payToVendorNumber": lambda n : setattr(self, 'pay_to_vendor_number', n.get_str_value()),
            "pricesIncludeTax": lambda n : setattr(self, 'prices_include_tax', n.get_bool_value()),
            "purchaseInvoiceLines": lambda n : setattr(self, 'purchase_invoice_lines', n.get_collection_of_object_values(PurchaseInvoiceLine)),
            "shipToAddress": lambda n : setattr(self, 'ship_to_address', n.get_object_value(PostalAddressType)),
            "shipToContact": lambda n : setattr(self, 'ship_to_contact', n.get_str_value()),
            "shipToName": lambda n : setattr(self, 'ship_to_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "totalAmountExcludingTax": lambda n : setattr(self, 'total_amount_excluding_tax', n.get_float_value()),
            "totalAmountIncludingTax": lambda n : setattr(self, 'total_amount_including_tax', n.get_float_value()),
            "totalTaxAmount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_object_value(Vendor)),
            "vendorId": lambda n : setattr(self, 'vendor_id', n.get_uuid_value()),
            "vendorInvoiceNumber": lambda n : setattr(self, 'vendor_invoice_number', n.get_str_value()),
            "vendorName": lambda n : setattr(self, 'vendor_name', n.get_str_value()),
            "vendorNumber": lambda n : setattr(self, 'vendor_number', n.get_str_value()),
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
        writer.write_object_value("buyFromAddress", self.buy_from_address)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_uuid_value("currencyId", self.currency_id)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_date_value("dueDate", self.due_date)
        writer.write_uuid_value("id", self.id)
        writer.write_date_value("invoiceDate", self.invoice_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("payToAddress", self.pay_to_address)
        writer.write_str_value("payToContact", self.pay_to_contact)
        writer.write_str_value("payToName", self.pay_to_name)
        writer.write_uuid_value("payToVendorId", self.pay_to_vendor_id)
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
        writer.write_uuid_value("vendorId", self.vendor_id)
        writer.write_str_value("vendorInvoiceNumber", self.vendor_invoice_number)
        writer.write_str_value("vendorName", self.vendor_name)
        writer.write_str_value("vendorNumber", self.vendor_number)
        writer.write_additional_data_value(self.additional_data)
    

