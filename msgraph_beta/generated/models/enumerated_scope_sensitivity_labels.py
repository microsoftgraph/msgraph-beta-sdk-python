from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .scope_sensitivity_labels import ScopeSensitivityLabels

from .scope_sensitivity_labels import ScopeSensitivityLabels

@dataclass
class EnumeratedScopeSensitivityLabels(ScopeSensitivityLabels, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.enumeratedScopeSensitivityLabels"
    # The sensitivity labels that are applicable to the scope type and have been preapproved. Required.
    sensitivity_labels: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnumeratedScopeSensitivityLabels:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnumeratedScopeSensitivityLabels
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnumeratedScopeSensitivityLabels()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .scope_sensitivity_labels import ScopeSensitivityLabels

        from .scope_sensitivity_labels import ScopeSensitivityLabels

        fields: Dict[str, Callable[[Any], None]] = {
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_primitive_values(str)),
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
        from .scope_sensitivity_labels import ScopeSensitivityLabels

        writer.write_collection_of_primitive_values("sensitivityLabels", self.sensitivity_labels)
    

