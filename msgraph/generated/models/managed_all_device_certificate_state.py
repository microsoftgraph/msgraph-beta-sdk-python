from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_revocation_status = lazy_import('msgraph.generated.models.certificate_revocation_status')
entity = lazy_import('msgraph.generated.models.entity')

class ManagedAllDeviceCertificateState(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
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
            value: Value to set for the certificateExpirationDateTime property.
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
            value: Value to set for the certificateExtendedKeyUsages property.
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
            value: Value to set for the certificateIssuanceDateTime property.
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
            value: Value to set for the certificateIssuerName property.
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
            value: Value to set for the certificateKeyUsages property.
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
            value: Value to set for the certificateRevokeStatus property.
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
            value: Value to set for the certificateRevokeStatusLastChangeDateTime property.
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
            value: Value to set for the certificateSerialNumber property.
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
            value: Value to set for the certificateSubjectName property.
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
            value: Value to set for the certificateThumbprint property.
        """
        self._certificate_thumbprint = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedAllDeviceCertificateState and sets the default values.
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
        fields = {
            "certificate_expiration_date_time": lambda n : setattr(self, 'certificate_expiration_date_time', n.get_datetime_value()),
            "certificate_extended_key_usages": lambda n : setattr(self, 'certificate_extended_key_usages', n.get_str_value()),
            "certificate_issuance_date_time": lambda n : setattr(self, 'certificate_issuance_date_time', n.get_datetime_value()),
            "certificate_issuer_name": lambda n : setattr(self, 'certificate_issuer_name', n.get_str_value()),
            "certificate_key_usages": lambda n : setattr(self, 'certificate_key_usages', n.get_int_value()),
            "certificate_revoke_status": lambda n : setattr(self, 'certificate_revoke_status', n.get_enum_value(certificate_revocation_status.CertificateRevocationStatus)),
            "certificate_revoke_status_last_change_date_time": lambda n : setattr(self, 'certificate_revoke_status_last_change_date_time', n.get_datetime_value()),
            "certificate_serial_number": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificate_subject_name": lambda n : setattr(self, 'certificate_subject_name', n.get_str_value()),
            "certificate_thumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "managed_device_display_name": lambda n : setattr(self, 'managed_device_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
            value: Value to set for the managedDeviceDisplayName property.
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
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

