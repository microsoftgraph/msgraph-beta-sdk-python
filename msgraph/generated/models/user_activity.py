from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_history_item, entity, json, status, visual_info

from . import entity

@dataclass
class UserActivity(entity.Entity):
    # The activationUrl property
    activation_url: Optional[str] = None
    # The activitySourceHost property
    activity_source_host: Optional[str] = None
    # The appActivityId property
    app_activity_id: Optional[str] = None
    # The appDisplayName property
    app_display_name: Optional[str] = None
    # The contentInfo property
    content_info: Optional[json.Json] = None
    # The contentUrl property
    content_url: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The expirationDateTime property
    expiration_date_time: Optional[datetime] = None
    # The fallbackUrl property
    fallback_url: Optional[str] = None
    # The historyItems property
    history_items: Optional[List[activity_history_item.ActivityHistoryItem]] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[status.Status] = None
    # The userTimezone property
    user_timezone: Optional[str] = None
    # The visualElements property
    visual_elements: Optional[visual_info.VisualInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_history_item, entity, json, status, visual_info

        from . import activity_history_item, entity, json, status, visual_info

        fields: Dict[str, Callable[[Any], None]] = {
            "activationUrl": lambda n : setattr(self, 'activation_url', n.get_str_value()),
            "activitySourceHost": lambda n : setattr(self, 'activity_source_host', n.get_str_value()),
            "appActivityId": lambda n : setattr(self, 'app_activity_id', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(json.Json)),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fallbackUrl": lambda n : setattr(self, 'fallback_url', n.get_str_value()),
            "historyItems": lambda n : setattr(self, 'history_items', n.get_collection_of_object_values(activity_history_item.ActivityHistoryItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(status.Status)),
            "userTimezone": lambda n : setattr(self, 'user_timezone', n.get_str_value()),
            "visualElements": lambda n : setattr(self, 'visual_elements', n.get_object_value(visual_info.VisualInfo)),
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
        writer.write_str_value("activationUrl", self.activation_url)
        writer.write_str_value("activitySourceHost", self.activity_source_host)
        writer.write_str_value("appActivityId", self.app_activity_id)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("fallbackUrl", self.fallback_url)
        writer.write_collection_of_object_values("historyItems", self.history_items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userTimezone", self.user_timezone)
        writer.write_object_value("visualElements", self.visual_elements)
    

