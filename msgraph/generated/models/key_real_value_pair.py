from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import key_typed_value_pair

from . import key_typed_value_pair

class KeyRealValuePair(key_typed_value_pair.KeyTypedValuePair):
    def __init__(self,) -> None:
        """
        Instantiates a new KeyRealValuePair and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.keyRealValuePair"
        # The real (floating-point) value of the key-value pair.
        self._value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KeyRealValuePair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: KeyRealValuePair
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return KeyRealValuePair()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import key_typed_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
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
        writer.write_float_value("value", self.value)
    
    @property
    def value(self,) -> Optional[float]:
        """
        Gets the value property value. The real (floating-point) value of the key-value pair.
        Returns: Optional[float]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[float] = None) -> None:
        """
        Sets the value property value. The real (floating-point) value of the key-value pair.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

