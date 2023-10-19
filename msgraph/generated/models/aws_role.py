from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_identity import AwsIdentity
    from .aws_role_trust_entity_type import AwsRoleTrustEntityType
    from .aws_role_type import AwsRoleType

from .aws_identity import AwsIdentity

@dataclass
class AwsRole(AwsIdentity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsRole"
    # The roleType property
    role_type: Optional[AwsRoleType] = None
    # The trustEntityType property
    trust_entity_type: Optional[AwsRoleTrustEntityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AwsRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsRole
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AwsRole()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_identity import AwsIdentity
        from .aws_role_trust_entity_type import AwsRoleTrustEntityType
        from .aws_role_type import AwsRoleType

        from .aws_identity import AwsIdentity
        from .aws_role_trust_entity_type import AwsRoleTrustEntityType
        from .aws_role_type import AwsRoleType

        fields: Dict[str, Callable[[Any], None]] = {
            "roleType": lambda n : setattr(self, 'role_type', n.get_enum_value(AwsRoleType)),
            "trustEntityType": lambda n : setattr(self, 'trust_entity_type', n.get_collection_of_enum_values(AwsRoleTrustEntityType)),
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
        writer.write_enum_value("roleType", self.role_type)
        writer.write_enum_value("trustEntityType", self.trust_entity_type)
    

