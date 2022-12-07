from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_app_start_layout_tile_size = lazy_import('msgraph.generated.models.windows_app_start_layout_tile_size')
windows_kiosk_app_type = lazy_import('msgraph.generated.models.windows_kiosk_app_type')

class WindowsKioskAppBase(AdditionalDataHolder, Parsable):
    """
    The base class for a type of apps
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app_type(self,) -> Optional[windows_kiosk_app_type.WindowsKioskAppType]:
        """
        Gets the appType property value. The type of Windows kiosk app.
        Returns: Optional[windows_kiosk_app_type.WindowsKioskAppType]
        """
        return self._app_type
    
    @app_type.setter
    def app_type(self,value: Optional[windows_kiosk_app_type.WindowsKioskAppType] = None) -> None:
        """
        Sets the appType property value. The type of Windows kiosk app.
        Args:
            value: Value to set for the appType property.
        """
        self._app_type = value
    
    @property
    def auto_launch(self,) -> Optional[bool]:
        """
        Gets the autoLaunch property value. Allow the app to be auto-launched in multi-app kiosk mode
        Returns: Optional[bool]
        """
        return self._auto_launch
    
    @auto_launch.setter
    def auto_launch(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoLaunch property value. Allow the app to be auto-launched in multi-app kiosk mode
        Args:
            value: Value to set for the autoLaunch property.
        """
        self._auto_launch = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsKioskAppBase and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of Windows kiosk app.
        self._app_type: Optional[windows_kiosk_app_type.WindowsKioskAppType] = None
        # Allow the app to be auto-launched in multi-app kiosk mode
        self._auto_launch: Optional[bool] = None
        # Represents the friendly name of an app
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tile size of Windows app in the start layout.
        self._start_layout_tile_size: Optional[windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskAppBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAppBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskAppBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_type": lambda n : setattr(self, 'app_type', n.get_enum_value(windows_kiosk_app_type.WindowsKioskAppType)),
            "auto_launch": lambda n : setattr(self, 'auto_launch', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_layout_tile_size": lambda n : setattr(self, 'start_layout_tile_size', n.get_enum_value(windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Represents the friendly name of an app
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Represents the friendly name of an app
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("appType", self.app_type)
        writer.write_bool_value("autoLaunch", self.auto_launch)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("startLayoutTileSize", self.start_layout_tile_size)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_layout_tile_size(self,) -> Optional[windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize]:
        """
        Gets the startLayoutTileSize property value. The tile size of Windows app in the start layout.
        Returns: Optional[windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize]
        """
        return self._start_layout_tile_size
    
    @start_layout_tile_size.setter
    def start_layout_tile_size(self,value: Optional[windows_app_start_layout_tile_size.WindowsAppStartLayoutTileSize] = None) -> None:
        """
        Sets the startLayoutTileSize property value. The tile size of Windows app in the start layout.
        Args:
            value: Value to set for the startLayoutTileSize property.
        """
        self._start_layout_tile_size = value
    

