from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_settings

from . import access_review_settings

class BusinessFlowSettings(access_review_settings.AccessReviewSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new BusinessFlowSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.businessFlowSettings"
        # The durationInDays property
        self._duration_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessFlowSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessFlowSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessFlowSettings()
    
    @property
    def duration_in_days(self,) -> Optional[int]:
        """
        Gets the durationInDays property value. The durationInDays property
        Returns: Optional[int]
        """
        return self._duration_in_days
    
    @duration_in_days.setter
    def duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInDays property value. The durationInDays property
        Args:
            value: Value to set for the duration_in_days property.
        """
        self._duration_in_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
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
        writer.write_int_value("durationInDays", self.duration_in_days)
    

