from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_azure_ad_trust_type = lazy_import('msgraph.generated.models.device_management_configuration_azure_ad_trust_type')
device_management_configuration_setting_applicability = lazy_import('msgraph.generated.models.device_management_configuration_setting_applicability')
device_management_configuration_windows_skus = lazy_import('msgraph.generated.models.device_management_configuration_windows_skus')

class DeviceManagementConfigurationWindowsSettingApplicability(device_management_configuration_setting_applicability.DeviceManagementConfigurationSettingApplicability):
    @property
    def configuration_service_provider_version(self,) -> Optional[str]:
        """
        Gets the configurationServiceProviderVersion property value. Version of CSP setting is a part of
        Returns: Optional[str]
        """
        return self._configuration_service_provider_version
    
    @configuration_service_provider_version.setter
    def configuration_service_provider_version(self,value: Optional[str] = None) -> None:
        """
        Sets the configurationServiceProviderVersion property value. Version of CSP setting is a part of
        Args:
            value: Value to set for the configurationServiceProviderVersion property.
        """
        self._configuration_service_provider_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationWindowsSettingApplicability and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability"
        # Version of CSP setting is a part of
        self._configuration_service_provider_version: Optional[str] = None
        # Maximum supported version of Windows
        self._maximum_supported_version: Optional[str] = None
        # Minimum supported version of Windows
        self._minimum_supported_version: Optional[str] = None
        # Required AAD Trust Type
        self._required_azure_ad_trust_type: Optional[device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType] = None
        # AzureAD setting requirement
        self._requires_azure_ad: Optional[bool] = None
        # List of Windows SKUs that the setting is applicable for
        self._windows_skus: Optional[List[device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationWindowsSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationWindowsSettingApplicability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationWindowsSettingApplicability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_service_provider_version": lambda n : setattr(self, 'configuration_service_provider_version', n.get_str_value()),
            "maximum_supported_version": lambda n : setattr(self, 'maximum_supported_version', n.get_str_value()),
            "minimum_supported_version": lambda n : setattr(self, 'minimum_supported_version', n.get_str_value()),
            "required_azure_ad_trust_type": lambda n : setattr(self, 'required_azure_ad_trust_type', n.get_enum_value(device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType)),
            "requires_azure_ad": lambda n : setattr(self, 'requires_azure_ad', n.get_bool_value()),
            "windows_skus": lambda n : setattr(self, 'windows_skus', n.get_collection_of_enum_values(device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_supported_version(self,) -> Optional[str]:
        """
        Gets the maximumSupportedVersion property value. Maximum supported version of Windows
        Returns: Optional[str]
        """
        return self._maximum_supported_version
    
    @maximum_supported_version.setter
    def maximum_supported_version(self,value: Optional[str] = None) -> None:
        """
        Sets the maximumSupportedVersion property value. Maximum supported version of Windows
        Args:
            value: Value to set for the maximumSupportedVersion property.
        """
        self._maximum_supported_version = value
    
    @property
    def minimum_supported_version(self,) -> Optional[str]:
        """
        Gets the minimumSupportedVersion property value. Minimum supported version of Windows
        Returns: Optional[str]
        """
        return self._minimum_supported_version
    
    @minimum_supported_version.setter
    def minimum_supported_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumSupportedVersion property value. Minimum supported version of Windows
        Args:
            value: Value to set for the minimumSupportedVersion property.
        """
        self._minimum_supported_version = value
    
    @property
    def required_azure_ad_trust_type(self,) -> Optional[device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType]:
        """
        Gets the requiredAzureAdTrustType property value. Required AAD Trust Type
        Returns: Optional[device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType]
        """
        return self._required_azure_ad_trust_type
    
    @required_azure_ad_trust_type.setter
    def required_azure_ad_trust_type(self,value: Optional[device_management_configuration_azure_ad_trust_type.DeviceManagementConfigurationAzureAdTrustType] = None) -> None:
        """
        Sets the requiredAzureAdTrustType property value. Required AAD Trust Type
        Args:
            value: Value to set for the requiredAzureAdTrustType property.
        """
        self._required_azure_ad_trust_type = value
    
    @property
    def requires_azure_ad(self,) -> Optional[bool]:
        """
        Gets the requiresAzureAd property value. AzureAD setting requirement
        Returns: Optional[bool]
        """
        return self._requires_azure_ad
    
    @requires_azure_ad.setter
    def requires_azure_ad(self,value: Optional[bool] = None) -> None:
        """
        Sets the requiresAzureAd property value. AzureAD setting requirement
        Args:
            value: Value to set for the requiresAzureAd property.
        """
        self._requires_azure_ad = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("configurationServiceProviderVersion", self.configuration_service_provider_version)
        writer.write_str_value("maximumSupportedVersion", self.maximum_supported_version)
        writer.write_str_value("minimumSupportedVersion", self.minimum_supported_version)
        writer.write_enum_value("requiredAzureAdTrustType", self.required_azure_ad_trust_type)
        writer.write_bool_value("requiresAzureAd", self.requires_azure_ad)
        writer.write_enum_value("windowsSkus", self.windows_skus)
    
    @property
    def windows_skus(self,) -> Optional[List[device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus]]:
        """
        Gets the windowsSkus property value. List of Windows SKUs that the setting is applicable for
        Returns: Optional[List[device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus]]
        """
        return self._windows_skus
    
    @windows_skus.setter
    def windows_skus(self,value: Optional[List[device_management_configuration_windows_skus.DeviceManagementConfigurationWindowsSkus]] = None) -> None:
        """
        Sets the windowsSkus property value. List of Windows SKUs that the setting is applicable for
        Args:
            value: Value to set for the windowsSkus property.
        """
        self._windows_skus = value
    

