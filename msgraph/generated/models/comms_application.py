from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

call = lazy_import('msgraph.generated.models.call')
online_meeting = lazy_import('msgraph.generated.models.online_meeting')

class CommsApplication(AdditionalDataHolder, Parsable):
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
    def calls(self,) -> Optional[List[call.Call]]:
        """
        Gets the calls property value. The calls property
        Returns: Optional[List[call.Call]]
        """
        return self._calls
    
    @calls.setter
    def calls(self,value: Optional[List[call.Call]] = None) -> None:
        """
        Sets the calls property value. The calls property
        Args:
            value: Value to set for the calls property.
        """
        self._calls = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CommsApplication and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The calls property
        self._calls: Optional[List[call.Call]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The onlineMeetings property
        self._online_meetings: Optional[List[online_meeting.OnlineMeeting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommsApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommsApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommsApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "calls": lambda n : setattr(self, 'calls', n.get_collection_of_object_values(call.Call)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "online_meetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(online_meeting.OnlineMeeting)),
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
    
    @property
    def online_meetings(self,) -> Optional[List[online_meeting.OnlineMeeting]]:
        """
        Gets the onlineMeetings property value. The onlineMeetings property
        Returns: Optional[List[online_meeting.OnlineMeeting]]
        """
        return self._online_meetings
    
    @online_meetings.setter
    def online_meetings(self,value: Optional[List[online_meeting.OnlineMeeting]] = None) -> None:
        """
        Sets the onlineMeetings property value. The onlineMeetings property
        Args:
            value: Value to set for the onlineMeetings property.
        """
        self._online_meetings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("calls", self.calls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_additional_data_value(self.additional_data)
    

