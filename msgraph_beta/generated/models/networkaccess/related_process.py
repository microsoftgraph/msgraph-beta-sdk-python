from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .related_resource import RelatedResource

from .related_resource import RelatedResource

@dataclass
class RelatedProcess(RelatedResource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.relatedProcess"
    # The isSuspicious property
    is_suspicious: Optional[bool] = None
    # The processName property
    process_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedProcess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedProcess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedProcess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .related_resource import RelatedResource

        from .related_resource import RelatedResource

        fields: Dict[str, Callable[[Any], None]] = {
            "isSuspicious": lambda n : setattr(self, 'is_suspicious', n.get_bool_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
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
        writer.write_bool_value("isSuspicious", self.is_suspicious)
        writer.write_str_value("processName", self.process_name)
    

