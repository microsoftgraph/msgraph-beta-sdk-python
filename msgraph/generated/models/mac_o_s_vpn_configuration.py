from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_vpn_configuration, mac_o_s_certificate_profile_base

from . import apple_vpn_configuration

@dataclass
class MacOSVpnConfiguration(apple_vpn_configuration.AppleVpnConfiguration):
    odata_type = "#microsoft.graph.macOSVpnConfiguration"
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSVpnConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_vpn_configuration, mac_o_s_certificate_profile_base

        from . import apple_vpn_configuration, mac_o_s_certificate_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase)),
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
        writer.write_object_value("identityCertificate", self.identity_certificate)
    

