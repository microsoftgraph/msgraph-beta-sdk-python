from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

account = lazy_import('msgraph.generated.models.account')
entity = lazy_import('msgraph.generated.models.entity')
item = lazy_import('msgraph.generated.models.item')

class SalesInvoiceLine(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def account(self,) -> Optional[account.Account]:
        """
        Gets the account property value. The account property
        Returns: Optional[account.Account]
        """
        return self._account
    
    @account.setter
    def account(self,value: Optional[account.Account] = None) -> None:
        """
        Sets the account property value. The account property
        Args:
            value: Value to set for the account property.
        """
        self._account = value
    
    @property
    def account_id(self,) -> Optional[Guid]:
        """
        Gets the accountId property value. The accountId property
        Returns: Optional[Guid]
        """
        return self._account_id
    
    @account_id.setter
    def account_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the accountId property value. The accountId property
        Args:
            value: Value to set for the accountId property.
        """
        self._account_id = value
    
    @property
    def amount_excluding_tax(self,) -> Optional[float]:
        """
        Gets the amountExcludingTax property value. The amountExcludingTax property
        Returns: Optional[float]
        """
        return self._amount_excluding_tax
    
    @amount_excluding_tax.setter
    def amount_excluding_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the amountExcludingTax property value. The amountExcludingTax property
        Args:
            value: Value to set for the amountExcludingTax property.
        """
        self._amount_excluding_tax = value
    
    @property
    def amount_including_tax(self,) -> Optional[float]:
        """
        Gets the amountIncludingTax property value. The amountIncludingTax property
        Returns: Optional[float]
        """
        return self._amount_including_tax
    
    @amount_including_tax.setter
    def amount_including_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the amountIncludingTax property value. The amountIncludingTax property
        Args:
            value: Value to set for the amountIncludingTax property.
        """
        self._amount_including_tax = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new salesInvoiceLine and sets the default values.
        """
        super().__init__()
        # The account property
        self._account: Optional[account.Account] = None
        # The accountId property
        self._account_id: Optional[Guid] = None
        # The amountExcludingTax property
        self._amount_excluding_tax: Optional[float] = None
        # The amountIncludingTax property
        self._amount_including_tax: Optional[float] = None
        # The description property
        self._description: Optional[str] = None
        # The discountAmount property
        self._discount_amount: Optional[float] = None
        # The discountAppliedBeforeTax property
        self._discount_applied_before_tax: Optional[bool] = None
        # The discountPercent property
        self._discount_percent: Optional[float] = None
        # The documentId property
        self._document_id: Optional[Guid] = None
        # The invoiceDiscountAllocation property
        self._invoice_discount_allocation: Optional[float] = None
        # The item property
        self._item: Optional[item.Item] = None
        # The itemId property
        self._item_id: Optional[Guid] = None
        # The lineType property
        self._line_type: Optional[str] = None
        # The netAmount property
        self._net_amount: Optional[float] = None
        # The netAmountIncludingTax property
        self._net_amount_including_tax: Optional[float] = None
        # The netTaxAmount property
        self._net_tax_amount: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The quantity property
        self._quantity: Optional[float] = None
        # The sequence property
        self._sequence: Optional[int] = None
        # The shipmentDate property
        self._shipment_date: Optional[Date] = None
        # The taxCode property
        self._tax_code: Optional[str] = None
        # The taxPercent property
        self._tax_percent: Optional[float] = None
        # The totalTaxAmount property
        self._total_tax_amount: Optional[float] = None
        # The unitOfMeasureId property
        self._unit_of_measure_id: Optional[Guid] = None
        # The unitPrice property
        self._unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SalesInvoiceLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SalesInvoiceLine
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SalesInvoiceLine()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
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
    def discount_percent(self,) -> Optional[float]:
        """
        Gets the discountPercent property value. The discountPercent property
        Returns: Optional[float]
        """
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self,value: Optional[float] = None) -> None:
        """
        Sets the discountPercent property value. The discountPercent property
        Args:
            value: Value to set for the discountPercent property.
        """
        self._discount_percent = value
    
    @property
    def document_id(self,) -> Optional[Guid]:
        """
        Gets the documentId property value. The documentId property
        Returns: Optional[Guid]
        """
        return self._document_id
    
    @document_id.setter
    def document_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the documentId property value. The documentId property
        Args:
            value: Value to set for the documentId property.
        """
        self._document_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(account.Account)),
            "account_id": lambda n : setattr(self, 'account_id', n.get_object_value(Guid)),
            "amount_excluding_tax": lambda n : setattr(self, 'amount_excluding_tax', n.get_float_value()),
            "amount_including_tax": lambda n : setattr(self, 'amount_including_tax', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discount_amount": lambda n : setattr(self, 'discount_amount', n.get_float_value()),
            "discount_applied_before_tax": lambda n : setattr(self, 'discount_applied_before_tax', n.get_bool_value()),
            "discount_percent": lambda n : setattr(self, 'discount_percent', n.get_float_value()),
            "document_id": lambda n : setattr(self, 'document_id', n.get_object_value(Guid)),
            "invoice_discount_allocation": lambda n : setattr(self, 'invoice_discount_allocation', n.get_float_value()),
            "item": lambda n : setattr(self, 'item', n.get_object_value(item.Item)),
            "item_id": lambda n : setattr(self, 'item_id', n.get_object_value(Guid)),
            "line_type": lambda n : setattr(self, 'line_type', n.get_str_value()),
            "net_amount": lambda n : setattr(self, 'net_amount', n.get_float_value()),
            "net_amount_including_tax": lambda n : setattr(self, 'net_amount_including_tax', n.get_float_value()),
            "net_tax_amount": lambda n : setattr(self, 'net_tax_amount', n.get_float_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "shipment_date": lambda n : setattr(self, 'shipment_date', n.get_object_value(Date)),
            "tax_code": lambda n : setattr(self, 'tax_code', n.get_str_value()),
            "tax_percent": lambda n : setattr(self, 'tax_percent', n.get_float_value()),
            "total_tax_amount": lambda n : setattr(self, 'total_tax_amount', n.get_float_value()),
            "unit_of_measure_id": lambda n : setattr(self, 'unit_of_measure_id', n.get_object_value(Guid)),
            "unit_price": lambda n : setattr(self, 'unit_price', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invoice_discount_allocation(self,) -> Optional[float]:
        """
        Gets the invoiceDiscountAllocation property value. The invoiceDiscountAllocation property
        Returns: Optional[float]
        """
        return self._invoice_discount_allocation
    
    @invoice_discount_allocation.setter
    def invoice_discount_allocation(self,value: Optional[float] = None) -> None:
        """
        Sets the invoiceDiscountAllocation property value. The invoiceDiscountAllocation property
        Args:
            value: Value to set for the invoiceDiscountAllocation property.
        """
        self._invoice_discount_allocation = value
    
    @property
    def item(self,) -> Optional[item.Item]:
        """
        Gets the item property value. The item property
        Returns: Optional[item.Item]
        """
        return self._item
    
    @item.setter
    def item(self,value: Optional[item.Item] = None) -> None:
        """
        Sets the item property value. The item property
        Args:
            value: Value to set for the item property.
        """
        self._item = value
    
    @property
    def item_id(self,) -> Optional[Guid]:
        """
        Gets the itemId property value. The itemId property
        Returns: Optional[Guid]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the itemId property value. The itemId property
        Args:
            value: Value to set for the itemId property.
        """
        self._item_id = value
    
    @property
    def line_type(self,) -> Optional[str]:
        """
        Gets the lineType property value. The lineType property
        Returns: Optional[str]
        """
        return self._line_type
    
    @line_type.setter
    def line_type(self,value: Optional[str] = None) -> None:
        """
        Sets the lineType property value. The lineType property
        Args:
            value: Value to set for the lineType property.
        """
        self._line_type = value
    
    @property
    def net_amount(self,) -> Optional[float]:
        """
        Gets the netAmount property value. The netAmount property
        Returns: Optional[float]
        """
        return self._net_amount
    
    @net_amount.setter
    def net_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the netAmount property value. The netAmount property
        Args:
            value: Value to set for the netAmount property.
        """
        self._net_amount = value
    
    @property
    def net_amount_including_tax(self,) -> Optional[float]:
        """
        Gets the netAmountIncludingTax property value. The netAmountIncludingTax property
        Returns: Optional[float]
        """
        return self._net_amount_including_tax
    
    @net_amount_including_tax.setter
    def net_amount_including_tax(self,value: Optional[float] = None) -> None:
        """
        Sets the netAmountIncludingTax property value. The netAmountIncludingTax property
        Args:
            value: Value to set for the netAmountIncludingTax property.
        """
        self._net_amount_including_tax = value
    
    @property
    def net_tax_amount(self,) -> Optional[float]:
        """
        Gets the netTaxAmount property value. The netTaxAmount property
        Returns: Optional[float]
        """
        return self._net_tax_amount
    
    @net_tax_amount.setter
    def net_tax_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the netTaxAmount property value. The netTaxAmount property
        Args:
            value: Value to set for the netTaxAmount property.
        """
        self._net_tax_amount = value
    
    @property
    def quantity(self,) -> Optional[float]:
        """
        Gets the quantity property value. The quantity property
        Returns: Optional[float]
        """
        return self._quantity
    
    @quantity.setter
    def quantity(self,value: Optional[float] = None) -> None:
        """
        Sets the quantity property value. The quantity property
        Args:
            value: Value to set for the quantity property.
        """
        self._quantity = value
    
    @property
    def sequence(self,) -> Optional[int]:
        """
        Gets the sequence property value. The sequence property
        Returns: Optional[int]
        """
        return self._sequence
    
    @sequence.setter
    def sequence(self,value: Optional[int] = None) -> None:
        """
        Sets the sequence property value. The sequence property
        Args:
            value: Value to set for the sequence property.
        """
        self._sequence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("account", self.account)
        writer.write_object_value("accountId", self.account_id)
        writer.write_float_value("amountExcludingTax", self.amount_excluding_tax)
        writer.write_float_value("amountIncludingTax", self.amount_including_tax)
        writer.write_str_value("description", self.description)
        writer.write_float_value("discountAmount", self.discount_amount)
        writer.write_bool_value("discountAppliedBeforeTax", self.discount_applied_before_tax)
        writer.write_float_value("discountPercent", self.discount_percent)
        writer.write_object_value("documentId", self.document_id)
        writer.write_float_value("invoiceDiscountAllocation", self.invoice_discount_allocation)
        writer.write_object_value("item", self.item)
        writer.write_object_value("itemId", self.item_id)
        writer.write_str_value("lineType", self.line_type)
        writer.write_float_value("netAmount", self.net_amount)
        writer.write_float_value("netAmountIncludingTax", self.net_amount_including_tax)
        writer.write_float_value("netTaxAmount", self.net_tax_amount)
        writer.write_float_value("quantity", self.quantity)
        writer.write_int_value("sequence", self.sequence)
        writer.write_object_value("shipmentDate", self.shipment_date)
        writer.write_str_value("taxCode", self.tax_code)
        writer.write_float_value("taxPercent", self.tax_percent)
        writer.write_float_value("totalTaxAmount", self.total_tax_amount)
        writer.write_object_value("unitOfMeasureId", self.unit_of_measure_id)
        writer.write_float_value("unitPrice", self.unit_price)
    
    @property
    def shipment_date(self,) -> Optional[Date]:
        """
        Gets the shipmentDate property value. The shipmentDate property
        Returns: Optional[Date]
        """
        return self._shipment_date
    
    @shipment_date.setter
    def shipment_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the shipmentDate property value. The shipmentDate property
        Args:
            value: Value to set for the shipmentDate property.
        """
        self._shipment_date = value
    
    @property
    def tax_code(self,) -> Optional[str]:
        """
        Gets the taxCode property value. The taxCode property
        Returns: Optional[str]
        """
        return self._tax_code
    
    @tax_code.setter
    def tax_code(self,value: Optional[str] = None) -> None:
        """
        Sets the taxCode property value. The taxCode property
        Args:
            value: Value to set for the taxCode property.
        """
        self._tax_code = value
    
    @property
    def tax_percent(self,) -> Optional[float]:
        """
        Gets the taxPercent property value. The taxPercent property
        Returns: Optional[float]
        """
        return self._tax_percent
    
    @tax_percent.setter
    def tax_percent(self,value: Optional[float] = None) -> None:
        """
        Sets the taxPercent property value. The taxPercent property
        Args:
            value: Value to set for the taxPercent property.
        """
        self._tax_percent = value
    
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
    def unit_of_measure_id(self,) -> Optional[Guid]:
        """
        Gets the unitOfMeasureId property value. The unitOfMeasureId property
        Returns: Optional[Guid]
        """
        return self._unit_of_measure_id
    
    @unit_of_measure_id.setter
    def unit_of_measure_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the unitOfMeasureId property value. The unitOfMeasureId property
        Args:
            value: Value to set for the unitOfMeasureId property.
        """
        self._unit_of_measure_id = value
    
    @property
    def unit_price(self,) -> Optional[float]:
        """
        Gets the unitPrice property value. The unitPrice property
        Returns: Optional[float]
        """
        return self._unit_price
    
    @unit_price.setter
    def unit_price(self,value: Optional[float] = None) -> None:
        """
        Sets the unitPrice property value. The unitPrice property
        Args:
            value: Value to set for the unitPrice property.
        """
        self._unit_price = value
    

