from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_type, date_time_time_zone, item_body, learning_course_activity

from . import learning_course_activity

class LearningAssignment(learning_course_activity.LearningCourseActivity):
    def __init__(self,) -> None:
        """
        Instantiates a new LearningAssignment and sets the default values.
        """
        super().__init__()
        # Assigned date for the course activity. Optional.
        self._assigned_date_time: Optional[datetime] = None
        # The user ID of the assigner. Optional.
        self._assigner_user_id: Optional[str] = None
        # The assignmentType property
        self._assignment_type: Optional[assignment_type.AssignmentType] = None
        # Due date for the course activity. Optional.
        self._due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Notes for the course activity. Optional.
        self._notes: Optional[item_body.ItemBody] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def assigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignedDateTime property value. Assigned date for the course activity. Optional.
        Returns: Optional[datetime]
        """
        return self._assigned_date_time
    
    @assigned_date_time.setter
    def assigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignedDateTime property value. Assigned date for the course activity. Optional.
        Args:
            value: Value to set for the assigned_date_time property.
        """
        self._assigned_date_time = value
    
    @property
    def assigner_user_id(self,) -> Optional[str]:
        """
        Gets the assignerUserId property value. The user ID of the assigner. Optional.
        Returns: Optional[str]
        """
        return self._assigner_user_id
    
    @assigner_user_id.setter
    def assigner_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assignerUserId property value. The user ID of the assigner. Optional.
        Args:
            value: Value to set for the assigner_user_id property.
        """
        self._assigner_user_id = value
    
    @property
    def assignment_type(self,) -> Optional[assignment_type.AssignmentType]:
        """
        Gets the assignmentType property value. The assignmentType property
        Returns: Optional[assignment_type.AssignmentType]
        """
        return self._assignment_type
    
    @assignment_type.setter
    def assignment_type(self,value: Optional[assignment_type.AssignmentType] = None) -> None:
        """
        Sets the assignmentType property value. The assignmentType property
        Args:
            value: Value to set for the assignment_type property.
        """
        self._assignment_type = value
    
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
    
    @property
    def due_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the dueDateTime property value. Due date for the course activity. Optional.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the dueDateTime property value. Due date for the course activity. Optional.
        Args:
            value: Value to set for the due_date_time property.
        """
        self._due_date_time = value
    
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
    
    @property
    def notes(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the notes property value. Notes for the course activity. Optional.
        Returns: Optional[item_body.ItemBody]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the notes property value. Notes for the course activity. Optional.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
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
    

