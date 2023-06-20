from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_task, entity, planner_plan_configuration, planner_task_configuration

from . import entity

@dataclass
class BusinessScenarioPlanner(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The configuration of Planner plans that will be created for the scenario.
    plan_configuration: Optional[planner_plan_configuration.PlannerPlanConfiguration] = None
    # The configuration of Planner tasks that will be created for the scenario.
    task_configuration: Optional[planner_task_configuration.PlannerTaskConfiguration] = None
    # The Planner tasks for the scenario.
    tasks: Optional[List[business_scenario_task.BusinessScenarioTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioPlanner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioPlanner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BusinessScenarioPlanner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_task, entity, planner_plan_configuration, planner_task_configuration

        from . import business_scenario_task, entity, planner_plan_configuration, planner_task_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "planConfiguration": lambda n : setattr(self, 'plan_configuration', n.get_object_value(planner_plan_configuration.PlannerPlanConfiguration)),
            "taskConfiguration": lambda n : setattr(self, 'task_configuration', n.get_object_value(planner_task_configuration.PlannerTaskConfiguration)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(business_scenario_task.BusinessScenarioTask)),
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
        writer.write_object_value("planConfiguration", self.plan_configuration)
        writer.write_object_value("taskConfiguration", self.task_configuration)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

