from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .cloud_pc_status_details import CloudPcStatusDetails

@dataclass
class CloudPcRemoteActionResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The specified action. Supported values in the Microsoft Endpoint Manager portal are: Reprovision, Resize, Restore. Supported values in enterprise Cloud PC devices are: Reboot, Rename, Reprovision, Troubleshoot.
    action_name: Optional[str] = None
    # State of the action. Possible values are: None, pending, canceled, active, done, failed, notSupported. Read-only.
    action_state: Optional[ActionState] = None
    # The ID of the Cloud PC device on which the remote action is performed. Read-only.
    cloud_pc_id: Optional[str] = None
    # Last update time for action. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The ID of the Intune managed device on which the remote action is performed. Read-only.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time the action was initiated. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
    start_date_time: Optional[datetime.datetime] = None
    # The details of the Cloud PC status.
    status_details: Optional[CloudPcStatusDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRemoteActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRemoteActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcRemoteActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .cloud_pc_status_details import CloudPcStatusDetails

        from .action_state import ActionState
        from .cloud_pc_status_details import CloudPcStatusDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(ActionState)),
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_object_value(CloudPcStatusDetails)),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_object_value("statusDetails", self.status_details)
        writer.write_additional_data_value(self.additional_data)
    

