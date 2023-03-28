from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity, teamwork_application_identity_type

from . import identity

class TeamworkApplicationIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkApplicationIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamworkApplicationIdentity"
        # Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, and outgoingWebhook.
        self._application_identity_type: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType] = None
    
    @property
    def application_identity_type(self,) -> Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType]:
        """
        Gets the applicationIdentityType property value. Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, and outgoingWebhook.
        Returns: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType]
        """
        return self._application_identity_type
    
    @application_identity_type.setter
    def application_identity_type(self,value: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType] = None) -> None:
        """
        Sets the applicationIdentityType property value. Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, and outgoingWebhook.
        Args:
            value: Value to set for the application_identity_type property.
        """
        self._application_identity_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkApplicationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkApplicationIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkApplicationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity, teamwork_application_identity_type

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationIdentityType": lambda n : setattr(self, 'application_identity_type', n.get_enum_value(teamwork_application_identity_type.TeamworkApplicationIdentityType)),
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
        writer.write_enum_value("applicationIdentityType", self.application_identity_type)
    

