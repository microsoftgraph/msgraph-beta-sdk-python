from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.windows_updates.update_category import UpdateCategory

@dataclass
class EnrollAssetsByIdPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The ids property
    ids: Optional[List[str]] = None
    # The memberEntityType property
    member_entity_type: Optional[str] = None
    # The updateCategory property
    update_category: Optional[UpdateCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnrollAssetsByIdPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnrollAssetsByIdPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnrollAssetsByIdPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.windows_updates.update_category import UpdateCategory

        from ......models.windows_updates.update_category import UpdateCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_primitive_values(str)),
            "memberEntityType": lambda n : setattr(self, 'member_entity_type', n.get_str_value()),
            "updateCategory": lambda n : setattr(self, 'update_category', n.get_enum_value(UpdateCategory)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("ids", self.ids)
        writer.write_str_value("memberEntityType", self.member_entity_type)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_additional_data_value(self.additional_data)
    

