from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

excluded_apps = lazy_import('msgraph.generated.models.excluded_apps')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
office_product_id = lazy_import('msgraph.generated.models.office_product_id')
office_suite_default_file_format_type = lazy_import('msgraph.generated.models.office_suite_default_file_format_type')
office_suite_install_progress_display_level = lazy_import('msgraph.generated.models.office_suite_install_progress_display_level')
office_update_channel = lazy_import('msgraph.generated.models.office_update_channel')
windows_architecture = lazy_import('msgraph.generated.models.windows_architecture')

class OfficeSuiteApp(mobile_app.MobileApp):
    @property
    def auto_accept_eula(self,) -> Optional[bool]:
        """
        Gets the autoAcceptEula property value. The value to accept the EULA automatically on the enduser's device.
        Returns: Optional[bool]
        """
        return self._auto_accept_eula
    
    @auto_accept_eula.setter
    def auto_accept_eula(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoAcceptEula property value. The value to accept the EULA automatically on the enduser's device.
        Args:
            value: Value to set for the autoAcceptEula property.
        """
        self._auto_accept_eula = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OfficeSuiteApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.officeSuiteApp"
        # The value to accept the EULA automatically on the enduser's device.
        self._auto_accept_eula: Optional[bool] = None
        # The property to represent the apps which are excluded from the selected Office365 Product Id.
        self._excluded_apps: Optional[excluded_apps.ExcludedApps] = None
        # The Enum to specify the level of display for the Installation Progress Setup UI on the Device.
        self._install_progress_display_level: Optional[office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel] = None
        # The property to represent the locales which are installed when the apps from Office365 is installed. It uses standard RFC 6033. Ref: https://technet.microsoft.com/library/cc179219(v=office.16).aspx
        self._locales_to_install: Optional[List[str]] = None
        # The property to represent the XML configuration file that can be specified for Office ProPlus Apps. Takes precedence over all other properties. When present, the XML configuration file will be used to create the app.
        self._office_configuration_xml: Optional[bytes] = None
        # Contains properties for Windows architecture.
        self._office_platform_architecture: Optional[windows_architecture.WindowsArchitecture] = None
        # Describes the OfficeSuiteApp file format types that can be selected.
        self._office_suite_app_default_file_format: Optional[office_suite_default_file_format_type.OfficeSuiteDefaultFileFormatType] = None
        # The Product Ids that represent the Office365 Suite SKU.
        self._product_ids: Optional[List[office_product_id.OfficeProductId]] = None
        # The property to determine whether to uninstall existing Office MSI if an Office365 app suite is deployed to the device or not.
        self._should_uninstall_older_versions_of_office: Optional[bool] = None
        # The property to represent the specific target version for the Office365 app suite that should be remained deployed on the devices.
        self._target_version: Optional[str] = None
        # The Enum to specify the Office365 Updates Channel.
        self._update_channel: Optional[office_update_channel.OfficeUpdateChannel] = None
        # The property to represent the update version in which the specific target version is available for the Office365 app suite.
        self._update_version: Optional[str] = None
        # The property to represent that whether the shared computer activation is used not for Office365 app suite.
        self._use_shared_computer_activation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeSuiteApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeSuiteApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeSuiteApp()
    
    @property
    def excluded_apps(self,) -> Optional[excluded_apps.ExcludedApps]:
        """
        Gets the excludedApps property value. The property to represent the apps which are excluded from the selected Office365 Product Id.
        Returns: Optional[excluded_apps.ExcludedApps]
        """
        return self._excluded_apps
    
    @excluded_apps.setter
    def excluded_apps(self,value: Optional[excluded_apps.ExcludedApps] = None) -> None:
        """
        Sets the excludedApps property value. The property to represent the apps which are excluded from the selected Office365 Product Id.
        Args:
            value: Value to set for the excludedApps property.
        """
        self._excluded_apps = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auto_accept_eula": lambda n : setattr(self, 'auto_accept_eula', n.get_bool_value()),
            "excluded_apps": lambda n : setattr(self, 'excluded_apps', n.get_object_value(excluded_apps.ExcludedApps)),
            "install_progress_display_level": lambda n : setattr(self, 'install_progress_display_level', n.get_enum_value(office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel)),
            "locales_to_install": lambda n : setattr(self, 'locales_to_install', n.get_collection_of_primitive_values(str)),
            "office_configuration_xml": lambda n : setattr(self, 'office_configuration_xml', n.get_bytes_value()),
            "office_platform_architecture": lambda n : setattr(self, 'office_platform_architecture', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "office_suite_app_default_file_format": lambda n : setattr(self, 'office_suite_app_default_file_format', n.get_enum_value(office_suite_default_file_format_type.OfficeSuiteDefaultFileFormatType)),
            "product_ids": lambda n : setattr(self, 'product_ids', n.get_collection_of_enum_values(office_product_id.OfficeProductId)),
            "should_uninstall_older_versions_of_office": lambda n : setattr(self, 'should_uninstall_older_versions_of_office', n.get_bool_value()),
            "target_version": lambda n : setattr(self, 'target_version', n.get_str_value()),
            "update_channel": lambda n : setattr(self, 'update_channel', n.get_enum_value(office_update_channel.OfficeUpdateChannel)),
            "update_version": lambda n : setattr(self, 'update_version', n.get_str_value()),
            "use_shared_computer_activation": lambda n : setattr(self, 'use_shared_computer_activation', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_progress_display_level(self,) -> Optional[office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel]:
        """
        Gets the installProgressDisplayLevel property value. The Enum to specify the level of display for the Installation Progress Setup UI on the Device.
        Returns: Optional[office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel]
        """
        return self._install_progress_display_level
    
    @install_progress_display_level.setter
    def install_progress_display_level(self,value: Optional[office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel] = None) -> None:
        """
        Sets the installProgressDisplayLevel property value. The Enum to specify the level of display for the Installation Progress Setup UI on the Device.
        Args:
            value: Value to set for the installProgressDisplayLevel property.
        """
        self._install_progress_display_level = value
    
    @property
    def locales_to_install(self,) -> Optional[List[str]]:
        """
        Gets the localesToInstall property value. The property to represent the locales which are installed when the apps from Office365 is installed. It uses standard RFC 6033. Ref: https://technet.microsoft.com/library/cc179219(v=office.16).aspx
        Returns: Optional[List[str]]
        """
        return self._locales_to_install
    
    @locales_to_install.setter
    def locales_to_install(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the localesToInstall property value. The property to represent the locales which are installed when the apps from Office365 is installed. It uses standard RFC 6033. Ref: https://technet.microsoft.com/library/cc179219(v=office.16).aspx
        Args:
            value: Value to set for the localesToInstall property.
        """
        self._locales_to_install = value
    
    @property
    def office_configuration_xml(self,) -> Optional[bytes]:
        """
        Gets the officeConfigurationXml property value. The property to represent the XML configuration file that can be specified for Office ProPlus Apps. Takes precedence over all other properties. When present, the XML configuration file will be used to create the app.
        Returns: Optional[bytes]
        """
        return self._office_configuration_xml
    
    @office_configuration_xml.setter
    def office_configuration_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the officeConfigurationXml property value. The property to represent the XML configuration file that can be specified for Office ProPlus Apps. Takes precedence over all other properties. When present, the XML configuration file will be used to create the app.
        Args:
            value: Value to set for the officeConfigurationXml property.
        """
        self._office_configuration_xml = value
    
    @property
    def office_platform_architecture(self,) -> Optional[windows_architecture.WindowsArchitecture]:
        """
        Gets the officePlatformArchitecture property value. Contains properties for Windows architecture.
        Returns: Optional[windows_architecture.WindowsArchitecture]
        """
        return self._office_platform_architecture
    
    @office_platform_architecture.setter
    def office_platform_architecture(self,value: Optional[windows_architecture.WindowsArchitecture] = None) -> None:
        """
        Sets the officePlatformArchitecture property value. Contains properties for Windows architecture.
        Args:
            value: Value to set for the officePlatformArchitecture property.
        """
        self._office_platform_architecture = value
    
    @property
    def office_suite_app_default_file_format(self,) -> Optional[office_suite_default_file_format_type.OfficeSuiteDefaultFileFormatType]:
        """
        Gets the officeSuiteAppDefaultFileFormat property value. Describes the OfficeSuiteApp file format types that can be selected.
        Returns: Optional[office_suite_default_file_format_type.OfficeSuiteDefaultFileFormatType]
        """
        return self._office_suite_app_default_file_format
    
    @office_suite_app_default_file_format.setter
    def office_suite_app_default_file_format(self,value: Optional[office_suite_default_file_format_type.OfficeSuiteDefaultFileFormatType] = None) -> None:
        """
        Sets the officeSuiteAppDefaultFileFormat property value. Describes the OfficeSuiteApp file format types that can be selected.
        Args:
            value: Value to set for the officeSuiteAppDefaultFileFormat property.
        """
        self._office_suite_app_default_file_format = value
    
    @property
    def product_ids(self,) -> Optional[List[office_product_id.OfficeProductId]]:
        """
        Gets the productIds property value. The Product Ids that represent the Office365 Suite SKU.
        Returns: Optional[List[office_product_id.OfficeProductId]]
        """
        return self._product_ids
    
    @product_ids.setter
    def product_ids(self,value: Optional[List[office_product_id.OfficeProductId]] = None) -> None:
        """
        Sets the productIds property value. The Product Ids that represent the Office365 Suite SKU.
        Args:
            value: Value to set for the productIds property.
        """
        self._product_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("autoAcceptEula", self.auto_accept_eula)
        writer.write_object_value("excludedApps", self.excluded_apps)
        writer.write_enum_value("installProgressDisplayLevel", self.install_progress_display_level)
        writer.write_collection_of_primitive_values("localesToInstall", self.locales_to_install)
        writer.write_object_value("officeConfigurationXml", self.office_configuration_xml)
        writer.write_enum_value("officePlatformArchitecture", self.office_platform_architecture)
        writer.write_enum_value("officeSuiteAppDefaultFileFormat", self.office_suite_app_default_file_format)
        writer.write_enum_value("productIds", self.product_ids)
        writer.write_bool_value("shouldUninstallOlderVersionsOfOffice", self.should_uninstall_older_versions_of_office)
        writer.write_str_value("targetVersion", self.target_version)
        writer.write_enum_value("updateChannel", self.update_channel)
        writer.write_str_value("updateVersion", self.update_version)
        writer.write_bool_value("useSharedComputerActivation", self.use_shared_computer_activation)
    
    @property
    def should_uninstall_older_versions_of_office(self,) -> Optional[bool]:
        """
        Gets the shouldUninstallOlderVersionsOfOffice property value. The property to determine whether to uninstall existing Office MSI if an Office365 app suite is deployed to the device or not.
        Returns: Optional[bool]
        """
        return self._should_uninstall_older_versions_of_office
    
    @should_uninstall_older_versions_of_office.setter
    def should_uninstall_older_versions_of_office(self,value: Optional[bool] = None) -> None:
        """
        Sets the shouldUninstallOlderVersionsOfOffice property value. The property to determine whether to uninstall existing Office MSI if an Office365 app suite is deployed to the device or not.
        Args:
            value: Value to set for the shouldUninstallOlderVersionsOfOffice property.
        """
        self._should_uninstall_older_versions_of_office = value
    
    @property
    def target_version(self,) -> Optional[str]:
        """
        Gets the targetVersion property value. The property to represent the specific target version for the Office365 app suite that should be remained deployed on the devices.
        Returns: Optional[str]
        """
        return self._target_version
    
    @target_version.setter
    def target_version(self,value: Optional[str] = None) -> None:
        """
        Sets the targetVersion property value. The property to represent the specific target version for the Office365 app suite that should be remained deployed on the devices.
        Args:
            value: Value to set for the targetVersion property.
        """
        self._target_version = value
    
    @property
    def update_channel(self,) -> Optional[office_update_channel.OfficeUpdateChannel]:
        """
        Gets the updateChannel property value. The Enum to specify the Office365 Updates Channel.
        Returns: Optional[office_update_channel.OfficeUpdateChannel]
        """
        return self._update_channel
    
    @update_channel.setter
    def update_channel(self,value: Optional[office_update_channel.OfficeUpdateChannel] = None) -> None:
        """
        Sets the updateChannel property value. The Enum to specify the Office365 Updates Channel.
        Args:
            value: Value to set for the updateChannel property.
        """
        self._update_channel = value
    
    @property
    def update_version(self,) -> Optional[str]:
        """
        Gets the updateVersion property value. The property to represent the update version in which the specific target version is available for the Office365 app suite.
        Returns: Optional[str]
        """
        return self._update_version
    
    @update_version.setter
    def update_version(self,value: Optional[str] = None) -> None:
        """
        Sets the updateVersion property value. The property to represent the update version in which the specific target version is available for the Office365 app suite.
        Args:
            value: Value to set for the updateVersion property.
        """
        self._update_version = value
    
    @property
    def use_shared_computer_activation(self,) -> Optional[bool]:
        """
        Gets the useSharedComputerActivation property value. The property to represent that whether the shared computer activation is used not for Office365 app suite.
        Returns: Optional[bool]
        """
        return self._use_shared_computer_activation
    
    @use_shared_computer_activation.setter
    def use_shared_computer_activation(self,value: Optional[bool] = None) -> None:
        """
        Sets the useSharedComputerActivation property value. The property to represent that whether the shared computer activation is used not for Office365 app suite.
        Args:
            value: Value to set for the useSharedComputerActivation property.
        """
        self._use_shared_computer_activation = value
    

