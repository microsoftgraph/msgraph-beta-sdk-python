from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')
group_policy_definition_file = lazy_import('msgraph.generated.models.group_policy_definition_file')
ingestion_source = lazy_import('msgraph.generated.models.ingestion_source')

class GroupPolicyCategory(entity.Entity):
    @property
    def children(self,) -> Optional[List[GroupPolicyCategory]]:
        """
        Gets the children property value. The children categories
        Returns: Optional[List[GroupPolicyCategory]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[GroupPolicyCategory]] = None) -> None:
        """
        Sets the children property value. The children categories
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyCategory and sets the default values.
        """
        super().__init__()
        # The children categories
        self._children: Optional[List[GroupPolicyCategory]] = None
        # The id of the definition file the category came from
        self._definition_file: Optional[group_policy_definition_file.GroupPolicyDefinitionFile] = None
        # The immediate GroupPolicyDefinition children of the category
        self._definitions: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None
        # The string id of the category's display name
        self._display_name: Optional[str] = None
        # Category Ingestion source
        self._ingestion_source: Optional[ingestion_source.IngestionSource] = None
        # Defines if the category is a root category
        self._is_root: Optional[bool] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parent category
        self._parent: Optional[GroupPolicyCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyCategory()
    
    @property
    def definition_file(self,) -> Optional[group_policy_definition_file.GroupPolicyDefinitionFile]:
        """
        Gets the definitionFile property value. The id of the definition file the category came from
        Returns: Optional[group_policy_definition_file.GroupPolicyDefinitionFile]
        """
        return self._definition_file
    
    @definition_file.setter
    def definition_file(self,value: Optional[group_policy_definition_file.GroupPolicyDefinitionFile] = None) -> None:
        """
        Sets the definitionFile property value. The id of the definition file the category came from
        Args:
            value: Value to set for the definitionFile property.
        """
        self._definition_file = value
    
    @property
    def definitions(self,) -> Optional[List[group_policy_definition.GroupPolicyDefinition]]:
        """
        Gets the definitions property value. The immediate GroupPolicyDefinition children of the category
        Returns: Optional[List[group_policy_definition.GroupPolicyDefinition]]
        """
        return self._definitions
    
    @definitions.setter
    def definitions(self,value: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None) -> None:
        """
        Sets the definitions property value. The immediate GroupPolicyDefinition children of the category
        Args:
            value: Value to set for the definitions property.
        """
        self._definitions = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The string id of the category's display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The string id of the category's display name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(GroupPolicyCategory)),
            "definition_file": lambda n : setattr(self, 'definition_file', n.get_object_value(group_policy_definition_file.GroupPolicyDefinitionFile)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(group_policy_definition.GroupPolicyDefinition)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ingestion_source": lambda n : setattr(self, 'ingestion_source', n.get_enum_value(ingestion_source.IngestionSource)),
            "is_root": lambda n : setattr(self, 'is_root', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(GroupPolicyCategory)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ingestion_source(self,) -> Optional[ingestion_source.IngestionSource]:
        """
        Gets the ingestionSource property value. Category Ingestion source
        Returns: Optional[ingestion_source.IngestionSource]
        """
        return self._ingestion_source
    
    @ingestion_source.setter
    def ingestion_source(self,value: Optional[ingestion_source.IngestionSource] = None) -> None:
        """
        Sets the ingestionSource property value. Category Ingestion source
        Args:
            value: Value to set for the ingestionSource property.
        """
        self._ingestion_source = value
    
    @property
    def is_root(self,) -> Optional[bool]:
        """
        Gets the isRoot property value. Defines if the category is a root category
        Returns: Optional[bool]
        """
        return self._is_root
    
    @is_root.setter
    def is_root(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRoot property value. Defines if the category is a root category
        Args:
            value: Value to set for the isRoot property.
        """
        self._is_root = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def parent(self,) -> Optional[GroupPolicyCategory]:
        """
        Gets the parent property value. The parent category
        Returns: Optional[GroupPolicyCategory]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[GroupPolicyCategory] = None) -> None:
        """
        Sets the parent property value. The parent category
        Args:
            value: Value to set for the parent property.
        """
        self._parent = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_object_value("definitionFile", self.definition_file)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("ingestionSource", self.ingestion_source)
        writer.write_bool_value("isRoot", self.is_root)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("parent", self.parent)
    

