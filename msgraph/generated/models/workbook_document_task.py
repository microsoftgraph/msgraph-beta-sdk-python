from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_comment import WorkbookComment
    from .workbook_document_task_change import WorkbookDocumentTaskChange
    from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
    from .workbook_email_identity import WorkbookEmailIdentity

from .entity import Entity

@dataclass
class WorkbookDocumentTask(Entity):
    # The assignees property
    assignees: Optional[List[WorkbookEmailIdentity]] = None
    # The changes property
    changes: Optional[List[WorkbookDocumentTaskChange]] = None
    # The comment property
    comment: Optional[WorkbookComment] = None
    # The completedBy property
    completed_by: Optional[WorkbookEmailIdentity] = None
    # The completedDateTime property
    completed_date_time: Optional[datetime.datetime] = None
    # The createdBy property
    created_by: Optional[WorkbookEmailIdentity] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The percentComplete property
    percent_complete: Optional[int] = None
    # The priority property
    priority: Optional[int] = None
    # The startAndDueDateTime property
    start_and_due_date_time: Optional[WorkbookDocumentTaskSchedule] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookDocumentTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookDocumentTask
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookDocumentTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_comment import WorkbookComment
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
        from .workbook_email_identity import WorkbookEmailIdentity

        from .entity import Entity
        from .workbook_comment import WorkbookComment
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
        from .workbook_email_identity import WorkbookEmailIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignees": lambda n : setattr(self, 'assignees', n.get_collection_of_object_values(WorkbookEmailIdentity)),
            "changes": lambda n : setattr(self, 'changes', n.get_collection_of_object_values(WorkbookDocumentTaskChange)),
            "comment": lambda n : setattr(self, 'comment', n.get_object_value(WorkbookComment)),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(WorkbookEmailIdentity)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(WorkbookEmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startAndDueDateTime": lambda n : setattr(self, 'start_and_due_date_time', n.get_object_value(WorkbookDocumentTaskSchedule)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignees", self.assignees)
        writer.write_collection_of_object_values("changes", self.changes)
        writer.write_object_value("comment", self.comment)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("startAndDueDateTime", self.start_and_due_date_time)
        writer.write_str_value("title", self.title)
    

