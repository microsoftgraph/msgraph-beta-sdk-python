from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_app_configuration = lazy_import('msgraph.generated.models.windows_kiosk_app_configuration')
windows_kiosk_win32_app = lazy_import('msgraph.generated.models.windows_kiosk_win32_app')

class WindowsKioskSingleWin32App(windows_kiosk_app_configuration.WindowsKioskAppConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskSingleWin32App and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskSingleWin32App"
        # The win32App property
        self._win32_app: Optional[windows_kiosk_win32_app.WindowsKioskWin32App] = None
    
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
        fields = {
            "win32_app": lambda n : setattr(self, 'win32_app', n.get_object_value(windows_kiosk_win32_app.WindowsKioskWin32App)),
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
    
    @property
    def win32_app(self,) -> Optional[windows_kiosk_win32_app.WindowsKioskWin32App]:
        """
        Gets the win32App property value. The win32App property
        Returns: Optional[windows_kiosk_win32_app.WindowsKioskWin32App]
        """
        return self._win32_app
    
    @win32_app.setter
    def win32_app(self,value: Optional[windows_kiosk_win32_app.WindowsKioskWin32App] = None) -> None:
        """
        Sets the win32App property value. The win32App property
        Args:
            value: Value to set for the win32App property.
        """
        self._win32_app = value
    

