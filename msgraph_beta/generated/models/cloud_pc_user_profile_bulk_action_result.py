from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_user_profile_snapshot_create_bulk_action_result import CloudPcUserProfileSnapshotCreateBulkActionResult
    from .cloud_pc_user_profile_snapshot_export_bulk_action_result import CloudPcUserProfileSnapshotExportBulkActionResult

@dataclass
class CloudPcUserProfileBulkActionResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The failedCount property
    failed_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The totalCount property
    total_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcUserProfileBulkActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserProfileBulkActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserProfileSnapshotCreateBulkActionResult".casefold():
            from .cloud_pc_user_profile_snapshot_create_bulk_action_result import CloudPcUserProfileSnapshotCreateBulkActionResult

            return CloudPcUserProfileSnapshotCreateBulkActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserProfileSnapshotExportBulkActionResult".casefold():
            from .cloud_pc_user_profile_snapshot_export_bulk_action_result import CloudPcUserProfileSnapshotExportBulkActionResult

            return CloudPcUserProfileSnapshotExportBulkActionResult()
        return CloudPcUserProfileBulkActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_user_profile_snapshot_create_bulk_action_result import CloudPcUserProfileSnapshotCreateBulkActionResult
        from .cloud_pc_user_profile_snapshot_export_bulk_action_result import CloudPcUserProfileSnapshotExportBulkActionResult

        from .cloud_pc_user_profile_snapshot_create_bulk_action_result import CloudPcUserProfileSnapshotCreateBulkActionResult
        from .cloud_pc_user_profile_snapshot_export_bulk_action_result import CloudPcUserProfileSnapshotExportBulkActionResult

        fields: dict[str, Callable[[Any], None]] = {
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
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
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_additional_data_value(self.additional_data)
    

