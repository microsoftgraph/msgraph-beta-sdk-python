from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import vpn_authentication_method, windows81_vpn_configuration, windows_phone81_certificate_profile_base

from . import windows81_vpn_configuration

@dataclass
class WindowsPhone81VpnConfiguration(windows81_vpn_configuration.Windows81VpnConfiguration):
    odata_type = "#microsoft.graph.windowsPhone81VpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
    # Bypass VPN on company Wi-Fi.
    bypass_vpn_on_company_wifi: Optional[bool] = None
    # Bypass VPN on home Wi-Fi.
    bypass_vpn_on_home_wifi: Optional[bool] = None
    # DNS suffix search list.
    dns_suffix_search_list: Optional[List[str]] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase] = None
    # Remember user credentials.
    remember_user_credentials: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81VpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81VpnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import vpn_authentication_method, windows81_vpn_configuration, windows_phone81_certificate_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "bypassVpnOnCompanyWifi": lambda n : setattr(self, 'bypass_vpn_on_company_wifi', n.get_bool_value()),
            "bypassVpnOnHomeWifi": lambda n : setattr(self, 'bypass_vpn_on_home_wifi', n.get_bool_value()),
            "dnsSuffixSearchList": lambda n : setattr(self, 'dns_suffix_search_list', n.get_collection_of_primitive_values(str)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase)),
            "rememberUserCredentials": lambda n : setattr(self, 'remember_user_credentials', n.get_bool_value()),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_bool_value("bypassVpnOnCompanyWifi", self.bypass_vpn_on_company_wifi)
        writer.write_bool_value("bypassVpnOnHomeWifi", self.bypass_vpn_on_home_wifi)
        writer.write_collection_of_primitive_values("dnsSuffixSearchList", self.dns_suffix_search_list)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("rememberUserCredentials", self.remember_user_credentials)
    

