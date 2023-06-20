from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class TeamsAppSettings(entity.Entity):
    # Indicates whether users are allowed to request access to the unavailable Teams apps.
    allow_user_requests_for_app_access: Optional[bool] = None
    # Indicates whether resource-specific consent for chats/meetings has been enabled for the tenant. If true, Teams apps that are allowed in the tenant and require resource-specific permissions can be installed inside chats and meetings. If false, the installation of any Teams app that requires resource-specific permissions in a chat or a meeting will be blocked.
    is_chat_resource_specific_consent_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allowUserRequestsForAppAccess": lambda n : setattr(self, 'allow_user_requests_for_app_access', n.get_bool_value()),
            "isChatResourceSpecificConsentEnabled": lambda n : setattr(self, 'is_chat_resource_specific_consent_enabled', n.get_bool_value()),
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
        writer.write_bool_value("allowUserRequestsForAppAccess", self.allow_user_requests_for_app_access)
        writer.write_bool_value("isChatResourceSpecificConsentEnabled", self.is_chat_resource_specific_consent_enabled)
    

