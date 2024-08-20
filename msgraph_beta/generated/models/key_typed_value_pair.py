from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_boolean_value_pair import KeyBooleanValuePair
    from .key_integer_value_pair import KeyIntegerValuePair
    from .key_real_value_pair import KeyRealValuePair
    from .key_string_value_pair import KeyStringValuePair

@dataclass
class KeyTypedValuePair(AdditionalDataHolder, BackedModel, Parsable):
    """
    A key-value pair with a string key and a typed value.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The string key of the key-value pair.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KeyTypedValuePair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyTypedValuePair
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyBooleanValuePair".casefold():
            from .key_boolean_value_pair import KeyBooleanValuePair

            return KeyBooleanValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyIntegerValuePair".casefold():
            from .key_integer_value_pair import KeyIntegerValuePair

            return KeyIntegerValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyRealValuePair".casefold():
            from .key_real_value_pair import KeyRealValuePair

            return KeyRealValuePair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.keyStringValuePair".casefold():
            from .key_string_value_pair import KeyStringValuePair

            return KeyStringValuePair()
        return KeyTypedValuePair()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_boolean_value_pair import KeyBooleanValuePair
        from .key_integer_value_pair import KeyIntegerValuePair
        from .key_real_value_pair import KeyRealValuePair
        from .key_string_value_pair import KeyStringValuePair

        from .key_boolean_value_pair import KeyBooleanValuePair
        from .key_integer_value_pair import KeyIntegerValuePair
        from .key_real_value_pair import KeyRealValuePair
        from .key_string_value_pair import KeyStringValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

