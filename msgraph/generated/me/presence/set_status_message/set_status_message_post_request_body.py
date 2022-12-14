from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

presence_status_message = lazy_import('msgraph.generated.models.presence_status_message')

class SetStatusMessagePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the setStatusMessage method.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new setStatusMessagePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The statusMessage property
        self._status_message: Optional[presence_status_message.PresenceStatusMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetStatusMessagePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetStatusMessagePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetStatusMessagePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "status_message": lambda n : setattr(self, 'status_message', n.get_object_value(presence_status_message.PresenceStatusMessage)),
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
        writer.write_object_value("statusMessage", self.status_message)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status_message(self,) -> Optional[presence_status_message.PresenceStatusMessage]:
        """
        Gets the statusMessage property value. The statusMessage property
        Returns: Optional[presence_status_message.PresenceStatusMessage]
        """
        return self._status_message
    
    @status_message.setter
    def status_message(self,value: Optional[presence_status_message.PresenceStatusMessage] = None) -> None:
        """
        Sets the statusMessage property value. The statusMessage property
        Args:
            value: Value to set for the statusMessage property.
        """
        self._status_message = value
    

