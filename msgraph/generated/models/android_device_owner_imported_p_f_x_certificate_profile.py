from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_certificate_access_type, android_device_owner_certificate_profile_base, android_device_owner_silent_certificate_access, intended_purpose, managed_device_certificate_state

from . import android_device_owner_certificate_profile_base

class AndroidDeviceOwnerImportedPFXCertificateProfile(android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerImportedPFXCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile"
        # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        self._certificate_access_type: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None
        # PFX Import Options.
        self._intended_purpose: Optional[intended_purpose.IntendedPurpose] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerImportedPFXCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def intended_purpose(self,) -> Optional[intended_purpose.IntendedPurpose]:
        """
        Gets the intendedPurpose property value. PFX Import Options.
        Returns: Optional[intended_purpose.IntendedPurpose]
        """
        return self._intended_purpose
    
    @intended_purpose.setter
    def intended_purpose(self,value: Optional[intended_purpose.IntendedPurpose] = None) -> None:
        """
        Sets the intendedPurpose property value. PFX Import Options.
        Args:
            value: Value to set for the intended_purpose property.
        """
        self._intended_purpose = value
    
    @property
    def managed_device_certificate_states(self,) -> Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]]:
        """
        Gets the managedDeviceCertificateStates property value. Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        Returns: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]]
        """
        return self._managed_device_certificate_states
    
    @managed_device_certificate_states.setter
    def managed_device_certificate_states(self,value: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None) -> None:
        """
        Sets the managedDeviceCertificateStates property value. Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        Args:
            value: Value to set for the managed_device_certificate_states property.
        """
        self._managed_device_certificate_states = value
    
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
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
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
    

