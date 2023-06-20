from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, ios_certificate_profile_base, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile

from . import device_configuration

@dataclass
class IosCertificateProfile(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.iosCertificateProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfileBase".casefold():
            from . import ios_certificate_profile_base

            return ios_certificate_profile_base.IosCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosImportedPFXCertificateProfile".casefold():
            from . import ios_imported_p_f_x_certificate_profile

            return ios_imported_p_f_x_certificate_profile.IosImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from . import ios_pkcs_certificate_profile

            return ios_pkcs_certificate_profile.IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from . import ios_scep_certificate_profile

            return ios_scep_certificate_profile.IosScepCertificateProfile()
        return IosCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, ios_certificate_profile_base, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile

        from . import device_configuration, ios_certificate_profile_base, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile

        fields: Dict[str, Callable[[Any], None]] = {
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
    

