from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_delta, planner_favorite_plan_reference_collection, planner_plan, planner_recent_plan_reference_collection, planner_task

from . import planner_delta

@dataclass
class PlannerUser(planner_delta.PlannerDelta):
    # The all property
    all: Optional[List[planner_delta.PlannerDelta]] = None
    # A collection that contains the references to the plans that the user has marked as favorites.
    favorite_plan_references: Optional[planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection] = None
    # Read-only. Nullable. Returns the plannerPlans that the user marked as favorites.
    favorite_plans: Optional[List[planner_plan.PlannerPlan]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The plans property
    plans: Optional[List[planner_plan.PlannerPlan]] = None
    # A collection that contains references to the plans that were viewed recently by the user in apps that support recent plans.
    recent_plan_references: Optional[planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection] = None
    # Read-only. Nullable. Returns the plannerPlans that have been recently viewed by the user in apps that support recent plans.
    recent_plans: Optional[List[planner_plan.PlannerPlan]] = None
    # Read-only. Nullable. Returns the plannerPlans contained by the plannerRosters the user is a member.
    roster_plans: Optional[List[planner_plan.PlannerPlan]] = None
    # Read-only. Nullable. Returns the plannerTasks assigned to the user.
    tasks: Optional[List[planner_task.PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_delta, planner_favorite_plan_reference_collection, planner_plan, planner_recent_plan_reference_collection, planner_task

        fields: Dict[str, Callable[[Any], None]] = {
            "all": lambda n : setattr(self, 'all', n.get_collection_of_object_values(planner_delta.PlannerDelta)),
            "favoritePlans": lambda n : setattr(self, 'favorite_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "favoritePlanReferences": lambda n : setattr(self, 'favorite_plan_references', n.get_object_value(planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "recentPlans": lambda n : setattr(self, 'recent_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "recentPlanReferences": lambda n : setattr(self, 'recent_plan_references', n.get_object_value(planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection)),
            "rosterPlans": lambda n : setattr(self, 'roster_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
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
        writer.write_collection_of_object_values("all", self.all)
        writer.write_collection_of_object_values("favoritePlans", self.favorite_plans)
        writer.write_object_value("favoritePlanReferences", self.favorite_plan_references)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_collection_of_object_values("recentPlans", self.recent_plans)
        writer.write_object_value("recentPlanReferences", self.recent_plan_references)
        writer.write_collection_of_object_values("rosterPlans", self.roster_plans)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

