from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .response_action import ResponseAction
    from .stop_and_quarantine_file_entity_identifier import StopAndQuarantineFileEntityIdentifier

from .response_action import ResponseAction

@dataclass
class StopAndQuarantineFileResponseAction(ResponseAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.stopAndQuarantineFileResponseAction"
    # The identifier property
    identifier: Optional[StopAndQuarantineFileEntityIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StopAndQuarantineFileResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StopAndQuarantineFileResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StopAndQuarantineFileResponseAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .response_action import ResponseAction
        from .stop_and_quarantine_file_entity_identifier import StopAndQuarantineFileEntityIdentifier

        from .response_action import ResponseAction
        from .stop_and_quarantine_file_entity_identifier import StopAndQuarantineFileEntityIdentifier

        fields: Dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_collection_of_enum_values(StopAndQuarantineFileEntityIdentifier)),
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
        from .response_action import ResponseAction
        from .stop_and_quarantine_file_entity_identifier import StopAndQuarantineFileEntityIdentifier

        writer.write_enum_value("identifier", self.identifier)
    

