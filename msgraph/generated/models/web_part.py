from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
site_page_data = lazy_import('msgraph.generated.models.site_page_data')

class WebPart(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new webPart and sets the default values.
        """
        super().__init__()
        # The data property
        self._data: Optional[site_page_data.SitePageData] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebPart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebPart
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebPart()
    
    @property
    def data(self,) -> Optional[site_page_data.SitePageData]:
        """
        Gets the data property value. The data property
        Returns: Optional[site_page_data.SitePageData]
        """
        return self._data
    
    @data.setter
    def data(self,value: Optional[site_page_data.SitePageData] = None) -> None:
        """
        Sets the data property value. The data property
        Args:
            value: Value to set for the data property.
        """
        self._data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(site_page_data.SitePageData)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_str_value("type", self.type)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

