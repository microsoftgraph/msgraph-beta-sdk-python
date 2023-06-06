from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy, entity

from . import entity

@dataclass
class DeviceCompliancePolicyGroupAssignment(entity.Entity):
    # The navigation link to the  device compliance polic targeted.
    device_compliance_policy: Optional[device_compliance_policy.DeviceCompliancePolicy] = None
    # Indicates if this group is should be excluded. Defaults that the group should be included
    exclude_group: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Id of the AAD group we are targeting the device compliance policy to.
    target_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyGroupAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyGroupAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_policy, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCompliancePolicy": lambda n : setattr(self, 'device_compliance_policy', n.get_object_value(device_compliance_policy.DeviceCompliancePolicy)),
            "excludeGroup": lambda n : setattr(self, 'exclude_group', n.get_bool_value()),
            "targetGroupId": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
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
        writer.write_object_value("deviceCompliancePolicy", self.device_compliance_policy)
        writer.write_bool_value("excludeGroup", self.exclude_group)
        writer.write_str_value("targetGroupId", self.target_group_id)
    

