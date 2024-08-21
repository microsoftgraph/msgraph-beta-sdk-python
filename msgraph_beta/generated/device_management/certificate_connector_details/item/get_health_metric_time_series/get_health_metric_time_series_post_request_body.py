from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.time_series_parameter import TimeSeriesParameter

@dataclass
class GetHealthMetricTimeSeriesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The timeSeries property
    time_series: Optional[TimeSeriesParameter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetHealthMetricTimeSeriesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetHealthMetricTimeSeriesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetHealthMetricTimeSeriesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.time_series_parameter import TimeSeriesParameter

        from .....models.time_series_parameter import TimeSeriesParameter

        fields: Dict[str, Callable[[Any], None]] = {
            "timeSeries": lambda n : setattr(self, 'time_series', n.get_object_value(TimeSeriesParameter)),
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
        writer.write_object_value("timeSeries", self.time_series)
        writer.write_additional_data_value(self.additional_data)
    

