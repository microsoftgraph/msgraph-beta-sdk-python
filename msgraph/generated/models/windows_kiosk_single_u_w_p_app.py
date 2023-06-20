from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_app_configuration, windows_kiosk_u_w_p_app

from . import windows_kiosk_app_configuration

@dataclass
class WindowsKioskSingleUWPApp(windows_kiosk_app_configuration.WindowsKioskAppConfiguration):
    odata_type = "#microsoft.graph.windowsKioskSingleUWPApp"
    # The uwpApp property
    uwp_app: Optional[windows_kiosk_u_w_p_app.WindowsKioskUWPApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskSingleUWPApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskSingleUWPApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskSingleUWPApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_app_configuration, windows_kiosk_u_w_p_app

        from . import windows_kiosk_app_configuration, windows_kiosk_u_w_p_app

        fields: Dict[str, Callable[[Any], None]] = {
            "uwpApp": lambda n : setattr(self, 'uwp_app', n.get_object_value(windows_kiosk_u_w_p_app.WindowsKioskUWPApp)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("uwpApp", self.uwp_app)
    

