from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet, phone_type

from . import item_facet

class ItemPhone(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemPhone and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemPhone"
        # Friendly name the user has assigned this phone number.
        self._display_name: Optional[str] = None
        # Phone number provided by the user.
        self._number: Optional[str] = None
        # The type property
        self._type: Optional[phone_type.PhoneType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemPhone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemPhone
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemPhone()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Friendly name the user has assigned this phone number.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Friendly name the user has assigned this phone number.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet, phone_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(phone_type.PhoneType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. Phone number provided by the user.
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. Phone number provided by the user.
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("number", self.number)
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[phone_type.PhoneType]:
        """
        Gets the type property value. The type property
        Returns: Optional[phone_type.PhoneType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[phone_type.PhoneType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

