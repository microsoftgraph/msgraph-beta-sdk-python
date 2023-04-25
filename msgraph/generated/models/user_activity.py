from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_history_item, entity, json, status, visual_info

from . import entity

class UserActivity(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserActivity and sets the default values.
        """
        super().__init__()
        # The activationUrl property
        self._activation_url: Optional[str] = None
        # The activitySourceHost property
        self._activity_source_host: Optional[str] = None
        # The appActivityId property
        self._app_activity_id: Optional[str] = None
        # The appDisplayName property
        self._app_display_name: Optional[str] = None
        # The contentInfo property
        self._content_info: Optional[json.Json] = None
        # The contentUrl property
        self._content_url: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The expirationDateTime property
        self._expiration_date_time: Optional[datetime] = None
        # The fallbackUrl property
        self._fallback_url: Optional[str] = None
        # The historyItems property
        self._history_items: Optional[List[activity_history_item.ActivityHistoryItem]] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[status.Status] = None
        # The userTimezone property
        self._user_timezone: Optional[str] = None
        # The visualElements property
        self._visual_elements: Optional[visual_info.VisualInfo] = None
    
    @property
    def activation_url(self,) -> Optional[str]:
        """
        Gets the activationUrl property value. The activationUrl property
        Returns: Optional[str]
        """
        return self._activation_url
    
    @activation_url.setter
    def activation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the activationUrl property value. The activationUrl property
        Args:
            value: Value to set for the activation_url property.
        """
        self._activation_url = value
    
    @property
    def activity_source_host(self,) -> Optional[str]:
        """
        Gets the activitySourceHost property value. The activitySourceHost property
        Returns: Optional[str]
        """
        return self._activity_source_host
    
    @activity_source_host.setter
    def activity_source_host(self,value: Optional[str] = None) -> None:
        """
        Sets the activitySourceHost property value. The activitySourceHost property
        Args:
            value: Value to set for the activity_source_host property.
        """
        self._activity_source_host = value
    
    @property
    def app_activity_id(self,) -> Optional[str]:
        """
        Gets the appActivityId property value. The appActivityId property
        Returns: Optional[str]
        """
        return self._app_activity_id
    
    @app_activity_id.setter
    def app_activity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appActivityId property value. The appActivityId property
        Args:
            value: Value to set for the app_activity_id property.
        """
        self._app_activity_id = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The appDisplayName property
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The appDisplayName property
        Args:
            value: Value to set for the app_display_name property.
        """
        self._app_display_name = value
    
    @property
    def content_info(self,) -> Optional[json.Json]:
        """
        Gets the contentInfo property value. The contentInfo property
        Returns: Optional[json.Json]
        """
        return self._content_info
    
    @content_info.setter
    def content_info(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the contentInfo property value. The contentInfo property
        Args:
            value: Value to set for the content_info property.
        """
        self._content_info = value
    
    @property
    def content_url(self,) -> Optional[str]:
        """
        Gets the contentUrl property value. The contentUrl property
        Returns: Optional[str]
        """
        return self._content_url
    
    @content_url.setter
    def content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentUrl property value. The contentUrl property
        Args:
            value: Value to set for the content_url property.
        """
        self._content_url = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserActivity()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    @property
    def fallback_url(self,) -> Optional[str]:
        """
        Gets the fallbackUrl property value. The fallbackUrl property
        Returns: Optional[str]
        """
        return self._fallback_url
    
    @fallback_url.setter
    def fallback_url(self,value: Optional[str] = None) -> None:
        """
        Sets the fallbackUrl property value. The fallbackUrl property
        Args:
            value: Value to set for the fallback_url property.
        """
        self._fallback_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def history_items(self,) -> Optional[List[activity_history_item.ActivityHistoryItem]]:
        """
        Gets the historyItems property value. The historyItems property
        Returns: Optional[List[activity_history_item.ActivityHistoryItem]]
        """
        return self._history_items
    
    @history_items.setter
    def history_items(self,value: Optional[List[activity_history_item.ActivityHistoryItem]] = None) -> None:
        """
        Sets the historyItems property value. The historyItems property
        Args:
            value: Value to set for the history_items property.
        """
        self._history_items = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def status(self,) -> Optional[status.Status]:
        """
        Gets the status property value. The status property
        Returns: Optional[status.Status]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[status.Status] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_timezone(self,) -> Optional[str]:
        """
        Gets the userTimezone property value. The userTimezone property
        Returns: Optional[str]
        """
        return self._user_timezone
    
    @user_timezone.setter
    def user_timezone(self,value: Optional[str] = None) -> None:
        """
        Sets the userTimezone property value. The userTimezone property
        Args:
            value: Value to set for the user_timezone property.
        """
        self._user_timezone = value
    
    @property
    def visual_elements(self,) -> Optional[visual_info.VisualInfo]:
        """
        Gets the visualElements property value. The visualElements property
        Returns: Optional[visual_info.VisualInfo]
        """
        return self._visual_elements
    
    @visual_elements.setter
    def visual_elements(self,value: Optional[visual_info.VisualInfo] = None) -> None:
        """
        Sets the visualElements property value. The visualElements property
        Args:
            value: Value to set for the visual_elements property.
        """
        self._visual_elements = value
    

