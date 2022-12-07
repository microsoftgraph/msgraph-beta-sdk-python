from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_app_configuration = lazy_import('msgraph.generated.models.windows_kiosk_app_configuration')
windows_kiosk_u_w_p_app = lazy_import('msgraph.generated.models.windows_kiosk_u_w_p_app')

class WindowsKioskSingleUWPApp(windows_kiosk_app_configuration.WindowsKioskAppConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskSingleUWPApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskSingleUWPApp"
        # The uwpApp property
        self._uwp_app: Optional[windows_kiosk_u_w_p_app.WindowsKioskUWPApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskSingleUWPApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskSingleUWPApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskSingleUWPApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "uwp_app": lambda n : setattr(self, 'uwp_app', n.get_object_value(windows_kiosk_u_w_p_app.WindowsKioskUWPApp)),
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
        writer.write_object_value("uwpApp", self.uwp_app)
    
    @property
    def uwp_app(self,) -> Optional[windows_kiosk_u_w_p_app.WindowsKioskUWPApp]:
        """
        Gets the uwpApp property value. The uwpApp property
        Returns: Optional[windows_kiosk_u_w_p_app.WindowsKioskUWPApp]
        """
        return self._uwp_app
    
    @uwp_app.setter
    def uwp_app(self,value: Optional[windows_kiosk_u_w_p_app.WindowsKioskUWPApp] = None) -> None:
        """
        Sets the uwpApp property value. The uwpApp property
        Args:
            value: Value to set for the uwpApp property.
        """
        self._uwp_app = value
    

