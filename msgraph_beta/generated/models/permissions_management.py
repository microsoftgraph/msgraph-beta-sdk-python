from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permissions_request_change import PermissionsRequestChange
    from .scheduled_permissions_request import ScheduledPermissionsRequest

from .entity import Entity

@dataclass
class PermissionsManagement(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsRequestChanges property
    permissions_request_changes: Optional[List[PermissionsRequestChange]] = None
    # The scheduledPermissionsRequests property
    scheduled_permissions_requests: Optional[List[ScheduledPermissionsRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionsManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permissions_request_change import PermissionsRequestChange
        from .scheduled_permissions_request import ScheduledPermissionsRequest

        from .entity import Entity
        from .permissions_request_change import PermissionsRequestChange
        from .scheduled_permissions_request import ScheduledPermissionsRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "permissionsRequestChanges": lambda n : setattr(self, 'permissions_request_changes', n.get_collection_of_object_values(PermissionsRequestChange)),
            "scheduledPermissionsRequests": lambda n : setattr(self, 'scheduled_permissions_requests', n.get_collection_of_object_values(ScheduledPermissionsRequest)),
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
        writer.write_collection_of_object_values("permissionsRequestChanges", self.permissions_request_changes)
        writer.write_collection_of_object_values("scheduledPermissionsRequests", self.scheduled_permissions_requests)
    

