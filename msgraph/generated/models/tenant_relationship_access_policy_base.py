from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy, policy_base

from . import policy_base

class TenantRelationshipAccessPolicyBase(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new TenantRelationshipAccessPolicyBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.tenantRelationshipAccessPolicyBase"
        # The definition property
        self._definition: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantRelationshipAccessPolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantRelationshipAccessPolicyBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicy":
                from . import cross_tenant_access_policy

                return cross_tenant_access_policy.CrossTenantAccessPolicy()
        return TenantRelationshipAccessPolicyBase()
    
    @property
    def definition(self,) -> Optional[List[str]]:
        """
        Gets the definition property value. The definition property
        Returns: Optional[List[str]]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the definition property value. The definition property
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("definition", self.definition)
    

