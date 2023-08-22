from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
    from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp

from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

@dataclass
class WindowsKioskSingleUWPApp(WindowsKioskAppConfiguration):
    """
    The class used to identify the UWP app info for the kiosk configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskSingleUWPApp"
    # The uwpApp property
    uwp_app: Optional[WindowsKioskUWPApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskSingleUWPApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp

        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp

        fields: Dict[str, Callable[[Any], None]] = {
            "uwpApp": lambda n : setattr(self, 'uwp_app', n.get_object_value(WindowsKioskUWPApp)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("uwpApp", self.uwp_app)
    

