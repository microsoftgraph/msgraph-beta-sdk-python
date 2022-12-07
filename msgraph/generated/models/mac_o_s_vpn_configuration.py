from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_vpn_configuration = lazy_import('msgraph.generated.models.apple_vpn_configuration')
mac_o_s_certificate_profile_base = lazy_import('msgraph.generated.models.mac_o_s_certificate_profile_base')

class MacOSVpnConfiguration(apple_vpn_configuration.AppleVpnConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSVpnConfiguration"
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSVpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("identityCertificate", self.identity_certificate)
    

