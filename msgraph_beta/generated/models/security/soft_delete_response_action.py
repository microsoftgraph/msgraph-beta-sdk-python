from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_entity_identifier import EmailEntityIdentifier
    from .response_action import ResponseAction

from .response_action import ResponseAction

@dataclass
class SoftDeleteResponseAction(ResponseAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.softDeleteResponseAction"
    # The identifier property
    identifier: Optional[EmailEntityIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SoftDeleteResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SoftDeleteResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SoftDeleteResponseAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_entity_identifier import EmailEntityIdentifier
        from .response_action import ResponseAction

        from .email_entity_identifier import EmailEntityIdentifier
        from .response_action import ResponseAction

        fields: dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_collection_of_enum_values(EmailEntityIdentifier)),
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
        writer.write_enum_value("identifier", self.identifier)
    

