from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .community import Community
    from .engagement_async_operation import EngagementAsyncOperation
    from .engagement_role import EngagementRole
    from .goals import Goals
    from .learning_course_activity import LearningCourseActivity
    from .learning_provider import LearningProvider

@dataclass
class EmployeeExperience(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a container that exposes navigation properties for employee experience resources.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
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
        from .goals import Goals
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        from .community import Community
        from .engagement_async_operation import EngagementAsyncOperation
        from .engagement_role import EngagementRole
        from .goals import Goals
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        fields: dict[str, Callable[[Any], None]] = {
            "communities": lambda n : setattr(self, 'communities', n.get_collection_of_object_values(Community)),
            "engagementAsyncOperations": lambda n : setattr(self, 'engagement_async_operations', n.get_collection_of_object_values(EngagementAsyncOperation)),
            "goals": lambda n : setattr(self, 'goals', n.get_object_value(Goals)),
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(LearningCourseActivity)),
            "learningProviders": lambda n : setattr(self, 'learning_providers', n.get_collection_of_object_values(LearningProvider)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(EngagementRole)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("communities", self.communities)
        writer.write_collection_of_object_values("engagementAsyncOperations", self.engagement_async_operations)
        writer.write_object_value("goals", self.goals)
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
        writer.write_collection_of_object_values("learningProviders", self.learning_providers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_additional_data_value(self.additional_data)
    

