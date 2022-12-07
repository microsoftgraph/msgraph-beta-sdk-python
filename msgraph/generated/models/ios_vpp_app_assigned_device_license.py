from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_vpp_app_assigned_license = lazy_import('msgraph.generated.models.ios_vpp_app_assigned_license')

class IosVppAppAssignedDeviceLicense(ios_vpp_app_assigned_license.IosVppAppAssignedLicense):
    def __init__(self,) -> None:
        """
        Instantiates a new IosVppAppAssignedDeviceLicense and sets the default values.
        """
        super().__init__()
        # The device name.
        self._device_name: Optional[str] = None
        # The managed device ID.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppAppAssignedDeviceLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignedDeviceLicense
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVppAppAssignedDeviceLicense()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The managed device ID.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The managed device ID.
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
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
    

