from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
payload_types = lazy_import('msgraph.generated.models.payload_types')
priority = lazy_import('msgraph.generated.models.priority')
target_policy_endpoints = lazy_import('msgraph.generated.models.target_policy_endpoints')

class Notification(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new notification and sets the default values.
        """
        super().__init__()
        # Sets how long (in seconds) this notification content will stay in each platform's notification viewer. For example, when the notification is delivered to a Windows device, the value of this property is passed on to ToastNotification.ExpirationTime, which determines how long the toast notification will stay in the user's Windows Action Center.
        self._display_time_to_live: Optional[int] = None
        # Sets a UTC expiration date and time on a user notification using ISO 8601 format (for example, midnight UTC on Jan 1, 2019 would look like this: '2019-01-01T00:00:00Z'). When time is up, the notification is removed from the Microsoft Graph notification feed store completely and is no longer part of notification history. Max value is 30 days.
        self._expiration_date_time: Optional[datetime] = None
        # The name of the group that this notification belongs to. It is set by the developer for the purpose of grouping notifications together.
        self._group_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The payload property
        self._payload: Optional[payload_types.PayloadTypes] = None
        # Indicates the priority of a raw user notification. Visual notifications are sent with high priority by default. Valid values are None, High and Low.
        self._priority: Optional[priority.Priority] = None
        # Represents the host name of the app to which the calling service wants to post the notification, for the given user. If targeting web endpoints (see targetPolicy.platformTypes), ensure that targetHostName is the same as the name used when creating a subscription on the client side within the application JSON property.
        self._target_host_name: Optional[str] = None
        # Target policy object handles notification delivery policy for endpoint types that should be targeted (Windows, iOS, Android and WebPush) for the given user.
        self._target_policy: Optional[target_policy_endpoints.TargetPolicyEndpoints] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Notification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Notification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Notification()
    
    @property
    def display_time_to_live(self,) -> Optional[int]:
        """
        Gets the displayTimeToLive property value. Sets how long (in seconds) this notification content will stay in each platform's notification viewer. For example, when the notification is delivered to a Windows device, the value of this property is passed on to ToastNotification.ExpirationTime, which determines how long the toast notification will stay in the user's Windows Action Center.
        Returns: Optional[int]
        """
        return self._display_time_to_live
    
    @display_time_to_live.setter
    def display_time_to_live(self,value: Optional[int] = None) -> None:
        """
        Sets the displayTimeToLive property value. Sets how long (in seconds) this notification content will stay in each platform's notification viewer. For example, when the notification is delivered to a Windows device, the value of this property is passed on to ToastNotification.ExpirationTime, which determines how long the toast notification will stay in the user's Windows Action Center.
        Args:
            value: Value to set for the displayTimeToLive property.
        """
        self._display_time_to_live = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Sets a UTC expiration date and time on a user notification using ISO 8601 format (for example, midnight UTC on Jan 1, 2019 would look like this: '2019-01-01T00:00:00Z'). When time is up, the notification is removed from the Microsoft Graph notification feed store completely and is no longer part of notification history. Max value is 30 days.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Sets a UTC expiration date and time on a user notification using ISO 8601 format (for example, midnight UTC on Jan 1, 2019 would look like this: '2019-01-01T00:00:00Z'). When time is up, the notification is removed from the Microsoft Graph notification feed store completely and is no longer part of notification history. Max value is 30 days.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_time_to_live": lambda n : setattr(self, 'display_time_to_live', n.get_int_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "group_name": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_object_value(payload_types.PayloadTypes)),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(priority.Priority)),
            "target_host_name": lambda n : setattr(self, 'target_host_name', n.get_str_value()),
            "target_policy": lambda n : setattr(self, 'target_policy', n.get_object_value(target_policy_endpoints.TargetPolicyEndpoints)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_name(self,) -> Optional[str]:
        """
        Gets the groupName property value. The name of the group that this notification belongs to. It is set by the developer for the purpose of grouping notifications together.
        Returns: Optional[str]
        """
        return self._group_name
    
    @group_name.setter
    def group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the groupName property value. The name of the group that this notification belongs to. It is set by the developer for the purpose of grouping notifications together.
        Args:
            value: Value to set for the groupName property.
        """
        self._group_name = value
    
    @property
    def payload(self,) -> Optional[payload_types.PayloadTypes]:
        """
        Gets the payload property value. The payload property
        Returns: Optional[payload_types.PayloadTypes]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[payload_types.PayloadTypes] = None) -> None:
        """
        Sets the payload property value. The payload property
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def priority(self,) -> Optional[priority.Priority]:
        """
        Gets the priority property value. Indicates the priority of a raw user notification. Visual notifications are sent with high priority by default. Valid values are None, High and Low.
        Returns: Optional[priority.Priority]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[priority.Priority] = None) -> None:
        """
        Sets the priority property value. Indicates the priority of a raw user notification. Visual notifications are sent with high priority by default. Valid values are None, High and Low.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("displayTimeToLive", self.display_time_to_live)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("groupName", self.group_name)
        writer.write_object_value("payload", self.payload)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("targetHostName", self.target_host_name)
        writer.write_object_value("targetPolicy", self.target_policy)
    
    @property
    def target_host_name(self,) -> Optional[str]:
        """
        Gets the targetHostName property value. Represents the host name of the app to which the calling service wants to post the notification, for the given user. If targeting web endpoints (see targetPolicy.platformTypes), ensure that targetHostName is the same as the name used when creating a subscription on the client side within the application JSON property.
        Returns: Optional[str]
        """
        return self._target_host_name
    
    @target_host_name.setter
    def target_host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetHostName property value. Represents the host name of the app to which the calling service wants to post the notification, for the given user. If targeting web endpoints (see targetPolicy.platformTypes), ensure that targetHostName is the same as the name used when creating a subscription on the client side within the application JSON property.
        Args:
            value: Value to set for the targetHostName property.
        """
        self._target_host_name = value
    
    @property
    def target_policy(self,) -> Optional[target_policy_endpoints.TargetPolicyEndpoints]:
        """
        Gets the targetPolicy property value. Target policy object handles notification delivery policy for endpoint types that should be targeted (Windows, iOS, Android and WebPush) for the given user.
        Returns: Optional[target_policy_endpoints.TargetPolicyEndpoints]
        """
        return self._target_policy
    
    @target_policy.setter
    def target_policy(self,value: Optional[target_policy_endpoints.TargetPolicyEndpoints] = None) -> None:
        """
        Sets the targetPolicy property value. Target policy object handles notification delivery policy for endpoint types that should be targeted (Windows, iOS, Android and WebPush) for the given user.
        Args:
            value: Value to set for the targetPolicy property.
        """
        self._target_policy = value
    

