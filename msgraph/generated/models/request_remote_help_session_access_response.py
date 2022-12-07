from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RequestRemoteHelpSessionAccessResponse(AdditionalDataHolder, Parsable):
    """
    Remote help - response we provide back to the helper after getting response from pubSub
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
        Instantiates a new requestRemoteHelpSessionAccessResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # AES encryption Initialization Vector for encrypting client messages sent to PubSub
        self._pub_sub_encryption: Optional[str] = None
        # The unique identifier for encrypting client messages sent to PubSub
        self._pub_sub_encryption_key: Optional[str] = None
        # The unique identifier for a session
        self._session_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestRemoteHelpSessionAccessResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestRemoteHelpSessionAccessResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestRemoteHelpSessionAccessResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pub_sub_encryption": lambda n : setattr(self, 'pub_sub_encryption', n.get_str_value()),
            "pub_sub_encryption_key": lambda n : setattr(self, 'pub_sub_encryption_key', n.get_str_value()),
            "session_key": lambda n : setattr(self, 'session_key', n.get_str_value()),
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
    def pub_sub_encryption(self,) -> Optional[str]:
        """
        Gets the pubSubEncryption property value. AES encryption Initialization Vector for encrypting client messages sent to PubSub
        Returns: Optional[str]
        """
        return self._pub_sub_encryption
    
    @pub_sub_encryption.setter
    def pub_sub_encryption(self,value: Optional[str] = None) -> None:
        """
        Sets the pubSubEncryption property value. AES encryption Initialization Vector for encrypting client messages sent to PubSub
        Args:
            value: Value to set for the pubSubEncryption property.
        """
        self._pub_sub_encryption = value
    
    @property
    def pub_sub_encryption_key(self,) -> Optional[str]:
        """
        Gets the pubSubEncryptionKey property value. The unique identifier for encrypting client messages sent to PubSub
        Returns: Optional[str]
        """
        return self._pub_sub_encryption_key
    
    @pub_sub_encryption_key.setter
    def pub_sub_encryption_key(self,value: Optional[str] = None) -> None:
        """
        Sets the pubSubEncryptionKey property value. The unique identifier for encrypting client messages sent to PubSub
        Args:
            value: Value to set for the pubSubEncryptionKey property.
        """
        self._pub_sub_encryption_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("pubSubEncryption", self.pub_sub_encryption)
        writer.write_str_value("pubSubEncryptionKey", self.pub_sub_encryption_key)
        writer.write_str_value("sessionKey", self.session_key)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_key(self,) -> Optional[str]:
        """
        Gets the sessionKey property value. The unique identifier for a session
        Returns: Optional[str]
        """
        return self._session_key
    
    @session_key.setter
    def session_key(self,value: Optional[str] = None) -> None:
        """
        Sets the sessionKey property value. The unique identifier for a session
        Args:
            value: Value to set for the sessionKey property.
        """
        self._session_key = value
    

