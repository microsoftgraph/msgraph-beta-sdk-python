from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import customer, entity

from . import entity

class CustomerPayment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new customerPayment and sets the default values.
        """
        super().__init__()
        # The amount property
        self._amount: Optional[float] = None
        # The appliesToInvoiceId property
        self._applies_to_invoice_id: Optional[UUID] = None
        # The appliesToInvoiceNumber property
        self._applies_to_invoice_number: Optional[str] = None
        # The comment property
        self._comment: Optional[str] = None
        # The contactId property
        self._contact_id: Optional[str] = None
        # The customer property
        self._customer: Optional[customer.Customer] = None
        # The customerId property
        self._customer_id: Optional[UUID] = None
        # The customerNumber property
        self._customer_number: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The documentNumber property
        self._document_number: Optional[str] = None
        # The externalDocumentNumber property
        self._external_document_number: Optional[str] = None
        # The journalDisplayName property
        self._journal_display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The lineNumber property
        self._line_number: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The postingDate property
        self._posting_date: Optional[date] = None
    
    @property
    def amount(self,) -> Optional[float]:
        """
        Gets the amount property value. The amount property
        Returns: Optional[float]
        """
        return self._amount
    
    @amount.setter
    def amount(self,value: Optional[float] = None) -> None:
        """
        Sets the amount property value. The amount property
        Args:
            value: Value to set for the amount property.
        """
        self._amount = value
    
    @property
    def applies_to_invoice_id(self,) -> Optional[UUID]:
        """
        Gets the appliesToInvoiceId property value. The appliesToInvoiceId property
        Returns: Optional[UUID]
        """
        return self._applies_to_invoice_id
    
    @applies_to_invoice_id.setter
    def applies_to_invoice_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the appliesToInvoiceId property value. The appliesToInvoiceId property
        Args:
            value: Value to set for the applies_to_invoice_id property.
        """
        self._applies_to_invoice_id = value
    
    @property
    def applies_to_invoice_number(self,) -> Optional[str]:
        """
        Gets the appliesToInvoiceNumber property value. The appliesToInvoiceNumber property
        Returns: Optional[str]
        """
        return self._applies_to_invoice_number
    
    @applies_to_invoice_number.setter
    def applies_to_invoice_number(self,value: Optional[str] = None) -> None:
        """
        Sets the appliesToInvoiceNumber property value. The appliesToInvoiceNumber property
        Args:
            value: Value to set for the applies_to_invoice_number property.
        """
        self._applies_to_invoice_number = value
    
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment property
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment property
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    @property
    def contact_id(self,) -> Optional[str]:
        """
        Gets the contactId property value. The contactId property
        Returns: Optional[str]
        """
        return self._contact_id
    
    @contact_id.setter
    def contact_id(self,value: Optional[str] = None) -> None:
        """
        Sets the contactId property value. The contactId property
        Args:
            value: Value to set for the contact_id property.
        """
        self._contact_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomerPayment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomerPayment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomerPayment()
    
    @property
    def customer(self,) -> Optional[customer.Customer]:
        """
        Gets the customer property value. The customer property
        Returns: Optional[customer.Customer]
        """
        return self._customer
    
    @customer.setter
    def customer(self,value: Optional[customer.Customer] = None) -> None:
        """
        Sets the customer property value. The customer property
        Args:
            value: Value to set for the customer property.
        """
        self._customer = value
    
    @property
    def customer_id(self,) -> Optional[UUID]:
        """
        Gets the customerId property value. The customerId property
        Returns: Optional[UUID]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the customerId property value. The customerId property
        Args:
            value: Value to set for the customer_id property.
        """
        self._customer_id = value
    
    @property
    def customer_number(self,) -> Optional[str]:
        """
        Gets the customerNumber property value. The customerNumber property
        Returns: Optional[str]
        """
        return self._customer_number
    
    @customer_number.setter
    def customer_number(self,value: Optional[str] = None) -> None:
        """
        Sets the customerNumber property value. The customerNumber property
        Args:
            value: Value to set for the customer_number property.
        """
        self._customer_number = value
    
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
    def document_number(self,) -> Optional[str]:
        """
        Gets the documentNumber property value. The documentNumber property
        Returns: Optional[str]
        """
        return self._document_number
    
    @document_number.setter
    def document_number(self,value: Optional[str] = None) -> None:
        """
        Sets the documentNumber property value. The documentNumber property
        Args:
            value: Value to set for the document_number property.
        """
        self._document_number = value
    
    @property
    def external_document_number(self,) -> Optional[str]:
        """
        Gets the externalDocumentNumber property value. The externalDocumentNumber property
        Returns: Optional[str]
        """
        return self._external_document_number
    
    @external_document_number.setter
    def external_document_number(self,value: Optional[str] = None) -> None:
        """
        Sets the externalDocumentNumber property value. The externalDocumentNumber property
        Args:
            value: Value to set for the external_document_number property.
        """
        self._external_document_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import customer, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "appliesToInvoiceId": lambda n : setattr(self, 'applies_to_invoice_id', n.get_uuid_value()),
            "appliesToInvoiceNumber": lambda n : setattr(self, 'applies_to_invoice_number', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "contactId": lambda n : setattr(self, 'contact_id', n.get_str_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(customer.Customer)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "customerNumber": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentNumber": lambda n : setattr(self, 'document_number', n.get_str_value()),
            "externalDocumentNumber": lambda n : setattr(self, 'external_document_number', n.get_str_value()),
            "journalDisplayName": lambda n : setattr(self, 'journal_display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lineNumber": lambda n : setattr(self, 'line_number', n.get_int_value()),
            "postingDate": lambda n : setattr(self, 'posting_date', n.get_date_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def journal_display_name(self,) -> Optional[str]:
        """
        Gets the journalDisplayName property value. The journalDisplayName property
        Returns: Optional[str]
        """
        return self._journal_display_name
    
    @journal_display_name.setter
    def journal_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the journalDisplayName property value. The journalDisplayName property
        Args:
            value: Value to set for the journal_display_name property.
        """
        self._journal_display_name = value
    
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
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def line_number(self,) -> Optional[int]:
        """
        Gets the lineNumber property value. The lineNumber property
        Returns: Optional[int]
        """
        return self._line_number
    
    @line_number.setter
    def line_number(self,value: Optional[int] = None) -> None:
        """
        Sets the lineNumber property value. The lineNumber property
        Args:
            value: Value to set for the line_number property.
        """
        self._line_number = value
    
    @property
    def posting_date(self,) -> Optional[date]:
        """
        Gets the postingDate property value. The postingDate property
        Returns: Optional[date]
        """
        return self._posting_date
    
    @posting_date.setter
    def posting_date(self,value: Optional[date] = None) -> None:
        """
        Sets the postingDate property value. The postingDate property
        Args:
            value: Value to set for the posting_date property.
        """
        self._posting_date = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("amount", self.amount)
        writer.write_uuid_value("appliesToInvoiceId", self.applies_to_invoice_id)
        writer.write_str_value("appliesToInvoiceNumber", self.applies_to_invoice_number)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("contactId", self.contact_id)
        writer.write_object_value("customer", self.customer)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_str_value("customerNumber", self.customer_number)
        writer.write_str_value("description", self.description)
        writer.write_str_value("documentNumber", self.document_number)
        writer.write_str_value("externalDocumentNumber", self.external_document_number)
        writer.write_str_value("journalDisplayName", self.journal_display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("lineNumber", self.line_number)
        writer.write_date_value("postingDate", self.posting_date)
    

