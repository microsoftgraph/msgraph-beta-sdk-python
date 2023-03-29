from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_task, entity, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user

from . import entity

class PlannerDelta(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerDelta and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerDelta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerDelta
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.businessScenarioTask":
                from . import business_scenario_task

                return business_scenario_task.BusinessScenarioTask()
            if mapping_value == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat":
                from . import planner_assigned_to_task_board_task_format

                return planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerBucket":
                from . import planner_bucket

                return planner_bucket.PlannerBucket()
            if mapping_value == "#microsoft.graph.plannerBucketTaskBoardTaskFormat":
                from . import planner_bucket_task_board_task_format

                return planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerPlan":
                from . import planner_plan

                return planner_plan.PlannerPlan()
            if mapping_value == "#microsoft.graph.plannerPlanDetails":
                from . import planner_plan_details

                return planner_plan_details.PlannerPlanDetails()
            if mapping_value == "#microsoft.graph.plannerProgressTaskBoardTaskFormat":
                from . import planner_progress_task_board_task_format

                return planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerTask":
                from . import planner_task

                return planner_task.PlannerTask()
            if mapping_value == "#microsoft.graph.plannerTaskDetails":
                from . import planner_task_details

                return planner_task_details.PlannerTaskDetails()
            if mapping_value == "#microsoft.graph.plannerUser":
                from . import planner_user

                return planner_user.PlannerUser()
        return PlannerDelta()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_task, entity, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user

        fields: Dict[str, Callable[[Any], None]] = {
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
    

