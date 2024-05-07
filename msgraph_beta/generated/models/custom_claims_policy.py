from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_base import CustomClaimBase
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomClaimsPolicy(Entity):
    # The audienceOverride property
    audience_override: Optional[str] = None
    # The claims property
    claims: Optional[List[CustomClaimBase]] = None
    # The includeApplicationIdInIssuer property
    include_application_id_in_issuer: Optional[bool] = None
    # The includeBasicClaimSet property
    include_basic_claim_set: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaimsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaimsPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomClaimsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_base import CustomClaimBase
        from .entity import Entity

        from .custom_claim_base import CustomClaimBase
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "audienceOverride": lambda n : setattr(self, 'audience_override', n.get_str_value()),
            "claims": lambda n : setattr(self, 'claims', n.get_collection_of_object_values(CustomClaimBase)),
            "includeApplicationIdInIssuer": lambda n : setattr(self, 'include_application_id_in_issuer', n.get_bool_value()),
            "includeBasicClaimSet": lambda n : setattr(self, 'include_basic_claim_set', n.get_bool_value()),
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
        writer.write_str_value("audienceOverride", self.audience_override)
        writer.write_collection_of_object_values("claims", self.claims)
        writer.write_bool_value("includeApplicationIdInIssuer", self.include_application_id_in_issuer)
        writer.write_bool_value("includeBasicClaimSet", self.include_basic_claim_set)
    

