from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

restore_time_range = lazy_import('msgraph.generated.models.restore_time_range')

class BulkRestoreCloudPcPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the bulkRestoreCloudPc method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bulkRestoreCloudPcPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The managedDeviceIds property
        self._managed_device_ids: Optional[List[str]] = None
        # The restorePointDateTime property
        self._restore_point_date_time: Optional[datetime] = None
        # The timeRange property
        self._time_range: Optional[restore_time_range.RestoreTimeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BulkRestoreCloudPcPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BulkRestoreCloudPcPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BulkRestoreCloudPcPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "managed_device_ids": lambda n : setattr(self, 'managed_device_ids', n.get_collection_of_primitive_values(str)),
            "restore_point_date_time": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "time_range": lambda n : setattr(self, 'time_range', n.get_enum_value(restore_time_range.RestoreTimeRange)),
        }
        return fields
    
    @property
    def managed_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the managedDeviceIds property value. The managedDeviceIds property
        Returns: Optional[List[str]]
        """
        return self._managed_device_ids
    
    @managed_device_ids.setter
    def managed_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the managedDeviceIds property value. The managedDeviceIds property
        Args:
            value: Value to set for the managedDeviceIds property.
        """
        self._managed_device_ids = value
    
    @property
    def restore_point_date_time(self,) -> Optional[datetime]:
        """
        Gets the restorePointDateTime property value. The restorePointDateTime property
        Returns: Optional[datetime]
        """
        return self._restore_point_date_time
    
    @restore_point_date_time.setter
    def restore_point_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the restorePointDateTime property value. The restorePointDateTime property
        Args:
            value: Value to set for the restorePointDateTime property.
        """
        self._restore_point_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("managedDeviceIds", self.managed_device_ids)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_enum_value("timeRange", self.time_range)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_range(self,) -> Optional[restore_time_range.RestoreTimeRange]:
        """
        Gets the timeRange property value. The timeRange property
        Returns: Optional[restore_time_range.RestoreTimeRange]
        """
        return self._time_range
    
    @time_range.setter
    def time_range(self,value: Optional[restore_time_range.RestoreTimeRange] = None) -> None:
        """
        Sets the timeRange property value. The timeRange property
        Args:
            value: Value to set for the timeRange property.
        """
        self._time_range = value
    

