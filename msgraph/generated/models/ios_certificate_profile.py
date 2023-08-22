from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .ios_certificate_profile_base import IosCertificateProfileBase
    from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
    from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
    from .ios_scep_certificate_profile import IosScepCertificateProfile

from .device_configuration import DeviceConfiguration

@dataclass
class IosCertificateProfile(DeviceConfiguration):
    """
    Device Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosCertificateProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfileBase".casefold():
            from .ios_certificate_profile_base import IosCertificateProfileBase

            return IosCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosImportedPFXCertificateProfile".casefold():
            from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile

            return IosImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile

            return IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from .ios_scep_certificate_profile import IosScepCertificateProfile

            return IosScepCertificateProfile()
        return IosCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile

        from .device_configuration import DeviceConfiguration
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

