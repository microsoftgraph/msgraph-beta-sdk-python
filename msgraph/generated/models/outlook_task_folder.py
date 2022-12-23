from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_task = lazy_import('msgraph.generated.models.outlook_task')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class OutlookTaskFolder(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def change_key(self,) -> Optional[str]:
        """
        Gets the changeKey property value. The version of the task folder.
        Returns: Optional[str]
        """
        return self._change_key
    
    @change_key.setter
    def change_key(self,value: Optional[str] = None) -> None:
        """
        Sets the changeKey property value. The version of the task folder.
        Args:
            value: Value to set for the changeKey property.
        """
        self._change_key = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new outlookTaskFolder and sets the default values.
        """
        super().__init__()
        # The version of the task folder.
        self._change_key: Optional[str] = None
        # True if the folder is the default task folder.
        self._is_default_folder: Optional[bool] = None
        # The collection of multi-value extended properties defined for the task folder. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The name of the task folder.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unique GUID identifier for the task folder's parent group.
        self._parent_group_key: Optional[Guid] = None
        # The collection of single-value extended properties defined for the task folder. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        # The tasks in this task folder. Read-only. Nullable.
        self._tasks: Optional[List[outlook_task.OutlookTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookTaskFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookTaskFolder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookTaskFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "change_key": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "is_default_folder": lambda n : setattr(self, 'is_default_folder', n.get_bool_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent_group_key": lambda n : setattr(self, 'parent_group_key', n.get_object_value(Guid)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(outlook_task.OutlookTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default_folder(self,) -> Optional[bool]:
        """
        Gets the isDefaultFolder property value. True if the folder is the default task folder.
        Returns: Optional[bool]
        """
        return self._is_default_folder
    
    @is_default_folder.setter
    def is_default_folder(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultFolder property value. True if the folder is the default task folder.
        Args:
            value: Value to set for the isDefaultFolder property.
        """
        self._is_default_folder = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the task folder. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the task folder. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the task folder.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the task folder.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def parent_group_key(self,) -> Optional[Guid]:
        """
        Gets the parentGroupKey property value. The unique GUID identifier for the task folder's parent group.
        Returns: Optional[Guid]
        """
        return self._parent_group_key
    
    @parent_group_key.setter
    def parent_group_key(self,value: Optional[Guid] = None) -> None:
        """
        Sets the parentGroupKey property value. The unique GUID identifier for the task folder's parent group.
        Args:
            value: Value to set for the parentGroupKey property.
        """
        self._parent_group_key = value
    
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
        writer.write_bool_value("isDefaultFolder", self.is_default_folder)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parentGroupKey", self.parent_group_key)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the task folder. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the task folder. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def tasks(self,) -> Optional[List[outlook_task.OutlookTask]]:
        """
        Gets the tasks property value. The tasks in this task folder. Read-only. Nullable.
        Returns: Optional[List[outlook_task.OutlookTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[outlook_task.OutlookTask]] = None) -> None:
        """
        Sets the tasks property value. The tasks in this task folder. Read-only. Nullable.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

