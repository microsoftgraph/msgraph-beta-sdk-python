from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .branch_site import BranchSite
    from .remote_network import RemoteNetwork
    from .web_category import WebCategory

from ..entity import Entity

@dataclass
class Connectivity(Entity):
    # Branches represent locations for connectivity. DEPRECATED AND TO BE RETIRED SOON. Use the remoteNetwork relationship and its associated APIs instead.
    branches: Optional[List[BranchSite]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represent locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
    remote_networks: Optional[List[RemoteNetwork]] = None
    # The webCategories property
    web_categories: Optional[List[WebCategory]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Connectivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connectivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Connectivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .branch_site import BranchSite
        from .remote_network import RemoteNetwork
        from .web_category import WebCategory

        from ..entity import Entity
        from .branch_site import BranchSite
        from .remote_network import RemoteNetwork
        from .web_category import WebCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "branches": lambda n : setattr(self, 'branches', n.get_collection_of_object_values(BranchSite)),
            "remoteNetworks": lambda n : setattr(self, 'remote_networks', n.get_collection_of_object_values(RemoteNetwork)),
            "webCategories": lambda n : setattr(self, 'web_categories', n.get_collection_of_object_values(WebCategory)),
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
        writer.write_collection_of_object_values("branches", self.branches)
        writer.write_collection_of_object_values("remoteNetworks", self.remote_networks)
        writer.write_collection_of_object_values("webCategories", self.web_categories)
    

