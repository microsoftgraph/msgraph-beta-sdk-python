from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy import DeviceCompliancePolicy

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class DefaultDeviceCompliancePolicy(DeviceCompliancePolicy):
    """
    Default device compliance policy rules that are enforced account wide.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.defaultDeviceCompliancePolicy"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultDeviceCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultDeviceCompliancePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DefaultDeviceCompliancePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy import DeviceCompliancePolicy

        from .device_compliance_policy import DeviceCompliancePolicy

        fields: Dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

