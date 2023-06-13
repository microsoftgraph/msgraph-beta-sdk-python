from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import user_set

@dataclass
class RequestorSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates whether new requests are accepted on this policy.
    accept_requests: Optional[bool] = None
    # The users who are allowed to request on this policy, which can be singleUser, groupMembers, and connectedOrganizationMembers.
    allowed_requestors: Optional[List[user_set.UserSet]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Who can request. One of NoSubjects, SpecificDirectorySubjects, SpecificConnectedOrganizationSubjects, AllConfiguredConnectedOrganizationSubjects, AllExistingConnectedOrganizationSubjects, AllExistingDirectoryMemberUsers, AllExistingDirectorySubjects or AllExternalSubjects.
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestorSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestorSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import user_set

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptRequests": lambda n : setattr(self, 'accept_requests', n.get_bool_value()),
            "allowedRequestors": lambda n : setattr(self, 'allowed_requestors', n.get_collection_of_object_values(user_set.UserSet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("acceptRequests", self.accept_requests)
        writer.write_collection_of_object_values("allowedRequestors", self.allowed_requestors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scopeType", self.scope_type)
        writer.write_additional_data_value(self.additional_data)
    

