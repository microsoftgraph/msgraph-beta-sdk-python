from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

@dataclass
class PersonalTeamsAppInstallationScopeInfo(TeamsAppInstallationScopeInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.personalTeamsAppInstallationScopeInfo"
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonalTeamsAppInstallationScopeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonalTeamsAppInstallationScopeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonalTeamsAppInstallationScopeInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

        from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("userId", self.user_id)
    

