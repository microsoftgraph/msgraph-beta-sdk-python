from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, drive_item, identity_set, list, list_item, permission, site

from . import base_item

class SharedDriveItem(base_item.BaseItem):
    def __init__(self,) -> None:
        """
        Instantiates a new SharedDriveItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sharedDriveItem"
        # Used to access the underlying driveItem
        self._drive_item: Optional[drive_item.DriveItem] = None
        # All driveItems contained in the sharing root. This collection cannot be enumerated.
        self._items: Optional[List[drive_item.DriveItem]] = None
        # Used to access the underlying list
        self._list: Optional[list.List] = None
        # Used to access the underlying listItem
        self._list_item: Optional[list_item.ListItem] = None
        # Information about the owner of the shared item being referenced.
        self._owner: Optional[identity_set.IdentitySet] = None
        # Used to access the permission representing the underlying sharing link
        self._permission: Optional[permission.Permission] = None
        # The root property
        self._root: Optional[drive_item.DriveItem] = None
        # Used to access the underlying site
        self._site: Optional[site.Site] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedDriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedDriveItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedDriveItem()
    
    @property
    def drive_item(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the driveItem property value. Used to access the underlying driveItem
        Returns: Optional[drive_item.DriveItem]
        """
        return self._drive_item
    
    @drive_item.setter
    def drive_item(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the driveItem property value. Used to access the underlying driveItem
        Args:
            value: Value to set for the drive_item property.
        """
        self._drive_item = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, drive_item, identity_set, list, list_item, permission, site

        fields: Dict[str, Callable[[Any], None]] = {
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(drive_item.DriveItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list.List)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "permission": lambda n : setattr(self, 'permission', n.get_object_value(permission.Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(drive_item.DriveItem)),
            "site": lambda n : setattr(self, 'site', n.get_object_value(site.Site)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[drive_item.DriveItem]]:
        """
        Gets the items property value. All driveItems contained in the sharing root. This collection cannot be enumerated.
        Returns: Optional[List[drive_item.DriveItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[drive_item.DriveItem]] = None) -> None:
        """
        Sets the items property value. All driveItems contained in the sharing root. This collection cannot be enumerated.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def list(self,) -> Optional[list.List]:
        """
        Gets the list property value. Used to access the underlying list
        Returns: Optional[list.List]
        """
        return self._list
    
    @list.setter
    def list(self,value: Optional[list.List] = None) -> None:
        """
        Sets the list property value. Used to access the underlying list
        Args:
            value: Value to set for the list property.
        """
        self._list = value
    
    @property
    def list_item(self,) -> Optional[list_item.ListItem]:
        """
        Gets the listItem property value. Used to access the underlying listItem
        Returns: Optional[list_item.ListItem]
        """
        return self._list_item
    
    @list_item.setter
    def list_item(self,value: Optional[list_item.ListItem] = None) -> None:
        """
        Sets the listItem property value. Used to access the underlying listItem
        Args:
            value: Value to set for the list_item property.
        """
        self._list_item = value
    
    @property
    def owner(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the owner property value. Information about the owner of the shared item being referenced.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the owner property value. Information about the owner of the shared item being referenced.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def permission(self,) -> Optional[permission.Permission]:
        """
        Gets the permission property value. Used to access the permission representing the underlying sharing link
        Returns: Optional[permission.Permission]
        """
        return self._permission
    
    @permission.setter
    def permission(self,value: Optional[permission.Permission] = None) -> None:
        """
        Sets the permission property value. Used to access the permission representing the underlying sharing link
        Args:
            value: Value to set for the permission property.
        """
        self._permission = value
    
    @property
    def root(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the root property value. The root property
        Returns: Optional[drive_item.DriveItem]
        """
        return self._root
    
    @root.setter
    def root(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the root property value. The root property
        Args:
            value: Value to set for the root property.
        """
        self._root = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("permission", self.permission)
        writer.write_object_value("root", self.root)
        writer.write_object_value("site", self.site)
    
    @property
    def site(self,) -> Optional[site.Site]:
        """
        Gets the site property value. Used to access the underlying site
        Returns: Optional[site.Site]
        """
        return self._site
    
    @site.setter
    def site(self,value: Optional[site.Site] = None) -> None:
        """
        Sets the site property value. Used to access the underlying site
        Args:
            value: Value to set for the site property.
        """
        self._site = value
    

