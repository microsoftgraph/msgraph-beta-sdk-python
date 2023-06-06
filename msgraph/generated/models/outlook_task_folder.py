from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, multi_value_legacy_extended_property, outlook_task, single_value_legacy_extended_property

from . import entity

@dataclass
class OutlookTaskFolder(entity.Entity):
    # The version of the task folder.
    change_key: Optional[str] = None
    # True if the folder is the default task folder.
    is_default_folder: Optional[bool] = None
    # The collection of multi-value extended properties defined for the task folder. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
    # The name of the task folder.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique GUID identifier for the task folder's parent group.
    parent_group_key: Optional[UUID] = None
    # The collection of single-value extended properties defined for the task folder. Read-only. Nullable.
    single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
    # The tasks in this task folder. Read-only. Nullable.
    tasks: Optional[List[outlook_task.OutlookTask]] = None
    
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
        from . import entity, multi_value_legacy_extended_property, outlook_task, single_value_legacy_extended_property

        fields: Dict[str, Callable[[Any], None]] = {
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "isDefaultFolder": lambda n : setattr(self, 'is_default_folder', n.get_bool_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentGroupKey": lambda n : setattr(self, 'parent_group_key', n.get_uuid_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(outlook_task.OutlookTask)),
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
        writer.write_str_value("changeKey", self.change_key)
        writer.write_bool_value("isDefaultFolder", self.is_default_folder)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("parentGroupKey", self.parent_group_key)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

