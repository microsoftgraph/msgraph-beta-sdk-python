from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RequestRemoteHelpSessionAccessPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the requestRemoteHelpSessionAccess method.
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
        Instantiates a new requestRemoteHelpSessionAccessPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The pubSubConnectionId property
        self._pub_sub_connection_id: Optional[str] = None
        # The sessionKey property
        self._session_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestRemoteHelpSessionAccessPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestRemoteHelpSessionAccessPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestRemoteHelpSessionAccessPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "pub_sub_connection_id": lambda n : setattr(self, 'pub_sub_connection_id', n.get_str_value()),
            "session_key": lambda n : setattr(self, 'session_key', n.get_str_value()),
        }
        return fields
    
    @property
    def pub_sub_connection_id(self,) -> Optional[str]:
        """
        Gets the pubSubConnectionId property value. The pubSubConnectionId property
        Returns: Optional[str]
        """
        return self._pub_sub_connection_id
    
    @pub_sub_connection_id.setter
    def pub_sub_connection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the pubSubConnectionId property value. The pubSubConnectionId property
        Args:
            value: Value to set for the pubSubConnectionId property.
        """
        self._pub_sub_connection_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("pubSubConnectionId", self.pub_sub_connection_id)
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
    

