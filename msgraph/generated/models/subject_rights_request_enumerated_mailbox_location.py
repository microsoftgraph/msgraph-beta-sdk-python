from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

@dataclass
class SubjectRightsRequestEnumeratedMailboxLocation(SubjectRightsRequestMailboxLocation):
    odata_type = "#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation"
    # Collection of mailboxes that should be included in the search. Includes the UPN (user principal name) of each mailbox, for example, Monica.Thompson@contoso.com.
    upns: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestEnumeratedMailboxLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestEnumeratedMailboxLocation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestEnumeratedMailboxLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "upns": lambda n : setattr(self, 'upns', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("upns", self.upns)
    

