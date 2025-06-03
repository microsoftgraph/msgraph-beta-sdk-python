from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .community import Community
    from .engagement_async_operation import EngagementAsyncOperation
    from .engagement_role import EngagementRole
    from .entity import Entity
    from .goals import Goals
    from .learning_course_activity import LearningCourseActivity
    from .learning_provider import LearningProvider

from .entity import Entity

@dataclass
class EmployeeExperience(Entity, Parsable):
    """
    Represents a container that exposes navigation properties for employee experience resources.
    """
    # A collection of communities in Viva Engage.
    communities: Optional[list[Community]] = None
    # A collection of long-running, asynchronous operations related to Viva Engage.
    engagement_async_operations: Optional[list[EngagementAsyncOperation]] = None
    # Represents a collection of goals in a Viva Goals organization.
    goals: Optional[Goals] = None
    # The learningCourseActivities property
    learning_course_activities: Optional[list[LearningCourseActivity]] = None
    # A collection of learning providers.
    learning_providers: Optional[list[LearningProvider]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of roles in Viva Engage.
    roles: Optional[list[EngagementRole]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmployeeExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeExperience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmployeeExperience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .community import Community
        from .engagement_async_operation import EngagementAsyncOperation
        from .engagement_role import EngagementRole
        from .entity import Entity
        from .goals import Goals
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        from .community import Community
        from .engagement_async_operation import EngagementAsyncOperation
        from .engagement_role import EngagementRole
        from .entity import Entity
        from .goals import Goals
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        fields: dict[str, Callable[[Any], None]] = {
            "communities": lambda n : setattr(self, 'communities', n.get_collection_of_object_values(Community)),
            "engagementAsyncOperations": lambda n : setattr(self, 'engagement_async_operations', n.get_collection_of_object_values(EngagementAsyncOperation)),
            "goals": lambda n : setattr(self, 'goals', n.get_object_value(Goals)),
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(LearningCourseActivity)),
            "learningProviders": lambda n : setattr(self, 'learning_providers', n.get_collection_of_object_values(LearningProvider)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(EngagementRole)),
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
        writer.write_collection_of_object_values("communities", self.communities)
        writer.write_collection_of_object_values("engagementAsyncOperations", self.engagement_async_operations)
        writer.write_object_value("goals", self.goals)
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
        writer.write_collection_of_object_values("learningProviders", self.learning_providers)
        writer.write_collection_of_object_values("roles", self.roles)
    

