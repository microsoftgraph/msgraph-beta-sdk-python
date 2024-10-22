from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
    from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
    from .teams_app_installation_scopes import TeamsAppInstallationScopes
    from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo

@dataclass
class TeamsAppInstallationScopeInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope property
    scope: Optional[TeamsAppInstallationScopes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppInstallationScopeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallationScopeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupChatTeamsAppInstallationScopeInfo".casefold():
            from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo

            return GroupChatTeamsAppInstallationScopeInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personalTeamsAppInstallationScopeInfo".casefold():
            from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo

            return PersonalTeamsAppInstallationScopeInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamTeamsAppInstallationScopeInfo".casefold():
            from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo

            return TeamTeamsAppInstallationScopeInfo()
        return TeamsAppInstallationScopeInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
        from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
        from .teams_app_installation_scopes import TeamsAppInstallationScopes
        from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo

        from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
        from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
        from .teams_app_installation_scopes import TeamsAppInstallationScopes
        from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_collection_of_enum_values(TeamsAppInstallationScopes)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
        from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
        from .teams_app_installation_scopes import TeamsAppInstallationScopes
        from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo

        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("scope", self.scope)
        writer.write_additional_data_value(self.additional_data)
    

