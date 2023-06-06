from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, managed_installer_status, windows_management_app_health_state

from . import entity

@dataclass
class WindowsManagementApp(entity.Entity):
    # Windows management app available version.
    available_version: Optional[str] = None
    # The list of health states for installed Windows management app.
    health_states: Optional[List[windows_management_app_health_state.WindowsManagementAppHealthState]] = None
    # ManagedInstallerStatus
    managed_installer: Optional[managed_installer_status.ManagedInstallerStatus] = None
    # Managed Installer Configured Date Time
    managed_installer_configured_date_time: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
        from . import entity, managed_installer_status, windows_management_app_health_state

        fields: Dict[str, Callable[[Any], None]] = {
            "availableVersion": lambda n : setattr(self, 'available_version', n.get_str_value()),
            "healthStates": lambda n : setattr(self, 'health_states', n.get_collection_of_object_values(windows_management_app_health_state.WindowsManagementAppHealthState)),
            "managedInstaller": lambda n : setattr(self, 'managed_installer', n.get_enum_value(managed_installer_status.ManagedInstallerStatus)),
            "managedInstallerConfiguredDateTime": lambda n : setattr(self, 'managed_installer_configured_date_time', n.get_str_value()),
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
        writer.write_str_value("availableVersion", self.available_version)
        writer.write_collection_of_object_values("healthStates", self.health_states)
        writer.write_enum_value("managedInstaller", self.managed_installer)
        writer.write_str_value("managedInstallerConfiguredDateTime", self.managed_installer_configured_date_time)
    

