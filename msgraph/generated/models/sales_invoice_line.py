from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .account import Account
    from .entity import Entity
    from .item import Item

from .entity import Entity

@dataclass
class SalesInvoiceLine(Entity):
    # The account property
    account: Optional[Account] = None
    # The accountId property
    account_id: Optional[UUID] = None
    # The amountExcludingTax property
    amount_excluding_tax: Optional[float] = None
    # The amountIncludingTax property
    amount_including_tax: Optional[float] = None
    # The description property
    description: Optional[str] = None
    # The discountAmount property
    discount_amount: Optional[float] = None
    # The discountAppliedBeforeTax property
    discount_applied_before_tax: Optional[bool] = None
    # The discountPercent property
    discount_percent: Optional[float] = None
    # The documentId property
    document_id: Optional[UUID] = None
    # The invoiceDiscountAllocation property
    invoice_discount_allocation: Optional[float] = None
    # The item property
    item: Optional[Item] = None
    # The itemId property
    item_id: Optional[UUID] = None
    # The lineType property
    line_type: Optional[str] = None
    # The netAmount property
    net_amount: Optional[float] = None
    # The netAmountIncludingTax property
    net_amount_including_tax: Optional[float] = None
    # The netTaxAmount property
    net_tax_amount: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The quantity property
    quantity: Optional[float] = None
    # The sequence property
    sequence: Optional[int] = None
    # The shipmentDate property
    shipment_date: Optional[datetime.date] = None
    # The taxCode property
    tax_code: Optional[str] = None
    # The taxPercent property
    tax_percent: Optional[float] = None
    # The totalTaxAmount property
    total_tax_amount: Optional[float] = None
    # The unitOfMeasureId property
    unit_of_measure_id: Optional[UUID] = None
    # The unitPrice property
    unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SalesInvoiceLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SalesInvoiceLine
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SalesInvoiceLine()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account import Account
        from .entity import Entity
        from .item import Item

        from .account import Account
        from .entity import Entity
        from .item import Item

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(Account)),
            "accountId": lambda n : setattr(self, 'account_id', n.get_uuid_value()),
            "amountExcludingTax": lambda n : setattr(self, 'amount_excluding_tax', n.get_float_value()),
            "amountIncludingTax": lambda n : setattr(self, 'amount_including_tax', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discountAmount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discountAppliedBeforeTax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "discountPercent": lambda n : setattr(self, 'discount_percent', n.get_float_value()),
            "documentId": lambda n : setattr(self, 'document_id', n.get_uuid_value()),
            "invoiceDiscountAllocation": lambda n : setattr(self, 'invoice_discount_allocation', n.get_float_value()),
            "item": lambda n : setattr(self, 'item', n.get_object_value(Item)),
            "itemId": lambda n : setattr(self, 'item_id', n.get_uuid_value()),
            "lineType": lambda n : setattr(self, 'line_type', n.get_str_value()),
            "netAmount": lambda n : setattr(self, 'net_amount', n.get_float_value()),
            "netAmountIncludingTax": lambda n : setattr(self, 'net_amount_including_tax', n.get_float_value()),
            "netTaxAmount": lambda n : setattr(self, 'net_tax_amount', n.get_float_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "shipmentDate": lambda n : setattr(self, 'shipment_date', n.get_date_value()),
            "taxCode": lambda n : setattr(self, 'tax_code', n.get_str_value()),
            "taxPercent": lambda n : setattr(self, 'tax_percent', n.get_float_value()),
            "totalTaxAmount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
            "unitOfMeasureId": lambda n : setattr(self, 'unit_of_measure_id', n.get_uuid_value()),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("account", self.account)
        writer.write_uuid_value("accountId", self.account_id)
        writer.write_float_value("amountExcludingTax", self.amount_excluding_tax)
        writer.write_float_value("amountIncludingTax", self.amount_including_tax)
        writer.write_str_value("description", self.description)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_float_value("discountPercent", self.discount_percent)
        writer.write_uuid_value("documentId", self.document_id)
        writer.write_float_value("invoiceDiscountAllocation", self.invoice_discount_allocation)
        writer.write_object_value("item", self.item)
        writer.write_uuid_value("itemId", self.item_id)
        writer.write_str_value("lineType", self.line_type)
        writer.write_float_value("netAmount", self.net_amount)
        writer.write_float_value("netAmountIncludingTax", self.net_amount_including_tax)
        writer.write_float_value("netTaxAmount", self.net_tax_amount)
        writer.write_float_value("quantity", self.quantity)
        writer.write_int_value("sequence", self.sequence)
        writer.write_date_value("shipmentDate", self.shipment_date)
        writer.write_str_value("taxCode", self.tax_code)
        writer.write_float_value("taxPercent", self.tax_percent)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
        writer.write_uuid_value("unitOfMeasureId", self.unit_of_measure_id)
        writer.write_float_value("unitPrice", self.unit_price)
    

