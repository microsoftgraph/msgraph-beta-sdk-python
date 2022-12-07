from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory(entity.Entity):
    """
    The user experience analytics battery health runtime history entity contains the trend of runtime of a device over a period of 30 days
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory and sets the default values.
        """
        super().__init__()
        # The unique identifier of the device, Intune DeviceID or SCCM device id.
        self._device_id: Optional[str] = None
        # The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        self._estimated_runtime_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The datetime for the instance of runtime history.
        self._runtime_date_time: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The unique identifier of the device, Intune DeviceID or SCCM device id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The unique identifier of the device, Intune DeviceID or SCCM device id.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def estimated_runtime_in_minutes(self,) -> Optional[int]:
        """
        Gets the estimatedRuntimeInMinutes property value. The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._estimated_runtime_in_minutes
    
    @estimated_runtime_in_minutes.setter
    def estimated_runtime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the estimatedRuntimeInMinutes property value. The estimated runtime of the device when the battery is fully charged. Unit in minutes. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the estimatedRuntimeInMinutes property.
        """
        self._estimated_runtime_in_minutes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "estimated_runtime_in_minutes": lambda n : setattr(self, 'estimated_runtime_in_minutes', n.get_int_value()),
            "runtime_date_time": lambda n : setattr(self, 'runtime_date_time', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def runtime_date_time(self,) -> Optional[str]:
        """
        Gets the runtimeDateTime property value. The datetime for the instance of runtime history.
        Returns: Optional[str]
        """
        return self._runtime_date_time
    
    @runtime_date_time.setter
    def runtime_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the runtimeDateTime property value. The datetime for the instance of runtime history.
        Args:
            value: Value to set for the runtimeDateTime property.
        """
        self._runtime_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("estimatedRuntimeInMinutes", self.estimated_runtime_in_minutes)
        writer.write_str_value("runtimeDateTime", self.runtime_date_time)
    

