from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_source, device_and_app_management_assignment_target, entity

from . import entity

@dataclass
class DeviceManagementConfigurationPolicyAssignment(entity.Entity):
    """
    The DeviceManagementConfigurationPolicyAssignment entity assigns a specific DeviceManagementConfigurationPolicy to an AAD group.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents source of assignment.
    source: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource] = None
    # The identifier of the source of the assignment.
    source_id: Optional[str] = None
    # The assignment target for the DeviceManagementConfigurationPolicy.
    target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationPolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicyAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationPolicyAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_source, device_and_app_management_assignment_target, entity

        from . import device_and_app_management_assignment_source, device_and_app_management_assignment_target, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "source": lambda n : setattr(self, 'source', n.get_enum_value(device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_enum_value("source", self.source)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_object_value("target", self.target)
    

