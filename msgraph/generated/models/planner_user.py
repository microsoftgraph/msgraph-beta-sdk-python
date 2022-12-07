from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_delta = lazy_import('msgraph.generated.models.planner_delta')
planner_favorite_plan_reference_collection = lazy_import('msgraph.generated.models.planner_favorite_plan_reference_collection')
planner_plan = lazy_import('msgraph.generated.models.planner_plan')
planner_recent_plan_reference_collection = lazy_import('msgraph.generated.models.planner_recent_plan_reference_collection')
planner_task = lazy_import('msgraph.generated.models.planner_task')

class PlannerUser(planner_delta.PlannerDelta):
    @property
    def all(self,) -> Optional[List[planner_delta.PlannerDelta]]:
        """
        Gets the all property value. The all property
        Returns: Optional[List[planner_delta.PlannerDelta]]
        """
        return self._all
    
    @all.setter
    def all(self,value: Optional[List[planner_delta.PlannerDelta]] = None) -> None:
        """
        Sets the all property value. The all property
        Args:
            value: Value to set for the all property.
        """
        self._all = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerUser and sets the default values.
        """
        super().__init__()
        # The all property
        self._all: Optional[List[planner_delta.PlannerDelta]] = None
        # A collection that contains the references to the plans that the user has marked as favorites.
        self._favorite_plan_references: Optional[planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection] = None
        # Read-only. Nullable. Returns the plannerPlans that the user marked as favorites.
        self._favorite_plans: Optional[List[planner_plan.PlannerPlan]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The plans property
        self._plans: Optional[List[planner_plan.PlannerPlan]] = None
        # A collection that contains references to the plans that were viewed recently by the user in apps that support recent plans.
        self._recent_plan_references: Optional[planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection] = None
        # Read-only. Nullable. Returns the plannerPlans that have been recently viewed by the user in apps that support recent plans.
        self._recent_plans: Optional[List[planner_plan.PlannerPlan]] = None
        # Read-only. Nullable. Returns the plannerPlans contained by the plannerRosters the user is a member.
        self._roster_plans: Optional[List[planner_plan.PlannerPlan]] = None
        # Read-only. Nullable. Returns the plannerTasks assigned to the user.
        self._tasks: Optional[List[planner_task.PlannerTask]] = None
    
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
    
    @property
    def favorite_plan_references(self,) -> Optional[planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection]:
        """
        Gets the favoritePlanReferences property value. A collection that contains the references to the plans that the user has marked as favorites.
        Returns: Optional[planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection]
        """
        return self._favorite_plan_references
    
    @favorite_plan_references.setter
    def favorite_plan_references(self,value: Optional[planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection] = None) -> None:
        """
        Sets the favoritePlanReferences property value. A collection that contains the references to the plans that the user has marked as favorites.
        Args:
            value: Value to set for the favoritePlanReferences property.
        """
        self._favorite_plan_references = value
    
    @property
    def favorite_plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the favoritePlans property value. Read-only. Nullable. Returns the plannerPlans that the user marked as favorites.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._favorite_plans
    
    @favorite_plans.setter
    def favorite_plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the favoritePlans property value. Read-only. Nullable. Returns the plannerPlans that the user marked as favorites.
        Args:
            value: Value to set for the favoritePlans property.
        """
        self._favorite_plans = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "all": lambda n : setattr(self, 'all', n.get_collection_of_object_values(planner_delta.PlannerDelta)),
            "favorite_plan_references": lambda n : setattr(self, 'favorite_plan_references', n.get_object_value(planner_favorite_plan_reference_collection.PlannerFavoritePlanReferenceCollection)),
            "favorite_plans": lambda n : setattr(self, 'favorite_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "recent_plan_references": lambda n : setattr(self, 'recent_plan_references', n.get_object_value(planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection)),
            "recent_plans": lambda n : setattr(self, 'recent_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "roster_plans": lambda n : setattr(self, 'roster_plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the plans property value. The plans property
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._plans
    
    @plans.setter
    def plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the plans property value. The plans property
        Args:
            value: Value to set for the plans property.
        """
        self._plans = value
    
    @property
    def recent_plan_references(self,) -> Optional[planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection]:
        """
        Gets the recentPlanReferences property value. A collection that contains references to the plans that were viewed recently by the user in apps that support recent plans.
        Returns: Optional[planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection]
        """
        return self._recent_plan_references
    
    @recent_plan_references.setter
    def recent_plan_references(self,value: Optional[planner_recent_plan_reference_collection.PlannerRecentPlanReferenceCollection] = None) -> None:
        """
        Sets the recentPlanReferences property value. A collection that contains references to the plans that were viewed recently by the user in apps that support recent plans.
        Args:
            value: Value to set for the recentPlanReferences property.
        """
        self._recent_plan_references = value
    
    @property
    def recent_plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the recentPlans property value. Read-only. Nullable. Returns the plannerPlans that have been recently viewed by the user in apps that support recent plans.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._recent_plans
    
    @recent_plans.setter
    def recent_plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the recentPlans property value. Read-only. Nullable. Returns the plannerPlans that have been recently viewed by the user in apps that support recent plans.
        Args:
            value: Value to set for the recentPlans property.
        """
        self._recent_plans = value
    
    @property
    def roster_plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the rosterPlans property value. Read-only. Nullable. Returns the plannerPlans contained by the plannerRosters the user is a member.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._roster_plans
    
    @roster_plans.setter
    def roster_plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the rosterPlans property value. Read-only. Nullable. Returns the plannerPlans contained by the plannerRosters the user is a member.
        Args:
            value: Value to set for the rosterPlans property.
        """
        self._roster_plans = value
    
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
        writer.write_object_value("favoritePlanReferences", self.favorite_plan_references)
        writer.write_collection_of_object_values("favoritePlans", self.favorite_plans)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_object_value("recentPlanReferences", self.recent_plan_references)
        writer.write_collection_of_object_values("recentPlans", self.recent_plans)
        writer.write_collection_of_object_values("rosterPlans", self.roster_plans)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def tasks(self,) -> Optional[List[planner_task.PlannerTask]]:
        """
        Gets the tasks property value. Read-only. Nullable. Returns the plannerTasks assigned to the user.
        Returns: Optional[List[planner_task.PlannerTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[planner_task.PlannerTask]] = None) -> None:
        """
        Sets the tasks property value. Read-only. Nullable. Returns the plannerTasks assigned to the user.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

