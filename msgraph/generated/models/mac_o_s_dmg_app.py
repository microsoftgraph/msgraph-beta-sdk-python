from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mac_o_s_included_app = lazy_import('msgraph.generated.models.mac_o_s_included_app')
mac_o_s_minimum_operating_system = lazy_import('msgraph.generated.models.mac_o_s_minimum_operating_system')
mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')

class MacOSDmgApp(mobile_lob_app.MobileLobApp):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSDmgApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSDmgApp"
        # A value indicating whether the app's version will be used to detect the app after it is installed on a device. Set this to true for apps that use a self-update feature. Set this to false to install the app when it is not already installed on the device, or if the deploying app's version number does not match the version that's already installed on the device.
        self._ignore_version_detection: Optional[bool] = None
        # The list of apps expected to be installed by the DMG.
        self._included_apps: Optional[List[mac_o_s_included_app.MacOSIncludedApp]] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem] = None
        # The primary CFBundleIdentifier of the DMG.
        self._primary_bundle_id: Optional[str] = None
        # The primary CFBundleVersion of the DMG.
        self._primary_bundle_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSDmgApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSDmgApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSDmgApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ignore_version_detection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "included_apps": lambda n : setattr(self, 'included_apps', n.get_collection_of_object_values(mac_o_s_included_app.MacOSIncludedApp)),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem)),
            "primary_bundle_id": lambda n : setattr(self, 'primary_bundle_id', n.get_str_value()),
            "primary_bundle_version": lambda n : setattr(self, 'primary_bundle_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ignore_version_detection(self,) -> Optional[bool]:
        """
        Gets the ignoreVersionDetection property value. A value indicating whether the app's version will be used to detect the app after it is installed on a device. Set this to true for apps that use a self-update feature. Set this to false to install the app when it is not already installed on the device, or if the deploying app's version number does not match the version that's already installed on the device.
        Returns: Optional[bool]
        """
        return self._ignore_version_detection
    
    @ignore_version_detection.setter
    def ignore_version_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the ignoreVersionDetection property value. A value indicating whether the app's version will be used to detect the app after it is installed on a device. Set this to true for apps that use a self-update feature. Set this to false to install the app when it is not already installed on the device, or if the deploying app's version number does not match the version that's already installed on the device.
        Args:
            value: Value to set for the ignoreVersionDetection property.
        """
        self._ignore_version_detection = value
    
    @property
    def included_apps(self,) -> Optional[List[mac_o_s_included_app.MacOSIncludedApp]]:
        """
        Gets the includedApps property value. The list of apps expected to be installed by the DMG.
        Returns: Optional[List[mac_o_s_included_app.MacOSIncludedApp]]
        """
        return self._included_apps
    
    @included_apps.setter
    def included_apps(self,value: Optional[List[mac_o_s_included_app.MacOSIncludedApp]] = None) -> None:
        """
        Sets the includedApps property value. The list of apps expected to be installed by the DMG.
        Args:
            value: Value to set for the includedApps property.
        """
        self._included_apps = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def primary_bundle_id(self,) -> Optional[str]:
        """
        Gets the primaryBundleId property value. The primary CFBundleIdentifier of the DMG.
        Returns: Optional[str]
        """
        return self._primary_bundle_id
    
    @primary_bundle_id.setter
    def primary_bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryBundleId property value. The primary CFBundleIdentifier of the DMG.
        Args:
            value: Value to set for the primaryBundleId property.
        """
        self._primary_bundle_id = value
    
    @property
    def primary_bundle_version(self,) -> Optional[str]:
        """
        Gets the primaryBundleVersion property value. The primary CFBundleVersion of the DMG.
        Returns: Optional[str]
        """
        return self._primary_bundle_version
    
    @primary_bundle_version.setter
    def primary_bundle_version(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryBundleVersion property value. The primary CFBundleVersion of the DMG.
        Args:
            value: Value to set for the primaryBundleVersion property.
        """
        self._primary_bundle_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_collection_of_object_values("includedApps", self.included_apps)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("primaryBundleId", self.primary_bundle_id)
        writer.write_str_value("primaryBundleVersion", self.primary_bundle_version)
    

