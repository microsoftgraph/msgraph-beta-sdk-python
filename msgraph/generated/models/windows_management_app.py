from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_installer_status = lazy_import('msgraph.generated.models.managed_installer_status')
windows_management_app_health_state = lazy_import('msgraph.generated.models.windows_management_app_health_state')

class WindowsManagementApp(entity.Entity):
    @property
    def available_version(self,) -> Optional[str]:
        """
        Gets the availableVersion property value. Windows management app available version.
        Returns: Optional[str]
        """
        return self._available_version
    
    @available_version.setter
    def available_version(self,value: Optional[str] = None) -> None:
        """
        Sets the availableVersion property value. Windows management app available version.
        Args:
            value: Value to set for the availableVersion property.
        """
        self._available_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsManagementApp and sets the default values.
        """
        super().__init__()
        # Windows management app available version.
        self._available_version: Optional[str] = None
        # The list of health states for installed Windows management app.
        self._health_states: Optional[List[windows_management_app_health_state.WindowsManagementAppHealthState]] = None
        # ManagedInstallerStatus
        self._managed_installer: Optional[managed_installer_status.ManagedInstallerStatus] = None
        # Managed Installer Configured Date Time
        self._managed_installer_configured_date_time: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsManagementApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagementApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsManagementApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "available_version": lambda n : setattr(self, 'available_version', n.get_str_value()),
            "health_states": lambda n : setattr(self, 'health_states', n.get_collection_of_object_values(windows_management_app_health_state.WindowsManagementAppHealthState)),
            "managed_installer": lambda n : setattr(self, 'managed_installer', n.get_enum_value(managed_installer_status.ManagedInstallerStatus)),
            "managed_installer_configured_date_time": lambda n : setattr(self, 'managed_installer_configured_date_time', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_states(self,) -> Optional[List[windows_management_app_health_state.WindowsManagementAppHealthState]]:
        """
        Gets the healthStates property value. The list of health states for installed Windows management app.
        Returns: Optional[List[windows_management_app_health_state.WindowsManagementAppHealthState]]
        """
        return self._health_states
    
    @health_states.setter
    def health_states(self,value: Optional[List[windows_management_app_health_state.WindowsManagementAppHealthState]] = None) -> None:
        """
        Sets the healthStates property value. The list of health states for installed Windows management app.
        Args:
            value: Value to set for the healthStates property.
        """
        self._health_states = value
    
    @property
    def managed_installer(self,) -> Optional[managed_installer_status.ManagedInstallerStatus]:
        """
        Gets the managedInstaller property value. ManagedInstallerStatus
        Returns: Optional[managed_installer_status.ManagedInstallerStatus]
        """
        return self._managed_installer
    
    @managed_installer.setter
    def managed_installer(self,value: Optional[managed_installer_status.ManagedInstallerStatus] = None) -> None:
        """
        Sets the managedInstaller property value. ManagedInstallerStatus
        Args:
            value: Value to set for the managedInstaller property.
        """
        self._managed_installer = value
    
    @property
    def managed_installer_configured_date_time(self,) -> Optional[str]:
        """
        Gets the managedInstallerConfiguredDateTime property value. Managed Installer Configured Date Time
        Returns: Optional[str]
        """
        return self._managed_installer_configured_date_time
    
    @managed_installer_configured_date_time.setter
    def managed_installer_configured_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the managedInstallerConfiguredDateTime property value. Managed Installer Configured Date Time
        Args:
            value: Value to set for the managedInstallerConfiguredDateTime property.
        """
        self._managed_installer_configured_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("availableVersion", self.available_version)
        writer.write_collection_of_object_values("healthStates", self.health_states)
        writer.write_enum_value("managedInstaller", self.managed_installer)
        writer.write_str_value("managedInstallerConfiguredDateTime", self.managed_installer_configured_date_time)
    

