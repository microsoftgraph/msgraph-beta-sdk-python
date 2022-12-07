from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
windows_kiosk_force_update_schedule = lazy_import('msgraph.generated.models.windows_kiosk_force_update_schedule')
windows_kiosk_profile = lazy_import('msgraph.generated.models.windows_kiosk_profile')

class WindowsKioskConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskConfiguration"
        # Enable public browsing kiosk mode for the Microsoft Edge browser. The Default is false.
        self._edge_kiosk_enable_public_browsing: Optional[bool] = None
        # Specify URLs that the kiosk browser is allowed to navigate to
        self._kiosk_browser_blocked_url_exceptions: Optional[List[str]] = None
        # Specify URLs that the kiosk browsers should not navigate to
        self._kiosk_browser_blocked_u_r_ls: Optional[List[str]] = None
        # Specify the default URL the browser should navigate to on launch.
        self._kiosk_browser_default_url: Optional[str] = None
        # Enable the kiosk browser's end session button. By default, the end session button is disabled.
        self._kiosk_browser_enable_end_session_button: Optional[bool] = None
        # Enable the kiosk browser's home button. By default, the home button is disabled.
        self._kiosk_browser_enable_home_button: Optional[bool] = None
        # Enable the kiosk browser's navigation buttons(forward/back). By default, the navigation buttons are disabled.
        self._kiosk_browser_enable_navigation_buttons: Optional[bool] = None
        # Specify the number of minutes the session is idle until the kiosk browser restarts in a fresh state.  Valid values are 1-1440. Valid values 1 to 1440
        self._kiosk_browser_restart_on_idle_time_in_minutes: Optional[int] = None
        # This policy setting allows to define a list of Kiosk profiles for a Kiosk configuration. This collection can contain a maximum of 3 elements.
        self._kiosk_profiles: Optional[List[windows_kiosk_profile.WindowsKioskProfile]] = None
        # force update schedule for Kiosk devices.
        self._windows_kiosk_force_update_schedule: Optional[windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule] = None
    
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
    
    @property
    def edge_kiosk_enable_public_browsing(self,) -> Optional[bool]:
        """
        Gets the edgeKioskEnablePublicBrowsing property value. Enable public browsing kiosk mode for the Microsoft Edge browser. The Default is false.
        Returns: Optional[bool]
        """
        return self._edge_kiosk_enable_public_browsing
    
    @edge_kiosk_enable_public_browsing.setter
    def edge_kiosk_enable_public_browsing(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeKioskEnablePublicBrowsing property value. Enable public browsing kiosk mode for the Microsoft Edge browser. The Default is false.
        Args:
            value: Value to set for the edgeKioskEnablePublicBrowsing property.
        """
        self._edge_kiosk_enable_public_browsing = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "edge_kiosk_enable_public_browsing": lambda n : setattr(self, 'edge_kiosk_enable_public_browsing', n.get_bool_value()),
            "kiosk_browser_blocked_url_exceptions": lambda n : setattr(self, 'kiosk_browser_blocked_url_exceptions', n.get_collection_of_primitive_values(str)),
            "kiosk_browser_blocked_u_r_ls": lambda n : setattr(self, 'kiosk_browser_blocked_u_r_ls', n.get_collection_of_primitive_values(str)),
            "kiosk_browser_default_url": lambda n : setattr(self, 'kiosk_browser_default_url', n.get_str_value()),
            "kiosk_browser_enable_end_session_button": lambda n : setattr(self, 'kiosk_browser_enable_end_session_button', n.get_bool_value()),
            "kiosk_browser_enable_home_button": lambda n : setattr(self, 'kiosk_browser_enable_home_button', n.get_bool_value()),
            "kiosk_browser_enable_navigation_buttons": lambda n : setattr(self, 'kiosk_browser_enable_navigation_buttons', n.get_bool_value()),
            "kiosk_browser_restart_on_idle_time_in_minutes": lambda n : setattr(self, 'kiosk_browser_restart_on_idle_time_in_minutes', n.get_int_value()),
            "kiosk_profiles": lambda n : setattr(self, 'kiosk_profiles', n.get_collection_of_object_values(windows_kiosk_profile.WindowsKioskProfile)),
            "windows_kiosk_force_update_schedule": lambda n : setattr(self, 'windows_kiosk_force_update_schedule', n.get_object_value(windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def kiosk_browser_blocked_url_exceptions(self,) -> Optional[List[str]]:
        """
        Gets the kioskBrowserBlockedUrlExceptions property value. Specify URLs that the kiosk browser is allowed to navigate to
        Returns: Optional[List[str]]
        """
        return self._kiosk_browser_blocked_url_exceptions
    
    @kiosk_browser_blocked_url_exceptions.setter
    def kiosk_browser_blocked_url_exceptions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the kioskBrowserBlockedUrlExceptions property value. Specify URLs that the kiosk browser is allowed to navigate to
        Args:
            value: Value to set for the kioskBrowserBlockedUrlExceptions property.
        """
        self._kiosk_browser_blocked_url_exceptions = value
    
    @property
    def kiosk_browser_blocked_u_r_ls(self,) -> Optional[List[str]]:
        """
        Gets the kioskBrowserBlockedURLs property value. Specify URLs that the kiosk browsers should not navigate to
        Returns: Optional[List[str]]
        """
        return self._kiosk_browser_blocked_u_r_ls
    
    @kiosk_browser_blocked_u_r_ls.setter
    def kiosk_browser_blocked_u_r_ls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the kioskBrowserBlockedURLs property value. Specify URLs that the kiosk browsers should not navigate to
        Args:
            value: Value to set for the kioskBrowserBlockedURLs property.
        """
        self._kiosk_browser_blocked_u_r_ls = value
    
    @property
    def kiosk_browser_default_url(self,) -> Optional[str]:
        """
        Gets the kioskBrowserDefaultUrl property value. Specify the default URL the browser should navigate to on launch.
        Returns: Optional[str]
        """
        return self._kiosk_browser_default_url
    
    @kiosk_browser_default_url.setter
    def kiosk_browser_default_url(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskBrowserDefaultUrl property value. Specify the default URL the browser should navigate to on launch.
        Args:
            value: Value to set for the kioskBrowserDefaultUrl property.
        """
        self._kiosk_browser_default_url = value
    
    @property
    def kiosk_browser_enable_end_session_button(self,) -> Optional[bool]:
        """
        Gets the kioskBrowserEnableEndSessionButton property value. Enable the kiosk browser's end session button. By default, the end session button is disabled.
        Returns: Optional[bool]
        """
        return self._kiosk_browser_enable_end_session_button
    
    @kiosk_browser_enable_end_session_button.setter
    def kiosk_browser_enable_end_session_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskBrowserEnableEndSessionButton property value. Enable the kiosk browser's end session button. By default, the end session button is disabled.
        Args:
            value: Value to set for the kioskBrowserEnableEndSessionButton property.
        """
        self._kiosk_browser_enable_end_session_button = value
    
    @property
    def kiosk_browser_enable_home_button(self,) -> Optional[bool]:
        """
        Gets the kioskBrowserEnableHomeButton property value. Enable the kiosk browser's home button. By default, the home button is disabled.
        Returns: Optional[bool]
        """
        return self._kiosk_browser_enable_home_button
    
    @kiosk_browser_enable_home_button.setter
    def kiosk_browser_enable_home_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskBrowserEnableHomeButton property value. Enable the kiosk browser's home button. By default, the home button is disabled.
        Args:
            value: Value to set for the kioskBrowserEnableHomeButton property.
        """
        self._kiosk_browser_enable_home_button = value
    
    @property
    def kiosk_browser_enable_navigation_buttons(self,) -> Optional[bool]:
        """
        Gets the kioskBrowserEnableNavigationButtons property value. Enable the kiosk browser's navigation buttons(forward/back). By default, the navigation buttons are disabled.
        Returns: Optional[bool]
        """
        return self._kiosk_browser_enable_navigation_buttons
    
    @kiosk_browser_enable_navigation_buttons.setter
    def kiosk_browser_enable_navigation_buttons(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskBrowserEnableNavigationButtons property value. Enable the kiosk browser's navigation buttons(forward/back). By default, the navigation buttons are disabled.
        Args:
            value: Value to set for the kioskBrowserEnableNavigationButtons property.
        """
        self._kiosk_browser_enable_navigation_buttons = value
    
    @property
    def kiosk_browser_restart_on_idle_time_in_minutes(self,) -> Optional[int]:
        """
        Gets the kioskBrowserRestartOnIdleTimeInMinutes property value. Specify the number of minutes the session is idle until the kiosk browser restarts in a fresh state.  Valid values are 1-1440. Valid values 1 to 1440
        Returns: Optional[int]
        """
        return self._kiosk_browser_restart_on_idle_time_in_minutes
    
    @kiosk_browser_restart_on_idle_time_in_minutes.setter
    def kiosk_browser_restart_on_idle_time_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the kioskBrowserRestartOnIdleTimeInMinutes property value. Specify the number of minutes the session is idle until the kiosk browser restarts in a fresh state.  Valid values are 1-1440. Valid values 1 to 1440
        Args:
            value: Value to set for the kioskBrowserRestartOnIdleTimeInMinutes property.
        """
        self._kiosk_browser_restart_on_idle_time_in_minutes = value
    
    @property
    def kiosk_profiles(self,) -> Optional[List[windows_kiosk_profile.WindowsKioskProfile]]:
        """
        Gets the kioskProfiles property value. This policy setting allows to define a list of Kiosk profiles for a Kiosk configuration. This collection can contain a maximum of 3 elements.
        Returns: Optional[List[windows_kiosk_profile.WindowsKioskProfile]]
        """
        return self._kiosk_profiles
    
    @kiosk_profiles.setter
    def kiosk_profiles(self,value: Optional[List[windows_kiosk_profile.WindowsKioskProfile]] = None) -> None:
        """
        Sets the kioskProfiles property value. This policy setting allows to define a list of Kiosk profiles for a Kiosk configuration. This collection can contain a maximum of 3 elements.
        Args:
            value: Value to set for the kioskProfiles property.
        """
        self._kiosk_profiles = value
    
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
    
    @property
    def windows_kiosk_force_update_schedule(self,) -> Optional[windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule]:
        """
        Gets the windowsKioskForceUpdateSchedule property value. force update schedule for Kiosk devices.
        Returns: Optional[windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule]
        """
        return self._windows_kiosk_force_update_schedule
    
    @windows_kiosk_force_update_schedule.setter
    def windows_kiosk_force_update_schedule(self,value: Optional[windows_kiosk_force_update_schedule.WindowsKioskForceUpdateSchedule] = None) -> None:
        """
        Sets the windowsKioskForceUpdateSchedule property value. force update schedule for Kiosk devices.
        Args:
            value: Value to set for the windowsKioskForceUpdateSchedule property.
        """
        self._windows_kiosk_force_update_schedule = value
    

