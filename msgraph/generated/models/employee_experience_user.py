from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, learning_course_activity

from . import entity

class EmployeeExperienceUser(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new EmployeeExperienceUser and sets the default values.
        """
        super().__init__()
        # The learningCourseActivities property
        self._learning_course_activities: Optional[List[learning_course_activity.LearningCourseActivity]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmployeeExperienceUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeExperienceUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmployeeExperienceUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, learning_course_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(learning_course_activity.LearningCourseActivity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def learning_course_activities(self,) -> Optional[List[learning_course_activity.LearningCourseActivity]]:
        """
        Gets the learningCourseActivities property value. The learningCourseActivities property
        Returns: Optional[List[learning_course_activity.LearningCourseActivity]]
        """
        return self._learning_course_activities
    
    @learning_course_activities.setter
    def learning_course_activities(self,value: Optional[List[learning_course_activity.LearningCourseActivity]] = None) -> None:
        """
        Sets the learningCourseActivities property value. The learningCourseActivities property
        Args:
            value: Value to set for the learning_course_activities property.
        """
        self._learning_course_activities = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
    

