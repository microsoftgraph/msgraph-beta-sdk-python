from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')

class DeviceManagementConfigurationRedirectSettingDefinition(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationRedirectSettingDefinition and sets the default values.
        """
        super().__init__()
        # A deep link that points to the specific location in the Intune console where feature support must be managed from.
        self._deep_link: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A message that explains that clicking the link will redirect the user to a supported page to manage the settings.
        self._redirect_message: Optional[str] = None
        # Indicates the reason for redirecting the user to an alternative location in the console.  For example: WiFi profiles are not supported in the settings catalog and must be created with a template policy.
        self._redirect_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationRedirectSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationRedirectSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationRedirectSettingDefinition()
    
    @property
    def deep_link(self,) -> Optional[str]:
        """
        Gets the deepLink property value. A deep link that points to the specific location in the Intune console where feature support must be managed from.
        Returns: Optional[str]
        """
        return self._deep_link
    
    @deep_link.setter
    def deep_link(self,value: Optional[str] = None) -> None:
        """
        Sets the deepLink property value. A deep link that points to the specific location in the Intune console where feature support must be managed from.
        Args:
            value: Value to set for the deepLink property.
        """
        self._deep_link = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deep_link": lambda n : setattr(self, 'deep_link', n.get_str_value()),
            "redirect_message": lambda n : setattr(self, 'redirect_message', n.get_str_value()),
            "redirect_reason": lambda n : setattr(self, 'redirect_reason', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def redirect_message(self,) -> Optional[str]:
        """
        Gets the redirectMessage property value. A message that explains that clicking the link will redirect the user to a supported page to manage the settings.
        Returns: Optional[str]
        """
        return self._redirect_message
    
    @redirect_message.setter
    def redirect_message(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectMessage property value. A message that explains that clicking the link will redirect the user to a supported page to manage the settings.
        Args:
            value: Value to set for the redirectMessage property.
        """
        self._redirect_message = value
    
    @property
    def redirect_reason(self,) -> Optional[str]:
        """
        Gets the redirectReason property value. Indicates the reason for redirecting the user to an alternative location in the console.  For example: WiFi profiles are not supported in the settings catalog and must be created with a template policy.
        Returns: Optional[str]
        """
        return self._redirect_reason
    
    @redirect_reason.setter
    def redirect_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectReason property value. Indicates the reason for redirecting the user to an alternative location in the console.  For example: WiFi profiles are not supported in the settings catalog and must be created with a template policy.
        Args:
            value: Value to set for the redirectReason property.
        """
        self._redirect_reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deepLink", self.deep_link)
        writer.write_str_value("redirectMessage", self.redirect_message)
        writer.write_str_value("redirectReason", self.redirect_reason)
    

