from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcForensicStorageAccount(Entity, Parsable):
    # Indicates the access tier of the storage account. Possible values are hot, cool, premium, cold, and unknownFutureValue. Default value is hot. Read-only.
    access_tier: Optional[CloudPcStorageAccountAccessTier] = None
    # Indicates whether immutability policies are configured for the storage account. When true, the storage account only accepts hot as the snapshot access tier. When false, the storage account accepts all valid access tiers. Read-Only.
    immutable_storage: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the ID of the storage account. Read-only.
    storage_account_id: Optional[str] = None
    # Indicates the name of the storage account. Read-only.
    storage_account_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcForensicStorageAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcForensicStorageAccount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcForensicStorageAccount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier
        from .entity import Entity

        from .cloud_pc_storage_account_access_tier import CloudPcStorageAccountAccessTier
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessTier": lambda n : setattr(self, 'access_tier', n.get_enum_value(CloudPcStorageAccountAccessTier)),
            "immutableStorage": lambda n : setattr(self, 'immutable_storage', n.get_bool_value()),
            "storageAccountId": lambda n : setattr(self, 'storage_account_id', n.get_str_value()),
            "storageAccountName": lambda n : setattr(self, 'storage_account_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("accessTier", self.access_tier)
        writer.write_bool_value("immutableStorage", self.immutable_storage)
        writer.write_str_value("storageAccountId", self.storage_account_id)
        writer.write_str_value("storageAccountName", self.storage_account_name)
    

