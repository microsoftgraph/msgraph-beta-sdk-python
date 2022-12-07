from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_home_screen_item = lazy_import('msgraph.generated.models.ios_home_screen_item')

class IosHomeScreenApp(ios_home_screen_item.IosHomeScreenItem):
    @property
    def bundle_i_d(self,) -> Optional[str]:
        """
        Gets the bundleID property value. BundleID of the app if isWebClip is false or the URL of a web clip if isWebClip is true.
        Returns: Optional[str]
        """
        return self._bundle_i_d
    
    @bundle_i_d.setter
    def bundle_i_d(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleID property value. BundleID of the app if isWebClip is false or the URL of a web clip if isWebClip is true.
        Args:
            value: Value to set for the bundleID property.
        """
        self._bundle_i_d = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosHomeScreenApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosHomeScreenApp"
        # BundleID of the app if isWebClip is false or the URL of a web clip if isWebClip is true.
        self._bundle_i_d: Optional[str] = None
        # When true, the bundle ID will be handled as a URL for a web clip.
        self._is_web_clip: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosHomeScreenApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosHomeScreenApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bundle_i_d": lambda n : setattr(self, 'bundle_i_d', n.get_str_value()),
            "is_web_clip": lambda n : setattr(self, 'is_web_clip', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_web_clip(self,) -> Optional[bool]:
        """
        Gets the isWebClip property value. When true, the bundle ID will be handled as a URL for a web clip.
        Returns: Optional[bool]
        """
        return self._is_web_clip
    
    @is_web_clip.setter
    def is_web_clip(self,value: Optional[bool] = None) -> None:
        """
        Sets the isWebClip property value. When true, the bundle ID will be handled as a URL for a web clip.
        Args:
            value: Value to set for the isWebClip property.
        """
        self._is_web_clip = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("bundleID", self.bundle_i_d)
        writer.write_bool_value("isWebClip", self.is_web_clip)
    

