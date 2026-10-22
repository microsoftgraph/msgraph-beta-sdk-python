from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier

@dataclass
class CloudPcUserProfileSnapshotStorageDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The accessTier property
    access_tier: Optional[CloudPcStorageAccountAccessTier] = None
    # The containerName property
    container_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The storageAccountId property
    storage_account_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcUserProfileSnapshotStorageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserProfileSnapshotStorageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserProfileSnapshotStorageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier

        from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier

        fields: dict[str, Callable[[Any], None]] = {
            "accessTier": lambda n : setattr(self, 'access_tier', n.get_enum_value(CloudPcStorageAccountAccessTier)),
            "containerName": lambda n : setattr(self, 'container_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "storageAccountId": lambda n : setattr(self, 'storage_account_id', n.get_str_value()),
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
        writer.write_enum_value("accessTier", self.access_tier)
        writer.write_str_value("containerName", self.container_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("storageAccountId", self.storage_account_id)
        writer.write_additional_data_value(self.additional_data)
    

