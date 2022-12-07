from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
importance = lazy_import('msgraph.generated.models.importance')
item_body = lazy_import('msgraph.generated.models.item_body')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
patterned_recurrence = lazy_import('msgraph.generated.models.patterned_recurrence')
sensitivity = lazy_import('msgraph.generated.models.sensitivity')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')
task_status = lazy_import('msgraph.generated.models.task_status')

class OutlookTask(outlook_item.OutlookItem):
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. The name of the person who has been assigned the task in Outlook. Read-only.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. The name of the person who has been assigned the task in Outlook. Read-only.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def attachments(self,) -> Optional[List[attachment.Attachment]]:
        """
        Gets the attachments property value. The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the task.  Read-only. Nullable.
        Returns: Optional[List[attachment.Attachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment.Attachment]] = None) -> None:
        """
        Sets the attachments property value. The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the task.  Read-only. Nullable.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The task body that typically contains information about the task. Note that only HTML type is supported.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The task body that typically contains information about the task. Note that only HTML type is supported.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def completed_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the completedDateTime property value. The date in the specified time zone that the task was finished.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the completedDateTime property value. The date in the specified time zone that the task was finished.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OutlookTask and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.outlookTask"
        # The name of the person who has been assigned the task in Outlook. Read-only.
        self._assigned_to: Optional[str] = None
        # The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the task.  Read-only. Nullable.
        self._attachments: Optional[List[attachment.Attachment]] = None
        # The task body that typically contains information about the task. Note that only HTML type is supported.
        self._body: Optional[item_body.ItemBody] = None
        # The date in the specified time zone that the task was finished.
        self._completed_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The date in the specified time zone that the task is to be finished.
        self._due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Set to true if the task has attachments.
        self._has_attachments: Optional[bool] = None
        # The importance property
        self._importance: Optional[importance.Importance] = None
        # The isReminderOn property
        self._is_reminder_on: Optional[bool] = None
        # The collection of multi-value extended properties defined for the task. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The owner property
        self._owner: Optional[str] = None
        # The parentFolderId property
        self._parent_folder_id: Optional[str] = None
        # The recurrence property
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The reminderDateTime property
        self._reminder_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The sensitivity property
        self._sensitivity: Optional[sensitivity.Sensitivity] = None
        # The collection of single-value extended properties defined for the task. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The status property
        self._status: Optional[task_status.TaskStatus] = None
        # The subject property
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookTask()
    
    @property
    def due_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the dueDateTime property value. The date in the specified time zone that the task is to be finished.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the dueDateTime property value. The date in the specified time zone that the task is to be finished.
        Args:
            value: Value to set for the dueDateTime property.
        """
        self._due_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(attachment.Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(importance.Importance)),
            "is_reminder_on": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "parent_folder_id": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "reminder_date_time": lambda n : setattr(self, 'reminder_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(sensitivity.Sensitivity)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(task_status.TaskStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Set to true if the task has attachments.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Set to true if the task has attachments.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def importance(self,) -> Optional[importance.Importance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[importance.Importance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def is_reminder_on(self,) -> Optional[bool]:
        """
        Gets the isReminderOn property value. The isReminderOn property
        Returns: Optional[bool]
        """
        return self._is_reminder_on
    
    @is_reminder_on.setter
    def is_reminder_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReminderOn property value. The isReminderOn property
        Args:
            value: Value to set for the isReminderOn property.
        """
        self._is_reminder_on = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the task. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the task. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
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
    
    @property
    def parent_folder_id(self,) -> Optional[str]:
        """
        Gets the parentFolderId property value. The parentFolderId property
        Returns: Optional[str]
        """
        return self._parent_folder_id
    
    @parent_folder_id.setter
    def parent_folder_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentFolderId property value. The parentFolderId property
        Args:
            value: Value to set for the parentFolderId property.
        """
        self._parent_folder_id = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. The recurrence property
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. The recurrence property
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    @property
    def reminder_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the reminderDateTime property value. The reminderDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._reminder_date_time
    
    @reminder_date_time.setter
    def reminder_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the reminderDateTime property value. The reminderDateTime property
        Args:
            value: Value to set for the reminderDateTime property.
        """
        self._reminder_date_time = value
    
    @property
    def sensitivity(self,) -> Optional[sensitivity.Sensitivity]:
        """
        Gets the sensitivity property value. The sensitivity property
        Returns: Optional[sensitivity.Sensitivity]
        """
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self,value: Optional[sensitivity.Sensitivity] = None) -> None:
        """
        Sets the sensitivity property value. The sensitivity property
        Args:
            value: Value to set for the sensitivity property.
        """
        self._sensitivity = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the task. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the task. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[task_status.TaskStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[task_status.TaskStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[task_status.TaskStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

