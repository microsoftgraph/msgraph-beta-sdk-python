from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .date_time_time_zone import DateTimeTimeZone
    from .importance import Importance
    from .item_body import ItemBody
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .patterned_recurrence import PatternedRecurrence
    from .sensitivity import Sensitivity
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
    from .task_status import TaskStatus

from .outlook_item import OutlookItem

@dataclass
class OutlookTask(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.outlookTask"
    # The name of the person who has been assigned the task in Outlook. Read-only.
    assigned_to: Optional[str] = None
    # The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the task.  Read-only. Nullable.
    attachments: Optional[List[Attachment]] = None
    # The task body that typically contains information about the task. Note that only HTML type is supported.
    body: Optional[ItemBody] = None
    # The date in the specified time zone that the task was finished.
    completed_date_time: Optional[DateTimeTimeZone] = None
    # The date in the specified time zone that the task is to be finished.
    due_date_time: Optional[DateTimeTimeZone] = None
    # Set to true if the task has attachments.
    has_attachments: Optional[bool] = None
    # The importance property
    importance: Optional[Importance] = None
    # The isReminderOn property
    is_reminder_on: Optional[bool] = None
    # The collection of multi-value extended properties defined for the task. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The owner property
    owner: Optional[str] = None
    # The parentFolderId property
    parent_folder_id: Optional[str] = None
    # The recurrence property
    recurrence: Optional[PatternedRecurrence] = None
    # The reminderDateTime property
    reminder_date_time: Optional[DateTimeTimeZone] = None
    # The sensitivity property
    sensitivity: Optional[Sensitivity] = None
    # The collection of single-value extended properties defined for the task. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    # The status property
    status: Optional[TaskStatus] = None
    # The subject property
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookTask
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OutlookTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .date_time_time_zone import DateTimeTimeZone
        from .importance import Importance
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .patterned_recurrence import PatternedRecurrence
        from .sensitivity import Sensitivity
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .task_status import TaskStatus

        from .attachment import Attachment
        from .date_time_time_zone import DateTimeTimeZone
        from .importance import Importance
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .patterned_recurrence import PatternedRecurrence
        from .sensitivity import Sensitivity
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .task_status import TaskStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_object_value(DateTimeTimeZone)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(DateTimeTimeZone)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(Importance)),
            "isReminderOn": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "reminderDateTime": lambda n : setattr(self, 'reminder_date_time', n.get_object_value(DateTimeTimeZone)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(Sensitivity)),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TaskStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_object_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_enum_value("importance", self.importance)
        writer.write_bool_value("isReminderOn", self.is_reminder_on)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_object_value("reminderDateTime", self.reminder_date_time)
        writer.write_enum_value("sensitivity", self.sensitivity)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
    

