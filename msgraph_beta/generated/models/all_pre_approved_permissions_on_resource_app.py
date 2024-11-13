from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pre_approved_permissions import PreApprovedPermissions

from .pre_approved_permissions import PreApprovedPermissions

@dataclass
class AllPreApprovedPermissionsOnResourceApp(PreApprovedPermissions, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.allPreApprovedPermissionsOnResourceApp"
    # The appId of the resource application (the API). Required.
    resource_application_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllPreApprovedPermissionsOnResourceApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllPreApprovedPermissionsOnResourceApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllPreApprovedPermissionsOnResourceApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .pre_approved_permissions import PreApprovedPermissions

        from .pre_approved_permissions import PreApprovedPermissions

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceApplicationId": lambda n : setattr(self, 'resource_application_id', n.get_str_value()),
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
        from .pre_approved_permissions import PreApprovedPermissions

        writer.write_str_value("resourceApplicationId", self.resource_application_id)
    

