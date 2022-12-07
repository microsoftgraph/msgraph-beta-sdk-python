from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SignDigestPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the signDigest method.
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
        Instantiates a new signDigestPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The digest property
        self._digest: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignDigestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignDigestPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignDigestPostRequestBody()
    
    @property
    def digest(self,) -> Optional[bytes]:
        """
        Gets the digest property value. The digest property
        Returns: Optional[bytes]
        """
        return self._digest
    
    @digest.setter
    def digest(self,value: Optional[bytes] = None) -> None:
        """
        Sets the digest property value. The digest property
        Args:
            value: Value to set for the digest property.
        """
        self._digest = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "digest": lambda n : setattr(self, 'digest', n.get_bytes_value()),
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
        writer.write_object_value("digest", self.digest)
        writer.write_additional_data_value(self.additional_data)
    

