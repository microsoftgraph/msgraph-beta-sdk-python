from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class EducationGradingCategory(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationGradingCategory and sets the default values.
        """
        super().__init__()
        # The name of the grading category.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The weight of the category; an integer between 0 and 100.
        self._percentage_weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationGradingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationGradingCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationGradingCategory()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the grading category.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the grading category.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "percentageWeight": lambda n : setattr(self, 'percentage_weight', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def percentage_weight(self,) -> Optional[int]:
        """
        Gets the percentageWeight property value. The weight of the category; an integer between 0 and 100.
        Returns: Optional[int]
        """
        return self._percentage_weight
    
    @percentage_weight.setter
    def percentage_weight(self,value: Optional[int] = None) -> None:
        """
        Sets the percentageWeight property value. The weight of the category; an integer between 0 and 100.
        Args:
            value: Value to set for the percentage_weight property.
        """
        self._percentage_weight = value
    
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
        writer.write_int_value("percentageWeight", self.percentage_weight)
    

