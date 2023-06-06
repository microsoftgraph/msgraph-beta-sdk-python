from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import customer, entity

from . import entity

@dataclass
class CustomerPayment(entity.Entity):
    # The amount property
    amount: Optional[float] = None
    # The appliesToInvoiceId property
    applies_to_invoice_id: Optional[UUID] = None
    # The appliesToInvoiceNumber property
    applies_to_invoice_number: Optional[str] = None
    # The comment property
    comment: Optional[str] = None
    # The contactId property
    contact_id: Optional[str] = None
    # The customer property
    customer: Optional[customer.Customer] = None
    # The customerId property
    customer_id: Optional[UUID] = None
    # The customerNumber property
    customer_number: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The documentNumber property
    document_number: Optional[str] = None
    # The externalDocumentNumber property
    external_document_number: Optional[str] = None
    # The journalDisplayName property
    journal_display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The lineNumber property
    line_number: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The postingDate property
    posting_date: Optional[date] = None
    
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
    

