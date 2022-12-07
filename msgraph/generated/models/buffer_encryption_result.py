from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BufferEncryptionResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new bufferEncryptionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The encryptedBuffer property
        self._encrypted_buffer: Optional[bytes] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The publishingLicense property
        self._publishing_license: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BufferEncryptionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BufferEncryptionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BufferEncryptionResult()
    
    @property
    def encrypted_buffer(self,) -> Optional[bytes]:
        """
        Gets the encryptedBuffer property value. The encryptedBuffer property
        Returns: Optional[bytes]
        """
        return self._encrypted_buffer
    
    @encrypted_buffer.setter
    def encrypted_buffer(self,value: Optional[bytes] = None) -> None:
        """
        Sets the encryptedBuffer property value. The encryptedBuffer property
        Args:
            value: Value to set for the encryptedBuffer property.
        """
        self._encrypted_buffer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "encrypted_buffer": lambda n : setattr(self, 'encrypted_buffer', n.get_bytes_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publishing_license": lambda n : setattr(self, 'publishing_license', n.get_bytes_value()),
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
    def publishing_license(self,) -> Optional[bytes]:
        """
        Gets the publishingLicense property value. The publishingLicense property
        Returns: Optional[bytes]
        """
        return self._publishing_license
    
    @publishing_license.setter
    def publishing_license(self,value: Optional[bytes] = None) -> None:
        """
        Sets the publishingLicense property value. The publishingLicense property
        Args:
            value: Value to set for the publishingLicense property.
        """
        self._publishing_license = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("encryptedBuffer", self.encrypted_buffer)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("publishingLicense", self.publishing_license)
        writer.write_additional_data_value(self.additional_data)
    

