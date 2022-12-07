from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary and sets the default values.
        """
        super().__init__()
        # Number of Devices that have successfully deployed this WindowsDefenderApplicationControl supplemental policy.
        self._deployed_device_count: Optional[int] = None
        # Number of Devices that have failed to deploy this WindowsDefenderApplicationControl supplemental policy.
        self._failed_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary()
    
    @property
    def deployed_device_count(self,) -> Optional[int]:
        """
        Gets the deployedDeviceCount property value. Number of Devices that have successfully deployed this WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[int]
        """
        return self._deployed_device_count
    
    @deployed_device_count.setter
    def deployed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedDeviceCount property value. Number of Devices that have successfully deployed this WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the deployedDeviceCount property.
        """
        self._deployed_device_count = value
    
    @property
    def failed_device_count(self,) -> Optional[int]:
        """
        Gets the failedDeviceCount property value. Number of Devices that have failed to deploy this WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[int]
        """
        return self._failed_device_count
    
    @failed_device_count.setter
    def failed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedDeviceCount property value. Number of Devices that have failed to deploy this WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the failedDeviceCount property.
        """
        self._failed_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deployed_device_count": lambda n : setattr(self, 'deployed_device_count', n.get_int_value()),
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
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
        writer.write_int_value("deployedDeviceCount", self.deployed_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
    

