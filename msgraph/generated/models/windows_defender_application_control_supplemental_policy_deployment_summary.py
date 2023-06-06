from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary(entity.Entity):
    # Number of Devices that have successfully deployed this WindowsDefenderApplicationControl supplemental policy.
    deployed_device_count: Optional[int] = None
    # Number of Devices that have failed to deploy this WindowsDefenderApplicationControl supplemental policy.
    failed_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deployedDeviceCount": lambda n : setattr(self, 'deployed_device_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
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
    

