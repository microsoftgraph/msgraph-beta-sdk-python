from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import child_selectability
    from .. import entity, identity_set

from .. import entity

class Tag(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Tag and sets the default values.
        """
        super().__init__()
        # Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        self._child_selectability: Optional[child_selectability.ChildSelectability] = None
        # Returns the tags that are a child of a tag.
        self._child_tags: Optional[List[tag.Tag]] = None
        # The user who created the tag.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The description for the tag.
        self._description: Optional[str] = None
        # Display name of the tag.
        self._display_name: Optional[str] = None
        # The date and time the tag was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Returns the parent tag of the specified tag.
        self._parent: Optional[tag.Tag] = None
    
    @property
    def child_selectability(self,) -> Optional[child_selectability.ChildSelectability]:
        """
        Gets the childSelectability property value. Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        Returns: Optional[child_selectability.ChildSelectability]
        """
        return self._child_selectability
    
    @child_selectability.setter
    def child_selectability(self,value: Optional[child_selectability.ChildSelectability] = None) -> None:
        """
        Sets the childSelectability property value. Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        Args:
            value: Value to set for the child_selectability property.
        """
        self._child_selectability = value
    
    @property
    def child_tags(self,) -> Optional[List[tag.Tag]]:
        """
        Gets the childTags property value. Returns the tags that are a child of a tag.
        Returns: Optional[List[tag.Tag]]
        """
        return self._child_tags
    
    @child_tags.setter
    def child_tags(self,value: Optional[List[tag.Tag]] = None) -> None:
        """
        Sets the childTags property value. Returns the tags that are a child of a tag.
        Args:
            value: Value to set for the child_tags property.
        """
        self._child_tags = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created the tag.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created the tag.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Tag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Tag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Tag()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the tag.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the tag.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the tag.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the tag.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import child_selectability
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "childSelectability": lambda n : setattr(self, 'child_selectability', n.get_enum_value(child_selectability.ChildSelectability)),
            "childTags": lambda n : setattr(self, 'child_tags', n.get_collection_of_object_values(tag.Tag)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(tag.Tag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the tag was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the tag was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def parent(self,) -> Optional[tag.Tag]:
        """
        Gets the parent property value. Returns the parent tag of the specified tag.
        Returns: Optional[tag.Tag]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[tag.Tag] = None) -> None:
        """
        Sets the parent property value. Returns the parent tag of the specified tag.
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
        writer.write_enum_value("childSelectability", self.child_selectability)
        writer.write_collection_of_object_values("childTags", self.child_tags)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("parent", self.parent)
    

