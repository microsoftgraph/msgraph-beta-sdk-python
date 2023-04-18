from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import pstn_user_block_mode

class PstnBlockedUsersLogRow(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new pstnBlockedUsersLogRow and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date and time when the user was blocked/unblocked from making PSTN calls. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._block_date_time: Optional[datetime] = None
        # The reason why the user is blocked/unblocked from making calls.
        self._block_reason: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique identifier (GUID) for the blocking/unblocking action.
        self._remediation_id: Optional[str] = None
        # Indicates whether the user is blocked or unblocked from making PSTN calls in Microsoft Teams. The possible values are: blocked, unblocked, unknownFutureValue.
        self._user_block_mode: Optional[pstn_user_block_mode.PstnUserBlockMode] = None
        # Display name of the user.
        self._user_display_name: Optional[str] = None
        # The unique identifier (GUID) of the user in Azure Active Directory.
        self._user_id: Optional[str] = None
        # The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        self._user_principal_name: Optional[str] = None
        # User's blocked number. For details, see E.164.
        self._user_telephone_number: Optional[str] = None
    
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
    def block_date_time(self,) -> Optional[datetime]:
        """
        Gets the blockDateTime property value. The date and time when the user was blocked/unblocked from making PSTN calls. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._block_date_time
    
    @block_date_time.setter
    def block_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the blockDateTime property value. The date and time when the user was blocked/unblocked from making PSTN calls. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the block_date_time property.
        """
        self._block_date_time = value
    
    @property
    def block_reason(self,) -> Optional[str]:
        """
        Gets the blockReason property value. The reason why the user is blocked/unblocked from making calls.
        Returns: Optional[str]
        """
        return self._block_reason
    
    @block_reason.setter
    def block_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the blockReason property value. The reason why the user is blocked/unblocked from making calls.
        Args:
            value: Value to set for the block_reason property.
        """
        self._block_reason = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PstnBlockedUsersLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PstnBlockedUsersLogRow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PstnBlockedUsersLogRow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import pstn_user_block_mode

        fields: Dict[str, Callable[[Any], None]] = {
            "blockDateTime": lambda n : setattr(self, 'block_date_time', n.get_datetime_value()),
            "blockReason": lambda n : setattr(self, 'block_reason', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediationId": lambda n : setattr(self, 'remediation_id', n.get_str_value()),
            "userBlockMode": lambda n : setattr(self, 'user_block_mode', n.get_enum_value(pstn_user_block_mode.PstnUserBlockMode)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userTelephoneNumber": lambda n : setattr(self, 'user_telephone_number', n.get_str_value()),
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
    def remediation_id(self,) -> Optional[str]:
        """
        Gets the remediationId property value. Unique identifier (GUID) for the blocking/unblocking action.
        Returns: Optional[str]
        """
        return self._remediation_id
    
    @remediation_id.setter
    def remediation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationId property value. Unique identifier (GUID) for the blocking/unblocking action.
        Args:
            value: Value to set for the remediation_id property.
        """
        self._remediation_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("blockDateTime", self.block_date_time)
        writer.write_str_value("blockReason", self.block_reason)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remediationId", self.remediation_id)
        writer.write_enum_value("userBlockMode", self.user_block_mode)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userTelephoneNumber", self.user_telephone_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_block_mode(self,) -> Optional[pstn_user_block_mode.PstnUserBlockMode]:
        """
        Gets the userBlockMode property value. Indicates whether the user is blocked or unblocked from making PSTN calls in Microsoft Teams. The possible values are: blocked, unblocked, unknownFutureValue.
        Returns: Optional[pstn_user_block_mode.PstnUserBlockMode]
        """
        return self._user_block_mode
    
    @user_block_mode.setter
    def user_block_mode(self,value: Optional[pstn_user_block_mode.PstnUserBlockMode] = None) -> None:
        """
        Sets the userBlockMode property value. Indicates whether the user is blocked or unblocked from making PSTN calls in Microsoft Teams. The possible values are: blocked, unblocked, unknownFutureValue.
        Args:
            value: Value to set for the user_block_mode property.
        """
        self._user_block_mode = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user.
        Args:
            value: Value to set for the user_display_name property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The unique identifier (GUID) of the user in Azure Active Directory.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The unique identifier (GUID) of the user in Azure Active Directory.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def user_telephone_number(self,) -> Optional[str]:
        """
        Gets the userTelephoneNumber property value. User's blocked number. For details, see E.164.
        Returns: Optional[str]
        """
        return self._user_telephone_number
    
    @user_telephone_number.setter
    def user_telephone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the userTelephoneNumber property value. User's blocked number. For details, see E.164.
        Args:
            value: Value to set for the user_telephone_number property.
        """
        self._user_telephone_number = value
    

