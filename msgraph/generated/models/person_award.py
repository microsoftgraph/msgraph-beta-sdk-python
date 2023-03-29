from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet

from . import item_facet

class PersonAward(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new PersonAward and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personAward"
        # Descpription of the award or honor.
        self._description: Optional[str] = None
        # Name of the award or honor.
        self._display_name: Optional[str] = None
        # The date that the award or honor was granted.
        self._issued_date: Optional[date] = None
        # Authority which granted the award or honor.
        self._issuing_authority: Optional[str] = None
        # URL referencing a thumbnail of the award or honor.
        self._thumbnail_url: Optional[str] = None
        # URL referencing the award or honor.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonAward:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonAward
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonAward()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Descpription of the award or honor.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Descpription of the award or honor.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the award or honor.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the award or honor.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "issuedDate": lambda n : setattr(self, 'issued_date', n.get_date_value()),
            "issuingAuthority": lambda n : setattr(self, 'issuing_authority', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issued_date(self,) -> Optional[date]:
        """
        Gets the issuedDate property value. The date that the award or honor was granted.
        Returns: Optional[date]
        """
        return self._issued_date
    
    @issued_date.setter
    def issued_date(self,value: Optional[date] = None) -> None:
        """
        Sets the issuedDate property value. The date that the award or honor was granted.
        Args:
            value: Value to set for the issued_date property.
        """
        self._issued_date = value
    
    @property
    def issuing_authority(self,) -> Optional[str]:
        """
        Gets the issuingAuthority property value. Authority which granted the award or honor.
        Returns: Optional[str]
        """
        return self._issuing_authority
    
    @issuing_authority.setter
    def issuing_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the issuingAuthority property value. Authority which granted the award or honor.
        Args:
            value: Value to set for the issuing_authority property.
        """
        self._issuing_authority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("issuedDate", self.issued_date)
        writer.write_str_value("issuingAuthority", self.issuing_authority)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. URL referencing a thumbnail of the award or honor.
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. URL referencing a thumbnail of the award or honor.
        Args:
            value: Value to set for the thumbnail_url property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL referencing the award or honor.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL referencing the award or honor.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

