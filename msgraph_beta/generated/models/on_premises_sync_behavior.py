from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class OnPremisesSyncBehavior(Entity, Parsable):
    # Indicates the state of synchronization for an object between the cloud and on-premises Active Directory. If true, updates from on-premises Active Directory are blocked in the cloud; if false, updates from on-premises Active Directory are allowed in the cloud and the object can be taken over by on-premises Active Directory.
    is_cloud_managed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesSyncBehavior:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesSyncBehavior
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesSyncBehavior()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "isCloudManaged": lambda n : setattr(self, 'is_cloud_managed', n.get_bool_value()),
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
        writer.write_bool_value("isCloudManaged", self.is_cloud_managed)
    

