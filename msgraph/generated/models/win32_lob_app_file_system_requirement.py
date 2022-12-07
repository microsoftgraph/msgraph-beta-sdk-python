from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_file_system_detection_type = lazy_import('msgraph.generated.models.win32_lob_app_file_system_detection_type')
win32_lob_app_requirement = lazy_import('msgraph.generated.models.win32_lob_app_requirement')

class Win32LobAppFileSystemRequirement(win32_lob_app_requirement.Win32LobAppRequirement):
    @property
    def check32_bit_on64_system(self,) -> Optional[bool]:
        """
        Gets the check32BitOn64System property value. A value indicating whether this file or folder is for checking 32-bit app on 64-bit system
        Returns: Optional[bool]
        """
        return self._check32_bit_on64_system
    
    @check32_bit_on64_system.setter
    def check32_bit_on64_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the check32BitOn64System property value. A value indicating whether this file or folder is for checking 32-bit app on 64-bit system
        Args:
            value: Value to set for the check32BitOn64System property.
        """
        self._check32_bit_on64_system = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppFileSystemRequirement and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppFileSystemRequirement"
        # A value indicating whether this file or folder is for checking 32-bit app on 64-bit system
        self._check32_bit_on64_system: Optional[bool] = None
        # Contains all supported file system detection type.
        self._detection_type: Optional[win32_lob_app_file_system_detection_type.Win32LobAppFileSystemDetectionType] = None
        # The file or folder name to detect Win32 Line of Business (LoB) app
        self._file_or_folder_name: Optional[str] = None
        # The file or folder path to detect Win32 Line of Business (LoB) app
        self._path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppFileSystemRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppFileSystemRequirement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppFileSystemRequirement()
    
    @property
    def detection_type(self,) -> Optional[win32_lob_app_file_system_detection_type.Win32LobAppFileSystemDetectionType]:
        """
        Gets the detectionType property value. Contains all supported file system detection type.
        Returns: Optional[win32_lob_app_file_system_detection_type.Win32LobAppFileSystemDetectionType]
        """
        return self._detection_type
    
    @detection_type.setter
    def detection_type(self,value: Optional[win32_lob_app_file_system_detection_type.Win32LobAppFileSystemDetectionType] = None) -> None:
        """
        Sets the detectionType property value. Contains all supported file system detection type.
        Args:
            value: Value to set for the detectionType property.
        """
        self._detection_type = value
    
    @property
    def file_or_folder_name(self,) -> Optional[str]:
        """
        Gets the fileOrFolderName property value. The file or folder name to detect Win32 Line of Business (LoB) app
        Returns: Optional[str]
        """
        return self._file_or_folder_name
    
    @file_or_folder_name.setter
    def file_or_folder_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileOrFolderName property value. The file or folder name to detect Win32 Line of Business (LoB) app
        Args:
            value: Value to set for the fileOrFolderName property.
        """
        self._file_or_folder_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "check32_bit_on64_system": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "detection_type": lambda n : setattr(self, 'detection_type', n.get_enum_value(win32_lob_app_file_system_detection_type.Win32LobAppFileSystemDetectionType)),
            "file_or_folder_name": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. The file or folder path to detect Win32 Line of Business (LoB) app
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. The file or folder path to detect Win32 Line of Business (LoB) app
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_enum_value("detectionType", self.detection_type)
        writer.write_str_value("fileOrFolderName", self.file_or_folder_name)
        writer.write_str_value("path", self.path)
    

