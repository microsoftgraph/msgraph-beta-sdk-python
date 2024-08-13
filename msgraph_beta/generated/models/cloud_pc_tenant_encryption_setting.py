from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_disk_encryption_type import CloudPcDiskEncryptionType

@dataclass
class CloudPcTenantEncryptionSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates the date and time when last sync tenant encryption setting.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the Cloud PC disk encryption type for a tenant. It is a tenant-level setting that applies globally to all Cloud PCs in the tenant. Possible values are: platformManagedKey, customerManagedKey, unknownFutureValue. Read-only.
    tenant_disk_encryption_type: Optional[CloudPcDiskEncryptionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcTenantEncryptionSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcTenantEncryptionSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcTenantEncryptionSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_disk_encryption_type import CloudPcDiskEncryptionType

        from .cloud_pc_disk_encryption_type import CloudPcDiskEncryptionType

        fields: Dict[str, Callable[[Any], None]] = {
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantDiskEncryptionType": lambda n : setattr(self, 'tenant_disk_encryption_type', n.get_enum_value(CloudPcDiskEncryptionType)),
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
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tenantDiskEncryptionType", self.tenant_disk_encryption_type)
        writer.write_additional_data_value(self.additional_data)
    

