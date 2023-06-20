from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_azure_ad_trust_type, device_management_configuration_setting_applicability, device_management_configuration_windows_skus

from . import device_management_configuration_setting_applicability

@dataclass
class DeviceManagementConfigurationWindowsSettingApplicability(device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability):
    odata_type = "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability"
    # Version of CSP setting is a part of
    configuration_service_provider_version: Optional[str] = None
    # Maximum supported version of Windows
    maximum_supported_version: Optional[str] = None
    # Minimum supported version of Windows
    minimum_supported_version: Optional[str] = None
    # Required AAD Trust Type
    required_azure_ad_trust_type: Optional[device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType] = None
    # AzureAD setting requirement
    requires_azure_ad: Optional[bool] = None
    # List of Windows SKUs that the setting is applicable for
    windows_skus: Optional[List[device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationWindowsSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationWindowsSettingApplicability
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationWindowsSettingApplicability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_azure_ad_trust_type, device_management_configuration_setting_applicability, device_management_configuration_windows_skus

        from . import device_management_configuration_azure_ad_trust_type, device_management_configuration_setting_applicability, device_management_configuration_windows_skus

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationServiceProviderVersion": lambda n : setattr(self, 'configuration_service_provider_version', n.get_str_value()),
            "maximumSupportedVersion": lambda n : setattr(self, 'maximum_supported_version', n.get_str_value()),
            "minimumSupportedVersion": lambda n : setattr(self, 'minimum_supported_version', n.get_str_value()),
            "requiredAzureAdTrustType": lambda n : setattr(self, 'required_azure_ad_trust_type', n.get_enum_value(device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType)),
            "requiresAzureAd": lambda n : setattr(self, 'requires_azure_ad', n.get_bool_value()),
            "windowsSkus": lambda n : setattr(self, 'windows_skus', n.get_collection_of_enum_values(device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus)),
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
        writer.write_str_value("configurationServiceProviderVersion", self.configuration_service_provider_version)
        writer.write_str_value("maximumSupportedVersion", self.maximum_supported_version)
        writer.write_str_value("minimumSupportedVersion", self.minimum_supported_version)
        writer.write_enum_value("requiredAzureAdTrustType", self.required_azure_ad_trust_type)
        writer.write_bool_value("requiresAzureAd", self.requires_azure_ad)
        writer.write_collection_of_enum_values("windowsSkus", self.windows_skus)
    

