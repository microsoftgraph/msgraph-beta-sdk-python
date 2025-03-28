from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teams_app import TeamsApp
    from .teams_tab_configuration import TeamsTabConfiguration

from .entity import Entity

@dataclass
class TeamsTab(Entity, Parsable):
    # Container for custom settings applied to a tab. The tab is considered configured only once this property is set.
    configuration: Optional[TeamsTabConfiguration] = None
    # Name of the tab.
    display_name: Optional[str] = None
    # The messageId property
    message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Index of the order used for sorting tabs.
    sort_order_index: Optional[str] = None
    # The application that is linked to the tab.
    teams_app: Optional[TeamsApp] = None
    # App definition identifier of the tab. This value can't be changed after tab creation. Because this property is deprecated, we recommend expanding teamsApp to retrieve the application that is linked to the tab.
    teams_app_id: Optional[str] = None
    # Deep link URL of the tab instance. Read only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsTab:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsTab
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsTab()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_tab_configuration import TeamsTabConfiguration

        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_tab_configuration import TeamsTabConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(TeamsTabConfiguration)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "sortOrderIndex": lambda n : setattr(self, 'sort_order_index', n.get_str_value()),
            "teamsApp": lambda n : setattr(self, 'teams_app', n.get_object_value(TeamsApp)),
            "teamsAppId": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("messageId", self.message_id)
        writer.write_str_value("sortOrderIndex", self.sort_order_index)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_str_value("webUrl", self.web_url)
    

