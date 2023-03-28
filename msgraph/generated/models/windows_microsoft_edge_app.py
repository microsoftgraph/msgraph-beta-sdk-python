from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import microsoft_edge_channel, mobile_app

from . import mobile_app

class WindowsMicrosoftEdgeApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsMicrosoftEdgeApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsMicrosoftEdgeApp"
        # The enum to specify the channels for Microsoft Edge apps.
        self._channel: Optional[microsoft_edge_channel.MicrosoftEdgeChannel] = None
        # The language locale to use when the Edge app displays text to the user.
        self._display_language_locale: Optional[str] = None
    
    @property
    def channel(self,) -> Optional[microsoft_edge_channel.MicrosoftEdgeChannel]:
        """
        Gets the channel property value. The enum to specify the channels for Microsoft Edge apps.
        Returns: Optional[microsoft_edge_channel.MicrosoftEdgeChannel]
        """
        return self._channel
    
    @channel.setter
    def channel(self,value: Optional[microsoft_edge_channel.MicrosoftEdgeChannel] = None) -> None:
        """
        Sets the channel property value. The enum to specify the channels for Microsoft Edge apps.
        Args:
            value: Value to set for the channel property.
        """
        self._channel = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsMicrosoftEdgeApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMicrosoftEdgeApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsMicrosoftEdgeApp()
    
    @property
    def display_language_locale(self,) -> Optional[str]:
        """
        Gets the displayLanguageLocale property value. The language locale to use when the Edge app displays text to the user.
        Returns: Optional[str]
        """
        return self._display_language_locale
    
    @display_language_locale.setter
    def display_language_locale(self,value: Optional[str] = None) -> None:
        """
        Sets the displayLanguageLocale property value. The language locale to use when the Edge app displays text to the user.
        Args:
            value: Value to set for the display_language_locale property.
        """
        self._display_language_locale = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import microsoft_edge_channel, mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(microsoft_edge_channel.MicrosoftEdgeChannel)),
            "displayLanguageLocale": lambda n : setattr(self, 'display_language_locale', n.get_str_value()),
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
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("displayLanguageLocale", self.display_language_locale)
    

