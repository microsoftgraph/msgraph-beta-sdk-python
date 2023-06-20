from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy, policy_base

from . import policy_base

@dataclass
class TenantRelationshipAccessPolicyBase(policy_base.PolicyBase):
    odata_type = "#microsoft.graph.tenantRelationshipAccessPolicyBase"
    # The definition property
    definition: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantRelationshipAccessPolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantRelationshipAccessPolicyBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from . import cross_tenant_access_policy

            return cross_tenant_access_policy.CrossTenantAccessPolicy()
        return TenantRelationshipAccessPolicyBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy, policy_base

        from . import cross_tenant_access_policy, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("definition", self.definition)
    

