from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import drive, drive_item, entity, identity_set, item_reference, list, list_item, shared_drive_item, site, site_page, user

from . import entity

class BaseItem(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new baseItem and sets the default values.
        """
        super().__init__()
        # Identity of the user, device, or application which created the item. Read-only.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The createdByUser property
        self._created_by_user: Optional[user.User] = None
        # Date and time of item creation. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # ETag for the item. Read-only.
        self._e_tag: Optional[str] = None
        # Identity of the user, device, and application which last modified the item. Read-only.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The lastModifiedByUser property
        self._last_modified_by_user: Optional[user.User] = None
        # Date and time the item was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The name of the item. Read-write.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Parent information, if the item has a parent. Read-write.
        self._parent_reference: Optional[item_reference.ItemReference] = None
        # URL that displays the resource in the browser. Read-only.
        self._web_url: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user, device, or application which created the item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user, device, or application which created the item. Read-only.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_by_user(self,) -> Optional[user.User]:
        """
        Gets the createdByUser property value. The createdByUser property
        Returns: Optional[user.User]
        """
        return self._created_by_user
    
    @created_by_user.setter
    def created_by_user(self,value: Optional[user.User] = None) -> None:
        """
        Sets the createdByUser property value. The createdByUser property
        Args:
            value: Value to set for the created_by_user property.
        """
        self._created_by_user = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of item creation. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of item creation. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.drive":
                from . import drive

                return drive.Drive()
            if mapping_value == "#microsoft.graph.driveItem":
                from . import drive_item

                return drive_item.DriveItem()
            if mapping_value == "#microsoft.graph.list":
                from . import list

                return list.List()
            if mapping_value == "#microsoft.graph.listItem":
                from . import list_item

                return list_item.ListItem()
            if mapping_value == "#microsoft.graph.sharedDriveItem":
                from . import shared_drive_item

                return shared_drive_item.SharedDriveItem()
            if mapping_value == "#microsoft.graph.site":
                from . import site

                return site.Site()
            if mapping_value == "#microsoft.graph.sitePage":
                from . import site_page

                return site_page.SitePage()
        return BaseItem()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def e_tag(self,) -> Optional[str]:
        """
        Gets the eTag property value. ETag for the item. Read-only.
        Returns: Optional[str]
        """
        return self._e_tag
    
    @e_tag.setter
    def e_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the eTag property value. ETag for the item. Read-only.
        Args:
            value: Value to set for the e_tag property.
        """
        self._e_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import drive, drive_item, entity, identity_set, item_reference, list, list_item, shared_drive_item, site, site_page, user

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdByUser": lambda n : setattr(self, 'created_by_user', n.get_object_value(user.User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "eTag": lambda n : setattr(self, 'e_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedByUser": lambda n : setattr(self, 'last_modified_by_user', n.get_object_value(user.User)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentReference": lambda n : setattr(self, 'parent_reference', n.get_object_value(item_reference.ItemReference)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user, device, and application which last modified the item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user, device, and application which last modified the item. Read-only.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_by_user(self,) -> Optional[user.User]:
        """
        Gets the lastModifiedByUser property value. The lastModifiedByUser property
        Returns: Optional[user.User]
        """
        return self._last_modified_by_user
    
    @last_modified_by_user.setter
    def last_modified_by_user(self,value: Optional[user.User] = None) -> None:
        """
        Sets the lastModifiedByUser property value. The lastModifiedByUser property
        Args:
            value: Value to set for the last_modified_by_user property.
        """
        self._last_modified_by_user = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time the item was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time the item was last modified. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the item. Read-write.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the item. Read-write.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def parent_reference(self,) -> Optional[item_reference.ItemReference]:
        """
        Gets the parentReference property value. Parent information, if the item has a parent. Read-write.
        Returns: Optional[item_reference.ItemReference]
        """
        return self._parent_reference
    
    @parent_reference.setter
    def parent_reference(self,value: Optional[item_reference.ItemReference] = None) -> None:
        """
        Sets the parentReference property value. Parent information, if the item has a parent. Read-write.
        Args:
            value: Value to set for the parent_reference property.
        """
        self._parent_reference = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_object_value("createdByUser", self.created_by_user)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("eTag", self.e_tag)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("lastModifiedByUser", self.last_modified_by_user)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parentReference", self.parent_reference)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL that displays the resource in the browser. Read-only.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL that displays the resource in the browser. Read-only.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

