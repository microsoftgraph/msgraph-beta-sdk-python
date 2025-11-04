from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_snapshot_import_file_type import CloudPcSnapshotImportFileType
    from .cloud_pc_snapshot_import_source_type import CloudPcSnapshotImportSourceType
    from .cloud_pc_storage_blob_detail import CloudPcStorageBlobDetail

@dataclass
class CloudPcSnapshotImportActionDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The fileType property
    file_type: Optional[CloudPcSnapshotImportFileType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The shared access signature URL of the snapshot import action.
    sas_url: Optional[str] = None
    # The sourceType property
    source_type: Optional[CloudPcSnapshotImportSourceType] = None
    # The storage account information of the snapshot import action.
    storage_blob_info: Optional[CloudPcStorageBlobDetail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSnapshotImportActionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSnapshotImportActionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSnapshotImportActionDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_snapshot_import_file_type import CloudPcSnapshotImportFileType
        from .cloud_pc_snapshot_import_source_type import CloudPcSnapshotImportSourceType
        from .cloud_pc_storage_blob_detail import CloudPcStorageBlobDetail

        from .cloud_pc_snapshot_import_file_type import CloudPcSnapshotImportFileType
        from .cloud_pc_snapshot_import_source_type import CloudPcSnapshotImportSourceType
        from .cloud_pc_storage_blob_detail import CloudPcStorageBlobDetail

        fields: dict[str, Callable[[Any], None]] = {
            "fileType": lambda n : setattr(self, 'file_type', n.get_enum_value(CloudPcSnapshotImportFileType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sasUrl": lambda n : setattr(self, 'sas_url', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(CloudPcSnapshotImportSourceType)),
            "storageBlobInfo": lambda n : setattr(self, 'storage_blob_info', n.get_object_value(CloudPcStorageBlobDetail)),
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
        writer.write_enum_value("fileType", self.file_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sasUrl", self.sas_url)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_object_value("storageBlobInfo", self.storage_blob_info)
        writer.write_additional_data_value(self.additional_data)
    

