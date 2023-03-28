from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, planner_bucket, planner_delta, planner_plan_container, planner_plan_context_collection, planner_plan_creation, planner_plan_details, planner_shared_with_container, planner_task

from . import planner_delta

class PlannerPlan(planner_delta.PlannerDelta):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerPlan and sets the default values.
        """
        super().__init__()
        # Collection of buckets in the plan. Read-only. Nullable.
        self._buckets: Optional[List[planner_bucket.PlannerBucket]] = None
        # Identifies the container of the plan. Specify only the url, the containerId and type, or all properties. After it is set, this property can’t be updated. Required.
        self._container: Optional[planner_plan_container.PlannerPlanContainer] = None
        # Read-only. Additional user experiences in which this plan is used, represented as plannerPlanContext entries.
        self._contexts: Optional[planner_plan_context_collection.PlannerPlanContextCollection] = None
        # Read-only. The user who created the plan.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # Contains information about the origin of the plan.
        self._creation_source: Optional[planner_plan_creation.PlannerPlanCreation] = None
        # Additional details about the plan. Read-only. Nullable.
        self._details: Optional[planner_plan_details.PlannerPlanDetails] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The owner property
        self._owner: Optional[str] = None
        # The sharedWithContainers property
        self._shared_with_containers: Optional[List[planner_shared_with_container.PlannerSharedWithContainer]] = None
        # Collection of tasks in the plan. Read-only. Nullable.
        self._tasks: Optional[List[planner_task.PlannerTask]] = None
        # Required. Title of the plan.
        self._title: Optional[str] = None
    
    @property
    def buckets(self,) -> Optional[List[planner_bucket.PlannerBucket]]:
        """
        Gets the buckets property value. Collection of buckets in the plan. Read-only. Nullable.
        Returns: Optional[List[planner_bucket.PlannerBucket]]
        """
        return self._buckets
    
    @buckets.setter
    def buckets(self,value: Optional[List[planner_bucket.PlannerBucket]] = None) -> None:
        """
        Sets the buckets property value. Collection of buckets in the plan. Read-only. Nullable.
        Args:
            value: Value to set for the buckets property.
        """
        self._buckets = value
    
    @property
    def container(self,) -> Optional[planner_plan_container.PlannerPlanContainer]:
        """
        Gets the container property value. Identifies the container of the plan. Specify only the url, the containerId and type, or all properties. After it is set, this property can’t be updated. Required.
        Returns: Optional[planner_plan_container.PlannerPlanContainer]
        """
        return self._container
    
    @container.setter
    def container(self,value: Optional[planner_plan_container.PlannerPlanContainer] = None) -> None:
        """
        Sets the container property value. Identifies the container of the plan. Specify only the url, the containerId and type, or all properties. After it is set, this property can’t be updated. Required.
        Args:
            value: Value to set for the container property.
        """
        self._container = value
    
    @property
    def contexts(self,) -> Optional[planner_plan_context_collection.PlannerPlanContextCollection]:
        """
        Gets the contexts property value. Read-only. Additional user experiences in which this plan is used, represented as plannerPlanContext entries.
        Returns: Optional[planner_plan_context_collection.PlannerPlanContextCollection]
        """
        return self._contexts
    
    @contexts.setter
    def contexts(self,value: Optional[planner_plan_context_collection.PlannerPlanContextCollection] = None) -> None:
        """
        Sets the contexts property value. Read-only. Additional user experiences in which this plan is used, represented as plannerPlanContext entries.
        Args:
            value: Value to set for the contexts property.
        """
        self._contexts = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Read-only. The user who created the plan.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Read-only. The user who created the plan.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
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
    
    @property
    def creation_source(self,) -> Optional[planner_plan_creation.PlannerPlanCreation]:
        """
        Gets the creationSource property value. Contains information about the origin of the plan.
        Returns: Optional[planner_plan_creation.PlannerPlanCreation]
        """
        return self._creation_source
    
    @creation_source.setter
    def creation_source(self,value: Optional[planner_plan_creation.PlannerPlanCreation] = None) -> None:
        """
        Sets the creationSource property value. Contains information about the origin of the plan.
        Args:
            value: Value to set for the creation_source property.
        """
        self._creation_source = value
    
    @property
    def details(self,) -> Optional[planner_plan_details.PlannerPlanDetails]:
        """
        Gets the details property value. Additional details about the plan. Read-only. Nullable.
        Returns: Optional[planner_plan_details.PlannerPlanDetails]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[planner_plan_details.PlannerPlanDetails] = None) -> None:
        """
        Sets the details property value. Additional details about the plan. Read-only. Nullable.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
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
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The owner property
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The owner property
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
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
    
    @property
    def shared_with_containers(self,) -> Optional[List[planner_shared_with_container.PlannerSharedWithContainer]]:
        """
        Gets the sharedWithContainers property value. The sharedWithContainers property
        Returns: Optional[List[planner_shared_with_container.PlannerSharedWithContainer]]
        """
        return self._shared_with_containers
    
    @shared_with_containers.setter
    def shared_with_containers(self,value: Optional[List[planner_shared_with_container.PlannerSharedWithContainer]] = None) -> None:
        """
        Sets the sharedWithContainers property value. The sharedWithContainers property
        Args:
            value: Value to set for the shared_with_containers property.
        """
        self._shared_with_containers = value
    
    @property
    def tasks(self,) -> Optional[List[planner_task.PlannerTask]]:
        """
        Gets the tasks property value. Collection of tasks in the plan. Read-only. Nullable.
        Returns: Optional[List[planner_task.PlannerTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[planner_task.PlannerTask]] = None) -> None:
        """
        Sets the tasks property value. Collection of tasks in the plan. Read-only. Nullable.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Required. Title of the plan.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Required. Title of the plan.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

