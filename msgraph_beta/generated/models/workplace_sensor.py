from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workplace_sensor_type import WorkplaceSensorType

@dataclass
class WorkplaceSensor(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The display name of the sensor. Optional.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the place that the sensor detects. If the device is installed in a room equipped with a mailbox, this property should match the ExternalDirectoryObjectId or Microsoft Entra object ID of the room mailbox. If the sensor detects the same place as the location of the device, the property can be omitted. The default value is the place identifier of the device. Optional.
    place_id: Optional[str] = None
    # The user-defined unique identifier of the sensor on the device. If the device has multiple sensors of the same type, the property must be provided to identify each sensor. If the device has only one sensor of a type, the property can be omitted. The default value is the sensor type. Optional.
    sensor_id: Optional[str] = None
    # The sensorType property
    sensor_type: Optional[WorkplaceSensorType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkplaceSensor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkplaceSensor
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkplaceSensor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .workplace_sensor_type import WorkplaceSensorType

        from .workplace_sensor_type import WorkplaceSensorType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "sensorId": lambda n : setattr(self, 'sensor_id', n.get_str_value()),
            "sensorType": lambda n : setattr(self, 'sensor_type', n.get_enum_value(WorkplaceSensorType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("placeId", self.place_id)
        writer.write_str_value("sensorId", self.sensor_id)
        writer.write_enum_value("sensorType", self.sensor_type)
        writer.write_additional_data_value(self.additional_data)
    

