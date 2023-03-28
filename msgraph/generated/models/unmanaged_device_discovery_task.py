from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_app_management_task, unmanaged_device

from . import device_app_management_task

class UnmanagedDeviceDiscoveryTask(device_app_management_task.DeviceAppManagementTask):
    def __init__(self,) -> None:
        """
        Instantiates a new UnmanagedDeviceDiscoveryTask and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unmanagedDeviceDiscoveryTask"
        # Unmanaged devices discovered in the network.
        self._unmanaged_devices: Optional[List[unmanaged_device.UnmanagedDevice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnmanagedDeviceDiscoveryTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnmanagedDeviceDiscoveryTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnmanagedDeviceDiscoveryTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_app_management_task, unmanaged_device

        fields: Dict[str, Callable[[Any], None]] = {
            "unmanagedDevices": lambda n : setattr(self, 'unmanaged_devices', n.get_collection_of_object_values(unmanaged_device.UnmanagedDevice)),
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
        writer.write_collection_of_object_values("unmanagedDevices", self.unmanaged_devices)
    
    @property
    def unmanaged_devices(self,) -> Optional[List[unmanaged_device.UnmanagedDevice]]:
        """
        Gets the unmanagedDevices property value. Unmanaged devices discovered in the network.
        Returns: Optional[List[unmanaged_device.UnmanagedDevice]]
        """
        return self._unmanaged_devices
    
    @unmanaged_devices.setter
    def unmanaged_devices(self,value: Optional[List[unmanaged_device.UnmanagedDevice]] = None) -> None:
        """
        Sets the unmanagedDevices property value. Unmanaged devices discovered in the network.
        Args:
            value: Value to set for the unmanaged_devices property.
        """
        self._unmanaged_devices = value
    

