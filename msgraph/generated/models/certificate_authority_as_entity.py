from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class CertificateAuthorityAsEntity(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new certificateAuthorityAsEntity and sets the default values.
        """
        super().__init__()
        # The certificate property
        self._certificate: Optional[bytes] = None
        # The isRootAuthority property
        self._is_root_authority: Optional[bool] = None
        # The issuer property
        self._issuer: Optional[str] = None
        # The issuerSubjectKeyIdentifier property
        self._issuer_subject_key_identifier: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def certificate(self,) -> Optional[bytes]:
        """
        Gets the certificate property value. The certificate property
        Returns: Optional[bytes]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the certificate property value. The certificate property
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateAuthorityAsEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthorityAsEntity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CertificateAuthorityAsEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerSubjectKeyIdentifier": lambda n : setattr(self, 'issuer_subject_key_identifier', n.get_str_value()),
            "isRootAuthority": lambda n : setattr(self, 'is_root_authority', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_root_authority(self,) -> Optional[bool]:
        """
        Gets the isRootAuthority property value. The isRootAuthority property
        Returns: Optional[bool]
        """
        return self._is_root_authority
    
    @is_root_authority.setter
    def is_root_authority(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRootAuthority property value. The isRootAuthority property
        Args:
            value: Value to set for the is_root_authority property.
        """
        self._is_root_authority = value
    
    @property
    def issuer(self,) -> Optional[str]:
        """
        Gets the issuer property value. The issuer property
        Returns: Optional[str]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the issuer property value. The issuer property
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
    @property
    def issuer_subject_key_identifier(self,) -> Optional[str]:
        """
        Gets the issuerSubjectKeyIdentifier property value. The issuerSubjectKeyIdentifier property
        Returns: Optional[str]
        """
        return self._issuer_subject_key_identifier
    
    @issuer_subject_key_identifier.setter
    def issuer_subject_key_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the issuerSubjectKeyIdentifier property value. The issuerSubjectKeyIdentifier property
        Args:
            value: Value to set for the issuer_subject_key_identifier property.
        """
        self._issuer_subject_key_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("certificate", self.certificate)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerSubjectKeyIdentifier", self.issuer_subject_key_identifier)
        writer.write_bool_value("isRootAuthority", self.is_root_authority)
    

