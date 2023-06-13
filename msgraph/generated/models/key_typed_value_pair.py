from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import key_boolean_value_pair, key_integer_value_pair, key_real_value_pair, key_string_value_pair

@dataclass
class KeyTypedValuePair(AdditionalDataHolder, Parsable):
    """
    A key-value pair with a string key and a typed value.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The string key of the key-value pair.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KeyTypedValuePair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: KeyTypedValuePair
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.keyBooleanValuePair":
                from . import key_boolean_value_pair

                return key_boolean_value_pair.KeyBooleanValuePair()
            if mapping_value == "#microsoft.graph.keyIntegerValuePair":
                from . import key_integer_value_pair

                return key_integer_value_pair.KeyIntegerValuePair()
            if mapping_value == "#microsoft.graph.keyRealValuePair":
                from . import key_real_value_pair

                return key_real_value_pair.KeyRealValuePair()
            if mapping_value == "#microsoft.graph.keyStringValuePair":
                from . import key_string_value_pair

                return key_string_value_pair.KeyStringValuePair()
        return KeyTypedValuePair()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import key_boolean_value_pair, key_integer_value_pair, key_real_value_pair, key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

