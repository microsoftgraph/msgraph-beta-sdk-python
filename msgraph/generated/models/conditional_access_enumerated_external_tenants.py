from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_external_tenants

from . import conditional_access_external_tenants

class ConditionalAccessEnumeratedExternalTenants(conditional_access_external_tenants.ConditionalAccessExternalTenants):
    def __init__(self,) -> None:
        """
        Instantiates a new ConditionalAccessEnumeratedExternalTenants and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.conditionalAccessEnumeratedExternalTenants"
        # Represents a collection of tenant ids in the scope of Conditional Access for guests and external users policy targeting.
        self._members: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessEnumeratedExternalTenants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessEnumeratedExternalTenants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessEnumeratedExternalTenants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_external_tenants

        fields: Dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[str]]:
        """
        Gets the members property value. Represents a collection of tenant ids in the scope of Conditional Access for guests and external users policy targeting.
        Returns: Optional[List[str]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the members property value. Represents a collection of tenant ids in the scope of Conditional Access for guests and external users policy targeting.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("members", self.members)
    

