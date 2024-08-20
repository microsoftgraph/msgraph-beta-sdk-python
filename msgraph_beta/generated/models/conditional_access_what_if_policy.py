from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy import ConditionalAccessPolicy
    from .conditional_access_what_if_reasons import ConditionalAccessWhatIfReasons

from .conditional_access_policy import ConditionalAccessPolicy

@dataclass
class ConditionalAccessWhatIfPolicy(ConditionalAccessPolicy):
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyApplies property
    policy_applies: Optional[bool] = None
    # The reasons property
    reasons: Optional[List[ConditionalAccessWhatIfReasons]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessWhatIfPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessWhatIfPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessWhatIfPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_what_if_reasons import ConditionalAccessWhatIfReasons

        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_what_if_reasons import ConditionalAccessWhatIfReasons

        fields: Dict[str, Callable[[Any], None]] = {
            "policyApplies": lambda n : setattr(self, 'policy_applies', n.get_bool_value()),
            "reasons": lambda n : setattr(self, 'reasons', n.get_collection_of_enum_values(ConditionalAccessWhatIfReasons)),
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
        writer.write_bool_value("policyApplies", self.policy_applies)
        writer.write_collection_of_enum_values("reasons", self.reasons)
    

