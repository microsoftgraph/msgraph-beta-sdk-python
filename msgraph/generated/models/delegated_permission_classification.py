from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, permission_classification_type

from . import entity

@dataclass
class DelegatedPermissionClassification(entity.Entity):
    # The classification value being given. Possible value: low. Does not support $filter.
    classification: Optional[permission_classification_type.PermissionClassificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier (id) for the delegated permission listed in the publishedPermissionScopes collection of the servicePrincipal. Required on create. Does not support $filter.
    permission_id: Optional[str] = None
    # The claim value (value) for the delegated permission listed in the publishedPermissionScopes collection of the servicePrincipal. Does not support $filter.
    permission_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedPermissionClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedPermissionClassification
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DelegatedPermissionClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, permission_classification_type

        from . import entity, permission_classification_type

        fields: Dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(permission_classification_type.PermissionClassificationType)),
            "permissionId": lambda n : setattr(self, 'permission_id', n.get_str_value()),
            "permissionName": lambda n : setattr(self, 'permission_name', n.get_str_value()),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_str_value("permissionId", self.permission_id)
        writer.write_str_value("permissionName", self.permission_name)
    

