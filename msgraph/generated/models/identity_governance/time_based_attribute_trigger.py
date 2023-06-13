from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import workflow_execution_trigger, workflow_trigger_time_based_attribute

from . import workflow_execution_trigger

@dataclass
class TimeBasedAttributeTrigger(workflow_execution_trigger.WorkflowExecutionTrigger):
    odata_type = "#microsoft.graph.identityGovernance.timeBasedAttributeTrigger"
    # How many days before or after the time-based attribute specified the workflow should trigger. For example, if the attribute is employeeHireDate and offsetInDays is -1, then the workflow should trigger one day before the employee hire date. The value can range between -180 and 180 days.
    offset_in_days: Optional[int] = None
    # The timeBasedAttribute property
    time_based_attribute: Optional[workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeBasedAttributeTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeBasedAttributeTrigger
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeBasedAttributeTrigger()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import workflow_execution_trigger, workflow_trigger_time_based_attribute

        fields: Dict[str, Callable[[Any], None]] = {
            "offsetInDays": lambda n : setattr(self, 'offset_in_days', n.get_int_value()),
            "timeBasedAttribute": lambda n : setattr(self, 'time_based_attribute', n.get_enum_value(workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute)),
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
        writer.write_int_value("offsetInDays", self.offset_in_days)
        writer.write_enum_value("timeBasedAttribute", self.time_based_attribute)
    

