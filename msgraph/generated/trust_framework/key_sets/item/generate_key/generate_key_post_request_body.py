from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class GenerateKeyPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new generateKeyPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The exp property
        self._exp: Optional[int] = None
        # The kty property
        self._kty: Optional[str] = None
        # The nbf property
        self._nbf: Optional[int] = None
        # The use property
        self._use: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GenerateKeyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GenerateKeyPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GenerateKeyPostRequestBody()
    
    @property
    def exp(self,) -> Optional[int]:
        """
        Gets the exp property value. The exp property
        Returns: Optional[int]
        """
        return self._exp
    
    @exp.setter
    def exp(self,value: Optional[int] = None) -> None:
        """
        Sets the exp property value. The exp property
        Args:
            value: Value to set for the exp property.
        """
        self._exp = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "exp": lambda n : setattr(self, 'exp', n.get_int_value()),
            "kty": lambda n : setattr(self, 'kty', n.get_str_value()),
            "nbf": lambda n : setattr(self, 'nbf', n.get_int_value()),
            "use": lambda n : setattr(self, 'use', n.get_str_value()),
        }
        return fields
    
    @property
    def kty(self,) -> Optional[str]:
        """
        Gets the kty property value. The kty property
        Returns: Optional[str]
        """
        return self._kty
    
    @kty.setter
    def kty(self,value: Optional[str] = None) -> None:
        """
        Sets the kty property value. The kty property
        Args:
            value: Value to set for the kty property.
        """
        self._kty = value
    
    @property
    def nbf(self,) -> Optional[int]:
        """
        Gets the nbf property value. The nbf property
        Returns: Optional[int]
        """
        return self._nbf
    
    @nbf.setter
    def nbf(self,value: Optional[int] = None) -> None:
        """
        Sets the nbf property value. The nbf property
        Args:
            value: Value to set for the nbf property.
        """
        self._nbf = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("exp", self.exp)
        writer.write_str_value("kty", self.kty)
        writer.write_int_value("nbf", self.nbf)
        writer.write_str_value("use", self.use)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def use(self,) -> Optional[str]:
        """
        Gets the use property value. The use property
        Returns: Optional[str]
        """
        return self._use
    
    @use.setter
    def use(self,value: Optional[str] = None) -> None:
        """
        Sets the use property value. The use property
        Args:
            value: Value to set for the use property.
        """
        self._use = value
    

