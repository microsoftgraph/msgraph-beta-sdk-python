from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, outlook_category, outlook_task, outlook_task_folder, outlook_task_group

from . import entity

@dataclass
class OutlookUser(entity.Entity):
    # A list of categories defined for the user.
    master_categories: Optional[List[outlook_category.OutlookCategory]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The taskFolders property
    task_folders: Optional[List[outlook_task_folder.OutlookTaskFolder]] = None
    # The taskGroups property
    task_groups: Optional[List[outlook_task_group.OutlookTaskGroup]] = None
    # The tasks property
    tasks: Optional[List[outlook_task.OutlookTask]] = None
    
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
    

