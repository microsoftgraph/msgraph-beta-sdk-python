from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_link

class SectionLinks(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sectionLinks and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Opens the section in the OneNote native client if it's installed.
        self._one_note_client_url: Optional[external_link.ExternalLink] = None
        # Opens the section in OneNote on the web.
        self._one_note_web_url: Optional[external_link.ExternalLink] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SectionLinks:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SectionLinks
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SectionLinks()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_link

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oneNoteClientUrl": lambda n : setattr(self, 'one_note_client_url', n.get_object_value(external_link.ExternalLink)),
            "oneNoteWebUrl": lambda n : setattr(self, 'one_note_web_url', n.get_object_value(external_link.ExternalLink)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def one_note_client_url(self,) -> Optional[external_link.ExternalLink]:
        """
        Gets the oneNoteClientUrl property value. Opens the section in the OneNote native client if it's installed.
        Returns: Optional[external_link.ExternalLink]
        """
        return self._one_note_client_url
    
    @one_note_client_url.setter
    def one_note_client_url(self,value: Optional[external_link.ExternalLink] = None) -> None:
        """
        Sets the oneNoteClientUrl property value. Opens the section in the OneNote native client if it's installed.
        Args:
            value: Value to set for the one_note_client_url property.
        """
        self._one_note_client_url = value
    
    @property
    def one_note_web_url(self,) -> Optional[external_link.ExternalLink]:
        """
        Gets the oneNoteWebUrl property value. Opens the section in OneNote on the web.
        Returns: Optional[external_link.ExternalLink]
        """
        return self._one_note_web_url
    
    @one_note_web_url.setter
    def one_note_web_url(self,value: Optional[external_link.ExternalLink] = None) -> None:
        """
        Sets the oneNoteWebUrl property value. Opens the section in OneNote on the web.
        Args:
            value: Value to set for the one_note_web_url property.
        """
        self._one_note_web_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("oneNoteClientUrl", self.one_note_client_url)
        writer.write_object_value("oneNoteWebUrl", self.one_note_web_url)
        writer.write_additional_data_value(self.additional_data)
    

