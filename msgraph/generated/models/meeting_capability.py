from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

auto_admitted_users_type = lazy_import('msgraph.generated.models.auto_admitted_users_type')

class MeetingCapability(AdditionalDataHolder, Parsable):
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
    def allow_anonymous_users_to_dial_out(self,) -> Optional[bool]:
        """
        Gets the allowAnonymousUsersToDialOut property value. Indicates whether anonymous users dialout is allowed in a meeting.
        Returns: Optional[bool]
        """
        return self._allow_anonymous_users_to_dial_out
    
    @allow_anonymous_users_to_dial_out.setter
    def allow_anonymous_users_to_dial_out(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAnonymousUsersToDialOut property value. Indicates whether anonymous users dialout is allowed in a meeting.
        Args:
            value: Value to set for the allowAnonymousUsersToDialOut property.
        """
        self._allow_anonymous_users_to_dial_out = value
    
    @property
    def allow_anonymous_users_to_start_meeting(self,) -> Optional[bool]:
        """
        Gets the allowAnonymousUsersToStartMeeting property value. Indicates whether anonymous users are allowed to start a meeting.
        Returns: Optional[bool]
        """
        return self._allow_anonymous_users_to_start_meeting
    
    @allow_anonymous_users_to_start_meeting.setter
    def allow_anonymous_users_to_start_meeting(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAnonymousUsersToStartMeeting property value. Indicates whether anonymous users are allowed to start a meeting.
        Args:
            value: Value to set for the allowAnonymousUsersToStartMeeting property.
        """
        self._allow_anonymous_users_to_start_meeting = value
    
    @property
    def auto_admitted_users(self,) -> Optional[auto_admitted_users_type.AutoAdmittedUsersType]:
        """
        Gets the autoAdmittedUsers property value. The autoAdmittedUsers property
        Returns: Optional[auto_admitted_users_type.AutoAdmittedUsersType]
        """
        return self._auto_admitted_users
    
    @auto_admitted_users.setter
    def auto_admitted_users(self,value: Optional[auto_admitted_users_type.AutoAdmittedUsersType] = None) -> None:
        """
        Sets the autoAdmittedUsers property value. The autoAdmittedUsers property
        Args:
            value: Value to set for the autoAdmittedUsers property.
        """
        self._auto_admitted_users = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new meetingCapability and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether anonymous users dialout is allowed in a meeting.
        self._allow_anonymous_users_to_dial_out: Optional[bool] = None
        # Indicates whether anonymous users are allowed to start a meeting.
        self._allow_anonymous_users_to_start_meeting: Optional[bool] = None
        # The autoAdmittedUsers property
        self._auto_admitted_users: Optional[auto_admitted_users_type.AutoAdmittedUsersType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingCapability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingCapability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_anonymous_users_to_dial_out": lambda n : setattr(self, 'allow_anonymous_users_to_dial_out', n.get_bool_value()),
            "allow_anonymous_users_to_start_meeting": lambda n : setattr(self, 'allow_anonymous_users_to_start_meeting', n.get_bool_value()),
            "auto_admitted_users": lambda n : setattr(self, 'auto_admitted_users', n.get_enum_value(auto_admitted_users_type.AutoAdmittedUsersType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_bool_value("allowAnonymousUsersToDialOut", self.allow_anonymous_users_to_dial_out)
        writer.write_bool_value("allowAnonymousUsersToStartMeeting", self.allow_anonymous_users_to_start_meeting)
        writer.write_enum_value("autoAdmittedUsers", self.auto_admitted_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

