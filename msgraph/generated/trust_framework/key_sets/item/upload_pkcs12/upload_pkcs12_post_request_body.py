from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UploadPkcs12PostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new uploadPkcs12PostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The key property
        self._key: Optional[str] = None
        # The password property
        self._password: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UploadPkcs12PostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UploadPkcs12PostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UploadPkcs12PostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
        }
        return fields
    
    @property
    def key(self,) -> Optional[str]:
        """
        Gets the key property value. The key property
        Returns: Optional[str]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[str] = None) -> None:
        """
        Sets the key property value. The key property
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password property
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password property
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("key", self.key)
        writer.write_str_value("password", self.password)
        writer.write_additional_data_value(self.additional_data)
    

