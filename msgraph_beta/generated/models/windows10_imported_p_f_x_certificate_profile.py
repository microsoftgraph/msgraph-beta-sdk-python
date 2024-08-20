from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .intended_purpose import IntendedPurpose
    from .managed_device_certificate_state import ManagedDeviceCertificateState
    from .windows_certificate_profile_base import WindowsCertificateProfileBase

from .windows_certificate_profile_base import WindowsCertificateProfileBase

@dataclass
class Windows10ImportedPFXCertificateProfile(WindowsCertificateProfileBase):
    """
    Windows 10 Desktop and Mobile PFX Import certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10ImportedPFXCertificateProfile"
    # PFX Import Options.
    intended_purpose: Optional[IntendedPurpose] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[ManagedDeviceCertificateState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10ImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10ImportedPFXCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10ImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        fields: Dict[str, Callable[[Any], None]] = {
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(IntendedPurpose)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
    

