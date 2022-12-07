from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsMetric(entity.Entity):
    """
    The user experience analytics metric contains the score and units of a metric of a user experience anlaytics category.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsMetric and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unit of the user experience analytics metric.
        self._unit: Optional[str] = None
        # The value of the user experience analytics metric.
        self._value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsMetric
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "unit": lambda n : setattr(self, 'unit', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
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
        writer.write_str_value("unit", self.unit)
        writer.write_float_value("value", self.value)
    
    @property
    def unit(self,) -> Optional[str]:
        """
        Gets the unit property value. The unit of the user experience analytics metric.
        Returns: Optional[str]
        """
        return self._unit
    
    @unit.setter
    def unit(self,value: Optional[str] = None) -> None:
        """
        Sets the unit property value. The unit of the user experience analytics metric.
        Args:
            value: Value to set for the unit property.
        """
        self._unit = value
    
    @property
    def value(self,) -> Optional[float]:
        """
        Gets the value property value. The value of the user experience analytics metric.
        Returns: Optional[float]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[float] = None) -> None:
        """
        Sets the value property value. The value of the user experience analytics metric.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

