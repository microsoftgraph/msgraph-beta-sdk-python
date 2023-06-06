from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity

@dataclass
class SharingLink(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The app the link is associated with.
    application: Optional[identity.Identity] = None
    # The configuratorUrl property
    configurator_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If true then the user can only use this link to view the item on the web, and cannot use it to download the contents of the item. Only for OneDrive for Business and SharePoint.
    prevents_download: Optional[bool] = None
    # The scope of the link represented by this permission. Value anonymous indicates the link is usable by anyone, organization indicates the link is only usable for users signed into the same tenant.
    scope: Optional[str] = None
    # The type of the link created.
    type: Optional[str] = None
    # For embed links, this property contains the HTML code for an <iframe> element that will embed the item in a webpage.
    web_html: Optional[str] = None
    # A URL that opens the item in the browser on the OneDrive website.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingLink
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharingLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(identity.Identity)),
            "configuratorUrl": lambda n : setattr(self, 'configurator_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preventsDownload": lambda n : setattr(self, 'prevents_download', n.get_bool_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "webHtml": lambda n : setattr(self, 'web_html', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("application", self.application)
        writer.write_str_value("configuratorUrl", self.configurator_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("preventsDownload", self.prevents_download)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_str_value("webHtml", self.web_html)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

