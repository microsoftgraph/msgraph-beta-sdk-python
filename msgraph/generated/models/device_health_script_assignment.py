from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_target, device_health_script_run_schedule, entity

from . import entity

@dataclass
class DeviceHealthScriptAssignment(entity.Entity):
    """
    Contains properties used to assign a device management script to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Determine whether we want to run detection script only or run both detection script and remediation script
    run_remediation_script: Optional[bool] = None
    # Script run schedule for the target group
    run_schedule: Optional[device_health_script_run_schedule.DeviceHealthScriptRunSchedule] = None
    # The Azure Active Directory group we are targeting the script to
    target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_target, device_health_script_run_schedule, entity

        from . import device_and_app_management_assignment_target, device_health_script_run_schedule, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "runRemediationScript": lambda n : setattr(self, 'run_remediation_script', n.get_bool_value()),
            "runSchedule": lambda n : setattr(self, 'run_schedule', n.get_object_value(device_health_script_run_schedule.DeviceHealthScriptRunSchedule)),
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
        writer.write_bool_value("runRemediationScript", self.run_remediation_script)
        writer.write_object_value("runSchedule", self.run_schedule)
        writer.write_object_value("target", self.target)
    

