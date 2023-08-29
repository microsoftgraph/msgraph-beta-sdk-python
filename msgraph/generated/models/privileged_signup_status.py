from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .setup_status import SetupStatus

from .entity import Entity

@dataclass
class PrivilegedSignupStatus(Entity):
    # The isRegistered property
    is_registered: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[SetupStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedSignupStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedSignupStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedSignupStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .setup_status import SetupStatus

        from .entity import Entity
        from .setup_status import SetupStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "isRegistered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SetupStatus)),
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
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_enum_value("status", self.status)
    

