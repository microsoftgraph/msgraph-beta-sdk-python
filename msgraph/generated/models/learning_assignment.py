from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_type, date_time_time_zone, item_body, learning_course_activity

from . import learning_course_activity

@dataclass
class LearningAssignment(learning_course_activity.LearningCourseActivity):
    # Assigned date for the course activity. Optional.
    assigned_date_time: Optional[datetime] = None
    # The user ID of the assigner. Optional.
    assigner_user_id: Optional[str] = None
    # The assignmentType property
    assignment_type: Optional[assignment_type.AssignmentType] = None
    # Due date for the course activity. Optional.
    due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # Notes for the course activity. Optional.
    notes: Optional[item_body.ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LearningAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LearningAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LearningAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assignment_type, date_time_time_zone, item_body, learning_course_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedDateTime": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "assignerUserId": lambda n : setattr(self, 'assigner_user_id', n.get_str_value()),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(assignment_type.AssignmentType)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
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
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_str_value("assignerUserId", self.assigner_user_id)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_object_value("notes", self.notes)
    

