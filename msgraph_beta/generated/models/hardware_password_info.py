from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class HardwarePasswordInfo(Entity, Parsable):
    """
    Intune will provide customer the ability to configure hardware/bios settings on the enrolled windows 10 Azure Active Directory joined devices. Starting from June, 2024 (Intune Release 2406), this type will no longer be supported and will be marked as deprecated
    """
    # Current device password. This property is read-only.
    current_password: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of previous device passwords. This property is read-only.
    previous_passwords: Optional[List[str]] = None
    # Associated device's serial number . This property is read-only.
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwarePasswordInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwarePasswordInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwarePasswordInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "currentPassword": lambda n : setattr(self, 'current_password', n.get_str_value()),
            "previousPasswords": lambda n : setattr(self, 'previous_passwords', n.get_collection_of_primitive_values(str)),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .entity import Entity

        writer.write_str_value("serialNumber", self.serial_number)
    

