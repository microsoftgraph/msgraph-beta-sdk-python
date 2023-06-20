from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_certificate_access_type, android_device_owner_certificate_profile_base, android_device_owner_silent_certificate_access, intended_purpose, managed_device_certificate_state

from . import android_device_owner_certificate_profile_base

@dataclass
class AndroidDeviceOwnerImportedPFXCertificateProfile(android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase):
    odata_type = "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile"
    # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
    certificate_access_type: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None
    # PFX Import Options.
    intended_purpose: Optional[intended_purpose.IntendedPurpose] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
    # Certificate access information. This collection can contain a maximum of 50 elements.
    silent_certificate_access_details: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerImportedPFXCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_certificate_access_type, android_device_owner_certificate_profile_base, android_device_owner_silent_certificate_access, intended_purpose, managed_device_certificate_state

        from . import android_device_owner_certificate_access_type, android_device_owner_certificate_profile_base, android_device_owner_silent_certificate_access, intended_purpose, managed_device_certificate_state

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateAccessType": lambda n : setattr(self, 'certificate_access_type', n.get_enum_value(android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType)),
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(intended_purpose.IntendedPurpose)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateAccessType", self.certificate_access_type)
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_collection_of_object_values("silentCertificateAccessDetails", self.silent_certificate_access_details)
    

