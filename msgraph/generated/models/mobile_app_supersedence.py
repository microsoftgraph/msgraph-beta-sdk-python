from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_relationship, mobile_app_supersedence_type

from . import mobile_app_relationship

@dataclass
class MobileAppSupersedence(mobile_app_relationship.MobileAppRelationship):
    odata_type = "#microsoft.graph.mobileAppSupersedence"
    # The total number of apps directly or indirectly superseded by the child app.
    superseded_app_count: Optional[int] = None
    # Indicates the supersedence type associated with a relationship between two mobile apps.
    supersedence_type: Optional[mobile_app_supersedence_type.MobileAppSupersedenceType] = None
    # The total number of apps directly or indirectly superseding the parent app.
    superseding_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppSupersedence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppSupersedence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppSupersedence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_relationship, mobile_app_supersedence_type

        fields: Dict[str, Callable[[Any], None]] = {
            "supersededAppCount": lambda n : setattr(self, 'superseded_app_count', n.get_int_value()),
            "supersedenceType": lambda n : setattr(self, 'supersedence_type', n.get_enum_value(mobile_app_supersedence_type.MobileAppSupersedenceType)),
            "supersedingAppCount": lambda n : setattr(self, 'superseding_app_count', n.get_int_value()),
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
        writer.write_int_value("supersededAppCount", self.superseded_app_count)
        writer.write_enum_value("supersedenceType", self.supersedence_type)
        writer.write_int_value("supersedingAppCount", self.superseding_app_count)
    

