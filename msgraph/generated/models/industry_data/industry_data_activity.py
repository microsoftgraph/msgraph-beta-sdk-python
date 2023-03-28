from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_file_flow, inbound_flow, readiness_status
    from .. import entity

from .. import entity

class IndustryDataActivity(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataActivity and sets the default values.
        """
        super().__init__()
        # The name of the activity. Maximum supported length is 100 characters.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The readinessStatus property
        self._readiness_status: Optional[readiness_status.ReadinessStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.inboundFileFlow":
                from . import inbound_file_flow

                return inbound_file_flow.InboundFileFlow()
            if mapping_value == "#microsoft.graph.industryData.inboundFlow":
                from . import inbound_flow

                return inbound_flow.InboundFlow()
        return IndustryDataActivity()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the activity. Maximum supported length is 100 characters.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the activity. Maximum supported length is 100 characters.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_file_flow, inbound_flow, readiness_status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "readinessStatus": lambda n : setattr(self, 'readiness_status', n.get_enum_value(readiness_status.ReadinessStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def readiness_status(self,) -> Optional[readiness_status.ReadinessStatus]:
        """
        Gets the readinessStatus property value. The readinessStatus property
        Returns: Optional[readiness_status.ReadinessStatus]
        """
        return self._readiness_status
    
    @readiness_status.setter
    def readiness_status(self,value: Optional[readiness_status.ReadinessStatus] = None) -> None:
        """
        Sets the readinessStatus property value. The readinessStatus property
        Args:
            value: Value to set for the readiness_status property.
        """
        self._readiness_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("readinessStatus", self.readiness_status)
    

