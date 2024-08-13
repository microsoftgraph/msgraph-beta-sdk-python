from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.security.content_info import ContentInfo
    from .....models.security.downgrade_justification import DowngradeJustification

@dataclass
class EvaluateRemovalPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The contentInfo property
    content_info: Optional[ContentInfo] = None
    # The downgradeJustification property
    downgrade_justification: Optional[DowngradeJustification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluateRemovalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateRemovalPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluateRemovalPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.security.content_info import ContentInfo
        from .....models.security.downgrade_justification import DowngradeJustification

        from .....models.security.content_info import ContentInfo
        from .....models.security.downgrade_justification import DowngradeJustification

        fields: Dict[str, Callable[[Any], None]] = {
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(ContentInfo)),
            "downgradeJustification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(DowngradeJustification)),
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
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_additional_data_value(self.additional_data)
    

