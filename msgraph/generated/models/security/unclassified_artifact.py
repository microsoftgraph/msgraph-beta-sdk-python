from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import artifact

from . import artifact

@dataclass
class UnclassifiedArtifact(artifact.Artifact):
    odata_type = "#microsoft.graph.security.unclassifiedArtifact"
    # The kind for this unclassifiedArtifact resource, describing what this value means.
    kind: Optional[str] = None
    # The value for this unclassifiedArtifact.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnclassifiedArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnclassifiedArtifact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnclassifiedArtifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import artifact

        fields: Dict[str, Callable[[Any], None]] = {
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("value", self.value)
    

