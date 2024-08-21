from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .account import Account

@dataclass
class JournalLine(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The account property
    account: Optional[Account] = None
    # The accountId property
    account_id: Optional[UUID] = None
    # The accountNumber property
    account_number: Optional[str] = None
    # The amount property
    amount: Optional[float] = None
    # The comment property
    comment: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The documentNumber property
    document_number: Optional[str] = None
    # The externalDocumentNumber property
    external_document_number: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The journalDisplayName property
    journal_display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The lineNumber property
    line_number: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The postingDate property
    posting_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JournalLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JournalLine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JournalLine()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account import Account

        from .account import Account

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(Account)),
            "accountId": lambda n : setattr(self, 'account_id', n.get_uuid_value()),
            "accountNumber": lambda n : setattr(self, 'account_number', n.get_str_value()),
            "amount": lambda n : setattr(self, 'amount', n.get_float_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentNumber": lambda n : setattr(self, 'document_number', n.get_str_value()),
            "externalDocumentNumber": lambda n : setattr(self, 'external_document_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "journalDisplayName": lambda n : setattr(self, 'journal_display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lineNumber": lambda n : setattr(self, 'line_number', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postingDate": lambda n : setattr(self, 'posting_date', n.get_date_value()),
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
        writer.write_object_value("account", self.account)
        writer.write_uuid_value("accountId", self.account_id)
        writer.write_str_value("accountNumber", self.account_number)
        writer.write_float_value("amount", self.amount)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("description", self.description)
        writer.write_str_value("documentNumber", self.document_number)
        writer.write_str_value("externalDocumentNumber", self.external_document_number)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("journalDisplayName", self.journal_display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("lineNumber", self.line_number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_date_value("postingDate", self.posting_date)
        writer.write_additional_data_value(self.additional_data)
    

