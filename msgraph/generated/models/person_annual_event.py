from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_facet, person_annual_event_type

from . import item_facet

class PersonAnnualEvent(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new PersonAnnualEvent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personAnnualEvent"
        # The date property
        self._date: Optional[date] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The type property
        self._type: Optional[person_annual_event_type.PersonAnnualEventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonAnnualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonAnnualEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonAnnualEvent()
    
    @property
    def date(self,) -> Optional[date]:
        """
        Gets the date property value. The date property
        Returns: Optional[date]
        """
        return self._date
    
    @date.setter
    def date(self,value: Optional[date] = None) -> None:
        """
        Sets the date property value. The date property
        Args:
            value: Value to set for the date property.
        """
        self._date = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_facet, person_annual_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(person_annual_event_type.PersonAnnualEventType)),
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
        writer.write_date_value("date", self.date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[person_annual_event_type.PersonAnnualEventType]:
        """
        Gets the type property value. The type property
        Returns: Optional[person_annual_event_type.PersonAnnualEventType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[person_annual_event_type.PersonAnnualEventType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

