from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class SharedEmailDomainInvitation(entity.Entity):
    # The expiryTime property
    expiry_time: Optional[datetime] = None
    # The invitationDomain property
    invitation_domain: Optional[str] = None
    # The invitationStatus property
    invitation_status: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedEmailDomainInvitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedEmailDomainInvitation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedEmailDomainInvitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "expiryTime": lambda n : setattr(self, 'expiry_time', n.get_datetime_value()),
            "invitationDomain": lambda n : setattr(self, 'invitation_domain', n.get_str_value()),
            "invitationStatus": lambda n : setattr(self, 'invitation_status', n.get_str_value()),
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
        writer.write_datetime_value("expiryTime", self.expiry_time)
        writer.write_str_value("invitationDomain", self.invitation_domain)
        writer.write_str_value("invitationStatus", self.invitation_status)
    

