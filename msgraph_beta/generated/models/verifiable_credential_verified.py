from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

@dataclass
class VerifiableCredentialVerified(VerifiableCredentialRequirementStatus):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.verifiableCredentialVerified"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiableCredentialVerified:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialVerified
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiableCredentialVerified()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        fields: Dict[str, Callable[[Any], None]] = {
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
    

