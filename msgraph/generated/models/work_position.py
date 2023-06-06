from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet, position_detail, related_person

from . import item_facet

@dataclass
class WorkPosition(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.workPosition"
    # Categories that the user has associated with this position.
    categories: Optional[List[str]] = None
    # Colleagues that are associated with this position.
    colleagues: Optional[List[related_person.RelatedPerson]] = None
    # The detail property
    detail: Optional[position_detail.PositionDetail] = None
    # Denotes whether or not the position is current.
    is_current: Optional[bool] = None
    # Contains detail of the user's manager in this position.
    manager: Optional[related_person.RelatedPerson] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkPosition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkPosition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet, position_detail, related_person

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "colleagues": lambda n : setattr(self, 'colleagues', n.get_collection_of_object_values(related_person.RelatedPerson)),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(position_detail.PositionDetail)),
            "isCurrent": lambda n : setattr(self, 'is_current', n.get_bool_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(related_person.RelatedPerson)),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_bool_value("isCurrent", self.is_current)
        writer.write_object_value("manager", self.manager)
    

