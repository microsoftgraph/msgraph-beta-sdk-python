from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class StrongAuthenticationDetail(entity.Entity):
    # The encryptedPinHashHistory property
    encrypted_pin_hash_history: Optional[bytes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The proofupTime property
    proofup_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StrongAuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StrongAuthenticationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "encryptedPinHashHistory": lambda n : setattr(self, 'encrypted_pin_hash_history', n.get_bytes_value()),
            "proofupTime": lambda n : setattr(self, 'proofup_time', n.get_int_value()),
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
        writer.write_object_value("encryptedPinHashHistory", self.encrypted_pin_hash_history)
        writer.write_int_value("proofupTime", self.proofup_time)
    

