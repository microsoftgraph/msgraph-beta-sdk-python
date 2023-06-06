from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_properties, business_scenario_task_target_base, planner_task

from . import planner_task

@dataclass
class BusinessScenarioTask(planner_task.PlannerTask):
    # Scenario-specific properties of the task. externalObjectId and externalBucketId properties must be specified when creating a task.
    business_scenario_properties: Optional[business_scenario_properties.BusinessScenarioProperties] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Target of the task that specifies where the task should be placed. Must be specified when creating a task.
    target: Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_properties, business_scenario_task_target_base, planner_task

        fields: Dict[str, Callable[[Any], None]] = {
            "businessScenarioProperties": lambda n : setattr(self, 'business_scenario_properties', n.get_object_value(business_scenario_properties.BusinessScenarioProperties)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(business_scenario_task_target_base.BusinessScenarioTaskTargetBase)),
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
        writer.write_object_value("businessScenarioProperties", self.business_scenario_properties)
        writer.write_object_value("target", self.target)
    

