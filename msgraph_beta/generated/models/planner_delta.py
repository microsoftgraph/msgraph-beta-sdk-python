from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_task import BusinessScenarioTask
    from .entity import Entity
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_bucket import PlannerBucket
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_plan import PlannerPlan
    from .planner_plan_details import PlannerPlanDetails
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_task import PlannerTask
    from .planner_task_details import PlannerTaskDetails
    from .planner_user import PlannerUser

from .entity import Entity

@dataclass
class PlannerDelta(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerDelta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerDelta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioTask".casefold():
            from .business_scenario_task import BusinessScenarioTask

            return BusinessScenarioTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat".casefold():
            from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat

            return PlannerAssignedToTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucket".casefold():
            from .planner_bucket import PlannerBucket

            return PlannerBucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucketTaskBoardTaskFormat".casefold():
            from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat

            return PlannerBucketTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlan".casefold():
            from .planner_plan import PlannerPlan

            return PlannerPlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanDetails".casefold():
            from .planner_plan_details import PlannerPlanDetails

            return PlannerPlanDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerProgressTaskBoardTaskFormat".casefold():
            from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat

            return PlannerProgressTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTask".casefold():
            from .planner_task import PlannerTask

            return PlannerTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskDetails".casefold():
            from .planner_task_details import PlannerTaskDetails

            return PlannerTaskDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerUser".casefold():
            from .planner_user import PlannerUser

            return PlannerUser()
        return PlannerDelta()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_task import BusinessScenarioTask
        from .entity import Entity
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser

        from .business_scenario_task import BusinessScenarioTask
        from .entity import Entity
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser

        fields: Dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

