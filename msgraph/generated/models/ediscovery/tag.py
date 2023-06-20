from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import child_selectability
    from .. import entity, identity_set

from .. import entity

@dataclass
class Tag(entity.Entity):
    # Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
    child_selectability: Optional[child_selectability.ChildSelectability] = None
    # Returns the tags that are a child of a tag.
    child_tags: Optional[List[Tag]] = None
    # The user who created the tag.
    created_by: Optional[identity_set.IdentitySet] = None
    # The description for the tag.
    description: Optional[str] = None
    # Display name of the tag.
    display_name: Optional[str] = None
    # The date and time the tag was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns the parent tag of the specified tag.
    parent: Optional[Tag] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Tag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Tag
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Tag()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import child_selectability
        from .. import entity, identity_set

        from . import child_selectability
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "childSelectability": lambda n : setattr(self, 'child_selectability', n.get_enum_value(child_selectability.ChildSelectability)),
            "childTags": lambda n : setattr(self, 'child_tags', n.get_collection_of_object_values(Tag)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(Tag)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("childSelectability", self.child_selectability)
        writer.write_collection_of_object_values("childTags", self.child_tags)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("parent", self.parent)
    

