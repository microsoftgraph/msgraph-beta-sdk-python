from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
teams_app = lazy_import('msgraph.generated.models.teams_app')
teams_tab_configuration = lazy_import('msgraph.generated.models.teams_tab_configuration')

class TeamsTab(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def configuration(self,) -> Optional[teams_tab_configuration.TeamsTabConfiguration]:
        """
        Gets the configuration property value. Container for custom settings applied to a tab. The tab is considered configured only once this property is set.
        Returns: Optional[teams_tab_configuration.TeamsTabConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[teams_tab_configuration.TeamsTabConfiguration] = None) -> None:
        """
        Sets the configuration property value. Container for custom settings applied to a tab. The tab is considered configured only once this property is set.
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamsTab and sets the default values.
        """
        super().__init__()
        # Container for custom settings applied to a tab. The tab is considered configured only once this property is set.
        self._configuration: Optional[teams_tab_configuration.TeamsTabConfiguration] = None
        # Name of the tab.
        self._display_name: Optional[str] = None
        # The messageId property
        self._message_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Index of the order used for sorting tabs.
        self._sort_order_index: Optional[str] = None
        # The application that is linked to the tab.
        self._teams_app: Optional[teams_app.TeamsApp] = None
        # The teamsAppId property
        self._teams_app_id: Optional[str] = None
        # Deep link URL of the tab instance. Read only.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsTab:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsTab
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsTab()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the tab.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the tab.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(teams_tab_configuration.TeamsTabConfiguration)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "message_id": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "sort_order_index": lambda n : setattr(self, 'sort_order_index', n.get_str_value()),
            "teams_app": lambda n : setattr(self, 'teams_app', n.get_object_value(teams_app.TeamsApp)),
            "teams_app_id": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message_id(self,) -> Optional[str]:
        """
        Gets the messageId property value. The messageId property
        Returns: Optional[str]
        """
        return self._message_id
    
    @message_id.setter
    def message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the messageId property value. The messageId property
        Args:
            value: Value to set for the messageId property.
        """
        self._message_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("messageId", self.message_id)
        writer.write_str_value("sortOrderIndex", self.sort_order_index)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def sort_order_index(self,) -> Optional[str]:
        """
        Gets the sortOrderIndex property value. Index of the order used for sorting tabs.
        Returns: Optional[str]
        """
        return self._sort_order_index
    
    @sort_order_index.setter
    def sort_order_index(self,value: Optional[str] = None) -> None:
        """
        Sets the sortOrderIndex property value. Index of the order used for sorting tabs.
        Args:
            value: Value to set for the sortOrderIndex property.
        """
        self._sort_order_index = value
    
    @property
    def teams_app(self,) -> Optional[teams_app.TeamsApp]:
        """
        Gets the teamsApp property value. The application that is linked to the tab.
        Returns: Optional[teams_app.TeamsApp]
        """
        return self._teams_app
    
    @teams_app.setter
    def teams_app(self,value: Optional[teams_app.TeamsApp] = None) -> None:
        """
        Sets the teamsApp property value. The application that is linked to the tab.
        Args:
            value: Value to set for the teamsApp property.
        """
        self._teams_app = value
    
    @property
    def teams_app_id(self,) -> Optional[str]:
        """
        Gets the teamsAppId property value. The teamsAppId property
        Returns: Optional[str]
        """
        return self._teams_app_id
    
    @teams_app_id.setter
    def teams_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsAppId property value. The teamsAppId property
        Args:
            value: Value to set for the teamsAppId property.
        """
        self._teams_app_id = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Deep link URL of the tab instance. Read only.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Deep link URL of the tab instance. Read only.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

