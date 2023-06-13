from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, volume_type

from . import entity

@dataclass
class BitlockerRecoveryKey(entity.Entity):
    # The date and time when the key was originally backed up to Azure Active Directory.
    created_date_time: Optional[datetime] = None
    # ID of the device the BitLocker key is originally backed up from.
    device_id: Optional[str] = None
    # The BitLocker recovery key.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of volume the BitLocker key is associated with. Possible values are: operatingSystemVolume, fixedDataVolume, removableDataVolume, unknownFutureValue.
    volume_type: Optional[volume_type.VolumeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitlockerRecoveryKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitlockerRecoveryKey
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitlockerRecoveryKey()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, volume_type

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "volumeType": lambda n : setattr(self, 'volume_type', n.get_enum_value(volume_type.VolumeType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("key", self.key)
        writer.write_enum_value("volumeType", self.volume_type)
    

