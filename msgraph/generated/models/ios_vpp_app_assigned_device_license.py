from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_vpp_app_assigned_license

from . import ios_vpp_app_assigned_license

@dataclass
class IosVppAppAssignedDeviceLicense(ios_vpp_app_assigned_license.IosVppAppAssignedLicense):
    # The device name.
    device_name: Optional[str] = None
    # The managed device ID.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppAppAssignedDeviceLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignedDeviceLicense
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosVppAppAssignedDeviceLicense()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_vpp_app_assigned_license

        from . import ios_vpp_app_assigned_license

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
    

