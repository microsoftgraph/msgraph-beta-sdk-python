from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AssignedComputeInstanceDetails(Entity):
    # The accessedStorageBuckets property
    accessed_storage_buckets: Optional[List[AuthorizationSystemResource]] = None
    # The assignedComputeInstance property
    assigned_compute_instance: Optional[AuthorizationSystemResource] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedComputeInstanceDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignedComputeInstanceDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignedComputeInstanceDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .entity import Entity

        from .authorization_system_resource import AuthorizationSystemResource
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessedStorageBuckets": lambda n : setattr(self, 'accessed_storage_buckets', n.get_collection_of_object_values(AuthorizationSystemResource)),
            "assignedComputeInstance": lambda n : setattr(self, 'assigned_compute_instance', n.get_object_value(AuthorizationSystemResource)),
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
        writer.write_collection_of_object_values("accessedStorageBuckets", self.accessed_storage_buckets)
        writer.write_object_value("assignedComputeInstance", self.assigned_compute_instance)
    

