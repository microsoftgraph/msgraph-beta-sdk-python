from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_bucket, planner_plan, planner_roster, planner_task

from . import entity

class Planner(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Planner and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Returns a collection of the specified buckets
        self._buckets: Optional[List[planner_bucket.PlannerBucket]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. Nullable. Returns a collection of the specified plans
        self._plans: Optional[List[planner_plan.PlannerPlan]] = None
        # Read-only. Nullable. Returns a collection of the specified rosters
        self._rosters: Optional[List[planner_roster.PlannerRoster]] = None
        # Read-only. Nullable. Returns a collection of the specified tasks
        self._tasks: Optional[List[planner_task.PlannerTask]] = None
    
    @property
    def buckets(self,) -> Optional[List[planner_bucket.PlannerBucket]]:
        """
        Gets the buckets property value. Read-only. Nullable. Returns a collection of the specified buckets
        Returns: Optional[List[planner_bucket.PlannerBucket]]
        """
        return self._buckets
    
    @buckets.setter
    def buckets(self,value: Optional[List[planner_bucket.PlannerBucket]] = None) -> None:
        """
        Sets the buckets property value. Read-only. Nullable. Returns a collection of the specified buckets
        Args:
            value: Value to set for the buckets property.
        """
        self._buckets = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Planner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Planner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Planner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_bucket, planner_plan, planner_roster, planner_task

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(planner_bucket.PlannerBucket)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "rosters": lambda n : setattr(self, 'rosters', n.get_collection_of_object_values(planner_roster.PlannerRoster)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the plans property value. Read-only. Nullable. Returns a collection of the specified plans
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._plans
    
    @plans.setter
    def plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the plans property value. Read-only. Nullable. Returns a collection of the specified plans
        Args:
            value: Value to set for the plans property.
        """
        self._plans = value
    
    @property
    def rosters(self,) -> Optional[List[planner_roster.PlannerRoster]]:
        """
        Gets the rosters property value. Read-only. Nullable. Returns a collection of the specified rosters
        Returns: Optional[List[planner_roster.PlannerRoster]]
        """
        return self._rosters
    
    @rosters.setter
    def rosters(self,value: Optional[List[planner_roster.PlannerRoster]] = None) -> None:
        """
        Sets the rosters property value. Read-only. Nullable. Returns a collection of the specified rosters
        Args:
            value: Value to set for the rosters property.
        """
        self._rosters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_collection_of_object_values("rosters", self.rosters)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def tasks(self,) -> Optional[List[planner_task.PlannerTask]]:
        """
        Gets the tasks property value. Read-only. Nullable. Returns a collection of the specified tasks
        Returns: Optional[List[planner_task.PlannerTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[planner_task.PlannerTask]] = None) -> None:
        """
        Sets the tasks property value. Read-only. Nullable. Returns a collection of the specified tasks
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

