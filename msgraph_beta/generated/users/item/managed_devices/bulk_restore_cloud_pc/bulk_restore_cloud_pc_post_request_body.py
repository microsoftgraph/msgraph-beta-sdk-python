from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.restore_time_range import RestoreTimeRange

@dataclass
class BulkRestoreCloudPcPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The managedDeviceIds property
    managed_device_ids: Optional[List[str]] = None
    # The restorePointDateTime property
    restore_point_date_time: Optional[datetime.datetime] = None
    # The timeRange property
    time_range: Optional[RestoreTimeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BulkRestoreCloudPcPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkRestoreCloudPcPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BulkRestoreCloudPcPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.restore_time_range import RestoreTimeRange

        from .....models.restore_time_range import RestoreTimeRange

        fields: Dict[str, Callable[[Any], None]] = {
            "managedDeviceIds": lambda n : setattr(self, 'managed_device_ids', n.get_collection_of_primitive_values(str)),
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "timeRange": lambda n : setattr(self, 'time_range', n.get_enum_value(RestoreTimeRange)),
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
        writer.write_collection_of_primitive_values("managedDeviceIds", self.managed_device_ids)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_enum_value("timeRange", self.time_range)
        writer.write_additional_data_value(self.additional_data)
    

