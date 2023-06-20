from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import policy_platform_type

@dataclass
class QueryByPlatformTypePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Supported platform types for policies.
    platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QueryByPlatformTypePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QueryByPlatformTypePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return QueryByPlatformTypePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import policy_platform_type

        from ....models import policy_platform_type

        fields: Dict[str, Callable[[Any], None]] = {
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
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
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_additional_data_value(self.additional_data)
    

