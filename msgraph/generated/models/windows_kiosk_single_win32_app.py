from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_app_configuration, windows_kiosk_win32_app

from . import windows_kiosk_app_configuration

@dataclass
class WindowsKioskSingleWin32App(windows_kiosk_app_configuration.WindowsKioskAppConfiguration):
    odata_type = "#microsoft.graph.windowsKioskSingleWin32App"
    # The win32App property
    win32_app: Optional[windows_kiosk_win32_app.WindowsKioskWin32App] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskSingleWin32App:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskSingleWin32App
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskSingleWin32App()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_app_configuration, windows_kiosk_win32_app

        fields: Dict[str, Callable[[Any], None]] = {
            "win32App": lambda n : setattr(self, 'win32_app', n.get_object_value(windows_kiosk_win32_app.WindowsKioskWin32App)),
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
        writer.write_object_value("win32App", self.win32_app)
    

