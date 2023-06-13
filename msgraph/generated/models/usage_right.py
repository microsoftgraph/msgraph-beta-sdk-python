from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, usage_right_state

from . import entity

@dataclass
class UsageRight(entity.Entity):
    # Product id corresponding to the usage right.
    catalog_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of the service corresponding to the usage right.
    service_identifier: Optional[str] = None
    # The state property
    state: Optional[usage_right_state.UsageRightState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UsageRight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UsageRight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UsageRight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, usage_right_state

        fields: Dict[str, Callable[[Any], None]] = {
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "serviceIdentifier": lambda n : setattr(self, 'service_identifier', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(usage_right_state.UsageRightState)),
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
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_str_value("serviceIdentifier", self.service_identifier)
        writer.write_enum_value("state", self.state)
    

