from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

retention_duration = lazy_import('msgraph.generated.models.security.retention_duration')

class RetentionDurationInDays(retention_duration.RetentionDuration):
    def __init__(self,) -> None:
        """
        Instantiates a new RetentionDurationInDays and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.retentionDurationInDays"
        # Specifies the time period in days for which an item with the applied retention label will be retained for.
        self._days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionDurationInDays:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionDurationInDays
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionDurationInDays()
    
    @property
    def days(self,) -> Optional[int]:
        """
        Gets the days property value. Specifies the time period in days for which an item with the applied retention label will be retained for.
        Returns: Optional[int]
        """
        return self._days
    
    @days.setter
    def days(self,value: Optional[int] = None) -> None:
        """
        Sets the days property value. Specifies the time period in days for which an item with the applied retention label will be retained for.
        Args:
            value: Value to set for the days property.
        """
        self._days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "days": lambda n : setattr(self, 'days', n.get_int_value()),
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
        writer.write_int_value("days", self.days)
    

