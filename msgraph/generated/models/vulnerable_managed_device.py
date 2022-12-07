from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class VulnerableManagedDevice(entity.Entity):
    """
    This entity represents a device associated with a task.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new vulnerableManagedDevice and sets the default values.
        """
        super().__init__()
        # The device name.
        self._display_name: Optional[str] = None
        # The last sync date.
        self._last_sync_date_time: Optional[datetime] = None
        # The Intune managed device ID.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VulnerableManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VulnerableManagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VulnerableManagedDevice()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The device name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The device name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The last sync date.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The last sync date.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The Intune managed device ID.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The Intune managed device ID.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
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
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
    

