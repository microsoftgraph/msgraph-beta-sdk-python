from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.content_info import ContentInfo
    from .........models.downgrade_justification import DowngradeJustification

@dataclass
class EvaluateRemovalPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The contentInfo property
    content_info: Optional[ContentInfo] = None
    # The downgradeJustification property
    downgrade_justification: Optional[DowngradeJustification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateRemovalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateRemovalPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateRemovalPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .........models.content_info import ContentInfo
        from .........models.downgrade_justification import DowngradeJustification

        from .........models.content_info import ContentInfo
        from .........models.downgrade_justification import DowngradeJustification

        fields: Dict[str, Callable[[Any], None]] = {
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(ContentInfo)),
            "downgradeJustification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(DowngradeJustification)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_additional_data_value(self.additional_data)
    

