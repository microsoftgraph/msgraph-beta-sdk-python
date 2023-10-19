from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_health_script_remediation_history_data import DeviceHealthScriptRemediationHistoryData

@dataclass
class DeviceHealthScriptRemediationHistory(AdditionalDataHolder, BackedModel, Parsable):
    """
    The number of devices remediated by a device health script on a given date with the last modified time.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of devices remediated by the device health script on the given date.
    history_data: Optional[List[DeviceHealthScriptRemediationHistoryData]] = None
    # The date on which the results history is calculated for the healthscript.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthScriptRemediationHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRemediationHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptRemediationHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_health_script_remediation_history_data import DeviceHealthScriptRemediationHistoryData

        from .device_health_script_remediation_history_data import DeviceHealthScriptRemediationHistoryData

        fields: Dict[str, Callable[[Any], None]] = {
            "historyData": lambda n : setattr(self, 'history_data', n.get_collection_of_object_values(DeviceHealthScriptRemediationHistoryData)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("historyData", self.history_data)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

