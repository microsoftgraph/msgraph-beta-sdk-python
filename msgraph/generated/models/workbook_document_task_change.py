from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_email_identity import WorkbookEmailIdentity

from .entity import Entity

@dataclass
class WorkbookDocumentTaskChange(Entity):
    # The assignee property
    assignee: Optional[WorkbookEmailIdentity] = None
    # The changedBy property
    changed_by: Optional[WorkbookEmailIdentity] = None
    # The commentId property
    comment_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The dueDateTime property
    due_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The percentComplete property
    percent_complete: Optional[int] = None
    # The priority property
    priority: Optional[int] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The title property
    title: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The undoChangeId property
    undo_change_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookDocumentTaskChange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookDocumentTaskChange
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookDocumentTaskChange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_email_identity import WorkbookEmailIdentity

        from .entity import Entity
        from .workbook_email_identity import WorkbookEmailIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignee": lambda n : setattr(self, 'assignee', n.get_object_value(WorkbookEmailIdentity)),
            "changedBy": lambda n : setattr(self, 'changed_by', n.get_object_value(WorkbookEmailIdentity)),
            "commentId": lambda n : setattr(self, 'comment_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "undoChangeId": lambda n : setattr(self, 'undo_change_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("assignee", self.assignee)
        writer.write_object_value("changedBy", self.changed_by)
        writer.write_str_value("commentId", self.comment_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_int_value("priority", self.priority)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_str_value("undoChangeId", self.undo_change_id)
    

