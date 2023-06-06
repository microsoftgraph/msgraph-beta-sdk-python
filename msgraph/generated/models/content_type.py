from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import column_definition, column_link, content_type_order, document_set, document_set_content, entity, item_reference

from . import entity

@dataclass
class ContentType(entity.Entity):
    # List of canonical URLs for hub sites with which this content type is associated to. This will contain all hubsites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type will be applied to the lists in the enforced sites.
    associated_hubs_urls: Optional[List[str]] = None
    # Parent contentType from which this content type is derived.
    base: Optional[ContentType] = None
    # The collection of content types that are ancestors of this content type.
    base_types: Optional[List[ContentType]] = None
    # The collection of columns that are required by this content type
    column_links: Optional[List[column_link.ColumnLink]] = None
    # Column order information in a content type.
    column_positions: Optional[List[column_definition.ColumnDefinition]] = None
    # The collection of column definitions for this contentType.
    columns: Optional[List[column_definition.ColumnDefinition]] = None
    # The descriptive text for the item.
    description: Optional[str] = None
    # Document Set metadata.
    document_set: Optional[document_set.DocumentSet] = None
    # Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.
    document_template: Optional[document_set_content.DocumentSetContent] = None
    # The name of the group this content type belongs to. Helps organize related content types.
    group: Optional[str] = None
    # Indicates whether the content type is hidden in the list's 'New' menu.
    hidden: Optional[bool] = None
    # If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.
    inherited_from: Optional[item_reference.ItemReference] = None
    # Specifies if a content type is a built-in content type.
    is_built_in: Optional[bool] = None
    # The name of the content type.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the order in which the content type appears in the selection UI.
    order: Optional[content_type_order.ContentTypeOrder] = None
    # The unique identifier of the content type.
    parent_id: Optional[str] = None
    # If true, any changes made to the content type will be pushed to inherited content types and lists that implement the content type.
    propagate_changes: Optional[bool] = None
    # If true, the content type cannot be modified unless this value is first set to false.
    read_only: Optional[bool] = None
    # If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.
    sealed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import column_definition, column_link, content_type_order, document_set, document_set_content, entity, item_reference

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedHubsUrls": lambda n : setattr(self, 'associated_hubs_urls', n.get_collection_of_primitive_values(str)),
            "base": lambda n : setattr(self, 'base', n.get_object_value(ContentType)),
            "baseTypes": lambda n : setattr(self, 'base_types', n.get_collection_of_object_values(ContentType)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "columnLinks": lambda n : setattr(self, 'column_links', n.get_collection_of_object_values(column_link.ColumnLink)),
            "columnPositions": lambda n : setattr(self, 'column_positions', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentSet": lambda n : setattr(self, 'document_set', n.get_object_value(document_set.DocumentSet)),
            "documentTemplate": lambda n : setattr(self, 'document_template', n.get_object_value(document_set_content.DocumentSetContent)),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "inheritedFrom": lambda n : setattr(self, 'inherited_from', n.get_object_value(item_reference.ItemReference)),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_object_value(content_type_order.ContentTypeOrder)),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "propagateChanges": lambda n : setattr(self, 'propagate_changes', n.get_bool_value()),
            "readOnly": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "sealed": lambda n : setattr(self, 'sealed', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("associatedHubsUrls", self.associated_hubs_urls)
        writer.write_object_value("base", self.base)
        writer.write_collection_of_object_values("baseTypes", self.base_types)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("columnLinks", self.column_links)
        writer.write_collection_of_object_values("columnPositions", self.column_positions)
        writer.write_str_value("description", self.description)
        writer.write_object_value("documentSet", self.document_set)
        writer.write_object_value("documentTemplate", self.document_template)
        writer.write_str_value("group", self.group)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("inheritedFrom", self.inherited_from)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_str_value("name", self.name)
        writer.write_object_value("order", self.order)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_bool_value("propagateChanges", self.propagate_changes)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_bool_value("sealed", self.sealed)
    

