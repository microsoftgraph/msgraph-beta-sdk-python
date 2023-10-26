from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .tenant_contact_information import TenantContactInformation

from ..entity import Entity

@dataclass
class TenantCustomizedInformation(Entity):
    # The collection of contacts for the managed tenant. Optional.
    contacts: Optional[List[TenantContactInformation]] = None
    # The display name for the managed tenant. Required. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    # The website for the managed tenant. Required.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantCustomizedInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantCustomizedInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantCustomizedInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .tenant_contact_information import TenantContactInformation

        from ..entity import Entity
        from .tenant_contact_information import TenantContactInformation

        fields: Dict[str, Callable[[Any], None]] = {
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(TenantContactInformation)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("website", self.website)
    

