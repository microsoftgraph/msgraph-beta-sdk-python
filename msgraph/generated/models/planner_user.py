from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_delta import PlannerDelta
    from .planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
    from .planner_plan import PlannerPlan
    from .planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
    from .planner_task import PlannerTask

from .planner_delta import PlannerDelta

@dataclass
class PlannerUser(PlannerDelta):
    # The all property
    all: Optional[List[PlannerDelta]] = None
    # A collection that contains the references to the plans that the user has marked as favorites.
    favorite_plan_references: Optional[PlannerFavoritePlanReferenceCollection] = None
    # Read-only. Nullable. Returns the plannerPlans that the user marked as favorites.
    favorite_plans: Optional[List[PlannerPlan]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The plans property
    plans: Optional[List[PlannerPlan]] = None
    # A collection that contains references to the plans that were viewed recently by the user in apps that support recent plans.
    recent_plan_references: Optional[PlannerRecentPlanReferenceCollection] = None
    # Read-only. Nullable. Returns the plannerPlans that have been recently viewed by the user in apps that support recent plans.
    recent_plans: Optional[List[PlannerPlan]] = None
    # Read-only. Nullable. Returns the plannerPlans contained by the plannerRosters the user is a member.
    roster_plans: Optional[List[PlannerPlan]] = None
    # Read-only. Nullable. Returns the plannerTasks assigned to the user.
    tasks: Optional[List[PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerUser
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .planner_delta import PlannerDelta
        from .planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
        from .planner_plan import PlannerPlan
        from .planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
        from .planner_task import PlannerTask

        from .planner_delta import PlannerDelta
        from .planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
        from .planner_plan import PlannerPlan
        from .planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
        from .planner_task import PlannerTask

        fields: Dict[str, Callable[[Any], None]] = {
            "all": lambda n : setattr(self, 'all', n.get_collection_of_object_values(PlannerDelta)),
            "favoritePlanReferences": lambda n : setattr(self, 'favorite_plan_references', n.get_object_value(PlannerFavoritePlanReferenceCollection)),
            "favoritePlans": lambda n : setattr(self, 'favorite_plans', n.get_collection_of_object_values(PlannerPlan)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(PlannerPlan)),
            "recentPlanReferences": lambda n : setattr(self, 'recent_plan_references', n.get_object_value(PlannerRecentPlanReferenceCollection)),
            "recentPlans": lambda n : setattr(self, 'recent_plans', n.get_collection_of_object_values(PlannerPlan)),
            "rosterPlans": lambda n : setattr(self, 'roster_plans', n.get_collection_of_object_values(PlannerPlan)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("all", self.all)
        writer.write_object_value("favoritePlanReferences", self.favorite_plan_references)
        writer.write_collection_of_object_values("favoritePlans", self.favorite_plans)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_object_value("recentPlanReferences", self.recent_plan_references)
        writer.write_collection_of_object_values("recentPlans", self.recent_plans)
        writer.write_collection_of_object_values("rosterPlans", self.roster_plans)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

