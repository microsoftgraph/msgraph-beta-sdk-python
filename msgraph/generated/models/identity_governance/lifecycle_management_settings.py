from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import email_settings, entity

from .. import entity

class LifecycleManagementSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new LifecycleManagementSettings and sets the default values.
        """
        super().__init__()
        # The emailSettings property
        self._email_settings: Optional[email_settings.EmailSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The interval in hours at which all workflows running in the tenant should be scheduled for execution. This interval has a minimum value of 1 and a maximum value of 24. The default value is 3 hours.
        self._workflow_schedule_interval_in_hours: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LifecycleManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LifecycleManagementSettings()
    
    @property
    def email_settings(self,) -> Optional[email_settings.EmailSettings]:
        """
        Gets the emailSettings property value. The emailSettings property
        Returns: Optional[email_settings.EmailSettings]
        """
        return self._email_settings
    
    @email_settings.setter
    def email_settings(self,value: Optional[email_settings.EmailSettings] = None) -> None:
        """
        Sets the emailSettings property value. The emailSettings property
        Args:
            value: Value to set for the email_settings property.
        """
        self._email_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import email_settings, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "emailSettings": lambda n : setattr(self, 'email_settings', n.get_object_value(email_settings.EmailSettings)),
            "workflowScheduleIntervalInHours": lambda n : setattr(self, 'workflow_schedule_interval_in_hours', n.get_int_value()),
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
        writer.write_object_value("emailSettings", self.email_settings)
        writer.write_int_value("workflowScheduleIntervalInHours", self.workflow_schedule_interval_in_hours)
    
    @property
    def workflow_schedule_interval_in_hours(self,) -> Optional[int]:
        """
        Gets the workflowScheduleIntervalInHours property value. The interval in hours at which all workflows running in the tenant should be scheduled for execution. This interval has a minimum value of 1 and a maximum value of 24. The default value is 3 hours.
        Returns: Optional[int]
        """
        return self._workflow_schedule_interval_in_hours
    
    @workflow_schedule_interval_in_hours.setter
    def workflow_schedule_interval_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the workflowScheduleIntervalInHours property value. The interval in hours at which all workflows running in the tenant should be scheduled for execution. This interval has a minimum value of 1 and a maximum value of 24. The default value is 3 hours.
        Args:
            value: Value to set for the workflow_schedule_interval_in_hours property.
        """
        self._workflow_schedule_interval_in_hours = value
    

