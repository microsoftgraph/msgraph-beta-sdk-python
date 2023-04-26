from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_revocation_status, entity

from . import entity

class ManagedAllDeviceCertificateState(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAllDeviceCertificateState and sets the default values.
        """
        super().__init__()
        # Certificate expiry date
        self._certificate_expiration_date_time: Optional[datetime] = None
        # Enhanced Key Usage
        self._certificate_extended_key_usages: Optional[str] = None
        # Issuance date
        self._certificate_issuance_date_time: Optional[datetime] = None
        # Issuer
        self._certificate_issuer_name: Optional[str] = None
        # Key Usage
        self._certificate_key_usages: Optional[int] = None
        # Certificate Revocation Status.
        self._certificate_revoke_status: Optional[certificate_revocation_status.CertificateRevocationStatus] = None
        # The time the revoke status was last changed
        self._certificate_revoke_status_last_change_date_time: Optional[datetime] = None
        # Serial number
        self._certificate_serial_number: Optional[str] = None
        # Certificate subject name
        self._certificate_subject_name: Optional[str] = None
        # Thumbprint
        self._certificate_thumbprint: Optional[str] = None
        # Device display name
        self._managed_device_display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User principal name
        self._user_principal_name: Optional[str] = None
    
    @property
    def certificate_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateExpirationDateTime property value. Certificate expiry date
        Returns: Optional[datetime]
        """
        return self._certificate_expiration_date_time
    
    @certificate_expiration_date_time.setter
    def certificate_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateExpirationDateTime property value. Certificate expiry date
        Args:
            value: Value to set for the certificate_expiration_date_time property.
        """
        self._certificate_expiration_date_time = value
    
    @property
    def certificate_extended_key_usages(self,) -> Optional[str]:
        """
        Gets the certificateExtendedKeyUsages property value. Enhanced Key Usage
        Returns: Optional[str]
        """
        return self._certificate_extended_key_usages
    
    @certificate_extended_key_usages.setter
    def certificate_extended_key_usages(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateExtendedKeyUsages property value. Enhanced Key Usage
        Args:
            value: Value to set for the certificate_extended_key_usages property.
        """
        self._certificate_extended_key_usages = value
    
    @property
    def certificate_issuance_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateIssuanceDateTime property value. Issuance date
        Returns: Optional[datetime]
        """
        return self._certificate_issuance_date_time
    
    @certificate_issuance_date_time.setter
    def certificate_issuance_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateIssuanceDateTime property value. Issuance date
        Args:
            value: Value to set for the certificate_issuance_date_time property.
        """
        self._certificate_issuance_date_time = value
    
    @property
    def certificate_issuer_name(self,) -> Optional[str]:
        """
        Gets the certificateIssuerName property value. Issuer
        Returns: Optional[str]
        """
        return self._certificate_issuer_name
    
    @certificate_issuer_name.setter
    def certificate_issuer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateIssuerName property value. Issuer
        Args:
            value: Value to set for the certificate_issuer_name property.
        """
        self._certificate_issuer_name = value
    
    @property
    def certificate_key_usages(self,) -> Optional[int]:
        """
        Gets the certificateKeyUsages property value. Key Usage
        Returns: Optional[int]
        """
        return self._certificate_key_usages
    
    @certificate_key_usages.setter
    def certificate_key_usages(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateKeyUsages property value. Key Usage
        Args:
            value: Value to set for the certificate_key_usages property.
        """
        self._certificate_key_usages = value
    
    @property
    def certificate_revoke_status(self,) -> Optional[certificate_revocation_status.CertificateRevocationStatus]:
        """
        Gets the certificateRevokeStatus property value. Certificate Revocation Status.
        Returns: Optional[certificate_revocation_status.CertificateRevocationStatus]
        """
        return self._certificate_revoke_status
    
    @certificate_revoke_status.setter
    def certificate_revoke_status(self,value: Optional[certificate_revocation_status.CertificateRevocationStatus] = None) -> None:
        """
        Sets the certificateRevokeStatus property value. Certificate Revocation Status.
        Args:
            value: Value to set for the certificate_revoke_status property.
        """
        self._certificate_revoke_status = value
    
    @property
    def certificate_revoke_status_last_change_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateRevokeStatusLastChangeDateTime property value. The time the revoke status was last changed
        Returns: Optional[datetime]
        """
        return self._certificate_revoke_status_last_change_date_time
    
    @certificate_revoke_status_last_change_date_time.setter
    def certificate_revoke_status_last_change_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateRevokeStatusLastChangeDateTime property value. The time the revoke status was last changed
        Args:
            value: Value to set for the certificate_revoke_status_last_change_date_time property.
        """
        self._certificate_revoke_status_last_change_date_time = value
    
    @property
    def certificate_serial_number(self,) -> Optional[str]:
        """
        Gets the certificateSerialNumber property value. Serial number
        Returns: Optional[str]
        """
        return self._certificate_serial_number
    
    @certificate_serial_number.setter
    def certificate_serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSerialNumber property value. Serial number
        Args:
            value: Value to set for the certificate_serial_number property.
        """
        self._certificate_serial_number = value
    
    @property
    def certificate_subject_name(self,) -> Optional[str]:
        """
        Gets the certificateSubjectName property value. Certificate subject name
        Returns: Optional[str]
        """
        return self._certificate_subject_name
    
    @certificate_subject_name.setter
    def certificate_subject_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSubjectName property value. Certificate subject name
        Args:
            value: Value to set for the certificate_subject_name property.
        """
        self._certificate_subject_name = value
    
    @property
    def certificate_thumbprint(self,) -> Optional[str]:
        """
        Gets the certificateThumbprint property value. Thumbprint
        Returns: Optional[str]
        """
        return self._certificate_thumbprint
    
    @certificate_thumbprint.setter
    def certificate_thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateThumbprint property value. Thumbprint
        Args:
            value: Value to set for the certificate_thumbprint property.
        """
        self._certificate_thumbprint = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAllDeviceCertificateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAllDeviceCertificateState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAllDeviceCertificateState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_revocation_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateExpirationDateTime": lambda n : setattr(self, 'certificate_expiration_date_time', n.get_datetime_value()),
            "certificateExtendedKeyUsages": lambda n : setattr(self, 'certificate_extended_key_usages', n.get_str_value()),
            "certificateIssuanceDateTime": lambda n : setattr(self, 'certificate_issuance_date_time', n.get_datetime_value()),
            "certificateIssuerName": lambda n : setattr(self, 'certificate_issuer_name', n.get_str_value()),
            "certificateKeyUsages": lambda n : setattr(self, 'certificate_key_usages', n.get_int_value()),
            "certificateRevokeStatus": lambda n : setattr(self, 'certificate_revoke_status', n.get_enum_value(certificate_revocation_status.CertificateRevocationStatus)),
            "certificateRevokeStatusLastChangeDateTime": lambda n : setattr(self, 'certificate_revoke_status_last_change_date_time', n.get_datetime_value()),
            "certificateSerialNumber": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificateSubjectName": lambda n : setattr(self, 'certificate_subject_name', n.get_str_value()),
            "certificateThumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "managedDeviceDisplayName": lambda n : setattr(self, 'managed_device_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_display_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceDisplayName property value. Device display name
        Returns: Optional[str]
        """
        return self._managed_device_display_name
    
    @managed_device_display_name.setter
    def managed_device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceDisplayName property value. Device display name
        Args:
            value: Value to set for the managed_device_display_name property.
        """
        self._managed_device_display_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("certificateExpirationDateTime", self.certificate_expiration_date_time)
        writer.write_str_value("certificateExtendedKeyUsages", self.certificate_extended_key_usages)
        writer.write_datetime_value("certificateIssuanceDateTime", self.certificate_issuance_date_time)
        writer.write_str_value("certificateIssuerName", self.certificate_issuer_name)
        writer.write_int_value("certificateKeyUsages", self.certificate_key_usages)
        writer.write_enum_value("certificateRevokeStatus", self.certificate_revoke_status)
        writer.write_datetime_value("certificateRevokeStatusLastChangeDateTime", self.certificate_revoke_status_last_change_date_time)
        writer.write_str_value("certificateSerialNumber", self.certificate_serial_number)
        writer.write_str_value("certificateSubjectName", self.certificate_subject_name)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_str_value("managedDeviceDisplayName", self.managed_device_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

