from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_status = lazy_import('msgraph.generated.models.certificate_status')
entity = lazy_import('msgraph.generated.models.entity')

class SymantecCodeSigningCertificate(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new symantecCodeSigningCertificate and sets the default values.
        """
        super().__init__()
        # The Windows Symantec Code-Signing Certificate in the raw data format.
        self._content: Optional[bytes] = None
        # The Cert Expiration Date.
        self._expiration_date_time: Optional[datetime] = None
        # The Issuer value for the cert.
        self._issuer: Optional[str] = None
        # The Issuer Name for the cert.
        self._issuer_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Password required for .pfx file.
        self._password: Optional[str] = None
        # The status property
        self._status: Optional[certificate_status.CertificateStatus] = None
        # The Subject value for the cert.
        self._subject: Optional[str] = None
        # The Subject Name for the cert.
        self._subject_name: Optional[str] = None
        # The Type of the CodeSigning Cert as Symantec Cert.
        self._upload_date_time: Optional[datetime] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The Windows Symantec Code-Signing Certificate in the raw data format.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The Windows Symantec Code-Signing Certificate in the raw data format.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SymantecCodeSigningCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SymantecCodeSigningCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SymantecCodeSigningCertificate()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The Cert Expiration Date.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The Cert Expiration Date.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuer_name": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(certificate_status.CertificateStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "subject_name": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "upload_date_time": lambda n : setattr(self, 'upload_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issuer(self,) -> Optional[str]:
        """
        Gets the issuer property value. The Issuer value for the cert.
        Returns: Optional[str]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the issuer property value. The Issuer value for the cert.
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
    @property
    def issuer_name(self,) -> Optional[str]:
        """
        Gets the issuerName property value. The Issuer Name for the cert.
        Returns: Optional[str]
        """
        return self._issuer_name
    
    @issuer_name.setter
    def issuer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the issuerName property value. The Issuer Name for the cert.
        Args:
            value: Value to set for the issuerName property.
        """
        self._issuer_name = value
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The Password required for .pfx file.
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The Password required for .pfx file.
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
        super().serialize(writer)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerName", self.issuer_name)
        writer.write_str_value("password", self.password)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_datetime_value("uploadDateTime", self.upload_date_time)
    
    @property
    def status(self,) -> Optional[certificate_status.CertificateStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[certificate_status.CertificateStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[certificate_status.CertificateStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The Subject value for the cert.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The Subject value for the cert.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def subject_name(self,) -> Optional[str]:
        """
        Gets the subjectName property value. The Subject Name for the cert.
        Returns: Optional[str]
        """
        return self._subject_name
    
    @subject_name.setter
    def subject_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectName property value. The Subject Name for the cert.
        Args:
            value: Value to set for the subjectName property.
        """
        self._subject_name = value
    
    @property
    def upload_date_time(self,) -> Optional[datetime]:
        """
        Gets the uploadDateTime property value. The Type of the CodeSigning Cert as Symantec Cert.
        Returns: Optional[datetime]
        """
        return self._upload_date_time
    
    @upload_date_time.setter
    def upload_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the uploadDateTime property value. The Type of the CodeSigning Cert as Symantec Cert.
        Args:
            value: Value to set for the uploadDateTime property.
        """
        self._upload_date_time = value
    

