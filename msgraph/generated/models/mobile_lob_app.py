from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_lob_app, ios_lob_app, mac_o_s_dmg_app, mac_o_s_lob_app, mobile_app, mobile_app_content, win32_lob_app, windows_app_x, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone_x_a_p, windows_universal_app_x

from . import mobile_app

class MobileLobApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileLobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mobileLobApp"
        # The internal committed content version.
        self._committed_content_version: Optional[str] = None
        # The list of content versions for this app.
        self._content_versions: Optional[List[mobile_app_content.MobileAppContent]] = None
        # The name of the main Lob application file.
        self._file_name: Optional[str] = None
        # The total size, including all uploaded files.
        self._size: Optional[int] = None
    
    @property
    def committed_content_version(self,) -> Optional[str]:
        """
        Gets the committedContentVersion property value. The internal committed content version.
        Returns: Optional[str]
        """
        return self._committed_content_version
    
    @committed_content_version.setter
    def committed_content_version(self,value: Optional[str] = None) -> None:
        """
        Sets the committedContentVersion property value. The internal committed content version.
        Args:
            value: Value to set for the committed_content_version property.
        """
        self._committed_content_version = value
    
    @property
    def content_versions(self,) -> Optional[List[mobile_app_content.MobileAppContent]]:
        """
        Gets the contentVersions property value. The list of content versions for this app.
        Returns: Optional[List[mobile_app_content.MobileAppContent]]
        """
        return self._content_versions
    
    @content_versions.setter
    def content_versions(self,value: Optional[List[mobile_app_content.MobileAppContent]] = None) -> None:
        """
        Sets the contentVersions property value. The list of content versions for this app.
        Args:
            value: Value to set for the content_versions property.
        """
        self._content_versions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileLobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidLobApp":
                from . import android_lob_app

                return android_lob_app.AndroidLobApp()
            if mapping_value == "#microsoft.graph.iosLobApp":
                from . import ios_lob_app

                return ios_lob_app.IosLobApp()
            if mapping_value == "#microsoft.graph.macOSDmgApp":
                from . import mac_o_s_dmg_app

                return mac_o_s_dmg_app.MacOSDmgApp()
            if mapping_value == "#microsoft.graph.macOSLobApp":
                from . import mac_o_s_lob_app

                return mac_o_s_lob_app.MacOSLobApp()
            if mapping_value == "#microsoft.graph.win32LobApp":
                from . import win32_lob_app

                return win32_lob_app.Win32LobApp()
            if mapping_value == "#microsoft.graph.windowsAppX":
                from . import windows_app_x

                return windows_app_x.WindowsAppX()
            if mapping_value == "#microsoft.graph.windowsMobileMSI":
                from . import windows_mobile_m_s_i

                return windows_mobile_m_s_i.WindowsMobileMSI()
            if mapping_value == "#microsoft.graph.windowsPhone81AppX":
                from . import windows_phone81_app_x

                return windows_phone81_app_x.WindowsPhone81AppX()
            if mapping_value == "#microsoft.graph.windowsPhone81AppXBundle":
                from . import windows_phone81_app_x_bundle

                return windows_phone81_app_x_bundle.WindowsPhone81AppXBundle()
            if mapping_value == "#microsoft.graph.windowsPhoneXAP":
                from . import windows_phone_x_a_p

                return windows_phone_x_a_p.WindowsPhoneXAP()
            if mapping_value == "#microsoft.graph.windowsUniversalAppX":
                from . import windows_universal_app_x

                return windows_universal_app_x.WindowsUniversalAppX()
        return MobileLobApp()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The name of the main Lob application file.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The name of the main Lob application file.
        Args:
            value: Value to set for the file_name property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_lob_app, ios_lob_app, mac_o_s_dmg_app, mac_o_s_lob_app, mobile_app, mobile_app_content, win32_lob_app, windows_app_x, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone_x_a_p, windows_universal_app_x

        fields: Dict[str, Callable[[Any], None]] = {
            "committedContentVersion": lambda n : setattr(self, 'committed_content_version', n.get_str_value()),
            "contentVersions": lambda n : setattr(self, 'content_versions', n.get_collection_of_object_values(mobile_app_content.MobileAppContent)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("committedContentVersion", self.committed_content_version)
        writer.write_collection_of_object_values("contentVersions", self.content_versions)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("size", self.size)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The total size, including all uploaded files.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The total size, including all uploaded files.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

