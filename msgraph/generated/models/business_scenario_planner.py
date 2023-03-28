from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_task, entity, planner_plan_configuration, planner_task_configuration

from . import entity

class BusinessScenarioPlanner(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new businessScenarioPlanner and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The configuration of Planner plans that will be created for the scenario.
        self._plan_configuration: Optional[planner_plan_configuration.PlannerPlanConfiguration] = None
        # The configuration of Planner tasks that will be created for the scenario.
        self._task_configuration: Optional[planner_task_configuration.PlannerTaskConfiguration] = None
        # The Planner tasks for the scenario.
        self._tasks: Optional[List[business_scenario_task.BusinessScenarioTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioPlanner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioPlanner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioPlanner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_task, entity, planner_plan_configuration, planner_task_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "planConfiguration": lambda n : setattr(self, 'plan_configuration', n.get_object_value(planner_plan_configuration.PlannerPlanConfiguration)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(business_scenario_task.BusinessScenarioTask)),
            "taskConfiguration": lambda n : setattr(self, 'task_configuration', n.get_object_value(planner_task_configuration.PlannerTaskConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def plan_configuration(self,) -> Optional[planner_plan_configuration.PlannerPlanConfiguration]:
        """
        Gets the planConfiguration property value. The configuration of Planner plans that will be created for the scenario.
        Returns: Optional[planner_plan_configuration.PlannerPlanConfiguration]
        """
        return self._plan_configuration
    
    @plan_configuration.setter
    def plan_configuration(self,value: Optional[planner_plan_configuration.PlannerPlanConfiguration] = None) -> None:
        """
        Sets the planConfiguration property value. The configuration of Planner plans that will be created for the scenario.
        Args:
            value: Value to set for the plan_configuration property.
        """
        self._plan_configuration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("planConfiguration", self.plan_configuration)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_object_value("taskConfiguration", self.task_configuration)
    
    @property
    def task_configuration(self,) -> Optional[planner_task_configuration.PlannerTaskConfiguration]:
        """
        Gets the taskConfiguration property value. The configuration of Planner tasks that will be created for the scenario.
        Returns: Optional[planner_task_configuration.PlannerTaskConfiguration]
        """
        return self._task_configuration
    
    @task_configuration.setter
    def task_configuration(self,value: Optional[planner_task_configuration.PlannerTaskConfiguration] = None) -> None:
        """
        Sets the taskConfiguration property value. The configuration of Planner tasks that will be created for the scenario.
        Args:
            value: Value to set for the task_configuration property.
        """
        self._task_configuration = value
    
    @property
    def tasks(self,) -> Optional[List[business_scenario_task.BusinessScenarioTask]]:
        """
        Gets the tasks property value. The Planner tasks for the scenario.
        Returns: Optional[List[business_scenario_task.BusinessScenarioTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[business_scenario_task.BusinessScenarioTask]] = None) -> None:
        """
        Sets the tasks property value. The Planner tasks for the scenario.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

