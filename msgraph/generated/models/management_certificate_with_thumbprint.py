from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ManagementCertificateWithThumbprint(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new managementCertificateWithThumbprint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Base 64 encoded management certificate
        self._certificate: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The thumbprint of the management certificate
        self._thumbprint: Optional[str] = None
    
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
    def certificate(self,) -> Optional[str]:
        """
        Gets the certificate property value. The Base 64 encoded management certificate
        Returns: Optional[str]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the certificate property value. The Base 64 encoded management certificate
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementCertificateWithThumbprint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementCertificateWithThumbprint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementCertificateWithThumbprint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
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
        writer.write_str_value("certificate", self.certificate)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def thumbprint(self,) -> Optional[str]:
        """
        Gets the thumbprint property value. The thumbprint of the management certificate
        Returns: Optional[str]
        """
        return self._thumbprint
    
    @thumbprint.setter
    def thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbprint property value. The thumbprint of the management certificate
        Args:
            value: Value to set for the thumbprint property.
        """
        self._thumbprint = value
    

