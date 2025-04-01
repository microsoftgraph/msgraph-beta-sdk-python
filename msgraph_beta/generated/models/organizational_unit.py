from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class OrganizationalUnit(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.organizationalUnit"
    # The children property
    children: Optional[list[OrganizationalUnit]] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The organizationalUnitParent property
    organizational_unit_parent: Optional[OrganizationalUnit] = None
    # The resources property
    resources: Optional[list[DirectoryObject]] = None
    # The transitiveChildren property
    transitive_children: Optional[list[OrganizationalUnit]] = None
    # The transitiveResources property
    transitive_resources: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalUnit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalUnit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(OrganizationalUnit)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "organizationalUnitParent": lambda n : setattr(self, 'organizational_unit_parent', n.get_object_value(OrganizationalUnit)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(DirectoryObject)),
            "transitiveChildren": lambda n : setattr(self, 'transitive_children', n.get_collection_of_object_values(OrganizationalUnit)),
            "transitiveResources": lambda n : setattr(self, 'transitive_resources', n.get_collection_of_object_values(DirectoryObject)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("organizationalUnitParent", self.organizational_unit_parent)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("transitiveChildren", self.transitive_children)
        writer.write_collection_of_object_values("transitiveResources", self.transitive_resources)
    

