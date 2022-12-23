from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
outlook_task_folder = lazy_import('msgraph.generated.models.outlook_task_folder')

class OutlookTaskGroup(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def change_key(self,) -> Optional[str]:
        """
        Gets the changeKey property value. The version of the task group.
        Returns: Optional[str]
        """
        return self._change_key
    
    @change_key.setter
    def change_key(self,value: Optional[str] = None) -> None:
        """
        Sets the changeKey property value. The version of the task group.
        Args:
            value: Value to set for the changeKey property.
        """
        self._change_key = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new outlookTaskGroup and sets the default values.
        """
        super().__init__()
        # The version of the task group.
        self._change_key: Optional[str] = None
        # The unique GUID identifier for the task group.
        self._group_key: Optional[Guid] = None
        # True if the task group is the default task group.
        self._is_default_group: Optional[bool] = None
        # The name of the task group.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of task folders in the task group. Read-only. Nullable.
        self._task_folders: Optional[List[outlook_task_folder.OutlookTaskFolder]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookTaskGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookTaskGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookTaskGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "change_key": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "group_key": lambda n : setattr(self, 'group_key', n.get_object_value(Guid)),
            "is_default_group": lambda n : setattr(self, 'is_default_group', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "task_folders": lambda n : setattr(self, 'task_folders', n.get_collection_of_object_values(outlook_task_folder.OutlookTaskFolder)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_key(self,) -> Optional[Guid]:
        """
        Gets the groupKey property value. The unique GUID identifier for the task group.
        Returns: Optional[Guid]
        """
        return self._group_key
    
    @group_key.setter
    def group_key(self,value: Optional[Guid] = None) -> None:
        """
        Sets the groupKey property value. The unique GUID identifier for the task group.
        Args:
            value: Value to set for the groupKey property.
        """
        self._group_key = value
    
    @property
    def is_default_group(self,) -> Optional[bool]:
        """
        Gets the isDefaultGroup property value. True if the task group is the default task group.
        Returns: Optional[bool]
        """
        return self._is_default_group
    
    @is_default_group.setter
    def is_default_group(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultGroup property value. True if the task group is the default task group.
        Args:
            value: Value to set for the isDefaultGroup property.
        """
        self._is_default_group = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the task group.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the task group.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_object_value("groupKey", self.group_key)
        writer.write_bool_value("isDefaultGroup", self.is_default_group)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("taskFolders", self.task_folders)
    
    @property
    def task_folders(self,) -> Optional[List[outlook_task_folder.OutlookTaskFolder]]:
        """
        Gets the taskFolders property value. The collection of task folders in the task group. Read-only. Nullable.
        Returns: Optional[List[outlook_task_folder.OutlookTaskFolder]]
        """
        return self._task_folders
    
    @task_folders.setter
    def task_folders(self,value: Optional[List[outlook_task_folder.OutlookTaskFolder]] = None) -> None:
        """
        Sets the taskFolders property value. The collection of task folders in the task group. Read-only. Nullable.
        Args:
            value: Value to set for the taskFolders property.
        """
        self._task_folders = value
    

