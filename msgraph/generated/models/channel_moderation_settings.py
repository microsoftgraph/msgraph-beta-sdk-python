from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import reply_restriction, user_new_message_restriction

class ChannelModerationSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new channelModerationSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether bots are allowed to post messages.
        self._allow_new_message_from_bots: Optional[bool] = None
        # Indicates whether connectors are allowed to post messages.
        self._allow_new_message_from_connectors: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates who is allowed to reply to the teams channel. Possible values are: everyone, authorAndModerators, unknownFutureValue.
        self._reply_restriction: Optional[reply_restriction.ReplyRestriction] = None
        # Indicates who is allowed to post messages to teams channel. Possible values are: everyone, everyoneExceptGuests, moderators, unknownFutureValue.
        self._user_new_message_restriction: Optional[user_new_message_restriction.UserNewMessageRestriction] = None
    
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
    def allow_new_message_from_bots(self,) -> Optional[bool]:
        """
        Gets the allowNewMessageFromBots property value. Indicates whether bots are allowed to post messages.
        Returns: Optional[bool]
        """
        return self._allow_new_message_from_bots
    
    @allow_new_message_from_bots.setter
    def allow_new_message_from_bots(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNewMessageFromBots property value. Indicates whether bots are allowed to post messages.
        Args:
            value: Value to set for the allow_new_message_from_bots property.
        """
        self._allow_new_message_from_bots = value
    
    @property
    def allow_new_message_from_connectors(self,) -> Optional[bool]:
        """
        Gets the allowNewMessageFromConnectors property value. Indicates whether connectors are allowed to post messages.
        Returns: Optional[bool]
        """
        return self._allow_new_message_from_connectors
    
    @allow_new_message_from_connectors.setter
    def allow_new_message_from_connectors(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNewMessageFromConnectors property value. Indicates whether connectors are allowed to post messages.
        Args:
            value: Value to set for the allow_new_message_from_connectors property.
        """
        self._allow_new_message_from_connectors = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelModerationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelModerationSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelModerationSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import reply_restriction, user_new_message_restriction

        fields: Dict[str, Callable[[Any], None]] = {
            "allowNewMessageFromBots": lambda n : setattr(self, 'allow_new_message_from_bots', n.get_bool_value()),
            "allowNewMessageFromConnectors": lambda n : setattr(self, 'allow_new_message_from_connectors', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "replyRestriction": lambda n : setattr(self, 'reply_restriction', n.get_enum_value(reply_restriction.ReplyRestriction)),
            "userNewMessageRestriction": lambda n : setattr(self, 'user_new_message_restriction', n.get_enum_value(user_new_message_restriction.UserNewMessageRestriction)),
        }
        return fields
    
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
    
    @property
    def reply_restriction(self,) -> Optional[reply_restriction.ReplyRestriction]:
        """
        Gets the replyRestriction property value. Indicates who is allowed to reply to the teams channel. Possible values are: everyone, authorAndModerators, unknownFutureValue.
        Returns: Optional[reply_restriction.ReplyRestriction]
        """
        return self._reply_restriction
    
    @reply_restriction.setter
    def reply_restriction(self,value: Optional[reply_restriction.ReplyRestriction] = None) -> None:
        """
        Sets the replyRestriction property value. Indicates who is allowed to reply to the teams channel. Possible values are: everyone, authorAndModerators, unknownFutureValue.
        Args:
            value: Value to set for the reply_restriction property.
        """
        self._reply_restriction = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowNewMessageFromBots", self.allow_new_message_from_bots)
        writer.write_bool_value("allowNewMessageFromConnectors", self.allow_new_message_from_connectors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("replyRestriction", self.reply_restriction)
        writer.write_enum_value("userNewMessageRestriction", self.user_new_message_restriction)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_new_message_restriction(self,) -> Optional[user_new_message_restriction.UserNewMessageRestriction]:
        """
        Gets the userNewMessageRestriction property value. Indicates who is allowed to post messages to teams channel. Possible values are: everyone, everyoneExceptGuests, moderators, unknownFutureValue.
        Returns: Optional[user_new_message_restriction.UserNewMessageRestriction]
        """
        return self._user_new_message_restriction
    
    @user_new_message_restriction.setter
    def user_new_message_restriction(self,value: Optional[user_new_message_restriction.UserNewMessageRestriction] = None) -> None:
        """
        Sets the userNewMessageRestriction property value. Indicates who is allowed to post messages to teams channel. Possible values are: everyone, everyoneExceptGuests, moderators, unknownFutureValue.
        Args:
            value: Value to set for the user_new_message_restriction property.
        """
        self._user_new_message_restriction = value
    

