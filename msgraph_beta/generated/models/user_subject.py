from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
    from .conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

from .conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

@dataclass
class UserSubject(ConditionalAccessWhatIfSubject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userSubject"
    # The externalTenantId property
    external_tenant_id: Optional[str] = None
    # The externalUserType property
    external_user_type: Optional[ConditionalAccessGuestOrExternalUserTypes] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSubject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
        from .conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
        from .conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

        fields: Dict[str, Callable[[Any], None]] = {
            "externalTenantId": lambda n : setattr(self, 'external_tenant_id', n.get_str_value()),
            "externalUserType": lambda n : setattr(self, 'external_user_type', n.get_collection_of_enum_values(ConditionalAccessGuestOrExternalUserTypes)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("externalTenantId", self.external_tenant_id)
        writer.write_enum_value("externalUserType", self.external_user_type)
        writer.write_str_value("userId", self.user_id)
    

