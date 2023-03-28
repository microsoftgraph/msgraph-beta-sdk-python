from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class JoinMeetingIdSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new joinMeetingIdSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether a passcode is required to join a meeting when using joinMeetingId. Optional.
        self._is_passcode_required: Optional[bool] = None
        # The meeting ID to be used to join a meeting. Optional. Read-only.
        self._join_meeting_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The passcode to join a meeting.  Optional. Read-only.
        self._passcode: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> JoinMeetingIdSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: JoinMeetingIdSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return JoinMeetingIdSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isPasscodeRequired": lambda n : setattr(self, 'is_passcode_required', n.get_bool_value()),
            "joinMeetingId": lambda n : setattr(self, 'join_meeting_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
        }
        return fields
    
    @property
    def is_passcode_required(self,) -> Optional[bool]:
        """
        Gets the isPasscodeRequired property value. Indicates whether a passcode is required to join a meeting when using joinMeetingId. Optional.
        Returns: Optional[bool]
        """
        return self._is_passcode_required
    
    @is_passcode_required.setter
    def is_passcode_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPasscodeRequired property value. Indicates whether a passcode is required to join a meeting when using joinMeetingId. Optional.
        Args:
            value: Value to set for the is_passcode_required property.
        """
        self._is_passcode_required = value
    
    @property
    def join_meeting_id(self,) -> Optional[str]:
        """
        Gets the joinMeetingId property value. The meeting ID to be used to join a meeting. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._join_meeting_id
    
    @join_meeting_id.setter
    def join_meeting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the joinMeetingId property value. The meeting ID to be used to join a meeting. Optional. Read-only.
        Args:
            value: Value to set for the join_meeting_id property.
        """
        self._join_meeting_id = value
    
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
    def passcode(self,) -> Optional[str]:
        """
        Gets the passcode property value. The passcode to join a meeting.  Optional. Read-only.
        Returns: Optional[str]
        """
        return self._passcode
    
    @passcode.setter
    def passcode(self,value: Optional[str] = None) -> None:
        """
        Sets the passcode property value. The passcode to join a meeting.  Optional. Read-only.
        Args:
            value: Value to set for the passcode property.
        """
        self._passcode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isPasscodeRequired", self.is_passcode_required)
        writer.write_str_value("joinMeetingId", self.join_meeting_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("passcode", self.passcode)
        writer.write_additional_data_value(self.additional_data)
    

