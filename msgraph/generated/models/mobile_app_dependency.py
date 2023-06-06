from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_dependency_type, mobile_app_relationship

from . import mobile_app_relationship

@dataclass
class MobileAppDependency(mobile_app_relationship.MobileAppRelationship):
    odata_type = "#microsoft.graph.mobileAppDependency"
    # Indicates the dependency type associated with a relationship between two mobile apps.
    dependency_type: Optional[mobile_app_dependency_type.MobileAppDependencyType] = None
    # The total number of apps that directly or indirectly depend on the parent app.
    dependent_app_count: Optional[int] = None
    # The total number of apps the child app directly or indirectly depends on.
    depends_on_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppDependency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppDependency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppDependency()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_dependency_type, mobile_app_relationship

        fields: Dict[str, Callable[[Any], None]] = {
            "dependencyType": lambda n : setattr(self, 'dependency_type', n.get_enum_value(mobile_app_dependency_type.MobileAppDependencyType)),
            "dependentAppCount": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "dependsOnAppCount": lambda n : setattr(self, 'depends_on_app_count', n.get_int_value()),
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
        writer.write_enum_value("dependencyType", self.dependency_type)
        writer.write_int_value("dependentAppCount", self.dependent_app_count)
        writer.write_int_value("dependsOnAppCount", self.depends_on_app_count)
    

