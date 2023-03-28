from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class DeviceManagementScriptRunSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementScriptRunSummary and sets the default values.
        """
        super().__init__()
        # Error device count.
        self._error_device_count: Optional[int] = None
        # Error user count.
        self._error_user_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Success device count.
        self._success_device_count: Optional[int] = None
        # Success user count.
        self._success_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementScriptRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptRunSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementScriptRunSummary()
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Error device count.
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Error device count.
        Args:
            value: Value to set for the error_device_count property.
        """
        self._error_device_count = value
    
    @property
    def error_user_count(self,) -> Optional[int]:
        """
        Gets the errorUserCount property value. Error user count.
        Returns: Optional[int]
        """
        return self._error_user_count
    
    @error_user_count.setter
    def error_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorUserCount property value. Error user count.
        Args:
            value: Value to set for the error_user_count property.
        """
        self._error_user_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "errorUserCount": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "successDeviceCount": lambda n : setattr(self, 'success_device_count', n.get_int_value()),
            "successUserCount": lambda n : setattr(self, 'success_user_count', n.get_int_value()),
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
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("successDeviceCount", self.success_device_count)
        writer.write_int_value("successUserCount", self.success_user_count)
    
    @property
    def success_device_count(self,) -> Optional[int]:
        """
        Gets the successDeviceCount property value. Success device count.
        Returns: Optional[int]
        """
        return self._success_device_count
    
    @success_device_count.setter
    def success_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successDeviceCount property value. Success device count.
        Args:
            value: Value to set for the success_device_count property.
        """
        self._success_device_count = value
    
    @property
    def success_user_count(self,) -> Optional[int]:
        """
        Gets the successUserCount property value. Success user count.
        Returns: Optional[int]
        """
        return self._success_user_count
    
    @success_user_count.setter
    def success_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successUserCount property value. Success user count.
        Args:
            value: Value to set for the success_user_count property.
        """
        self._success_user_count = value
    

