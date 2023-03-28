from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app

from . import mobile_app

class WindowsPhone81StoreApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhone81StoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81StoreApp"
        # The Windows Phone 8.1 app store URL.
        self._app_store_url: Optional[str] = None
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Windows Phone 8.1 app store URL.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Windows Phone 8.1 app store URL.
        Args:
            value: Value to set for the app_store_url property.
        """
        self._app_store_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81StoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81StoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81StoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
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
        writer.write_str_value("appStoreUrl", self.app_store_url)
    

