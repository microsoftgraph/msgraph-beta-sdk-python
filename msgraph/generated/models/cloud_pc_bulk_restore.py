from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .restore_time_range import RestoreTimeRange

from .cloud_pc_bulk_action import CloudPcBulkAction

@dataclass
class CloudPcBulkRestore(CloudPcBulkAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcBulkRestore"
    # The restorePointDateTime property
    restore_point_date_time: Optional[datetime.datetime] = None
    # The timeRange property
    time_range: Optional[RestoreTimeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcBulkRestore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkRestore
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkRestore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .restore_time_range import RestoreTimeRange

        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .restore_time_range import RestoreTimeRange

        fields: Dict[str, Callable[[Any], None]] = {
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "timeRange": lambda n : setattr(self, 'time_range', n.get_enum_value(RestoreTimeRange)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_enum_value("timeRange", self.time_range)
    

