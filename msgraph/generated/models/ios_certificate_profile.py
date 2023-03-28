from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, ios_certificate_profile_base, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile

from . import device_configuration

class IosCertificateProfile(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new iosCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosCertificateProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosCertificateProfileBase":
                from . import ios_certificate_profile_base

                return ios_certificate_profile_base.IosCertificateProfileBase()
            if mapping_value == "#microsoft.graph.iosImportedPFXCertificateProfile":
                from . import ios_imported_p_f_x_certificate_profile

                return ios_imported_p_f_x_certificate_profile.IosImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.iosPkcsCertificateProfile":
                from . import ios_pkcs_certificate_profile

                return ios_pkcs_certificate_profile.IosPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.iosScepCertificateProfile":
                from . import ios_scep_certificate_profile

                return ios_scep_certificate_profile.IosScepCertificateProfile()
        return IosCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

