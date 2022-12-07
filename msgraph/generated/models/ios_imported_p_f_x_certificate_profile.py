from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

intended_purpose = lazy_import('msgraph.generated.models.intended_purpose')
ios_certificate_profile = lazy_import('msgraph.generated.models.ios_certificate_profile')
managed_device_certificate_state = lazy_import('msgraph.generated.models.managed_device_certificate_state')

class IosImportedPFXCertificateProfile(ios_certificate_profile.IosCertificateProfile):
    def __init__(self,) -> None:
        """
        Instantiates a new IosImportedPFXCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosImportedPFXCertificateProfile"
        # PFX Import Options.
        self._intended_purpose: Optional[intended_purpose.IntendedPurpose] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosImportedPFXCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "intended_purpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(intended_purpose.IntendedPurpose)),
            "managed_device_certificate_states": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
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
            value: Value to set for the intendedPurpose property.
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
            value: Value to set for the managedDeviceCertificateStates property.
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
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
    

