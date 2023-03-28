from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, content_type_info, deleted, document_set_version, drive_item, field_value_set, item_activity_o_l_d, item_analytics, list_item_version, sharepoint_ids

from . import base_item

class ListItem(base_item.BaseItem):
    def __init__(self,) -> None:
        """
        Instantiates a new listItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.listItem"
        # The list of recent activities that took place on this item.
        self._activities: Optional[List[item_activity_o_l_d.ItemActivityOLD]] = None
        # Analytics about the view activities that took place on this item.
        self._analytics: Optional[item_analytics.ItemAnalytics] = None
        # The content type of this list item
        self._content_type: Optional[content_type_info.ContentTypeInfo] = None
        # The deleted property
        self._deleted: Optional[deleted.Deleted] = None
        # Version information for a document set version created by a user.
        self._document_set_versions: Optional[List[document_set_version.DocumentSetVersion]] = None
        # For document libraries, the driveItem relationship exposes the listItem as a [driveItem][]
        self._drive_item: Optional[drive_item.DriveItem] = None
        # The values of the columns set on this list item.
        self._fields: Optional[field_value_set.FieldValueSet] = None
        # Returns identifiers useful for SharePoint REST compatibility. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # The list of previous versions of the list item.
        self._versions: Optional[List[list_item_version.ListItemVersion]] = None
    
    @property
    def activities(self,) -> Optional[List[item_activity_o_l_d.ItemActivityOLD]]:
        """
        Gets the activities property value. The list of recent activities that took place on this item.
        Returns: Optional[List[item_activity_o_l_d.ItemActivityOLD]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[item_activity_o_l_d.ItemActivityOLD]] = None) -> None:
        """
        Sets the activities property value. The list of recent activities that took place on this item.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    @property
    def analytics(self,) -> Optional[item_analytics.ItemAnalytics]:
        """
        Gets the analytics property value. Analytics about the view activities that took place on this item.
        Returns: Optional[item_analytics.ItemAnalytics]
        """
        return self._analytics
    
    @analytics.setter
    def analytics(self,value: Optional[item_analytics.ItemAnalytics] = None) -> None:
        """
        Sets the analytics property value. Analytics about the view activities that took place on this item.
        Args:
            value: Value to set for the analytics property.
        """
        self._analytics = value
    
    @property
    def content_type(self,) -> Optional[content_type_info.ContentTypeInfo]:
        """
        Gets the contentType property value. The content type of this list item
        Returns: Optional[content_type_info.ContentTypeInfo]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[content_type_info.ContentTypeInfo] = None) -> None:
        """
        Sets the contentType property value. The content type of this list item
        Args:
            value: Value to set for the content_type property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ListItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ListItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ListItem()
    
    @property
    def deleted(self,) -> Optional[deleted.Deleted]:
        """
        Gets the deleted property value. The deleted property
        Returns: Optional[deleted.Deleted]
        """
        return self._deleted
    
    @deleted.setter
    def deleted(self,value: Optional[deleted.Deleted] = None) -> None:
        """
        Sets the deleted property value. The deleted property
        Args:
            value: Value to set for the deleted property.
        """
        self._deleted = value
    
    @property
    def document_set_versions(self,) -> Optional[List[document_set_version.DocumentSetVersion]]:
        """
        Gets the documentSetVersions property value. Version information for a document set version created by a user.
        Returns: Optional[List[document_set_version.DocumentSetVersion]]
        """
        return self._document_set_versions
    
    @document_set_versions.setter
    def document_set_versions(self,value: Optional[List[document_set_version.DocumentSetVersion]] = None) -> None:
        """
        Sets the documentSetVersions property value. Version information for a document set version created by a user.
        Args:
            value: Value to set for the document_set_versions property.
        """
        self._document_set_versions = value
    
    @property
    def drive_item(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the driveItem property value. For document libraries, the driveItem relationship exposes the listItem as a [driveItem][]
        Returns: Optional[drive_item.DriveItem]
        """
        return self._drive_item
    
    @drive_item.setter
    def drive_item(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the driveItem property value. For document libraries, the driveItem relationship exposes the listItem as a [driveItem][]
        Args:
            value: Value to set for the drive_item property.
        """
        self._drive_item = value
    
    @property
    def fields(self,) -> Optional[field_value_set.FieldValueSet]:
        """
        Gets the fields property value. The values of the columns set on this list item.
        Returns: Optional[field_value_set.FieldValueSet]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[field_value_set.FieldValueSet] = None) -> None:
        """
        Sets the fields property value. The values of the columns set on this list item.
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, content_type_info, deleted, document_set_version, drive_item, field_value_set, item_activity_o_l_d, item_analytics, list_item_version, sharepoint_ids

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(item_activity_o_l_d.ItemActivityOLD)),
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(deleted.Deleted)),
            "documentSetVersions": lambda n : setattr(self, 'document_set_versions', n.get_collection_of_object_values(document_set_version.DocumentSetVersion)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(field_value_set.FieldValueSet)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(list_item_version.ListItemVersion)),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("contentType", self.content_type)
        writer.write_object_value("deleted", self.deleted)
        writer.write_collection_of_object_values("documentSetVersions", self.document_set_versions)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("fields", self.fields)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_collection_of_object_values("versions", self.versions)
    
    @property
    def sharepoint_ids(self,) -> Optional[sharepoint_ids.SharepointIds]:
        """
        Gets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._sharepoint_ids
    
    @sharepoint_ids.setter
    def sharepoint_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Args:
            value: Value to set for the sharepoint_ids property.
        """
        self._sharepoint_ids = value
    
    @property
    def versions(self,) -> Optional[List[list_item_version.ListItemVersion]]:
        """
        Gets the versions property value. The list of previous versions of the list item.
        Returns: Optional[List[list_item_version.ListItemVersion]]
        """
        return self._versions
    
    @versions.setter
    def versions(self,value: Optional[List[list_item_version.ListItemVersion]] = None) -> None:
        """
        Sets the versions property value. The list of previous versions of the list item.
        Args:
            value: Value to set for the versions property.
        """
        self._versions = value
    

