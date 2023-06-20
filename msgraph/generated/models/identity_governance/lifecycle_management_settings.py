from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import email_settings, entity

from .. import entity

@dataclass
class LifecycleManagementSettings(entity.Entity):
    # The emailSettings property
    email_settings: Optional[email_settings.EmailSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The interval in hours at which all workflows running in the tenant should be scheduled for execution. This interval has a minimum value of 1 and a maximum value of 24. The default value is 3 hours.
    workflow_schedule_interval_in_hours: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LifecycleManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleManagementSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LifecycleManagementSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import email_settings, entity

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("emailSettings", self.email_settings)
        writer.write_int_value("workflowScheduleIntervalInHours", self.workflow_schedule_interval_in_hours)
    

