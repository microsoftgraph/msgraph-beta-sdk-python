from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_detection = lazy_import('msgraph.generated.models.win32_lob_app_detection')
win32_lob_app_detection_operator = lazy_import('msgraph.generated.models.win32_lob_app_detection_operator')
win32_lob_app_registry_detection_type = lazy_import('msgraph.generated.models.win32_lob_app_registry_detection_type')

class Win32LobAppRegistryDetection(win32_lob_app_detection.Win32LobAppDetection):
    @property
    def check32_bit_on64_system(self,) -> Optional[bool]:
        """
        Gets the check32BitOn64System property value. A value indicating whether this registry path is for checking 32-bit app on 64-bit system
        Returns: Optional[bool]
        """
        return self._check32_bit_on64_system
    
    @check32_bit_on64_system.setter
    def check32_bit_on64_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the check32BitOn64System property value. A value indicating whether this registry path is for checking 32-bit app on 64-bit system
        Args:
            value: Value to set for the check32BitOn64System property.
        """
        self._check32_bit_on64_system = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppRegistryDetection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppRegistryDetection"
        # A value indicating whether this registry path is for checking 32-bit app on 64-bit system
        self._check32_bit_on64_system: Optional[bool] = None
        # Contains all supported registry data detection type.
        self._detection_type: Optional[win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType] = None
        # The registry detection value
        self._detection_value: Optional[str] = None
        # The registry key path to detect Win32 Line of Business (LoB) app
        self._key_path: Optional[str] = None
        # Contains properties for detection operator.
        self._operator: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None
        # The registry value name
        self._value_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRegistryDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRegistryDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppRegistryDetection()
    
    @property
    def detection_type(self,) -> Optional[win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType]:
        """
        Gets the detectionType property value. Contains all supported registry data detection type.
        Returns: Optional[win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType]
        """
        return self._detection_type
    
    @detection_type.setter
    def detection_type(self,value: Optional[win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType] = None) -> None:
        """
        Sets the detectionType property value. Contains all supported registry data detection type.
        Args:
            value: Value to set for the detectionType property.
        """
        self._detection_type = value
    
    @property
    def detection_value(self,) -> Optional[str]:
        """
        Gets the detectionValue property value. The registry detection value
        Returns: Optional[str]
        """
        return self._detection_value
    
    @detection_value.setter
    def detection_value(self,value: Optional[str] = None) -> None:
        """
        Sets the detectionValue property value. The registry detection value
        Args:
            value: Value to set for the detectionValue property.
        """
        self._detection_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "check32_bit_on64_system": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "detection_type": lambda n : setattr(self, 'detection_type', n.get_enum_value(win32_lob_app_registry_detection_type.Win32LobAppRegistryDetectionType)),
            "detection_value": lambda n : setattr(self, 'detection_value', n.get_str_value()),
            "key_path": lambda n : setattr(self, 'key_path', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_detection_operator.Win32LobAppDetectionOperator)),
            "value_name": lambda n : setattr(self, 'value_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_path(self,) -> Optional[str]:
        """
        Gets the keyPath property value. The registry key path to detect Win32 Line of Business (LoB) app
        Returns: Optional[str]
        """
        return self._key_path
    
    @key_path.setter
    def key_path(self,value: Optional[str] = None) -> None:
        """
        Sets the keyPath property value. The registry key path to detect Win32 Line of Business (LoB) app
        Args:
            value: Value to set for the keyPath property.
        """
        self._key_path = value
    
    @property
    def operator(self,) -> Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]:
        """
        Gets the operator property value. Contains properties for detection operator.
        Returns: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None) -> None:
        """
        Sets the operator property value. Contains properties for detection operator.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
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
        writer.write_str_value("detectionValue", self.detection_value)
        writer.write_str_value("keyPath", self.key_path)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("valueName", self.value_name)
    
    @property
    def value_name(self,) -> Optional[str]:
        """
        Gets the valueName property value. The registry value name
        Returns: Optional[str]
        """
        return self._value_name
    
    @value_name.setter
    def value_name(self,value: Optional[str] = None) -> None:
        """
        Sets the valueName property value. The registry value name
        Args:
            value: Value to set for the valueName property.
        """
        self._value_name = value
    

