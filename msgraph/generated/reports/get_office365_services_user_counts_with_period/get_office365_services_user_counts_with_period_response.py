from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import base_collection_pagination_count_response, office365_services_user_counts

from ...models import base_collection_pagination_count_response

@dataclass
class GetOffice365ServicesUserCountsWithPeriodResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    # The value property
    value: Optional[List[office365_services_user_counts.Office365ServicesUserCounts]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetOffice365ServicesUserCountsWithPeriodResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetOffice365ServicesUserCountsWithPeriodResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetOffice365ServicesUserCountsWithPeriodResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import base_collection_pagination_count_response, office365_services_user_counts

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(office365_services_user_counts.Office365ServicesUserCounts)),
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
        writer.write_collection_of_object_values("value", self.value)
    

