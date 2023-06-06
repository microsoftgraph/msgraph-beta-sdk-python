from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import pstn_user_block_mode

@dataclass
class PstnBlockedUsersLogRow(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date and time when the user was blocked/unblocked from making PSTN calls. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    block_date_time: Optional[datetime] = None
    # The reason why the user is blocked/unblocked from making calls.
    block_reason: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier (GUID) for the blocking/unblocking action.
    remediation_id: Optional[str] = None
    # Indicates whether the user is blocked or unblocked from making PSTN calls in Microsoft Teams. The possible values are: blocked, unblocked, unknownFutureValue.
    user_block_mode: Optional[pstn_user_block_mode.PstnUserBlockMode] = None
    # Display name of the user.
    user_display_name: Optional[str] = None
    # The unique identifier (GUID) of the user in Azure Active Directory.
    user_id: Optional[str] = None
    # The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
    user_principal_name: Optional[str] = None
    # User's blocked number. For details, see E.164.
    user_telephone_number: Optional[str] = None
    
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
    

