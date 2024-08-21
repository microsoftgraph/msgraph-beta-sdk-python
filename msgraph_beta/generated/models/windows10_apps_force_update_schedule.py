from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows10_apps_update_recurrence import Windows10AppsUpdateRecurrence

@dataclass
class Windows10AppsForceUpdateSchedule(AdditionalDataHolder, BackedModel, Parsable):
    """
    Windows 10 force update schedule for Apps
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Possible values for App update on Windows10 recurrence.
    recurrence: Optional[Windows10AppsUpdateRecurrence] = None
    # If true, runs the task immediately if StartDateTime is in the past, else, runs at the next recurrence.
    run_immediately_if_after_start_date_time: Optional[bool] = None
    # The start time for the force restart.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10AppsForceUpdateSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10AppsForceUpdateSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10AppsForceUpdateSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows10_apps_update_recurrence import Windows10AppsUpdateRecurrence

        from .windows10_apps_update_recurrence import Windows10AppsUpdateRecurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_enum_value(Windows10AppsUpdateRecurrence)),
            "runImmediatelyIfAfterStartDateTime": lambda n : setattr(self, 'run_immediately_if_after_start_date_time', n.get_bool_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_enum_value("recurrence", self.recurrence)
        writer.write_bool_value("runImmediatelyIfAfterStartDateTime", self.run_immediately_if_after_start_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

