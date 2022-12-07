from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
teamwork_hosted_content = lazy_import('msgraph.generated.models.teamwork_hosted_content')

class TeamsAppIcon(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppIcon and sets the default values.
        """
        super().__init__()
        # The contents of the app icon if the icon is hosted within the Teams infrastructure.
        self._hosted_content: Optional[teamwork_hosted_content.TeamworkHostedContent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The web URL that can be used for downloading the image.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppIcon:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppIcon
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppIcon()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hosted_content": lambda n : setattr(self, 'hosted_content', n.get_object_value(teamwork_hosted_content.TeamworkHostedContent)),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hosted_content(self,) -> Optional[teamwork_hosted_content.TeamworkHostedContent]:
        """
        Gets the hostedContent property value. The contents of the app icon if the icon is hosted within the Teams infrastructure.
        Returns: Optional[teamwork_hosted_content.TeamworkHostedContent]
        """
        return self._hosted_content
    
    @hosted_content.setter
    def hosted_content(self,value: Optional[teamwork_hosted_content.TeamworkHostedContent] = None) -> None:
        """
        Sets the hostedContent property value. The contents of the app icon if the icon is hosted within the Teams infrastructure.
        Args:
            value: Value to set for the hostedContent property.
        """
        self._hosted_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("hostedContent", self.hosted_content)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The web URL that can be used for downloading the image.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The web URL that can be used for downloading the image.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

