from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, domain_name_source, ios_eas_email_profile_configuration, username_source, user_email_source, windows10_eas_email_profile_configuration, windows_phone_e_a_s_email_profile_configuration

from . import device_configuration

@dataclass
class EasEmailProfileConfigurationBase(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.easEmailProfileConfigurationBase"
    # Custom domain name value used while generating an email profile before installing on the device.
    custom_domain_name: Optional[str] = None
    # UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
    user_domain_name_source: Optional[domain_name_source.DomainNameSource] = None
    # Name of the AAD field, that will be used to retrieve UserName for email profile. Possible values are: userPrincipalName, primarySmtpAddress, samAccountName.
    username_a_a_d_source: Optional[username_source.UsernameSource] = None
    # Possible values for username source or email source.
    username_source: Optional[user_email_source.UserEmailSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EasEmailProfileConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EasEmailProfileConfigurationBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEasEmailProfileConfiguration".casefold():
            from . import ios_eas_email_profile_configuration

            return ios_eas_email_profile_configuration.IosEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EasEmailProfileConfiguration".casefold():
            from . import windows10_eas_email_profile_configuration

            return windows10_eas_email_profile_configuration.Windows10EasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration".casefold():
            from . import windows_phone_e_a_s_email_profile_configuration

            return windows_phone_e_a_s_email_profile_configuration.WindowsPhoneEASEmailProfileConfiguration()
        return EasEmailProfileConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, domain_name_source, ios_eas_email_profile_configuration, username_source, user_email_source, windows10_eas_email_profile_configuration, windows_phone_e_a_s_email_profile_configuration

        from . import device_configuration, domain_name_source, ios_eas_email_profile_configuration, username_source, user_email_source, windows10_eas_email_profile_configuration, windows_phone_e_a_s_email_profile_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "customDomainName": lambda n : setattr(self, 'custom_domain_name', n.get_str_value()),
            "userDomainNameSource": lambda n : setattr(self, 'user_domain_name_source', n.get_enum_value(domain_name_source.DomainNameSource)),
            "usernameAADSource": lambda n : setattr(self, 'username_a_a_d_source', n.get_enum_value(username_source.UsernameSource)),
            "usernameSource": lambda n : setattr(self, 'username_source', n.get_enum_value(user_email_source.UserEmailSource)),
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
        writer.write_str_value("customDomainName", self.custom_domain_name)
        writer.write_enum_value("userDomainNameSource", self.user_domain_name_source)
        writer.write_enum_value("usernameAADSource", self.username_a_a_d_source)
        writer.write_enum_value("usernameSource", self.username_source)
    

