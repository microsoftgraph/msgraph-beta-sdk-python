from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_storage_container_type_app_permission import FileStorageContainerTypeAppPermission

@dataclass
class FileStorageContainerTypeAppPermissionGrant(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appId property
    app_id: Optional[str] = None
    # The applicationPermissions property
    application_permissions: Optional[list[FileStorageContainerTypeAppPermission]] = None
    # The delegatedPermissions property
    delegated_permissions: Optional[list[FileStorageContainerTypeAppPermission]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainerTypeAppPermissionGrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainerTypeAppPermissionGrant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainerTypeAppPermissionGrant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_storage_container_type_app_permission import FileStorageContainerTypeAppPermission

        from .file_storage_container_type_app_permission import FileStorageContainerTypeAppPermission

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applicationPermissions": lambda n : setattr(self, 'application_permissions', n.get_collection_of_enum_values(FileStorageContainerTypeAppPermission)),
            "delegatedPermissions": lambda n : setattr(self, 'delegated_permissions', n.get_collection_of_enum_values(FileStorageContainerTypeAppPermission)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_enum_values("applicationPermissions", self.application_permissions)
        writer.write_collection_of_enum_values("delegatedPermissions", self.delegated_permissions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

