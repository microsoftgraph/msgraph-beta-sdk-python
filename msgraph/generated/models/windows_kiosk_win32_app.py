from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_edge_kiosk_type = lazy_import('msgraph.generated.models.windows_edge_kiosk_type')
windows_kiosk_app_base = lazy_import('msgraph.generated.models.windows_kiosk_app_base')

class WindowsKioskWin32App(windows_kiosk_app_base.WindowsKioskAppBase):
    @property
    def classic_app_path(self,) -> Optional[str]:
        """
        Gets the classicAppPath property value. This is the classicapppath to be used by v4 Win32 app while in Kiosk Mode
        Returns: Optional[str]
        """
        return self._classic_app_path
    
    @classic_app_path.setter
    def classic_app_path(self,value: Optional[str] = None) -> None:
        """
        Sets the classicAppPath property value. This is the classicapppath to be used by v4 Win32 app while in Kiosk Mode
        Args:
            value: Value to set for the classicAppPath property.
        """
        self._classic_app_path = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskWin32App and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskWin32App"
        # This is the classicapppath to be used by v4 Win32 app while in Kiosk Mode
        self._classic_app_path: Optional[str] = None
        # Edge kiosk (url) for Edge kiosk mode
        self._edge_kiosk: Optional[str] = None
        # Edge kiosk idle timeout in minutes for Edge kiosk mode. Valid values 0 to 1440
        self._edge_kiosk_idle_timeout_minutes: Optional[int] = None
        # Edge kiosk type
        self._edge_kiosk_type: Optional[windows_edge_kiosk_type.WindowsEdgeKioskType] = None
        # Edge first run flag for Edge kiosk mode
        self._edge_no_first_run: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskWin32App:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskWin32App
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskWin32App()
    
    @property
    def edge_kiosk(self,) -> Optional[str]:
        """
        Gets the edgeKiosk property value. Edge kiosk (url) for Edge kiosk mode
        Returns: Optional[str]
        """
        return self._edge_kiosk
    
    @edge_kiosk.setter
    def edge_kiosk(self,value: Optional[str] = None) -> None:
        """
        Sets the edgeKiosk property value. Edge kiosk (url) for Edge kiosk mode
        Args:
            value: Value to set for the edgeKiosk property.
        """
        self._edge_kiosk = value
    
    @property
    def edge_kiosk_idle_timeout_minutes(self,) -> Optional[int]:
        """
        Gets the edgeKioskIdleTimeoutMinutes property value. Edge kiosk idle timeout in minutes for Edge kiosk mode. Valid values 0 to 1440
        Returns: Optional[int]
        """
        return self._edge_kiosk_idle_timeout_minutes
    
    @edge_kiosk_idle_timeout_minutes.setter
    def edge_kiosk_idle_timeout_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the edgeKioskIdleTimeoutMinutes property value. Edge kiosk idle timeout in minutes for Edge kiosk mode. Valid values 0 to 1440
        Args:
            value: Value to set for the edgeKioskIdleTimeoutMinutes property.
        """
        self._edge_kiosk_idle_timeout_minutes = value
    
    @property
    def edge_kiosk_type(self,) -> Optional[windows_edge_kiosk_type.WindowsEdgeKioskType]:
        """
        Gets the edgeKioskType property value. Edge kiosk type
        Returns: Optional[windows_edge_kiosk_type.WindowsEdgeKioskType]
        """
        return self._edge_kiosk_type
    
    @edge_kiosk_type.setter
    def edge_kiosk_type(self,value: Optional[windows_edge_kiosk_type.WindowsEdgeKioskType] = None) -> None:
        """
        Sets the edgeKioskType property value. Edge kiosk type
        Args:
            value: Value to set for the edgeKioskType property.
        """
        self._edge_kiosk_type = value
    
    @property
    def edge_no_first_run(self,) -> Optional[bool]:
        """
        Gets the edgeNoFirstRun property value. Edge first run flag for Edge kiosk mode
        Returns: Optional[bool]
        """
        return self._edge_no_first_run
    
    @edge_no_first_run.setter
    def edge_no_first_run(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeNoFirstRun property value. Edge first run flag for Edge kiosk mode
        Args:
            value: Value to set for the edgeNoFirstRun property.
        """
        self._edge_no_first_run = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classic_app_path": lambda n : setattr(self, 'classic_app_path', n.get_str_value()),
            "edge_kiosk": lambda n : setattr(self, 'edge_kiosk', n.get_str_value()),
            "edge_kiosk_idle_timeout_minutes": lambda n : setattr(self, 'edge_kiosk_idle_timeout_minutes', n.get_int_value()),
            "edge_kiosk_type": lambda n : setattr(self, 'edge_kiosk_type', n.get_enum_value(windows_edge_kiosk_type.WindowsEdgeKioskType)),
            "edge_no_first_run": lambda n : setattr(self, 'edge_no_first_run', n.get_bool_value()),
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
        writer.write_str_value("classicAppPath", self.classic_app_path)
        writer.write_str_value("edgeKiosk", self.edge_kiosk)
        writer.write_int_value("edgeKioskIdleTimeoutMinutes", self.edge_kiosk_idle_timeout_minutes)
        writer.write_enum_value("edgeKioskType", self.edge_kiosk_type)
        writer.write_bool_value("edgeNoFirstRun", self.edge_no_first_run)
    

