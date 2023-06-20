from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import intended_purpose, managed_device_certificate_state, windows_certificate_profile_base

from . import windows_certificate_profile_base

@dataclass
class Windows10ImportedPFXCertificateProfile(windows_certificate_profile_base.WindowsCertificateProfileBase):
    odata_type = "#microsoft.graph.windows10ImportedPFXCertificateProfile"
    # PFX Import Options.
    intended_purpose: Optional[intended_purpose.IntendedPurpose] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10ImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10ImportedPFXCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10ImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import intended_purpose, managed_device_certificate_state, windows_certificate_profile_base

        from . import intended_purpose, managed_device_certificate_state, windows_certificate_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(intended_purpose.IntendedPurpose)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
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
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
    

