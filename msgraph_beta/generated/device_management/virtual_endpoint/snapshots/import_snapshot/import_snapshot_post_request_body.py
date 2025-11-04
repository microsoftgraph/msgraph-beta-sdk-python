from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_pc_snapshot_import_action_detail import CloudPcSnapshotImportActionDetail

@dataclass
class ImportSnapshotPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The assignedUserId property
    assigned_user_id: Optional[str] = None
    # The sourceFiles property
    source_files: Optional[list[CloudPcSnapshotImportActionDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportSnapshotPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportSnapshotPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportSnapshotPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.cloud_pc_snapshot_import_action_detail import CloudPcSnapshotImportActionDetail

        from .....models.cloud_pc_snapshot_import_action_detail import CloudPcSnapshotImportActionDetail

        fields: dict[str, Callable[[Any], None]] = {
            "assignedUserId": lambda n : setattr(self, 'assigned_user_id', n.get_str_value()),
            "sourceFiles": lambda n : setattr(self, 'source_files', n.get_collection_of_object_values(CloudPcSnapshotImportActionDetail)),
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
        writer.write_str_value("assignedUserId", self.assigned_user_id)
        writer.write_collection_of_object_values("sourceFiles", self.source_files)
        writer.write_additional_data_value(self.additional_data)
    

