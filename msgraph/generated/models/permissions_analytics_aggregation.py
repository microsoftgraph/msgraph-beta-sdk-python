from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permissions_analytics import PermissionsAnalytics

from .entity import Entity

@dataclass
class PermissionsAnalyticsAggregation(Entity):
    # The aws property
    aws: Optional[PermissionsAnalytics] = None
    # The azure property
    azure: Optional[PermissionsAnalytics] = None
    # The gcp property
    gcp: Optional[PermissionsAnalytics] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsAnalyticsAggregation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsAnalyticsAggregation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionsAnalyticsAggregation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permissions_analytics import PermissionsAnalytics

        from .entity import Entity
        from .permissions_analytics import PermissionsAnalytics

        fields: Dict[str, Callable[[Any], None]] = {
            "aws": lambda n : setattr(self, 'aws', n.get_object_value(PermissionsAnalytics)),
            "azure": lambda n : setattr(self, 'azure', n.get_object_value(PermissionsAnalytics)),
            "gcp": lambda n : setattr(self, 'gcp', n.get_object_value(PermissionsAnalytics)),
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
        writer.write_object_value("aws", self.aws)
        writer.write_object_value("azure", self.azure)
        writer.write_object_value("gcp", self.gcp)
    

