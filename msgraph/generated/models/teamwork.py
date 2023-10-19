from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deleted_chat import DeletedChat
    from .deleted_team import DeletedTeam
    from .entity import Entity
    from .teams_app_settings import TeamsAppSettings
    from .teamwork_device import TeamworkDevice
    from .team_template import TeamTemplate
    from .workforce_integration import WorkforceIntegration

from .entity import Entity

@dataclass
class Teamwork(Entity):
    # A collection of deleted chats.
    deleted_chats: Optional[List[DeletedChat]] = None
    # A collection of deleted teams.
    deleted_teams: Optional[List[DeletedTeam]] = None
    # The Teams devices provisioned for the tenant.
    devices: Optional[List[TeamworkDevice]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The templates associated with a team.
    team_templates: Optional[List[TeamTemplate]] = None
    # Represents tenant-wide settings for all Teams apps in the tenant.
    teams_app_settings: Optional[TeamsAppSettings] = None
    # A workforce integration with shifts.
    workforce_integrations: Optional[List[WorkforceIntegration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Teamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Teamwork
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Teamwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .deleted_chat import DeletedChat
        from .deleted_team import DeletedTeam
        from .entity import Entity
        from .teams_app_settings import TeamsAppSettings
        from .teamwork_device import TeamworkDevice
        from .team_template import TeamTemplate
        from .workforce_integration import WorkforceIntegration

        from .deleted_chat import DeletedChat
        from .deleted_team import DeletedTeam
        from .entity import Entity
        from .teams_app_settings import TeamsAppSettings
        from .teamwork_device import TeamworkDevice
        from .team_template import TeamTemplate
        from .workforce_integration import WorkforceIntegration

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedChats": lambda n : setattr(self, 'deleted_chats', n.get_collection_of_object_values(DeletedChat)),
            "deletedTeams": lambda n : setattr(self, 'deleted_teams', n.get_collection_of_object_values(DeletedTeam)),
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(TeamworkDevice)),
            "teamTemplates": lambda n : setattr(self, 'team_templates', n.get_collection_of_object_values(TeamTemplate)),
            "teamsAppSettings": lambda n : setattr(self, 'teams_app_settings', n.get_object_value(TeamsAppSettings)),
            "workforceIntegrations": lambda n : setattr(self, 'workforce_integrations', n.get_collection_of_object_values(WorkforceIntegration)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("deletedChats", self.deleted_chats)
        writer.write_collection_of_object_values("deletedTeams", self.deleted_teams)
        writer.write_collection_of_object_values("devices", self.devices)
        writer.write_collection_of_object_values("teamTemplates", self.team_templates)
        writer.write_object_value("teamsAppSettings", self.teams_app_settings)
        writer.write_collection_of_object_values("workforceIntegrations", self.workforce_integrations)
    

