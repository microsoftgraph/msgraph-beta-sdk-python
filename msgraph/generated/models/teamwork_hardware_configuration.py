from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_peripheral

@dataclass
class TeamworkHardwareConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The compute property
    compute: Optional[teamwork_peripheral.TeamworkPeripheral] = None
    # The hdmiIngest property
    hdmi_ingest: Optional[teamwork_peripheral.TeamworkPeripheral] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The CPU model on the device.
    processor_model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHardwareConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkHardwareConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_peripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "compute": lambda n : setattr(self, 'compute', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "hdmiIngest": lambda n : setattr(self, 'hdmi_ingest', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processorModel": lambda n : setattr(self, 'processor_model', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("compute", self.compute)
        writer.write_object_value("hdmiIngest", self.hdmi_ingest)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("processorModel", self.processor_model)
        writer.write_additional_data_value(self.additional_data)
    

