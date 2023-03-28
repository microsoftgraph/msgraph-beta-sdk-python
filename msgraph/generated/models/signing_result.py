from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SigningResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new signingResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The signature property
        self._signature: Optional[bytes] = None
        # The signingKeyId property
        self._signing_key_id: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SigningResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SigningResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SigningResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signature": lambda n : setattr(self, 'signature', n.get_bytes_value()),
            "signingKeyId": lambda n : setattr(self, 'signing_key_id', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("signature", self.signature)
        writer.write_str_value("signingKeyId", self.signing_key_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def signature(self,) -> Optional[bytes]:
        """
        Gets the signature property value. The signature property
        Returns: Optional[bytes]
        """
        return self._signature
    
    @signature.setter
    def signature(self,value: Optional[bytes] = None) -> None:
        """
        Sets the signature property value. The signature property
        Args:
            value: Value to set for the signature property.
        """
        self._signature = value
    
    @property
    def signing_key_id(self,) -> Optional[str]:
        """
        Gets the signingKeyId property value. The signingKeyId property
        Returns: Optional[str]
        """
        return self._signing_key_id
    
    @signing_key_id.setter
    def signing_key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the signingKeyId property value. The signingKeyId property
        Args:
            value: Value to set for the signing_key_id property.
        """
        self._signing_key_id = value
    

