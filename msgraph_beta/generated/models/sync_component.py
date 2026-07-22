from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sync_component_status import SyncComponentStatus

@dataclass
class SyncComponent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates additional information for this sync stage. This is a flexible string that can be null (no additional info), a progress indicator such as '3/6' (completed out of total), or a list of individual item names. Read-only. Nullable.
    more_info: Optional[str] = None
    # Indicates the sync stage name. The backend abstracts internal infrastructure into 6 user-facing stages. Fixed values are: notifyingDevice, deviceConnecting, policies, applications, scripts, compliance. Read-only. Not nullable.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the date and time when this stage last reported status. The date and time information is shown using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only. Not nullable.
    reported_date_time: Optional[datetime.datetime] = None
    # A list of possible status states for a sync infrastructure component or policy during a device sync operation.
    status: Optional[SyncComponentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SyncComponent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SyncComponent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SyncComponent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sync_component_status import SyncComponentStatus

        from .sync_component_status import SyncComponentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "moreInfo": lambda n : setattr(self, 'more_info', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reportedDateTime": lambda n : setattr(self, 'reported_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SyncComponentStatus)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

