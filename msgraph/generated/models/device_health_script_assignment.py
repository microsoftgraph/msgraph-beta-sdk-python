from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_target = lazy_import('msgraph.generated.models.device_and_app_management_assignment_target')
device_health_script_run_schedule = lazy_import('msgraph.generated.models.device_health_script_run_schedule')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceHealthScriptAssignment(entity.Entity):
    """
    Contains properties used to assign a device management script to a group.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthScriptAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Determine whether we want to run detection script only or run both detection script and remediation script
        self._run_remediation_script: Optional[bool] = None
        # Script run schedule for the target group
        self._run_schedule: Optional[device_health_script_run_schedule.DeviceHealthScriptRunSchedule] = None
        # The Azure Active Directory group we are targeting the script to
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "run_remediation_script": lambda n : setattr(self, 'run_remediation_script', n.get_bool_value()),
            "run_schedule": lambda n : setattr(self, 'run_schedule', n.get_object_value(device_health_script_run_schedule.DeviceHealthScriptRunSchedule)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def run_remediation_script(self,) -> Optional[bool]:
        """
        Gets the runRemediationScript property value. Determine whether we want to run detection script only or run both detection script and remediation script
        Returns: Optional[bool]
        """
        return self._run_remediation_script
    
    @run_remediation_script.setter
    def run_remediation_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the runRemediationScript property value. Determine whether we want to run detection script only or run both detection script and remediation script
        Args:
            value: Value to set for the runRemediationScript property.
        """
        self._run_remediation_script = value
    
    @property
    def run_schedule(self,) -> Optional[device_health_script_run_schedule.DeviceHealthScriptRunSchedule]:
        """
        Gets the runSchedule property value. Script run schedule for the target group
        Returns: Optional[device_health_script_run_schedule.DeviceHealthScriptRunSchedule]
        """
        return self._run_schedule
    
    @run_schedule.setter
    def run_schedule(self,value: Optional[device_health_script_run_schedule.DeviceHealthScriptRunSchedule] = None) -> None:
        """
        Sets the runSchedule property value. Script run schedule for the target group
        Args:
            value: Value to set for the runSchedule property.
        """
        self._run_schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("runRemediationScript", self.run_remediation_script)
        writer.write_object_value("runSchedule", self.run_schedule)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. The Azure Active Directory group we are targeting the script to
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The Azure Active Directory group we are targeting the script to
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

