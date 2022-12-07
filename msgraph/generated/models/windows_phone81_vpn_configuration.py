from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

vpn_authentication_method = lazy_import('msgraph.generated.models.vpn_authentication_method')
windows_phone81_certificate_profile_base = lazy_import('msgraph.generated.models.windows_phone81_certificate_profile_base')
windows81_vpn_configuration = lazy_import('msgraph.generated.models.windows81_vpn_configuration')

class WindowsPhone81VpnConfiguration(windows81_vpn_configuration.Windows81VpnConfiguration):
    @property
    def authentication_method(self,) -> Optional[vpn_authentication_method.VpnAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. VPN Authentication Method.
        Returns: Optional[vpn_authentication_method.VpnAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. VPN Authentication Method.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    @property
    def bypass_vpn_on_company_wifi(self,) -> Optional[bool]:
        """
        Gets the bypassVpnOnCompanyWifi property value. Bypass VPN on company Wi-Fi.
        Returns: Optional[bool]
        """
        return self._bypass_vpn_on_company_wifi
    
    @bypass_vpn_on_company_wifi.setter
    def bypass_vpn_on_company_wifi(self,value: Optional[bool] = None) -> None:
        """
        Sets the bypassVpnOnCompanyWifi property value. Bypass VPN on company Wi-Fi.
        Args:
            value: Value to set for the bypassVpnOnCompanyWifi property.
        """
        self._bypass_vpn_on_company_wifi = value
    
    @property
    def bypass_vpn_on_home_wifi(self,) -> Optional[bool]:
        """
        Gets the bypassVpnOnHomeWifi property value. Bypass VPN on home Wi-Fi.
        Returns: Optional[bool]
        """
        return self._bypass_vpn_on_home_wifi
    
    @bypass_vpn_on_home_wifi.setter
    def bypass_vpn_on_home_wifi(self,value: Optional[bool] = None) -> None:
        """
        Sets the bypassVpnOnHomeWifi property value. Bypass VPN on home Wi-Fi.
        Args:
            value: Value to set for the bypassVpnOnHomeWifi property.
        """
        self._bypass_vpn_on_home_wifi = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhone81VpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81VpnConfiguration"
        # VPN Authentication Method.
        self._authentication_method: Optional[vpn_authentication_method.VpnAuthenticationMethod] = None
        # Bypass VPN on company Wi-Fi.
        self._bypass_vpn_on_company_wifi: Optional[bool] = None
        # Bypass VPN on home Wi-Fi.
        self._bypass_vpn_on_home_wifi: Optional[bool] = None
        # DNS suffix search list.
        self._dns_suffix_search_list: Optional[List[str]] = None
        # Identity certificate for client authentication when authentication method is certificate.
        self._identity_certificate: Optional[windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase] = None
        # Remember user credentials.
        self._remember_user_credentials: Optional[bool] = None
    
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
    
    @property
    def dns_suffix_search_list(self,) -> Optional[List[str]]:
        """
        Gets the dnsSuffixSearchList property value. DNS suffix search list.
        Returns: Optional[List[str]]
        """
        return self._dns_suffix_search_list
    
    @dns_suffix_search_list.setter
    def dns_suffix_search_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dnsSuffixSearchList property value. DNS suffix search list.
        Args:
            value: Value to set for the dnsSuffixSearchList property.
        """
        self._dns_suffix_search_list = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(vpn_authentication_method.VpnAuthenticationMethod)),
            "bypass_vpn_on_company_wifi": lambda n : setattr(self, 'bypass_vpn_on_company_wifi', n.get_bool_value()),
            "bypass_vpn_on_home_wifi": lambda n : setattr(self, 'bypass_vpn_on_home_wifi', n.get_bool_value()),
            "dns_suffix_search_list": lambda n : setattr(self, 'dns_suffix_search_list', n.get_collection_of_primitive_values(str)),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase)),
            "remember_user_credentials": lambda n : setattr(self, 'remember_user_credentials', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_certificate(self,) -> Optional[windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Returns: Optional[windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate for client authentication when authentication method is certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    @property
    def remember_user_credentials(self,) -> Optional[bool]:
        """
        Gets the rememberUserCredentials property value. Remember user credentials.
        Returns: Optional[bool]
        """
        return self._remember_user_credentials
    
    @remember_user_credentials.setter
    def remember_user_credentials(self,value: Optional[bool] = None) -> None:
        """
        Sets the rememberUserCredentials property value. Remember user credentials.
        Args:
            value: Value to set for the rememberUserCredentials property.
        """
        self._remember_user_credentials = value
    
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
    

