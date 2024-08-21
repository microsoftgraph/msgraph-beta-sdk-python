from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_of_week import DayOfWeek

@dataclass
class CustomUpdateTimeWindow(AdditionalDataHolder, BackedModel, Parsable):
    """
    Custom update time window
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The endDay property
    end_day: Optional[DayOfWeek] = None
    # End time of the time window
    end_time: Optional[datetime.time] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDay property
    start_day: Optional[DayOfWeek] = None
    # Start time of the time window
    start_time: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomUpdateTimeWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomUpdateTimeWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomUpdateTimeWindow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .day_of_week import DayOfWeek

        from .day_of_week import DayOfWeek

        fields: Dict[str, Callable[[Any], None]] = {
            "endDay": lambda n : setattr(self, 'end_day', n.get_enum_value(DayOfWeek)),
            "endTime": lambda n : setattr(self, 'end_time', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDay": lambda n : setattr(self, 'start_day', n.get_enum_value(DayOfWeek)),
            "startTime": lambda n : setattr(self, 'start_time', n.get_time_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("endDay", self.end_day)
        writer.write_time_value("endTime", self.end_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("startDay", self.start_day)
        writer.write_time_value("startTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)
    

