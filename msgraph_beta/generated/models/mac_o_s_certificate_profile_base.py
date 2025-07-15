from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
    from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
    from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSCertificateProfileBase(DeviceConfiguration, Parsable):
    """
    Mac OS certificate profile.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCertificateProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSImportedPFXCertificateProfile".casefold():
            from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile

            return MacOSImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkcsCertificateProfile".casefold():
            from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile

            return MacOSPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSScepCertificateProfile".casefold():
            from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

            return MacOSScepCertificateProfile()
        return MacOSCertificateProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

        from .device_configuration import DeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

        fields: dict[str, Callable[[Any], None]] = {
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
    

