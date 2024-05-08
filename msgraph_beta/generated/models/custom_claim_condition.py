from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .claim_condition_user_type import ClaimConditionUserType
    from .custom_claim_condition_base import CustomClaimConditionBase

from .custom_claim_condition_base import CustomClaimConditionBase

@dataclass
class CustomClaimCondition(CustomClaimConditionBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customClaimCondition"
    # The memberOf property
    member_of: Optional[List[str]] = None
    # The userType property
    user_type: Optional[ClaimConditionUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaimCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaimCondition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomClaimCondition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .claim_condition_user_type import ClaimConditionUserType
        from .custom_claim_condition_base import CustomClaimConditionBase

        from .claim_condition_user_type import ClaimConditionUserType
        from .custom_claim_condition_base import CustomClaimConditionBase

        fields: Dict[str, Callable[[Any], None]] = {
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_primitive_values(str)),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(ClaimConditionUserType)),
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
        writer.write_collection_of_primitive_values("memberOf", self.member_of)
        writer.write_enum_value("userType", self.user_type)
    

