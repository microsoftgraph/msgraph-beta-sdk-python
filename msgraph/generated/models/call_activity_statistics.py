from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_statistics = lazy_import('msgraph.generated.models.activity_statistics')

class CallActivityStatistics(activity_statistics.ActivityStatistics):
    @property
    def after_hours(self,) -> Optional[Timedelta]:
        """
        Gets the afterHours property value. Time spent on calls outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the afterHours property value. Time spent on calls outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the afterHours property.
        """
        self._after_hours = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CallActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callActivityStatistics"
        # Time spent on calls outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallActivityStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "after_hours": lambda n : setattr(self, 'after_hours', n.get_object_value(Timedelta)),
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
        writer.write_object_value("afterHours", self.after_hours)
    

