from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PersonNamePronounciation(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new personNamePronounciation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The displayName property
        self._display_name: Optional[str] = None
        # The first property
        self._first: Optional[str] = None
        # The last property
        self._last: Optional[str] = None
        # The maiden property
        self._maiden: Optional[str] = None
        # The middle property
        self._middle: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonNamePronounciation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonNamePronounciation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonNamePronounciation()
    
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
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def first(self,) -> Optional[str]:
        """
        Gets the first property value. The first property
        Returns: Optional[str]
        """
        return self._first
    
    @first.setter
    def first(self,value: Optional[str] = None) -> None:
        """
        Sets the first property value. The first property
        Args:
            value: Value to set for the first property.
        """
        self._first = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "first": lambda n : setattr(self, 'first', n.get_str_value()),
            "last": lambda n : setattr(self, 'last', n.get_str_value()),
            "maiden": lambda n : setattr(self, 'maiden', n.get_str_value()),
            "middle": lambda n : setattr(self, 'middle', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last(self,) -> Optional[str]:
        """
        Gets the last property value. The last property
        Returns: Optional[str]
        """
        return self._last
    
    @last.setter
    def last(self,value: Optional[str] = None) -> None:
        """
        Sets the last property value. The last property
        Args:
            value: Value to set for the last property.
        """
        self._last = value
    
    @property
    def maiden(self,) -> Optional[str]:
        """
        Gets the maiden property value. The maiden property
        Returns: Optional[str]
        """
        return self._maiden
    
    @maiden.setter
    def maiden(self,value: Optional[str] = None) -> None:
        """
        Sets the maiden property value. The maiden property
        Args:
            value: Value to set for the maiden property.
        """
        self._maiden = value
    
    @property
    def middle(self,) -> Optional[str]:
        """
        Gets the middle property value. The middle property
        Returns: Optional[str]
        """
        return self._middle
    
    @middle.setter
    def middle(self,value: Optional[str] = None) -> None:
        """
        Sets the middle property value. The middle property
        Args:
            value: Value to set for the middle property.
        """
        self._middle = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("first", self.first)
        writer.write_str_value("last", self.last)
        writer.write_str_value("maiden", self.maiden)
        writer.write_str_value("middle", self.middle)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

