from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_app_base

from . import windows_kiosk_app_base

class WindowsKioskUWPApp(windows_kiosk_app_base.WindowsKioskAppBase):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskUWPApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskUWPApp"
        # This references an Intune App that will be target to the same assignments as Kiosk configuration
        self._app_id: Optional[str] = None
        # This is the only Application User Model ID (AUMID) that will be available to launch use while in Kiosk Mode
        self._app_user_model_id: Optional[str] = None
        # This references an contained App from an Intune App
        self._contained_app_id: Optional[str] = None
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. This references an Intune App that will be target to the same assignments as Kiosk configuration
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. This references an Intune App that will be target to the same assignments as Kiosk configuration
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @property
    def app_user_model_id(self,) -> Optional[str]:
        """
        Gets the appUserModelId property value. This is the only Application User Model ID (AUMID) that will be available to launch use while in Kiosk Mode
        Returns: Optional[str]
        """
        return self._app_user_model_id
    
    @app_user_model_id.setter
    def app_user_model_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appUserModelId property value. This is the only Application User Model ID (AUMID) that will be available to launch use while in Kiosk Mode
        Args:
            value: Value to set for the app_user_model_id property.
        """
        self._app_user_model_id = value
    
    @property
    def contained_app_id(self,) -> Optional[str]:
        """
        Gets the containedAppId property value. This references an contained App from an Intune App
        Returns: Optional[str]
        """
        return self._contained_app_id
    
    @contained_app_id.setter
    def contained_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the containedAppId property value. This references an contained App from an Intune App
        Args:
            value: Value to set for the contained_app_id property.
        """
        self._contained_app_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskUWPApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskUWPApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskUWPApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_app_base

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appUserModelId": lambda n : setattr(self, 'app_user_model_id', n.get_str_value()),
            "containedAppId": lambda n : setattr(self, 'contained_app_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appUserModelId", self.app_user_model_id)
        writer.write_str_value("containedAppId", self.contained_app_id)
    

