from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_detection import Win32LobAppDetection
    from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
    from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType

from .win32_lob_app_detection import Win32LobAppDetection

@dataclass
class Win32LobAppFileSystemDetection(Win32LobAppDetection):
    """
    Contains file or folder path to detect a Win32 App
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppFileSystemDetection"
    # A value indicating whether this file or folder is for checking 32-bit app on 64-bit system
    check32_bit_on64_system: Optional[bool] = None
    # Contains all supported file system detection type.
    detection_type: Optional[Win32LobAppFileSystemDetectionType] = None
    # The file or folder detection value
    detection_value: Optional[str] = None
    # The file or folder name to detect Win32 Line of Business (LoB) app
    file_or_folder_name: Optional[str] = None
    # Contains properties for detection operator.
    operator: Optional[Win32LobAppDetectionOperator] = None
    # The file or folder path to detect Win32 Line of Business (LoB) app
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppFileSystemDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppFileSystemDetection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppFileSystemDetection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_detection import Win32LobAppDetection
        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
        from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType

        from .win32_lob_app_detection import Win32LobAppDetection
        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
        from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType

        fields: Dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "detectionType": lambda n : setattr(self, 'detection_type', n.get_enum_value(Win32LobAppFileSystemDetectionType)),
            "detectionValue": lambda n : setattr(self, 'detection_value', n.get_str_value()),
            "fileOrFolderName": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_collection_of_enum_values(Win32LobAppDetectionOperator)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_enum_value("detectionType", self.detection_type)
        writer.write_str_value("detectionValue", self.detection_value)
        writer.write_str_value("fileOrFolderName", self.file_or_folder_name)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("path", self.path)
    

