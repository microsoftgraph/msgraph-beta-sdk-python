from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, planner_bucket, planner_delta, planner_plan_container, planner_plan_context_collection, planner_plan_creation, planner_plan_details, planner_shared_with_container, planner_task

from . import planner_delta

@dataclass
class PlannerPlan(planner_delta.PlannerDelta):
    # Collection of buckets in the plan. Read-only. Nullable.
    buckets: Optional[List[planner_bucket.PlannerBucket]] = None
    # Identifies the container of the plan. Specify only the url, the containerId and type, or all properties. After it is set, this property can’t be updated. Required.
    container: Optional[planner_plan_container.PlannerPlanContainer] = None
    # Read-only. Additional user experiences in which this plan is used, represented as plannerPlanContext entries.
    contexts: Optional[planner_plan_context_collection.PlannerPlanContextCollection] = None
    # Read-only. The user who created the plan.
    created_by: Optional[identity_set.IdentitySet] = None
    # Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # Contains information about the origin of the plan.
    creation_source: Optional[planner_plan_creation.PlannerPlanCreation] = None
    # Additional details about the plan. Read-only. Nullable.
    details: Optional[planner_plan_details.PlannerPlanDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The owner property
    owner: Optional[str] = None
    # List of containers the plan is shared with.
    shared_with_containers: Optional[List[planner_shared_with_container.PlannerSharedWithContainer]] = None
    # Collection of tasks in the plan. Read-only. Nullable.
    tasks: Optional[List[planner_task.PlannerTask]] = None
    # Required. Title of the plan.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlan
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerPlan()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, planner_bucket, planner_delta, planner_plan_container, planner_plan_context_collection, planner_plan_creation, planner_plan_details, planner_shared_with_container, planner_task

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(planner_bucket.PlannerBucket)),
            "container": lambda n : setattr(self, 'container', n.get_object_value(planner_plan_container.PlannerPlanContainer)),
            "contexts": lambda n : setattr(self, 'contexts', n.get_object_value(planner_plan_context_collection.PlannerPlanContextCollection)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(planner_plan_creation.PlannerPlanCreation)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(planner_plan_details.PlannerPlanDetails)),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "sharedWithContainers": lambda n : setattr(self, 'shared_with_containers', n.get_collection_of_object_values(planner_shared_with_container.PlannerSharedWithContainer)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("container", self.container)
        writer.write_object_value("contexts", self.contexts)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_object_value("details", self.details)
        writer.write_str_value("owner", self.owner)
        writer.write_collection_of_object_values("sharedWithContainers", self.shared_with_containers)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_str_value("title", self.title)
    

