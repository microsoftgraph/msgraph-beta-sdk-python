from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_id_entity_identifier import DeviceIdEntityIdentifier
    from .response_action import ResponseAction

from .response_action import ResponseAction

@dataclass
class InitiateInvestigationResponseAction(ResponseAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.initiateInvestigationResponseAction"
    # The identifier property
    identifier: Optional[DeviceIdEntityIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InitiateInvestigationResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InitiateInvestigationResponseAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InitiateInvestigationResponseAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_id_entity_identifier import DeviceIdEntityIdentifier
        from .response_action import ResponseAction

        from .device_id_entity_identifier import DeviceIdEntityIdentifier
        from .response_action import ResponseAction

        fields: Dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_collection_of_enum_values(DeviceIdEntityIdentifier)),
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
        writer.write_enum_value("identifier", self.identifier)
    

