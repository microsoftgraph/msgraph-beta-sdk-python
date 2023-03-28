from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import automatic_replies_setting, delegate_meeting_message_delivery_options, locale_info, mailbox_recipient_type, user_purpose, working_hours

class MailboxSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new mailboxSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Folder ID of an archive folder for the user. Read-only.
        self._archive_folder: Optional[str] = None
        # Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        self._automatic_replies_setting: Optional[automatic_replies_setting.AutomaticRepliesSetting] = None
        # The date format for the user's mailbox.
        self._date_format: Optional[str] = None
        # If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly. The default is sendToDelegateOnly.
        self._delegate_meeting_message_delivery_options: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions] = None
        # The locale information for the user, including the preferred language and country/region.
        self._language: Optional[locale_info.LocaleInfo] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time format for the user's mailbox.
        self._time_format: Optional[str] = None
        # The default time zone for the user's mailbox.
        self._time_zone: Optional[str] = None
        # The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. Possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
        self._user_purpose: Optional[user_purpose.UserPurpose] = None
        # The userPurposeV2 property
        self._user_purpose_v2: Optional[mailbox_recipient_type.MailboxRecipientType] = None
        # The days of the week and hours in a specific time zone that the user works.
        self._working_hours: Optional[working_hours.WorkingHours] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def archive_folder(self,) -> Optional[str]:
        """
        Gets the archiveFolder property value. Folder ID of an archive folder for the user. Read-only.
        Returns: Optional[str]
        """
        return self._archive_folder
    
    @archive_folder.setter
    def archive_folder(self,value: Optional[str] = None) -> None:
        """
        Sets the archiveFolder property value. Folder ID of an archive folder for the user. Read-only.
        Args:
            value: Value to set for the archive_folder property.
        """
        self._archive_folder = value
    
    @property
    def automatic_replies_setting(self,) -> Optional[automatic_replies_setting.AutomaticRepliesSetting]:
        """
        Gets the automaticRepliesSetting property value. Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        Returns: Optional[automatic_replies_setting.AutomaticRepliesSetting]
        """
        return self._automatic_replies_setting
    
    @automatic_replies_setting.setter
    def automatic_replies_setting(self,value: Optional[automatic_replies_setting.AutomaticRepliesSetting] = None) -> None:
        """
        Sets the automaticRepliesSetting property value. Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        Args:
            value: Value to set for the automatic_replies_setting property.
        """
        self._automatic_replies_setting = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailboxSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailboxSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailboxSettings()
    
    @property
    def date_format(self,) -> Optional[str]:
        """
        Gets the dateFormat property value. The date format for the user's mailbox.
        Returns: Optional[str]
        """
        return self._date_format
    
    @date_format.setter
    def date_format(self,value: Optional[str] = None) -> None:
        """
        Sets the dateFormat property value. The date format for the user's mailbox.
        Args:
            value: Value to set for the date_format property.
        """
        self._date_format = value
    
    @property
    def delegate_meeting_message_delivery_options(self,) -> Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions]:
        """
        Gets the delegateMeetingMessageDeliveryOptions property value. If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly. The default is sendToDelegateOnly.
        Returns: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions]
        """
        return self._delegate_meeting_message_delivery_options
    
    @delegate_meeting_message_delivery_options.setter
    def delegate_meeting_message_delivery_options(self,value: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions] = None) -> None:
        """
        Sets the delegateMeetingMessageDeliveryOptions property value. If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly. The default is sendToDelegateOnly.
        Args:
            value: Value to set for the delegate_meeting_message_delivery_options property.
        """
        self._delegate_meeting_message_delivery_options = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import automatic_replies_setting, delegate_meeting_message_delivery_options, locale_info, mailbox_recipient_type, user_purpose, working_hours

        fields: Dict[str, Callable[[Any], None]] = {
            "archiveFolder": lambda n : setattr(self, 'archive_folder', n.get_str_value()),
            "automaticRepliesSetting": lambda n : setattr(self, 'automatic_replies_setting', n.get_object_value(automatic_replies_setting.AutomaticRepliesSetting)),
            "dateFormat": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "delegateMeetingMessageDeliveryOptions": lambda n : setattr(self, 'delegate_meeting_message_delivery_options', n.get_enum_value(delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions)),
            "language": lambda n : setattr(self, 'language', n.get_object_value(locale_info.LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeFormat": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "userPurpose": lambda n : setattr(self, 'user_purpose', n.get_enum_value(user_purpose.UserPurpose)),
            "userPurposeV2": lambda n : setattr(self, 'user_purpose_v2', n.get_enum_value(mailbox_recipient_type.MailboxRecipientType)),
            "workingHours": lambda n : setattr(self, 'working_hours', n.get_object_value(working_hours.WorkingHours)),
        }
        return fields
    
    @property
    def language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the language property value. The locale information for the user, including the preferred language and country/region.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the language property value. The locale information for the user, including the preferred language and country/region.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("archiveFolder", self.archive_folder)
        writer.write_object_value("automaticRepliesSetting", self.automatic_replies_setting)
        writer.write_str_value("dateFormat", self.date_format)
        writer.write_enum_value("delegateMeetingMessageDeliveryOptions", self.delegate_meeting_message_delivery_options)
        writer.write_object_value("language", self.language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("timeFormat", self.time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_enum_value("userPurpose", self.user_purpose)
        writer.write_enum_value("userPurposeV2", self.user_purpose_v2)
        writer.write_object_value("workingHours", self.working_hours)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_format(self,) -> Optional[str]:
        """
        Gets the timeFormat property value. The time format for the user's mailbox.
        Returns: Optional[str]
        """
        return self._time_format
    
    @time_format.setter
    def time_format(self,value: Optional[str] = None) -> None:
        """
        Sets the timeFormat property value. The time format for the user's mailbox.
        Args:
            value: Value to set for the time_format property.
        """
        self._time_format = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The default time zone for the user's mailbox.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The default time zone for the user's mailbox.
        Args:
            value: Value to set for the time_zone property.
        """
        self._time_zone = value
    
    @property
    def user_purpose(self,) -> Optional[user_purpose.UserPurpose]:
        """
        Gets the userPurpose property value. The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. Possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
        Returns: Optional[user_purpose.UserPurpose]
        """
        return self._user_purpose
    
    @user_purpose.setter
    def user_purpose(self,value: Optional[user_purpose.UserPurpose] = None) -> None:
        """
        Sets the userPurpose property value. The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. Possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
        Args:
            value: Value to set for the user_purpose property.
        """
        self._user_purpose = value
    
    @property
    def user_purpose_v2(self,) -> Optional[mailbox_recipient_type.MailboxRecipientType]:
        """
        Gets the userPurposeV2 property value. The userPurposeV2 property
        Returns: Optional[mailbox_recipient_type.MailboxRecipientType]
        """
        return self._user_purpose_v2
    
    @user_purpose_v2.setter
    def user_purpose_v2(self,value: Optional[mailbox_recipient_type.MailboxRecipientType] = None) -> None:
        """
        Sets the userPurposeV2 property value. The userPurposeV2 property
        Args:
            value: Value to set for the user_purpose_v2 property.
        """
        self._user_purpose_v2 = value
    
    @property
    def working_hours(self,) -> Optional[working_hours.WorkingHours]:
        """
        Gets the workingHours property value. The days of the week and hours in a specific time zone that the user works.
        Returns: Optional[working_hours.WorkingHours]
        """
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self,value: Optional[working_hours.WorkingHours] = None) -> None:
        """
        Sets the workingHours property value. The days of the week and hours in a specific time zone that the user works.
        Args:
            value: Value to set for the working_hours property.
        """
        self._working_hours = value
    

