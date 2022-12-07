from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_rights_request_mailbox_location = lazy_import('msgraph.generated.models.subject_rights_request_mailbox_location')

class SubjectRightsRequestEnumeratedMailboxLocation(subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation):
    def __init__(self,) -> None:
        """
        Instantiates a new SubjectRightsRequestEnumeratedMailboxLocation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation"
        # Collection of mailboxes that should be included in the search. Includes the UPN (user principal name) of each mailbox, for example, Monica.Thompson@contoso.com.
        self._upns: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestEnumeratedMailboxLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestEnumeratedMailboxLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequestEnumeratedMailboxLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("upns", self.upns)
    
    @property
    def upns(self,) -> Optional[List[str]]:
        """
        Gets the upns property value. Collection of mailboxes that should be included in the search. Includes the UPN (user principal name) of each mailbox, for example, Monica.Thompson@contoso.com.
        Returns: Optional[List[str]]
        """
        return self._upns
    
    @upns.setter
    def upns(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the upns property value. Collection of mailboxes that should be included in the search. Includes the UPN (user principal name) of each mailbox, for example, Monica.Thompson@contoso.com.
        Args:
            value: Value to set for the upns property.
        """
        self._upns = value
    

