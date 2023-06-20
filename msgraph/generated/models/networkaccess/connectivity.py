from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import branch_site
    from .. import entity

from .. import entity

@dataclass
class Connectivity(entity.Entity):
    # The branches property
    branches: Optional[List[branch_site.BranchSite]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Connectivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Connectivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Connectivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import branch_site
        from .. import entity

        from . import branch_site
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "branches": lambda n : setattr(self, 'branches', n.get_collection_of_object_values(branch_site.BranchSite)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("branches", self.branches)
    

