from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_status, entity

from . import entity

@dataclass
class SymantecCodeSigningCertificate(entity.Entity):
    # The Windows Symantec Code-Signing Certificate in the raw data format.
    content: Optional[bytes] = None
    # The Cert Expiration Date.
    expiration_date_time: Optional[datetime] = None
    # The Issuer value for the cert.
    issuer: Optional[str] = None
    # The Issuer Name for the cert.
    issuer_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Password required for .pfx file.
    password: Optional[str] = None
    # The status property
    status: Optional[certificate_status.CertificateStatus] = None
    # The Subject value for the cert.
    subject: Optional[str] = None
    # The Subject Name for the cert.
    subject_name: Optional[str] = None
    # The Type of the CodeSigning Cert as Symantec Cert.
    upload_date_time: Optional[datetime] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerName": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(certificate_status.CertificateStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "uploadDateTime": lambda n : setattr(self, 'upload_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

