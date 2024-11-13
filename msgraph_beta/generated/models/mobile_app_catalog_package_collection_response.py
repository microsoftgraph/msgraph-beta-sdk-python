from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .mobile_app_catalog_package import MobileAppCatalogPackage

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class MobileAppCatalogPackageCollectionResponse(BaseCollectionPaginationCountResponse, Parsable):
    # The value property
    value: Optional[List[MobileAppCatalogPackage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppCatalogPackageCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppCatalogPackageCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppCatalogPackageCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .mobile_app_catalog_package import MobileAppCatalogPackage

        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .mobile_app_catalog_package import MobileAppCatalogPackage

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(MobileAppCatalogPackage)),
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
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .mobile_app_catalog_package import MobileAppCatalogPackage

        writer.write_collection_of_object_values("value", self.value)
    

