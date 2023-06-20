from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_file_flow, inbound_flow, readiness_status
    from .. import entity

from .. import entity

@dataclass
class IndustryDataActivity(entity.Entity):
    # The name of the activity. Maximum supported length is 100 characters.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The readinessStatus property
    readiness_status: Optional[readiness_status.ReadinessStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFileFlow".casefold():
            from . import inbound_file_flow

            return inbound_file_flow.InboundFileFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFlow".casefold():
            from . import inbound_flow

            return inbound_flow.InboundFlow()
        return IndustryDataActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_file_flow, inbound_flow, readiness_status
        from .. import entity

        from . import inbound_file_flow, inbound_flow, readiness_status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "readinessStatus": lambda n : setattr(self, 'readiness_status', n.get_enum_value(readiness_status.ReadinessStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("readinessStatus", self.readiness_status)
    

