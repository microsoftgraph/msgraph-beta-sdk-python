from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import account, entity

from . import entity

@dataclass
class GeneralLedgerEntry(entity.Entity):
    # The account property
    account: Optional[account.Account] = None
    # The accountId property
    account_id: Optional[UUID] = None
    # The accountNumber property
    account_number: Optional[str] = None
    # The creditAmount property
    credit_amount: Optional[float] = None
    # The debitAmount property
    debit_amount: Optional[float] = None
    # The description property
    description: Optional[str] = None
    # The documentNumber property
    document_number: Optional[str] = None
    # The documentType property
    document_type: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The postingDate property
    posting_date: Optional[date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GeneralLedgerEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GeneralLedgerEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GeneralLedgerEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(account.Account)),
            "accountId": lambda n : setattr(self, 'account_id', n.get_uuid_value()),
            "accountNumber": lambda n : setattr(self, 'account_number', n.get_str_value()),
            "creditAmount": lambda n : setattr(self, 'credit_amount', n.get_float_value()),
            "debitAmount": lambda n : setattr(self, 'debit_amount', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentNumber": lambda n : setattr(self, 'document_number', n.get_str_value()),
            "documentType": lambda n : setattr(self, 'document_type', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("account", self.account)
        writer.write_uuid_value("accountId", self.account_id)
        writer.write_str_value("accountNumber", self.account_number)
        writer.write_float_value("creditAmount", self.credit_amount)
        writer.write_float_value("debitAmount", self.debit_amount)
        writer.write_str_value("description", self.description)
        writer.write_str_value("documentNumber", self.document_number)
        writer.write_str_value("documentType", self.document_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_date_value("postingDate", self.posting_date)
    

