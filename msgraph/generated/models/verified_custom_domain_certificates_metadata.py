from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VerifiedCustomDomainCertificatesMetadata(AdditionalDataHolder, Parsable):
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
        Instantiates a new verifiedCustomDomainCertificatesMetadata and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expiry date of the custom domain certificate. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._expiry_date: Optional[datetime] = None
        # The issue date of the custom domain. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._issue_date: Optional[datetime] = None
        # The issuer name of the custom domain certificate.
        self._issuer_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The subject name of the custom domain certificate.
        self._subject_name: Optional[str] = None
        # The thumbprint associated with the custom domain certificate.
        self._thumbprint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiedCustomDomainCertificatesMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedCustomDomainCertificatesMetadata
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiedCustomDomainCertificatesMetadata()
    
    @property
    def expiry_date(self,) -> Optional[datetime]:
        """
        Gets the expiryDate property value. The expiry date of the custom domain certificate. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._expiry_date
    
    @expiry_date.setter
    def expiry_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiryDate property value. The expiry date of the custom domain certificate. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the expiryDate property.
        """
        self._expiry_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiry_date": lambda n : setattr(self, 'expiry_date', n.get_datetime_value()),
            "issue_date": lambda n : setattr(self, 'issue_date', n.get_datetime_value()),
            "issuer_name": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subject_name": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
        }
        return fields
    
    @property
    def issue_date(self,) -> Optional[datetime]:
        """
        Gets the issueDate property value. The issue date of the custom domain. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._issue_date
    
    @issue_date.setter
    def issue_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the issueDate property value. The issue date of the custom domain. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the issueDate property.
        """
        self._issue_date = value
    
    @property
    def issuer_name(self,) -> Optional[str]:
        """
        Gets the issuerName property value. The issuer name of the custom domain certificate.
        Returns: Optional[str]
        """
        return self._issuer_name
    
    @issuer_name.setter
    def issuer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the issuerName property value. The issuer name of the custom domain certificate.
        Args:
            value: Value to set for the issuerName property.
        """
        self._issuer_name = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("expiryDate", self.expiry_date)
        writer.write_datetime_value("issueDate", self.issue_date)
        writer.write_str_value("issuerName", self.issuer_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subject_name(self,) -> Optional[str]:
        """
        Gets the subjectName property value. The subject name of the custom domain certificate.
        Returns: Optional[str]
        """
        return self._subject_name
    
    @subject_name.setter
    def subject_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectName property value. The subject name of the custom domain certificate.
        Args:
            value: Value to set for the subjectName property.
        """
        self._subject_name = value
    
    @property
    def thumbprint(self,) -> Optional[str]:
        """
        Gets the thumbprint property value. The thumbprint associated with the custom domain certificate.
        Returns: Optional[str]
        """
        return self._thumbprint
    
    @thumbprint.setter
    def thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbprint property value. The thumbprint associated with the custom domain certificate.
        Args:
            value: Value to set for the thumbprint property.
        """
        self._thumbprint = value
    

