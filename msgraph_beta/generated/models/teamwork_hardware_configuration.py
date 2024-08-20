from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkHardwareConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The compute property
    compute: Optional[TeamworkPeripheral] = None
    # The hdmiIngest property
    hdmi_ingest: Optional[TeamworkPeripheral] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The CPU model on the device.
    processor_model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkHardwareConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkHardwareConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_peripheral import TeamworkPeripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "compute": lambda n : setattr(self, 'compute', n.get_object_value(TeamworkPeripheral)),
            "hdmiIngest": lambda n : setattr(self, 'hdmi_ingest', n.get_object_value(TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processorModel": lambda n : setattr(self, 'processor_model', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("compute", self.compute)
        writer.write_object_value("hdmiIngest", self.hdmi_ingest)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("processorModel", self.processor_model)
        writer.write_additional_data_value(self.additional_data)
    

