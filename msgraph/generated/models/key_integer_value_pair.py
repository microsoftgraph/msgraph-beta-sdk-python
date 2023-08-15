from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_typed_value_pair import KeyTypedValuePair

from .key_typed_value_pair import KeyTypedValuePair

@dataclass
class KeyIntegerValuePair(KeyTypedValuePair):
    """
    A key-value pair with a string key and an integer value.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.keyIntegerValuePair"
    # The integer value of the key-value pair.
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KeyIntegerValuePair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyIntegerValuePair
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return KeyIntegerValuePair()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_typed_value_pair import KeyTypedValuePair

        from .key_typed_value_pair import KeyTypedValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_int_value("value", self.value)
    

