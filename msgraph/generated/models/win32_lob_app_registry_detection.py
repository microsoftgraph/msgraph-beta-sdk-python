from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import win32_lob_app_detection, win32_lob_app_detection_operator, win32_lob_app_registry_detection_type

from . import win32_lob_app_detection

@dataclass
class Win32LobAppRegistryDetection(win32_lob_app_detection.Win32LobAppDetection):
    odata_type = "#microsoft.graph.win32LobAppRegistryDetection"
    # A value indicating whether this registry path is for checking 32-bit app on 64-bit system
    check32_bit_on64_system: Optional[bool] = None
    # Contains all supported registry data detection type.
    detection_type: Optional[win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType] = None
    # The registry detection value
    detection_value: Optional[str] = None
    # The registry key path to detect Win32 Line of Business (LoB) app
    key_path: Optional[str] = None
    # Contains properties for detection operator.
    operator: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None
    # The registry value name
    value_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRegistryDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRegistryDetection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppRegistryDetection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import win32_lob_app_detection, win32_lob_app_detection_operator, win32_lob_app_registry_detection_type

        from . import win32_lob_app_detection, win32_lob_app_detection_operator, win32_lob_app_registry_detection_type

        fields: Dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "detectionType": lambda n : setattr(self, 'detection_type', n.get_enum_value(win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType)),
            "detectionValue": lambda n : setattr(self, 'detection_value', n.get_str_value()),
            "keyPath": lambda n : setattr(self, 'key_path', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_detection_operator.Win32LobAppDetectionOperator)),
            "valueName": lambda n : setattr(self, 'value_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_enum_value("detectionType", self.detection_type)
        writer.write_str_value("detectionValue", self.detection_value)
        writer.write_str_value("keyPath", self.key_path)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("valueName", self.value_name)
    

