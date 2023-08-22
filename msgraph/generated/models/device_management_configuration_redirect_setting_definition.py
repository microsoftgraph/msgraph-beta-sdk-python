from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

@dataclass
class DeviceManagementConfigurationRedirectSettingDefinition(DeviceManagementConfigurationSettingDefinition):
    # A deep link that points to the specific location in the Intune console where feature support must be managed from.
    deep_link: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A message that explains that clicking the link will redirect the user to a supported page to manage the settings.
    redirect_message: Optional[str] = None
    # Indicates the reason for redirecting the user to an alternative location in the console.  For example: WiFi profiles are not supported in the settings catalog and must be created with a template policy.
    redirect_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationRedirectSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationRedirectSettingDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationRedirectSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "deepLink": lambda n : setattr(self, 'deep_link', n.get_str_value()),
            "redirectMessage": lambda n : setattr(self, 'redirect_message', n.get_str_value()),
            "redirectReason": lambda n : setattr(self, 'redirect_reason', n.get_str_value()),
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
        writer.write_str_value("deepLink", self.deep_link)
        writer.write_str_value("redirectMessage", self.redirect_message)
        writer.write_str_value("redirectReason", self.redirect_reason)
    

