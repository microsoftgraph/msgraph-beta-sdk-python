from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import deleted_team, entity, teams_app_settings, teamwork_device, team_template, workforce_integration

from . import entity

@dataclass
class Teamwork(entity.Entity):
    # A collection of deleted teams.
    deleted_teams: Optional[List[deleted_team.DeletedTeam]] = None
    # The Teams devices provisioned for the tenant.
    devices: Optional[List[teamwork_device.TeamworkDevice]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The templates associated with a team.
    team_templates: Optional[List[team_template.TeamTemplate]] = None
    # Represents tenant-wide settings for all Teams apps in the tenant.
    teams_app_settings: Optional[teams_app_settings.TeamsAppSettings] = None
    # A workforce integration with shifts.
    workforce_integrations: Optional[List[workforce_integration.WorkforceIntegration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Teamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Teamwork
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Teamwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import deleted_team, entity, teams_app_settings, teamwork_device, team_template, workforce_integration

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedTeams": lambda n : setattr(self, 'deleted_teams', n.get_collection_of_object_values(deleted_team.DeletedTeam)),
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(teamwork_device.TeamworkDevice)),
            "teamsAppSettings": lambda n : setattr(self, 'teams_app_settings', n.get_object_value(teams_app_settings.TeamsAppSettings)),
            "teamTemplates": lambda n : setattr(self, 'team_templates', n.get_collection_of_object_values(team_template.TeamTemplate)),
            "workforceIntegrations": lambda n : setattr(self, 'workforce_integrations', n.get_collection_of_object_values(workforce_integration.WorkforceIntegration)),
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
        writer.write_collection_of_object_values("deletedTeams", self.deleted_teams)
        writer.write_collection_of_object_values("devices", self.devices)
        writer.write_object_value("teamsAppSettings", self.teams_app_settings)
        writer.write_collection_of_object_values("teamTemplates", self.team_templates)
        writer.write_collection_of_object_values("workforceIntegrations", self.workforce_integrations)
    

