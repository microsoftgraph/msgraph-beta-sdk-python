from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_snapshot_status = lazy_import('msgraph.generated.models.cloud_pc_snapshot_status')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcSnapshot(entity.Entity):
    @property
    def cloud_pc_id(self,) -> Optional[str]:
        """
        Gets the cloudPcId property value. The unique identifier for the Cloud PC.
        Returns: Optional[str]
        """
        return self._cloud_pc_id
    
    @cloud_pc_id.setter
    def cloud_pc_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcId property value. The unique identifier for the Cloud PC.
        Args:
            value: Value to set for the cloudPcId property.
        """
        self._cloud_pc_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcSnapshot and sets the default values.
        """
        super().__init__()
        # The unique identifier for the Cloud PC.
        self._cloud_pc_id: Optional[str] = None
        # The date and time at which the snapshot was taken. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The date and time at which the snapshot was last used to restore the Cloud PC device. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_restored_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of the Cloud PC snapshot. The possible values are: ready, unknownFutureValue.
        self._status: Optional[cloud_pc_snapshot_status.CloudPcSnapshotStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time at which the snapshot was taken. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time at which the snapshot was taken. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSnapshot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcSnapshot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cloud_pc_id": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_restored_date_time": lambda n : setattr(self, 'last_restored_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_snapshot_status.CloudPcSnapshotStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_restored_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRestoredDateTime property value. The date and time at which the snapshot was last used to restore the Cloud PC device. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_restored_date_time
    
    @last_restored_date_time.setter
    def last_restored_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRestoredDateTime property value. The date and time at which the snapshot was last used to restore the Cloud PC device. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastRestoredDateTime property.
        """
        self._last_restored_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastRestoredDateTime", self.last_restored_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[cloud_pc_snapshot_status.CloudPcSnapshotStatus]:
        """
        Gets the status property value. The status of the Cloud PC snapshot. The possible values are: ready, unknownFutureValue.
        Returns: Optional[cloud_pc_snapshot_status.CloudPcSnapshotStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_snapshot_status.CloudPcSnapshotStatus] = None) -> None:
        """
        Sets the status property value. The status of the Cloud PC snapshot. The possible values are: ready, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

