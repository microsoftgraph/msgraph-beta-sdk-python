from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_certificate_access_type, android_device_owner_silent_certificate_access, device_configuration, device_management_derived_credential_settings

from . import device_configuration

class AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration"
        # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        self._certificate_access_type: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
        # Certificate access information. This collection can contain a maximum of 50 elements.
        self._silent_certificate_access_details: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]] = None
    
    @property
    def certificate_access_type(self,) -> Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType]:
        """
        Gets the certificateAccessType property value. Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        Returns: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType]
        """
        return self._certificate_access_type
    
    @certificate_access_type.setter
    def certificate_access_type(self,value: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None) -> None:
        """
        Sets the certificateAccessType property value. Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        Args:
            value: Value to set for the certificate_access_type property.
        """
        self._certificate_access_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
    
    @property
    def derived_credential_settings(self,) -> Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]:
        """
        Gets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Returns: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]
        """
        return self._derived_credential_settings
    
    @derived_credential_settings.setter
    def derived_credential_settings(self,value: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None) -> None:
        """
        Sets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Args:
            value: Value to set for the derived_credential_settings property.
        """
        self._derived_credential_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_certificate_access_type, android_device_owner_silent_certificate_access, device_configuration, device_management_derived_credential_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateAccessType": lambda n : setattr(self, 'certificate_access_type', n.get_enum_value(android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "silentCertificateAccessDetails": lambda n : setattr(self, 'silent_certificate_access_details', n.get_collection_of_object_values(android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess)),
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
        writer.write_enum_value("certificateAccessType", self.certificate_access_type)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_collection_of_object_values("silentCertificateAccessDetails", self.silent_certificate_access_details)
    
    @property
    def silent_certificate_access_details(self,) -> Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]]:
        """
        Gets the silentCertificateAccessDetails property value. Certificate access information. This collection can contain a maximum of 50 elements.
        Returns: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]]
        """
        return self._silent_certificate_access_details
    
    @silent_certificate_access_details.setter
    def silent_certificate_access_details(self,value: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]] = None) -> None:
        """
        Sets the silentCertificateAccessDetails property value. Certificate access information. This collection can contain a maximum of 50 elements.
        Args:
            value: Value to set for the silent_certificate_access_details property.
        """
        self._silent_certificate_access_details = value
    

