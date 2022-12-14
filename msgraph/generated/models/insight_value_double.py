from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_experience_analytics_insight_value = lazy_import('msgraph.generated.models.user_experience_analytics_insight_value')

class InsightValueDouble(user_experience_analytics_insight_value.UserExperienceAnalyticsInsightValue):
    def __init__(self,) -> None:
        """
        Instantiates a new InsightValueDouble and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.insightValueDouble"
        # Not yet documented
        self._value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InsightValueDouble:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InsightValueDouble
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InsightValueDouble()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        writer.write_float_value("value", self.value)
    
    @property
    def value(self,) -> Optional[float]:
        """
        Gets the value property value. Not yet documented
        Returns: Optional[float]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[float] = None) -> None:
        """
        Sets the value property value. Not yet documented
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

