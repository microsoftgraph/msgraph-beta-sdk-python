from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_health_script_parameter = lazy_import('msgraph.generated.models.device_health_script_parameter')

class DeviceHealthScriptStringParameter(device_health_script_parameter.DeviceHealthScriptParameter):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceHealthScriptStringParameter and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceHealthScriptStringParameter"
        # The default value of string param
        self._default_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptStringParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptStringParameter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptStringParameter()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. The default value of string param
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. The default value of string param
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_str_value()),
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
        writer.write_str_value("defaultValue", self.default_value)
    

