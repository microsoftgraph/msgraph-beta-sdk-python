from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, teams_app, teams_app_definition, teams_app_permission_set, user_scope_teams_app_installation

from . import entity

class TeamsAppInstallation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppInstallation and sets the default values.
        """
        super().__init__()
        # The set of resource-specific permissions consented to while installing or upgrading the teamsApp.
        self._consented_permission_set: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The app that is installed.
        self._teams_app: Optional[teams_app.TeamsApp] = None
        # The details of this version of the app.
        self._teams_app_definition: Optional[teams_app_definition.TeamsAppDefinition] = None
    
    @property
    def consented_permission_set(self,) -> Optional[teams_app_permission_set.TeamsAppPermissionSet]:
        """
        Gets the consentedPermissionSet property value. The set of resource-specific permissions consented to while installing or upgrading the teamsApp.
        Returns: Optional[teams_app_permission_set.TeamsAppPermissionSet]
        """
        return self._consented_permission_set
    
    @consented_permission_set.setter
    def consented_permission_set(self,value: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None) -> None:
        """
        Sets the consentedPermissionSet property value. The set of resource-specific permissions consented to while installing or upgrading the teamsApp.
        Args:
            value: Value to set for the consented_permission_set property.
        """
        self._consented_permission_set = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.userScopeTeamsAppInstallation":
                from . import user_scope_teams_app_installation

                return user_scope_teams_app_installation.UserScopeTeamsAppInstallation()
        return TeamsAppInstallation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, teams_app, teams_app_definition, teams_app_permission_set, user_scope_teams_app_installation

        fields: Dict[str, Callable[[Any], None]] = {
            "consentedPermissionSet": lambda n : setattr(self, 'consented_permission_set', n.get_object_value(teams_app_permission_set.TeamsAppPermissionSet)),
            "teamsApp": lambda n : setattr(self, 'teams_app', n.get_object_value(teams_app.TeamsApp)),
            "teamsAppDefinition": lambda n : setattr(self, 'teams_app_definition', n.get_object_value(teams_app_definition.TeamsAppDefinition)),
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
        writer.write_object_value("consentedPermissionSet", self.consented_permission_set)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_object_value("teamsAppDefinition", self.teams_app_definition)
    
    @property
    def teams_app(self,) -> Optional[teams_app.TeamsApp]:
        """
        Gets the teamsApp property value. The app that is installed.
        Returns: Optional[teams_app.TeamsApp]
        """
        return self._teams_app
    
    @teams_app.setter
    def teams_app(self,value: Optional[teams_app.TeamsApp] = None) -> None:
        """
        Sets the teamsApp property value. The app that is installed.
        Args:
            value: Value to set for the teams_app property.
        """
        self._teams_app = value
    
    @property
    def teams_app_definition(self,) -> Optional[teams_app_definition.TeamsAppDefinition]:
        """
        Gets the teamsAppDefinition property value. The details of this version of the app.
        Returns: Optional[teams_app_definition.TeamsAppDefinition]
        """
        return self._teams_app_definition
    
    @teams_app_definition.setter
    def teams_app_definition(self,value: Optional[teams_app_definition.TeamsAppDefinition] = None) -> None:
        """
        Sets the teamsAppDefinition property value. The details of this version of the app.
        Args:
            value: Value to set for the teams_app_definition property.
        """
        self._teams_app_definition = value
    

