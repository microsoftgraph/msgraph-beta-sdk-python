from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_health_script_parameter

from . import device_health_script_parameter

class DeviceHealthScriptIntegerParameter(device_health_script_parameter.DeviceHealthScriptParameter):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceHealthScriptIntegerParameter and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceHealthScriptIntegerParameter"
        # The default value of Integer param. Valid values -2147483648 to 2147483647
        self._default_value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptIntegerParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptIntegerParameter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthScriptIntegerParameter()
    
    @property
    def default_value(self,) -> Optional[int]:
        """
        Gets the defaultValue property value. The default value of Integer param. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultValue property value. The default value of Integer param. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the default_value property.
        """
        self._default_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_health_script_parameter

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_int_value()),
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
        writer.write_int_value("defaultValue", self.default_value)
    

