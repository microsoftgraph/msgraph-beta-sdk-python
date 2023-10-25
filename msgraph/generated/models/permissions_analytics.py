from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .finding import Finding
    from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

from .entity import Entity

@dataclass
class PermissionsAnalytics(Entity):
    # The findings property
    findings: Optional[List[Finding]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndexDistributions property
    permissions_creep_index_distributions: Optional[List[PermissionsCreepIndexDistribution]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsAnalytics
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionsAnalytics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .finding import Finding
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

        from .entity import Entity
        from .finding import Finding
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

        fields: Dict[str, Callable[[Any], None]] = {
            "findings": lambda n : setattr(self, 'findings', n.get_collection_of_object_values(Finding)),
            "permissionsCreepIndexDistributions": lambda n : setattr(self, 'permissions_creep_index_distributions', n.get_collection_of_object_values(PermissionsCreepIndexDistribution)),
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
        writer.write_collection_of_object_values("findings", self.findings)
        writer.write_collection_of_object_values("permissionsCreepIndexDistributions", self.permissions_creep_index_distributions)
    

