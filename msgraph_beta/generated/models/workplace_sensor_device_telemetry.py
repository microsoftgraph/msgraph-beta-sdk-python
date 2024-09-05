from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workplace_sensor_event_value import WorkplaceSensorEventValue
    from .workplace_sensor_type import WorkplaceSensorType

@dataclass
class WorkplaceSensorDeviceTelemetry(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The value of the sensor can be true or false. Use it for sensors that report binary values, such as occupancy or heartbeat.
    bool_value: Optional[bool] = None
    # The user-defined unique identifier of the device provided at the time of creation. Don't use the system generated identifier of the device.
    device_id: Optional[str] = None
    # The extra values associated with badge signals.
    event_value: Optional[WorkplaceSensorEventValue] = None
    # The value of the sensor as an integer. Use it for sensors that report numerical values, such as people count.
    int_value: Optional[int] = None
    # The additional information to indicate the location of the device.
    location_hint: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user-defined unique identifier of the sensor on the device. Optional. If the device has multiple sensors of the same type, the property must be provided to identify each sensor. If the device has unique sensor types, the property can be omitted. The default value is the sensor type.
    sensor_id: Optional[str] = None
    # The sensorType property
    sensor_type: Optional[WorkplaceSensorType] = None
    # The date and time when the sensor measured and reported its value. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkplaceSensorDeviceTelemetry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkplaceSensorDeviceTelemetry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkplaceSensorDeviceTelemetry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .workplace_sensor_event_value import WorkplaceSensorEventValue
        from .workplace_sensor_type import WorkplaceSensorType

        from .workplace_sensor_event_value import WorkplaceSensorEventValue
        from .workplace_sensor_type import WorkplaceSensorType

        fields: Dict[str, Callable[[Any], None]] = {
            "boolValue": lambda n : setattr(self, 'bool_value', n.get_bool_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "eventValue": lambda n : setattr(self, 'event_value', n.get_object_value(WorkplaceSensorEventValue)),
            "intValue": lambda n : setattr(self, 'int_value', n.get_int_value()),
            "locationHint": lambda n : setattr(self, 'location_hint', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensorId": lambda n : setattr(self, 'sensor_id', n.get_str_value()),
            "sensorType": lambda n : setattr(self, 'sensor_type', n.get_enum_value(WorkplaceSensorType)),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_bool_value("boolValue", self.bool_value)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_object_value("eventValue", self.event_value)
        writer.write_int_value("intValue", self.int_value)
        writer.write_str_value("locationHint", self.location_hint)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensorId", self.sensor_id)
        writer.write_enum_value("sensorType", self.sensor_type)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

