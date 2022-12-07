from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_type = lazy_import('msgraph.generated.models.email_type')
item_facet = lazy_import('msgraph.generated.models.item_facet')

class ItemEmail(item_facet.ItemFacet):
    @property
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. The email address itself.
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. The email address itself.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ItemEmail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemEmail"
        # The email address itself.
        self._address: Optional[str] = None
        # The name or label a user has associated with a particular email address.
        self._display_name: Optional[str] = None
        # The type property
        self._type: Optional[email_type.EmailType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemEmail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemEmail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemEmail()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name or label a user has associated with a particular email address.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name or label a user has associated with a particular email address.
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
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(email_type.EmailType)),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[email_type.EmailType]:
        """
        Gets the type property value. The type property
        Returns: Optional[email_type.EmailType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[email_type.EmailType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

