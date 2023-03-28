from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, domain_name_source, ios_eas_email_profile_configuration, username_source, user_email_source, windows10_eas_email_profile_configuration, windows_phone_e_a_s_email_profile_configuration

from . import device_configuration

class EasEmailProfileConfigurationBase(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new EasEmailProfileConfigurationBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.easEmailProfileConfigurationBase"
        # Custom domain name value used while generating an email profile before installing on the device.
        self._custom_domain_name: Optional[str] = None
        # UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        self._user_domain_name_source: Optional[domain_name_source.DomainNameSource] = None
        # Name of the AAD field, that will be used to retrieve UserName for email profile. Possible values are: userPrincipalName, primarySmtpAddress, samAccountName.
        self._username_a_a_d_source: Optional[username_source.UsernameSource] = None
        # Possible values for username source or email source.
        self._username_source: Optional[user_email_source.UserEmailSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EasEmailProfileConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EasEmailProfileConfigurationBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosEasEmailProfileConfiguration":
                from . import ios_eas_email_profile_configuration

                return ios_eas_email_profile_configuration.IosEasEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.windows10EasEmailProfileConfiguration":
                from . import windows10_eas_email_profile_configuration

                return windows10_eas_email_profile_configuration.Windows10EasEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration":
                from . import windows_phone_e_a_s_email_profile_configuration

                return windows_phone_e_a_s_email_profile_configuration.WindowsPhoneEASEmailProfileConfiguration()
        return EasEmailProfileConfigurationBase()
    
    @property
    def custom_domain_name(self,) -> Optional[str]:
        """
        Gets the customDomainName property value. Custom domain name value used while generating an email profile before installing on the device.
        Returns: Optional[str]
        """
        return self._custom_domain_name
    
    @custom_domain_name.setter
    def custom_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customDomainName property value. Custom domain name value used while generating an email profile before installing on the device.
        Args:
            value: Value to set for the custom_domain_name property.
        """
        self._custom_domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, domain_name_source, ios_eas_email_profile_configuration, username_source, user_email_source, windows10_eas_email_profile_configuration, windows_phone_e_a_s_email_profile_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "customDomainName": lambda n : setattr(self, 'custom_domain_name', n.get_str_value()),
            "usernameAADSource": lambda n : setattr(self, 'username_a_a_d_source', n.get_enum_value(username_source.UsernameSource)),
            "usernameSource": lambda n : setattr(self, 'username_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "userDomainNameSource": lambda n : setattr(self, 'user_domain_name_source', n.get_enum_value(domain_name_source.DomainNameSource)),
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
        writer.write_str_value("customDomainName", self.custom_domain_name)
        writer.write_enum_value("usernameAADSource", self.username_a_a_d_source)
        writer.write_enum_value("usernameSource", self.username_source)
        writer.write_enum_value("userDomainNameSource", self.user_domain_name_source)
    
    @property
    def user_domain_name_source(self,) -> Optional[domain_name_source.DomainNameSource]:
        """
        Gets the userDomainNameSource property value. UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        Returns: Optional[domain_name_source.DomainNameSource]
        """
        return self._user_domain_name_source
    
    @user_domain_name_source.setter
    def user_domain_name_source(self,value: Optional[domain_name_source.DomainNameSource] = None) -> None:
        """
        Sets the userDomainNameSource property value. UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
        Args:
            value: Value to set for the user_domain_name_source property.
        """
        self._user_domain_name_source = value
    
    @property
    def username_a_a_d_source(self,) -> Optional[username_source.UsernameSource]:
        """
        Gets the usernameAADSource property value. Name of the AAD field, that will be used to retrieve UserName for email profile. Possible values are: userPrincipalName, primarySmtpAddress, samAccountName.
        Returns: Optional[username_source.UsernameSource]
        """
        return self._username_a_a_d_source
    
    @username_a_a_d_source.setter
    def username_a_a_d_source(self,value: Optional[username_source.UsernameSource] = None) -> None:
        """
        Sets the usernameAADSource property value. Name of the AAD field, that will be used to retrieve UserName for email profile. Possible values are: userPrincipalName, primarySmtpAddress, samAccountName.
        Args:
            value: Value to set for the username_a_a_d_source property.
        """
        self._username_a_a_d_source = value
    
    @property
    def username_source(self,) -> Optional[user_email_source.UserEmailSource]:
        """
        Gets the usernameSource property value. Possible values for username source or email source.
        Returns: Optional[user_email_source.UserEmailSource]
        """
        return self._username_source
    
    @username_source.setter
    def username_source(self,value: Optional[user_email_source.UserEmailSource] = None) -> None:
        """
        Sets the usernameSource property value. Possible values for username source or email source.
        Args:
            value: Value to set for the username_source property.
        """
        self._username_source = value
    

