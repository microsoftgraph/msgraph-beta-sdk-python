from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_dependency import MobileAppDependency
    from .mobile_app_relationship_type import MobileAppRelationshipType
    from .mobile_app_supersedence import MobileAppSupersedence

from .entity import Entity

@dataclass
class MobileAppRelationship(Entity):
    """
    Describes a relationship between two mobile apps.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name of the app that is the target of the mobile app relationship entity. Read-Only. This property is read-only.
    target_display_name: Optional[str] = None
    # The display version of the app that is the target of the mobile app relationship entity. Read-Only. This property is read-only.
    target_display_version: Optional[str] = None
    # App ID of the app that is the target of the mobile app relationship entity. Read-Only
    target_id: Optional[str] = None
    # The publisher of the app that is the target of the mobile app relationship entity. Read-Only. This property is read-only.
    target_publisher: Optional[str] = None
    # Indicates whether the target of a relationship is the parent or the child in the relationship.
    target_type: Optional[MobileAppRelationshipType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppRelationship
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppDependency".casefold():
            from .mobile_app_dependency import MobileAppDependency

            return MobileAppDependency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppSupersedence".casefold():
            from .mobile_app_supersedence import MobileAppSupersedence

            return MobileAppSupersedence()
        return MobileAppRelationship()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_relationship_type import MobileAppRelationshipType
        from .mobile_app_supersedence import MobileAppSupersedence

        from .entity import Entity
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_relationship_type import MobileAppRelationshipType
        from .mobile_app_supersedence import MobileAppSupersedence

        fields: Dict[str, Callable[[Any], None]] = {
            "targetDisplayName": lambda n : setattr(self, 'target_display_name', n.get_str_value()),
            "targetDisplayVersion": lambda n : setattr(self, 'target_display_version', n.get_str_value()),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "targetPublisher": lambda n : setattr(self, 'target_publisher', n.get_str_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(MobileAppRelationshipType)),
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
        writer.write_str_value("targetId", self.target_id)
        writer.write_enum_value("targetType", self.target_type)
    

