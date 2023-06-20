from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_app_start_layout_tile_size, windows_kiosk_app_type, windows_kiosk_desktop_app, windows_kiosk_u_w_p_app, windows_kiosk_win32_app

@dataclass
class WindowsKioskAppBase(AdditionalDataHolder, Parsable):
    """
    The base class for a type of apps
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The type of Windows kiosk app.
    app_type: Optional[windows_kiosk_app_type.WindowsKioskAppType] = None
    # Allow the app to be auto-launched in multi-app kiosk mode
    auto_launch: Optional[bool] = None
    # Represents the friendly name of an app
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tile size of Windows app in the start layout.
    start_layout_tile_size: Optional[windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskAppBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAppBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskDesktopApp".casefold():
            from . import windows_kiosk_desktop_app

            return windows_kiosk_desktop_app.WindowsKioskDesktopApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskUWPApp".casefold():
            from . import windows_kiosk_u_w_p_app

            return windows_kiosk_u_w_p_app.WindowsKioskUWPApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskWin32App".casefold():
            from . import windows_kiosk_win32_app

            return windows_kiosk_win32_app.WindowsKioskWin32App()
        return WindowsKioskAppBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_app_start_layout_tile_size, windows_kiosk_app_type, windows_kiosk_desktop_app, windows_kiosk_u_w_p_app, windows_kiosk_win32_app

        from . import windows_app_start_layout_tile_size, windows_kiosk_app_type, windows_kiosk_desktop_app, windows_kiosk_u_w_p_app, windows_kiosk_win32_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appType": lambda n : setattr(self, 'app_type', n.get_enum_value(windows_kiosk_app_type.WindowsKioskAppType)),
            "autoLaunch": lambda n : setattr(self, 'auto_launch', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startLayoutTileSize": lambda n : setattr(self, 'start_layout_tile_size', n.get_enum_value(windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("appType", self.app_type)
        writer.write_bool_value("autoLaunch", self.auto_launch)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("startLayoutTileSize", self.start_layout_tile_size)
        writer.write_additional_data_value(self.additional_data)
    

