from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

@dataclass
class SubjectRightsRequestEnumeratedMailboxLocation(SubjectRightsRequestMailboxLocation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation"
    # Collection of mailboxes that should be included in the search. Includes the UPN of each mailbox, for example, Monica.Thompson@contoso.com. Going forward, use the userPrincipalNames property. If you specify either upns or userPrincipalNames, the same values are populated automatically to the other property.
    upns: Optional[list[str]] = None
    # Collection of mailboxes that should be included in the search. Includes the user principal name (UPN) of each mailbox, for example, Monica.Thompson@contoso.com.
    user_principal_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectRightsRequestEnumeratedMailboxLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestEnumeratedMailboxLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestEnumeratedMailboxLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        fields: dict[str, Callable[[Any], None]] = {
            "upns": lambda n : setattr(self, 'upns', n.get_collection_of_primitive_values(str)),
            "userPrincipalNames": lambda n : setattr(self, 'user_principal_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("upns", self.upns)
        writer.write_collection_of_primitive_values("userPrincipalNames", self.user_principal_names)
    

