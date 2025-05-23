from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .information_protection_action import InformationProtectionAction
    from .key_value_pair import KeyValuePair

from .information_protection_action import InformationProtectionAction

@dataclass
class CustomAction(InformationProtectionAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customAction"
    # Name of the custom action.
    name: Optional[str] = None
    # Properties, in key value pair format, of the action.
    properties: Optional[list[KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .information_protection_action import InformationProtectionAction
        from .key_value_pair import KeyValuePair

        from .information_protection_action import InformationProtectionAction
        from .key_value_pair import KeyValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(KeyValuePair)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("properties", self.properties)
    

