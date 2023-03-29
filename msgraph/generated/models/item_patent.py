from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet

from . import item_facet

class ItemPatent(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemPatent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemPatent"
        # Descpription of the patent or filing.
        self._description: Optional[str] = None
        # Title of the patent or filing.
        self._display_name: Optional[str] = None
        # Indicates the patent is pending.
        self._is_pending: Optional[bool] = None
        # The date that the patent was granted.
        self._issued_date: Optional[date] = None
        # Authority which granted the patent.
        self._issuing_authority: Optional[str] = None
        # The patent number.
        self._number: Optional[str] = None
        # URL referencing the patent or filing.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemPatent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemPatent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemPatent()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Descpription of the patent or filing.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Descpription of the patent or filing.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Title of the patent or filing.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Title of the patent or filing.
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
            "isPending": lambda n : setattr(self, 'is_pending', n.get_bool_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_pending(self,) -> Optional[bool]:
        """
        Gets the isPending property value. Indicates the patent is pending.
        Returns: Optional[bool]
        """
        return self._is_pending
    
    @is_pending.setter
    def is_pending(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPending property value. Indicates the patent is pending.
        Args:
            value: Value to set for the is_pending property.
        """
        self._is_pending = value
    
    @property
    def issued_date(self,) -> Optional[date]:
        """
        Gets the issuedDate property value. The date that the patent was granted.
        Returns: Optional[date]
        """
        return self._issued_date
    
    @issued_date.setter
    def issued_date(self,value: Optional[date] = None) -> None:
        """
        Sets the issuedDate property value. The date that the patent was granted.
        Args:
            value: Value to set for the issued_date property.
        """
        self._issued_date = value
    
    @property
    def issuing_authority(self,) -> Optional[str]:
        """
        Gets the issuingAuthority property value. Authority which granted the patent.
        Returns: Optional[str]
        """
        return self._issuing_authority
    
    @issuing_authority.setter
    def issuing_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the issuingAuthority property value. Authority which granted the patent.
        Args:
            value: Value to set for the issuing_authority property.
        """
        self._issuing_authority = value
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The patent number.
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The patent number.
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
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
        writer.write_bool_value("isPending", self.is_pending)
        writer.write_str_value("number", self.number)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL referencing the patent or filing.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL referencing the patent or filing.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

