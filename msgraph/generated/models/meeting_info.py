from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import join_meeting_id_meeting_info, organizer_meeting_info, token_meeting_info

class MeetingInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new meetingInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The allowConversationWithoutHost property
        self._allow_conversation_without_host: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def allow_conversation_without_host(self,) -> Optional[bool]:
        """
        Gets the allowConversationWithoutHost property value. The allowConversationWithoutHost property
        Returns: Optional[bool]
        """
        return self._allow_conversation_without_host
    
    @allow_conversation_without_host.setter
    def allow_conversation_without_host(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowConversationWithoutHost property value. The allowConversationWithoutHost property
        Args:
            value: Value to set for the allow_conversation_without_host property.
        """
        self._allow_conversation_without_host = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.joinMeetingIdMeetingInfo":
                from . import join_meeting_id_meeting_info

                return join_meeting_id_meeting_info.JoinMeetingIdMeetingInfo()
            if mapping_value == "#microsoft.graph.organizerMeetingInfo":
                from . import organizer_meeting_info

                return organizer_meeting_info.OrganizerMeetingInfo()
            if mapping_value == "#microsoft.graph.tokenMeetingInfo":
                from . import token_meeting_info

                return token_meeting_info.TokenMeetingInfo()
        return MeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import join_meeting_id_meeting_info, organizer_meeting_info, token_meeting_info

        fields: Dict[str, Callable[[Any], None]] = {
            "allowConversationWithoutHost": lambda n : setattr(self, 'allow_conversation_without_host', n.get_bool_value()),
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
        writer.write_bool_value("allowConversationWithoutHost", self.allow_conversation_without_host)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

