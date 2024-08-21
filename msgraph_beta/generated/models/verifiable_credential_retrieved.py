from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

@dataclass
class VerifiableCredentialRetrieved(VerifiableCredentialRequirementStatus):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.verifiableCredentialRetrieved"
    # The specific date and time that the presentation request will expire and a new one will need to be generated.
    expiry_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiableCredentialRetrieved:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialRetrieved
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiableCredentialRetrieved()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("expiryDateTime", self.expiry_date_time)
    

