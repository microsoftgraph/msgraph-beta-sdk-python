from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import learning_course_activity

from . import learning_course_activity

class LearningSelfInitiatedCourse(learning_course_activity.LearningCourseActivity):
    def __init__(self,) -> None:
        """
        Instantiates a new LearningSelfInitiatedCourse and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date time value on which the self-initiated course was started by the learner. Optional.
        self._started_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LearningSelfInitiatedCourse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LearningSelfInitiatedCourse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LearningSelfInitiatedCourse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import learning_course_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("startedDateTime", self.started_date_time)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The date time value on which the self-initiated course was started by the learner. Optional.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The date time value on which the self-initiated course was started by the learner. Optional.
        Args:
            value: Value to set for the started_date_time property.
        """
        self._started_date_time = value
    

