from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, windows_kiosk_force_update_schedule, windows_kiosk_profile

from . import device_configuration

@dataclass
class WindowsKioskConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.windowsKioskConfiguration"
    # Enable public browsing kiosk mode for the Microsoft Edge browser. The Default is false.
    edge_kiosk_enable_public_browsing: Optional[bool] = None
    # Specify URLs that the kiosk browsers should not navigate to
    kiosk_browser_blocked_u_r_ls: Optional[List[str]] = None
    # Specify URLs that the kiosk browser is allowed to navigate to
    kiosk_browser_blocked_url_exceptions: Optional[List[str]] = None
    # Specify the default URL the browser should navigate to on launch.
    kiosk_browser_default_url: Optional[str] = None
    # Enable the kiosk browser's end session button. By default, the end session button is disabled.
    kiosk_browser_enable_end_session_button: Optional[bool] = None
    # Enable the kiosk browser's home button. By default, the home button is disabled.
    kiosk_browser_enable_home_button: Optional[bool] = None
    # Enable the kiosk browser's navigation buttons(forward/back). By default, the navigation buttons are disabled.
    kiosk_browser_enable_navigation_buttons: Optional[bool] = None
    # Specify the number of minutes the session is idle until the kiosk browser restarts in a fresh state.  Valid values are 1-1440. Valid values 1 to 1440
    kiosk_browser_restart_on_idle_time_in_minutes: Optional[int] = None
    # This policy setting allows to define a list of Kiosk profiles for a Kiosk configuration. This collection can contain a maximum of 3 elements.
    kiosk_profiles: Optional[List[windows_kiosk_profile.WindowsKioskProfile]] = None
    # force update schedule for Kiosk devices.
    windows_kiosk_force_update_schedule: Optional[windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, windows_kiosk_force_update_schedule, windows_kiosk_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "edgeKioskEnablePublicBrowsing": lambda n : setattr(self, 'edge_kiosk_enable_public_browsing', n.get_bool_value()),
            "kioskBrowserBlockedUrlExceptions": lambda n : setattr(self, 'kiosk_browser_blocked_url_exceptions', n.get_collection_of_primitive_values(str)),
            "kioskBrowserBlockedURLs": lambda n : setattr(self, 'kiosk_browser_blocked_u_r_ls', n.get_collection_of_primitive_values(str)),
            "kioskBrowserDefaultUrl": lambda n : setattr(self, 'kiosk_browser_default_url', n.get_str_value()),
            "kioskBrowserEnableEndSessionButton": lambda n : setattr(self, 'kiosk_browser_enable_end_session_button', n.get_bool_value()),
            "kioskBrowserEnableHomeButton": lambda n : setattr(self, 'kiosk_browser_enable_home_button', n.get_bool_value()),
            "kioskBrowserEnableNavigationButtons": lambda n : setattr(self, 'kiosk_browser_enable_navigation_buttons', n.get_bool_value()),
            "kioskBrowserRestartOnIdleTimeInMinutes": lambda n : setattr(self, 'kiosk_browser_restart_on_idle_time_in_minutes', n.get_int_value()),
            "kioskProfiles": lambda n : setattr(self, 'kiosk_profiles', n.get_collection_of_object_values(windows_kiosk_profile.WindowsKioskProfile)),
            "windowsKioskForceUpdateSchedule": lambda n : setattr(self, 'windows_kiosk_force_update_schedule', n.get_object_value(windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule)),
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
        writer.write_bool_value("edgeKioskEnablePublicBrowsing", self.edge_kiosk_enable_public_browsing)
        writer.write_collection_of_primitive_values("kioskBrowserBlockedUrlExceptions", self.kiosk_browser_blocked_url_exceptions)
        writer.write_collection_of_primitive_values("kioskBrowserBlockedURLs", self.kiosk_browser_blocked_u_r_ls)
        writer.write_str_value("kioskBrowserDefaultUrl", self.kiosk_browser_default_url)
        writer.write_bool_value("kioskBrowserEnableEndSessionButton", self.kiosk_browser_enable_end_session_button)
        writer.write_bool_value("kioskBrowserEnableHomeButton", self.kiosk_browser_enable_home_button)
        writer.write_bool_value("kioskBrowserEnableNavigationButtons", self.kiosk_browser_enable_navigation_buttons)
        writer.write_int_value("kioskBrowserRestartOnIdleTimeInMinutes", self.kiosk_browser_restart_on_idle_time_in_minutes)
        writer.write_collection_of_object_values("kioskProfiles", self.kiosk_profiles)
        writer.write_object_value("windowsKioskForceUpdateSchedule", self.windows_kiosk_force_update_schedule)
    

