from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import calendar_color, calendar_permission, email_address, entity, event, multi_value_legacy_extended_property, online_meeting_provider_type, single_value_legacy_extended_property

from . import entity

class Calendar(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new calendar and sets the default values.
        """
        super().__init__()
        # Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        self._allowed_online_meeting_providers: Optional[List[online_meeting_provider_type.OnlineMeetingProviderType]] = None
        # The calendarGroup in which to create the calendar. If the user has never explicitly set a group for the calendar, this property is  null.
        self._calendar_group_id: Optional[str] = None
        # The permissions of the users with whom the calendar is shared.
        self._calendar_permissions: Optional[List[calendar_permission.CalendarPermission]] = None
        # The calendar view for the calendar. Navigation property. Read-only.
        self._calendar_view: Optional[List[event.Event]] = None
        # true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access, through an Outlook client or the corresponding calendarPermission resource. Read-only.
        self._can_edit: Optional[bool] = None
        # true if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it. Read-only.
        self._can_share: Optional[bool] = None
        # true if the user can read calendar items that have been marked private, false otherwise. This property is set through an Outlook client or the corresponding calendarPermission resource. Read-only.
        self._can_view_private_items: Optional[bool] = None
        # Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        self._change_key: Optional[str] = None
        # Specifies the color theme to distinguish the calendar from other calendars in a UI. The property values are: auto, lightBlue, lightGreen, lightOrange, lightGray, lightYellow, lightTeal, lightPink, lightBrown, lightRed, maxColor.
        self._color: Optional[calendar_color.CalendarColor] = None
        # The default online meeting provider for meetings sent from this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        self._default_online_meeting_provider: Optional[online_meeting_provider_type.OnlineMeetingProviderType] = None
        # The events in the calendar. Navigation property. Read-only.
        self._events: Optional[List[event.Event]] = None
        # The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is  empty.
        self._hex_color: Optional[str] = None
        # true if this is the default calendar where new events are created by default, false otherwise.
        self._is_default_calendar: Optional[bool] = None
        # Indicates whether this user calendar can be deleted from the user mailbox.
        self._is_removable: Optional[bool] = None
        # true if the user has shared the calendar with other users, false otherwise. Since only the user who created the calendar can share it, isShared and isSharedWithMe cannot be true for the same user. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        self._is_shared: Optional[bool] = None
        # true if the user has been shared this calendar, false otherwise. This property is always false for a calendar owner. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        self._is_shared_with_me: Optional[bool] = None
        # Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
        self._is_tallying_responses: Optional[bool] = None
        # The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The calendar name.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # If set, this represents the user who created or added the calendar. For a calendar that the user created or added, the owner property is set to the user. For a calendar shared with the user, the owner property is set to the person who shared that calendar with the user. Read-only.
        self._owner: Optional[email_address.EmailAddress] = None
        # The collection of single-value extended properties defined for the calendar. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
    
    @property
    def allowed_online_meeting_providers(self,) -> Optional[List[online_meeting_provider_type.OnlineMeetingProviderType]]:
        """
        Gets the allowedOnlineMeetingProviders property value. Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        Returns: Optional[List[online_meeting_provider_type.OnlineMeetingProviderType]]
        """
        return self._allowed_online_meeting_providers
    
    @allowed_online_meeting_providers.setter
    def allowed_online_meeting_providers(self,value: Optional[List[online_meeting_provider_type.OnlineMeetingProviderType]] = None) -> None:
        """
        Sets the allowedOnlineMeetingProviders property value. Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        Args:
            value: Value to set for the allowed_online_meeting_providers property.
        """
        self._allowed_online_meeting_providers = value
    
    @property
    def calendar_group_id(self,) -> Optional[str]:
        """
        Gets the calendarGroupId property value. The calendarGroup in which to create the calendar. If the user has never explicitly set a group for the calendar, this property is  null.
        Returns: Optional[str]
        """
        return self._calendar_group_id
    
    @calendar_group_id.setter
    def calendar_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the calendarGroupId property value. The calendarGroup in which to create the calendar. If the user has never explicitly set a group for the calendar, this property is  null.
        Args:
            value: Value to set for the calendar_group_id property.
        """
        self._calendar_group_id = value
    
    @property
    def calendar_permissions(self,) -> Optional[List[calendar_permission.CalendarPermission]]:
        """
        Gets the calendarPermissions property value. The permissions of the users with whom the calendar is shared.
        Returns: Optional[List[calendar_permission.CalendarPermission]]
        """
        return self._calendar_permissions
    
    @calendar_permissions.setter
    def calendar_permissions(self,value: Optional[List[calendar_permission.CalendarPermission]] = None) -> None:
        """
        Sets the calendarPermissions property value. The permissions of the users with whom the calendar is shared.
        Args:
            value: Value to set for the calendar_permissions property.
        """
        self._calendar_permissions = value
    
    @property
    def calendar_view(self,) -> Optional[List[event.Event]]:
        """
        Gets the calendarView property value. The calendar view for the calendar. Navigation property. Read-only.
        Returns: Optional[List[event.Event]]
        """
        return self._calendar_view
    
    @calendar_view.setter
    def calendar_view(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the calendarView property value. The calendar view for the calendar. Navigation property. Read-only.
        Args:
            value: Value to set for the calendar_view property.
        """
        self._calendar_view = value
    
    @property
    def can_edit(self,) -> Optional[bool]:
        """
        Gets the canEdit property value. true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access, through an Outlook client or the corresponding calendarPermission resource. Read-only.
        Returns: Optional[bool]
        """
        return self._can_edit
    
    @can_edit.setter
    def can_edit(self,value: Optional[bool] = None) -> None:
        """
        Sets the canEdit property value. true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access, through an Outlook client or the corresponding calendarPermission resource. Read-only.
        Args:
            value: Value to set for the can_edit property.
        """
        self._can_edit = value
    
    @property
    def can_share(self,) -> Optional[bool]:
        """
        Gets the canShare property value. true if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it. Read-only.
        Returns: Optional[bool]
        """
        return self._can_share
    
    @can_share.setter
    def can_share(self,value: Optional[bool] = None) -> None:
        """
        Sets the canShare property value. true if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it. Read-only.
        Args:
            value: Value to set for the can_share property.
        """
        self._can_share = value
    
    @property
    def can_view_private_items(self,) -> Optional[bool]:
        """
        Gets the canViewPrivateItems property value. true if the user can read calendar items that have been marked private, false otherwise. This property is set through an Outlook client or the corresponding calendarPermission resource. Read-only.
        Returns: Optional[bool]
        """
        return self._can_view_private_items
    
    @can_view_private_items.setter
    def can_view_private_items(self,value: Optional[bool] = None) -> None:
        """
        Sets the canViewPrivateItems property value. true if the user can read calendar items that have been marked private, false otherwise. This property is set through an Outlook client or the corresponding calendarPermission resource. Read-only.
        Args:
            value: Value to set for the can_view_private_items property.
        """
        self._can_view_private_items = value
    
    @property
    def change_key(self,) -> Optional[str]:
        """
        Gets the changeKey property value. Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        Returns: Optional[str]
        """
        return self._change_key
    
    @change_key.setter
    def change_key(self,value: Optional[str] = None) -> None:
        """
        Sets the changeKey property value. Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        Args:
            value: Value to set for the change_key property.
        """
        self._change_key = value
    
    @property
    def color(self,) -> Optional[calendar_color.CalendarColor]:
        """
        Gets the color property value. Specifies the color theme to distinguish the calendar from other calendars in a UI. The property values are: auto, lightBlue, lightGreen, lightOrange, lightGray, lightYellow, lightTeal, lightPink, lightBrown, lightRed, maxColor.
        Returns: Optional[calendar_color.CalendarColor]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[calendar_color.CalendarColor] = None) -> None:
        """
        Sets the color property value. Specifies the color theme to distinguish the calendar from other calendars in a UI. The property values are: auto, lightBlue, lightGreen, lightOrange, lightGray, lightYellow, lightTeal, lightPink, lightBrown, lightRed, maxColor.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Calendar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Calendar
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Calendar()
    
    @property
    def default_online_meeting_provider(self,) -> Optional[online_meeting_provider_type.OnlineMeetingProviderType]:
        """
        Gets the defaultOnlineMeetingProvider property value. The default online meeting provider for meetings sent from this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        Returns: Optional[online_meeting_provider_type.OnlineMeetingProviderType]
        """
        return self._default_online_meeting_provider
    
    @default_online_meeting_provider.setter
    def default_online_meeting_provider(self,value: Optional[online_meeting_provider_type.OnlineMeetingProviderType] = None) -> None:
        """
        Sets the defaultOnlineMeetingProvider property value. The default online meeting provider for meetings sent from this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
        Args:
            value: Value to set for the default_online_meeting_provider property.
        """
        self._default_online_meeting_provider = value
    
    @property
    def events(self,) -> Optional[List[event.Event]]:
        """
        Gets the events property value. The events in the calendar. Navigation property. Read-only.
        Returns: Optional[List[event.Event]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the events property value. The events in the calendar. Navigation property. Read-only.
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import calendar_color, calendar_permission, email_address, entity, event, multi_value_legacy_extended_property, online_meeting_provider_type, single_value_legacy_extended_property

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedOnlineMeetingProviders": lambda n : setattr(self, 'allowed_online_meeting_providers', n.get_collection_of_enum_values(online_meeting_provider_type.OnlineMeetingProviderType)),
            "calendarGroupId": lambda n : setattr(self, 'calendar_group_id', n.get_str_value()),
            "calendarPermissions": lambda n : setattr(self, 'calendar_permissions', n.get_collection_of_object_values(calendar_permission.CalendarPermission)),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(event.Event)),
            "canEdit": lambda n : setattr(self, 'can_edit', n.get_bool_value()),
            "canShare": lambda n : setattr(self, 'can_share', n.get_bool_value()),
            "canViewPrivateItems": lambda n : setattr(self, 'can_view_private_items', n.get_bool_value()),
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "color": lambda n : setattr(self, 'color', n.get_enum_value(calendar_color.CalendarColor)),
            "defaultOnlineMeetingProvider": lambda n : setattr(self, 'default_online_meeting_provider', n.get_enum_value(online_meeting_provider_type.OnlineMeetingProviderType)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(event.Event)),
            "hexColor": lambda n : setattr(self, 'hex_color', n.get_str_value()),
            "isDefaultCalendar": lambda n : setattr(self, 'is_default_calendar', n.get_bool_value()),
            "isRemovable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "isShared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "isSharedWithMe": lambda n : setattr(self, 'is_shared_with_me', n.get_bool_value()),
            "isTallyingResponses": lambda n : setattr(self, 'is_tallying_responses', n.get_bool_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(email_address.EmailAddress)),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hex_color(self,) -> Optional[str]:
        """
        Gets the hexColor property value. The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is  empty.
        Returns: Optional[str]
        """
        return self._hex_color
    
    @hex_color.setter
    def hex_color(self,value: Optional[str] = None) -> None:
        """
        Sets the hexColor property value. The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is  empty.
        Args:
            value: Value to set for the hex_color property.
        """
        self._hex_color = value
    
    @property
    def is_default_calendar(self,) -> Optional[bool]:
        """
        Gets the isDefaultCalendar property value. true if this is the default calendar where new events are created by default, false otherwise.
        Returns: Optional[bool]
        """
        return self._is_default_calendar
    
    @is_default_calendar.setter
    def is_default_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultCalendar property value. true if this is the default calendar where new events are created by default, false otherwise.
        Args:
            value: Value to set for the is_default_calendar property.
        """
        self._is_default_calendar = value
    
    @property
    def is_removable(self,) -> Optional[bool]:
        """
        Gets the isRemovable property value. Indicates whether this user calendar can be deleted from the user mailbox.
        Returns: Optional[bool]
        """
        return self._is_removable
    
    @is_removable.setter
    def is_removable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemovable property value. Indicates whether this user calendar can be deleted from the user mailbox.
        Args:
            value: Value to set for the is_removable property.
        """
        self._is_removable = value
    
    @property
    def is_shared(self,) -> Optional[bool]:
        """
        Gets the isShared property value. true if the user has shared the calendar with other users, false otherwise. Since only the user who created the calendar can share it, isShared and isSharedWithMe cannot be true for the same user. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        Returns: Optional[bool]
        """
        return self._is_shared
    
    @is_shared.setter
    def is_shared(self,value: Optional[bool] = None) -> None:
        """
        Sets the isShared property value. true if the user has shared the calendar with other users, false otherwise. Since only the user who created the calendar can share it, isShared and isSharedWithMe cannot be true for the same user. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        Args:
            value: Value to set for the is_shared property.
        """
        self._is_shared = value
    
    @property
    def is_shared_with_me(self,) -> Optional[bool]:
        """
        Gets the isSharedWithMe property value. true if the user has been shared this calendar, false otherwise. This property is always false for a calendar owner. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        Returns: Optional[bool]
        """
        return self._is_shared_with_me
    
    @is_shared_with_me.setter
    def is_shared_with_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSharedWithMe property value. true if the user has been shared this calendar, false otherwise. This property is always false for a calendar owner. This property is set when sharing is initiated in an Outlook client, and can be reset when the sharing is cancelled through the client or the corresponding calendarPermission resource. Read-only.
        Args:
            value: Value to set for the is_shared_with_me property.
        """
        self._is_shared_with_me = value
    
    @property
    def is_tallying_responses(self,) -> Optional[bool]:
        """
        Gets the isTallyingResponses property value. Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
        Returns: Optional[bool]
        """
        return self._is_tallying_responses
    
    @is_tallying_responses.setter
    def is_tallying_responses(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTallyingResponses property value. Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
        Args:
            value: Value to set for the is_tallying_responses property.
        """
        self._is_tallying_responses = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
        Args:
            value: Value to set for the multi_value_extended_properties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The calendar name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The calendar name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def owner(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the owner property value. If set, this represents the user who created or added the calendar. For a calendar that the user created or added, the owner property is set to the user. For a calendar shared with the user, the owner property is set to the person who shared that calendar with the user. Read-only.
        Returns: Optional[email_address.EmailAddress]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the owner property value. If set, this represents the user who created or added the calendar. For a calendar that the user created or added, the owner property is set to the user. For a calendar shared with the user, the owner property is set to the person who shared that calendar with the user. Read-only.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedOnlineMeetingProviders", self.allowed_online_meeting_providers)
        writer.write_str_value("calendarGroupId", self.calendar_group_id)
        writer.write_collection_of_object_values("calendarPermissions", self.calendar_permissions)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_bool_value("canEdit", self.can_edit)
        writer.write_bool_value("canShare", self.can_share)
        writer.write_bool_value("canViewPrivateItems", self.can_view_private_items)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_enum_value("color", self.color)
        writer.write_enum_value("defaultOnlineMeetingProvider", self.default_online_meeting_provider)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("hexColor", self.hex_color)
        writer.write_bool_value("isDefaultCalendar", self.is_default_calendar)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_bool_value("isSharedWithMe", self.is_shared_with_me)
        writer.write_bool_value("isTallyingResponses", self.is_tallying_responses)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("name", self.name)
        writer.write_object_value("owner", self.owner)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the calendar. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the calendar. Read-only. Nullable.
        Args:
            value: Value to set for the single_value_extended_properties property.
        """
        self._single_value_extended_properties = value
    

