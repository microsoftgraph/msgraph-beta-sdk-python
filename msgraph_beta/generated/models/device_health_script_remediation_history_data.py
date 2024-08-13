from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceHealthScriptRemediationHistoryData(AdditionalDataHolder, BackedModel, Parsable):
    """
    The number of devices remediated by a device health script on a given date.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The date on which devices were remediated by the device health script.
    date: Optional[datetime.date] = None
    # The number of devices for which the detection script found an issue.
    detect_failed_device_count: Optional[int] = None
    # The number of devices that were found to have no issue by the device health script.
    no_issue_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of devices remediated by the device health script.
    remediated_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptRemediationHistoryData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptRemediationHistoryData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptRemediationHistoryData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "detectFailedDeviceCount": lambda n : setattr(self, 'detect_failed_device_count', n.get_int_value()),
            "noIssueDeviceCount": lambda n : setattr(self, 'no_issue_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediatedDeviceCount": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
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
        writer.write_date_value("date", self.date)
        writer.write_int_value("detectFailedDeviceCount", self.detect_failed_device_count)
        writer.write_int_value("noIssueDeviceCount", self.no_issue_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_additional_data_value(self.additional_data)
    

