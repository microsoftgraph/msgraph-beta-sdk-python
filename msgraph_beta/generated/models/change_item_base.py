from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .announcement import Announcement
    from .entity import Entity
    from .roadmap import Roadmap

from .entity import Entity

@dataclass
class ChangeItemBase(Entity, Parsable):
    # Specifies the Microsoft Entra service name to which this item belongs. Supports $filter (eq, ne, in) and $orderby.
    change_item_service: Optional[str] = None
    # Description of the new feature or change announcement. Supports $filter (eq, ne, in, startswith) and $orderby.
    description: Optional[str] = None
    # Link to the feature or change documentation. Supports $filter (any with eq).
    documentation_urls: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A short description of the feature or change. Supports $filter (eq, ne, in, startswith) and $orderby.
    short_description: Optional[str] = None
    # Microsoft Entra-specific tags. Example values: Top announcement - entraroadmaphighlightproductnews, New release highlight - entraroadmaphighlightnewfeature. Supports $filter (any with eq).
    system_tags: Optional[List[str]] = None
    # Identity and Access Management (IAM) related tags. Example values: External Identities, Reliability and Resilience. Supports $filter (any with eq).
    tags: Optional[List[str]] = None
    # Title of the feature or change. Supports $filter (eq, ne, in, startswith) and $orderby.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeItemBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeItemBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.announcement".casefold():
            from .announcement import Announcement

            return Announcement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roadmap".casefold():
            from .roadmap import Roadmap

            return Roadmap()
        return ChangeItemBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .announcement import Announcement
        from .entity import Entity
        from .roadmap import Roadmap

        from .announcement import Announcement
        from .entity import Entity
        from .roadmap import Roadmap

        fields: Dict[str, Callable[[Any], None]] = {
            "changeItemService": lambda n : setattr(self, 'change_item_service', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentationUrls": lambda n : setattr(self, 'documentation_urls', n.get_collection_of_primitive_values(str)),
            "shortDescription": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        from .announcement import Announcement
        from .entity import Entity
        from .roadmap import Roadmap

        writer.write_str_value("changeItemService", self.change_item_service)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("documentationUrls", self.documentation_urls)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
    

