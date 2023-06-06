from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import payload_detail

from . import payload_detail

@dataclass
class EmailPayloadDetail(payload_detail.PayloadDetail):
    odata_type = "#microsoft.graph.emailPayloadDetail"
    # Email address of the user.
    from_email: Optional[str] = None
    # Display name of the user.
    from_name: Optional[str] = None
    # Indicates whether the sender is not from the user's organization.
    is_external_sender: Optional[bool] = None
    # The subject of the email address sent to the user.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailPayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailPayloadDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailPayloadDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import payload_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "fromEmail": lambda n : setattr(self, 'from_email', n.get_str_value()),
            "fromName": lambda n : setattr(self, 'from_name', n.get_str_value()),
            "isExternalSender": lambda n : setattr(self, 'is_external_sender', n.get_bool_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_str_value("fromEmail", self.from_email)
        writer.write_str_value("fromName", self.from_name)
        writer.write_bool_value("isExternalSender", self.is_external_sender)
        writer.write_str_value("subject", self.subject)
    

