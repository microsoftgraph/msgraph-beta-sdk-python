from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workflow_execution_trigger = lazy_import('msgraph.generated.models.identity_governance.workflow_execution_trigger')
workflow_trigger_time_based_attribute = lazy_import('msgraph.generated.models.identity_governance.workflow_trigger_time_based_attribute')

class TimeBasedAttributeTrigger(workflow_execution_trigger.WorkflowExecutionTrigger):
    def __init__(self,) -> None:
        """
        Instantiates a new TimeBasedAttributeTrigger and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.timeBasedAttributeTrigger"
        # How many days before or after the time-based attribute specified the workflow should trigger. For example, if the attribute is employeeHireDate and offsetInDays is -1, then the workflow should trigger one day before the employee hire date. The value can range between -60 and 60 days.
        self._offset_in_days: Optional[int] = None
        # The timeBasedAttribute property
        self._time_based_attribute: Optional[workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute] = None
    
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
        fields = {
            "offset_in_days": lambda n : setattr(self, 'offset_in_days', n.get_int_value()),
            "time_based_attribute": lambda n : setattr(self, 'time_based_attribute', n.get_enum_value(workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def offset_in_days(self,) -> Optional[int]:
        """
        Gets the offsetInDays property value. How many days before or after the time-based attribute specified the workflow should trigger. For example, if the attribute is employeeHireDate and offsetInDays is -1, then the workflow should trigger one day before the employee hire date. The value can range between -60 and 60 days.
        Returns: Optional[int]
        """
        return self._offset_in_days
    
    @offset_in_days.setter
    def offset_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the offsetInDays property value. How many days before or after the time-based attribute specified the workflow should trigger. For example, if the attribute is employeeHireDate and offsetInDays is -1, then the workflow should trigger one day before the employee hire date. The value can range between -60 and 60 days.
        Args:
            value: Value to set for the offsetInDays property.
        """
        self._offset_in_days = value
    
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
    
    @property
    def time_based_attribute(self,) -> Optional[workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute]:
        """
        Gets the timeBasedAttribute property value. The timeBasedAttribute property
        Returns: Optional[workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute]
        """
        return self._time_based_attribute
    
    @time_based_attribute.setter
    def time_based_attribute(self,value: Optional[workflow_trigger_time_based_attribute.WorkflowTriggerTimeBasedAttribute] = None) -> None:
        """
        Sets the timeBasedAttribute property value. The timeBasedAttribute property
        Args:
            value: Value to set for the timeBasedAttribute property.
        """
        self._time_based_attribute = value
    

