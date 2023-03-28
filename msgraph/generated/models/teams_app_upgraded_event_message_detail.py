from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set

from . import event_message_detail

class TeamsAppUpgradedEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamsAppUpgradedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamsAppUpgradedEventMessageDetail"
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # Display name of the teamsApp.
        self._teams_app_display_name: Optional[str] = None
        # Unique identifier of the teamsApp.
        self._teams_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppUpgradedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppUpgradedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppUpgradedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "teamsAppDisplayName": lambda n : setattr(self, 'teams_app_display_name', n.get_str_value()),
            "teamsAppId": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("teamsAppDisplayName", self.teams_app_display_name)
        writer.write_str_value("teamsAppId", self.teams_app_id)
    
    @property
    def teams_app_display_name(self,) -> Optional[str]:
        """
        Gets the teamsAppDisplayName property value. Display name of the teamsApp.
        Returns: Optional[str]
        """
        return self._teams_app_display_name
    
    @teams_app_display_name.setter
    def teams_app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsAppDisplayName property value. Display name of the teamsApp.
        Args:
            value: Value to set for the teams_app_display_name property.
        """
        self._teams_app_display_name = value
    
    @property
    def teams_app_id(self,) -> Optional[str]:
        """
        Gets the teamsAppId property value. Unique identifier of the teamsApp.
        Returns: Optional[str]
        """
        return self._teams_app_id
    
    @teams_app_id.setter
    def teams_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsAppId property value. Unique identifier of the teamsApp.
        Args:
            value: Value to set for the teams_app_id property.
        """
        self._teams_app_id = value
    

