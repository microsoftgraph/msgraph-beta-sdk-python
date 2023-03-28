from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, outlook_category, outlook_task, outlook_task_folder, outlook_task_group

from . import entity

class OutlookUser(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new outlookUser and sets the default values.
        """
        super().__init__()
        # A list of categories defined for the user.
        self._master_categories: Optional[List[outlook_category.OutlookCategory]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The taskFolders property
        self._task_folders: Optional[List[outlook_task_folder.OutlookTaskFolder]] = None
        # The taskGroups property
        self._task_groups: Optional[List[outlook_task_group.OutlookTaskGroup]] = None
        # The tasks property
        self._tasks: Optional[List[outlook_task.OutlookTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, outlook_category, outlook_task, outlook_task_folder, outlook_task_group

        fields: Dict[str, Callable[[Any], None]] = {
            "masterCategories": lambda n : setattr(self, 'master_categories', n.get_collection_of_object_values(outlook_category.OutlookCategory)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(outlook_task.OutlookTask)),
            "taskFolders": lambda n : setattr(self, 'task_folders', n.get_collection_of_object_values(outlook_task_folder.OutlookTaskFolder)),
            "taskGroups": lambda n : setattr(self, 'task_groups', n.get_collection_of_object_values(outlook_task_group.OutlookTaskGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def master_categories(self,) -> Optional[List[outlook_category.OutlookCategory]]:
        """
        Gets the masterCategories property value. A list of categories defined for the user.
        Returns: Optional[List[outlook_category.OutlookCategory]]
        """
        return self._master_categories
    
    @master_categories.setter
    def master_categories(self,value: Optional[List[outlook_category.OutlookCategory]] = None) -> None:
        """
        Sets the masterCategories property value. A list of categories defined for the user.
        Args:
            value: Value to set for the master_categories property.
        """
        self._master_categories = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("masterCategories", self.master_categories)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_collection_of_object_values("taskFolders", self.task_folders)
        writer.write_collection_of_object_values("taskGroups", self.task_groups)
    
    @property
    def task_folders(self,) -> Optional[List[outlook_task_folder.OutlookTaskFolder]]:
        """
        Gets the taskFolders property value. The taskFolders property
        Returns: Optional[List[outlook_task_folder.OutlookTaskFolder]]
        """
        return self._task_folders
    
    @task_folders.setter
    def task_folders(self,value: Optional[List[outlook_task_folder.OutlookTaskFolder]] = None) -> None:
        """
        Sets the taskFolders property value. The taskFolders property
        Args:
            value: Value to set for the task_folders property.
        """
        self._task_folders = value
    
    @property
    def task_groups(self,) -> Optional[List[outlook_task_group.OutlookTaskGroup]]:
        """
        Gets the taskGroups property value. The taskGroups property
        Returns: Optional[List[outlook_task_group.OutlookTaskGroup]]
        """
        return self._task_groups
    
    @task_groups.setter
    def task_groups(self,value: Optional[List[outlook_task_group.OutlookTaskGroup]] = None) -> None:
        """
        Sets the taskGroups property value. The taskGroups property
        Args:
            value: Value to set for the task_groups property.
        """
        self._task_groups = value
    
    @property
    def tasks(self,) -> Optional[List[outlook_task.OutlookTask]]:
        """
        Gets the tasks property value. The tasks property
        Returns: Optional[List[outlook_task.OutlookTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[outlook_task.OutlookTask]] = None) -> None:
        """
        Sets the tasks property value. The tasks property
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

