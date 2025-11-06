from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_imported_snapshot_state import CloudPcImportedSnapshotState
    from .cloud_pc_snapshot_import_action_status import CloudPcSnapshotImportActionStatus

@dataclass
class CloudPcSnapshotImportActionResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # More details about the snapshot import action. For example, The snapshot import has failed because the file format is incorrect. This property only contains a value when errors occur during the process. Read-only.
    additional_detail: Optional[str] = None
    # The assigned user's principal name. For example, ryan@contoso.com.
    assigned_user_principal_name: Optional[str] = None
    # The end time of the snapshot import action. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appear as 2014-01-01T00:00:00Z. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # The file name for the imported snapshot. For example: MyCloudPc.vhd. Read-only.
    filename: Optional[str] = None
    # The importStatus property
    import_status: Optional[CloudPcSnapshotImportActionStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the assigned provisioning policy for the upload action. This policy takes effect if a new Cloud PC is provisioned. For example, MyProvisioningPolicy. Read-only.
    policy_name: Optional[str] = None
    # The unique identifier for the imported snapshot. For example, d09ae73d-b70f-4836-95c1-59652c947e1c. Read-only.
    snapshot_id: Optional[str] = None
    # The start time of the snapshot import action. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appear as 2014-01-01T00:00:00Z. Read-only.
    start_date_time: Optional[datetime.datetime] = None
    # The usageStatus property
    usage_status: Optional[CloudPcImportedSnapshotState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSnapshotImportActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSnapshotImportActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSnapshotImportActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_imported_snapshot_state import CloudPcImportedSnapshotState
        from .cloud_pc_snapshot_import_action_status import CloudPcSnapshotImportActionStatus

        from .cloud_pc_imported_snapshot_state import CloudPcImportedSnapshotState
        from .cloud_pc_snapshot_import_action_status import CloudPcSnapshotImportActionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "additionalDetail": lambda n : setattr(self, 'additional_detail', n.get_str_value()),
            "assignedUserPrincipalName": lambda n : setattr(self, 'assigned_user_principal_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "importStatus": lambda n : setattr(self, 'import_status', n.get_enum_value(CloudPcSnapshotImportActionStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "snapshotId": lambda n : setattr(self, 'snapshot_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "usageStatus": lambda n : setattr(self, 'usage_status', n.get_enum_value(CloudPcImportedSnapshotState)),
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
        writer.write_str_value("additionalDetail", self.additional_detail)
        writer.write_str_value("assignedUserPrincipalName", self.assigned_user_principal_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("filename", self.filename)
        writer.write_enum_value("importStatus", self.import_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("snapshotId", self.snapshot_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("usageStatus", self.usage_status)
        writer.write_additional_data_value(self.additional_data)
    

