from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .position_detail import PositionDetail
    from .related_person import RelatedPerson

from .item_facet import ItemFacet

@dataclass
class WorkPosition(ItemFacet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workPosition"
    # Categories that the user has associated with this position.
    categories: Optional[List[str]] = None
    # Colleagues that are associated with this position.
    colleagues: Optional[List[RelatedPerson]] = None
    # The detail property
    detail: Optional[PositionDetail] = None
    # Denotes whether or not the position is current.
    is_current: Optional[bool] = None
    # Contains detail of the user's manager in this position.
    manager: Optional[RelatedPerson] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkPosition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkPosition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .position_detail import PositionDetail
        from .related_person import RelatedPerson

        from .item_facet import ItemFacet
        from .position_detail import PositionDetail
        from .related_person import RelatedPerson

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "colleagues": lambda n : setattr(self, 'colleagues', n.get_collection_of_object_values(RelatedPerson)),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(PositionDetail)),
            "isCurrent": lambda n : setattr(self, 'is_current', n.get_bool_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(RelatedPerson)),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_bool_value("isCurrent", self.is_current)
        writer.write_object_value("manager", self.manager)
    

