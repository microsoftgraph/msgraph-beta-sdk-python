from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import deleted_team, entity, teams_app_settings, teamwork_device, team_template, workforce_integration

from . import entity

class Teamwork(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Teamwork and sets the default values.
        """
        super().__init__()
        # A collection of deleted teams.
        self._deleted_teams: Optional[List[deleted_team.DeletedTeam]] = None
        # The Teams devices provisioned for the tenant.
        self._devices: Optional[List[teamwork_device.TeamworkDevice]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The templates associated with a team.
        self._team_templates: Optional[List[team_template.TeamTemplate]] = None
        # Represents tenant-wide settings for all Teams apps in the tenant.
        self._teams_app_settings: Optional[teams_app_settings.TeamsAppSettings] = None
        # A workforce integration with shifts.
        self._workforce_integrations: Optional[List[workforce_integration.WorkforceIntegration]] = None
    
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
    
    @property
    def deleted_teams(self,) -> Optional[List[deleted_team.DeletedTeam]]:
        """
        Gets the deletedTeams property value. A collection of deleted teams.
        Returns: Optional[List[deleted_team.DeletedTeam]]
        """
        return self._deleted_teams
    
    @deleted_teams.setter
    def deleted_teams(self,value: Optional[List[deleted_team.DeletedTeam]] = None) -> None:
        """
        Sets the deletedTeams property value. A collection of deleted teams.
        Args:
            value: Value to set for the deleted_teams property.
        """
        self._deleted_teams = value
    
    @property
    def devices(self,) -> Optional[List[teamwork_device.TeamworkDevice]]:
        """
        Gets the devices property value. The Teams devices provisioned for the tenant.
        Returns: Optional[List[teamwork_device.TeamworkDevice]]
        """
        return self._devices
    
    @devices.setter
    def devices(self,value: Optional[List[teamwork_device.TeamworkDevice]] = None) -> None:
        """
        Sets the devices property value. The Teams devices provisioned for the tenant.
        Args:
            value: Value to set for the devices property.
        """
        self._devices = value
    
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
    
    @property
    def team_templates(self,) -> Optional[List[team_template.TeamTemplate]]:
        """
        Gets the teamTemplates property value. The templates associated with a team.
        Returns: Optional[List[team_template.TeamTemplate]]
        """
        return self._team_templates
    
    @team_templates.setter
    def team_templates(self,value: Optional[List[team_template.TeamTemplate]] = None) -> None:
        """
        Sets the teamTemplates property value. The templates associated with a team.
        Args:
            value: Value to set for the team_templates property.
        """
        self._team_templates = value
    
    @property
    def teams_app_settings(self,) -> Optional[teams_app_settings.TeamsAppSettings]:
        """
        Gets the teamsAppSettings property value. Represents tenant-wide settings for all Teams apps in the tenant.
        Returns: Optional[teams_app_settings.TeamsAppSettings]
        """
        return self._teams_app_settings
    
    @teams_app_settings.setter
    def teams_app_settings(self,value: Optional[teams_app_settings.TeamsAppSettings] = None) -> None:
        """
        Sets the teamsAppSettings property value. Represents tenant-wide settings for all Teams apps in the tenant.
        Args:
            value: Value to set for the teams_app_settings property.
        """
        self._teams_app_settings = value
    
    @property
    def workforce_integrations(self,) -> Optional[List[workforce_integration.WorkforceIntegration]]:
        """
        Gets the workforceIntegrations property value. A workforce integration with shifts.
        Returns: Optional[List[workforce_integration.WorkforceIntegration]]
        """
        return self._workforce_integrations
    
    @workforce_integrations.setter
    def workforce_integrations(self,value: Optional[List[workforce_integration.WorkforceIntegration]] = None) -> None:
        """
        Sets the workforceIntegrations property value. A workforce integration with shifts.
        Args:
            value: Value to set for the workforce_integrations property.
        """
        self._workforce_integrations = value
    

