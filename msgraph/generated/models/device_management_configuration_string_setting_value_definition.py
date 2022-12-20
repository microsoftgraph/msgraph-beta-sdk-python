from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_value_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_value_definition')
device_management_configuration_string_format = lazy_import('msgraph.generated.models.device_management_configuration_string_format')

class DeviceManagementConfigurationStringSettingValueDefinition(device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationStringSettingValueDefinition and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationStringSettingValueDefinition"
        # Supported file types for this setting.
        self._file_types: Optional[List[str]] = None
        # The format property
        self._format: Optional[device_management_configuration_string_format.DeviceManagementConfigurationStringFormat] = None
        # Regular expression or any xml or json schema that the input string should match
        self._input_validation_schema: Optional[str] = None
        # Specifies whether the setting needs to be treated as a secret. Settings marked as yes will be encrypted in transit and at rest and will be displayed as asterisks when represented in the UX.
        self._is_secret: Optional[bool] = None
        # Maximum length of string
        self._maximum_length: Optional[int] = None
        # Minimum length of string
        self._minimum_length: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationStringSettingValueDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValueDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationStringSettingValueDefinition()
    
    @property
    def file_types(self,) -> Optional[List[str]]:
        """
        Gets the fileTypes property value. Supported file types for this setting.
        Returns: Optional[List[str]]
        """
        return self._file_types
    
    @file_types.setter
    def file_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fileTypes property value. Supported file types for this setting.
        Args:
            value: Value to set for the fileTypes property.
        """
        self._file_types = value
    
    @property
    def format(self,) -> Optional[device_management_configuration_string_format.DeviceManagementConfigurationStringFormat]:
        """
        Gets the format property value. The format property
        Returns: Optional[device_management_configuration_string_format.DeviceManagementConfigurationStringFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[device_management_configuration_string_format.DeviceManagementConfigurationStringFormat] = None) -> None:
        """
        Sets the format property value. The format property
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_types": lambda n : setattr(self, 'file_types', n.get_collection_of_primitive_values(str)),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(device_management_configuration_string_format.DeviceManagementConfigurationStringFormat)),
            "input_validation_schema": lambda n : setattr(self, 'input_validation_schema', n.get_str_value()),
            "is_secret": lambda n : setattr(self, 'is_secret', n.get_bool_value()),
            "maximum_length": lambda n : setattr(self, 'maximum_length', n.get_int_value()),
            "minimum_length": lambda n : setattr(self, 'minimum_length', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def input_validation_schema(self,) -> Optional[str]:
        """
        Gets the inputValidationSchema property value. Regular expression or any xml or json schema that the input string should match
        Returns: Optional[str]
        """
        return self._input_validation_schema
    
    @input_validation_schema.setter
    def input_validation_schema(self,value: Optional[str] = None) -> None:
        """
        Sets the inputValidationSchema property value. Regular expression or any xml or json schema that the input string should match
        Args:
            value: Value to set for the inputValidationSchema property.
        """
        self._input_validation_schema = value
    
    @property
    def is_secret(self,) -> Optional[bool]:
        """
        Gets the isSecret property value. Specifies whether the setting needs to be treated as a secret. Settings marked as yes will be encrypted in transit and at rest and will be displayed as asterisks when represented in the UX.
        Returns: Optional[bool]
        """
        return self._is_secret
    
    @is_secret.setter
    def is_secret(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSecret property value. Specifies whether the setting needs to be treated as a secret. Settings marked as yes will be encrypted in transit and at rest and will be displayed as asterisks when represented in the UX.
        Args:
            value: Value to set for the isSecret property.
        """
        self._is_secret = value
    
    @property
    def maximum_length(self,) -> Optional[int]:
        """
        Gets the maximumLength property value. Maximum length of string
        Returns: Optional[int]
        """
        return self._maximum_length
    
    @maximum_length.setter
    def maximum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumLength property value. Maximum length of string
        Args:
            value: Value to set for the maximumLength property.
        """
        self._maximum_length = value
    
    @property
    def minimum_length(self,) -> Optional[int]:
        """
        Gets the minimumLength property value. Minimum length of string
        Returns: Optional[int]
        """
        return self._minimum_length
    
    @minimum_length.setter
    def minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumLength property value. Minimum length of string
        Args:
            value: Value to set for the minimumLength property.
        """
        self._minimum_length = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("fileTypes", self.file_types)
        writer.write_enum_value("format", self.format)
        writer.write_str_value("inputValidationSchema", self.input_validation_schema)
        writer.write_bool_value("isSecret", self.is_secret)
        writer.write_int_value("maximumLength", self.maximum_length)
        writer.write_int_value("minimumLength", self.minimum_length)
    

