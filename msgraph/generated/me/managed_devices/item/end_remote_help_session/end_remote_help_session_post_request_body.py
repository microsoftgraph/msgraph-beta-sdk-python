from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EndRemoteHelpSessionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the endRemoteHelpSession method.
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
        Instantiates a new endRemoteHelpSessionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The sessionKey property
        self._session_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EndRemoteHelpSessionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EndRemoteHelpSessionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EndRemoteHelpSessionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "session_key": lambda n : setattr(self, 'session_key', n.get_str_value()),
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
        writer.write_str_value("sessionKey", self.session_key)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_key(self,) -> Optional[str]:
        """
        Gets the sessionKey property value. The sessionKey property
        Returns: Optional[str]
        """
        return self._session_key
    
    @session_key.setter
    def session_key(self,value: Optional[str] = None) -> None:
        """
        Sets the sessionKey property value. The sessionKey property
        Args:
            value: Value to set for the sessionKey property.
        """
        self._session_key = value
    

