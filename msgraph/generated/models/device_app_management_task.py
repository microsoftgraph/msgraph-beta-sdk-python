from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_app_management_task_category = lazy_import('msgraph.generated.models.device_app_management_task_category')
device_app_management_task_priority = lazy_import('msgraph.generated.models.device_app_management_task_priority')
device_app_management_task_status = lazy_import('msgraph.generated.models.device_app_management_task_status')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceAppManagementTask(entity.Entity):
    """
    A device app management task.
    """
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. The name or email of the admin this task is assigned to.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. The name or email of the admin this task is assigned to.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def category(self,) -> Optional[device_app_management_task_category.DeviceAppManagementTaskCategory]:
        """
        Gets the category property value. Device app management task category.
        Returns: Optional[device_app_management_task_category.DeviceAppManagementTaskCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[device_app_management_task_category.DeviceAppManagementTaskCategory] = None) -> None:
        """
        Sets the category property value. Device app management task category.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceAppManagementTask and sets the default values.
        """
        super().__init__()
        # The name or email of the admin this task is assigned to.
        self._assigned_to: Optional[str] = None
        # Device app management task category.
        self._category: Optional[device_app_management_task_category.DeviceAppManagementTaskCategory] = None
        # The created date.
        self._created_date_time: Optional[datetime] = None
        # The email address of the creator.
        self._creator: Optional[str] = None
        # Notes from the creator.
        self._creator_notes: Optional[str] = None
        # The description.
        self._description: Optional[str] = None
        # The name.
        self._display_name: Optional[str] = None
        # The due date.
        self._due_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device app management task priority.
        self._priority: Optional[device_app_management_task_priority.DeviceAppManagementTaskPriority] = None
        # Device app management task status.
        self._status: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The created date.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The created date.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAppManagementTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagementTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAppManagementTask()
    
    @property
    def creator(self,) -> Optional[str]:
        """
        Gets the creator property value. The email address of the creator.
        Returns: Optional[str]
        """
        return self._creator
    
    @creator.setter
    def creator(self,value: Optional[str] = None) -> None:
        """
        Sets the creator property value. The email address of the creator.
        Args:
            value: Value to set for the creator property.
        """
        self._creator = value
    
    @property
    def creator_notes(self,) -> Optional[str]:
        """
        Gets the creatorNotes property value. Notes from the creator.
        Returns: Optional[str]
        """
        return self._creator_notes
    
    @creator_notes.setter
    def creator_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the creatorNotes property value. Notes from the creator.
        Args:
            value: Value to set for the creatorNotes property.
        """
        self._creator_notes = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def due_date_time(self,) -> Optional[datetime]:
        """
        Gets the dueDateTime property value. The due date.
        Returns: Optional[datetime]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dueDateTime property value. The due date.
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
            "category": lambda n : setattr(self, 'category', n.get_enum_value(device_app_management_task_category.DeviceAppManagementTaskCategory)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creator": lambda n : setattr(self, 'creator', n.get_str_value()),
            "creator_notes": lambda n : setattr(self, 'creator_notes', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(device_app_management_task_priority.DeviceAppManagementTaskPriority)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_app_management_task_status.DeviceAppManagementTaskStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def priority(self,) -> Optional[device_app_management_task_priority.DeviceAppManagementTaskPriority]:
        """
        Gets the priority property value. Device app management task priority.
        Returns: Optional[device_app_management_task_priority.DeviceAppManagementTaskPriority]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[device_app_management_task_priority.DeviceAppManagementTaskPriority] = None) -> None:
        """
        Sets the priority property value. Device app management task priority.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
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
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("creator", self.creator)
        writer.write_str_value("creatorNotes", self.creator_notes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[device_app_management_task_status.DeviceAppManagementTaskStatus]:
        """
        Gets the status property value. Device app management task status.
        Returns: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus] = None) -> None:
        """
        Sets the status property value. Device app management task status.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

