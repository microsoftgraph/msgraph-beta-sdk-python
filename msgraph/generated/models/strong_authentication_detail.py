from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class StrongAuthenticationDetail(Entity):
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
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return StrongAuthenticationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bytes_value("encryptedPinHashHistory", self.encrypted_pin_hash_history)
        writer.write_int_value("proofupTime", self.proofup_time)
    

