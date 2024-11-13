from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .assigned_label import AssignedLabel
    from .column_definition import ColumnDefinition
    from .drive import Drive
    from .entity import Entity
    from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
    from .file_storage_container_ownership_type import FileStorageContainerOwnershipType
    from .file_storage_container_settings import FileStorageContainerSettings
    from .file_storage_container_status import FileStorageContainerStatus
    from .file_storage_container_viewpoint import FileStorageContainerViewpoint
    from .permission import Permission
    from .recycle_bin import RecycleBin
    from .site_lock_state import SiteLockState
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class FileStorageContainer(Entity, Parsable):
    # Sensitivity label assigned to the fileStorageContainer. Read-write.
    assigned_sensitivity_label: Optional[AssignedLabel] = None
    # The set of custom structured metadata supported by the fileStorageContainer. Read-write.
    columns: Optional[List[ColumnDefinition]] = None
    # Container type ID of the fileStorageContainer. Each container must have only one container type. Read-only.
    container_type_id: Optional[UUID] = None
    # Date and time of the fileStorageContainer creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Custom property collection for the fileStorageContainer. Read-write.
    custom_properties: Optional[FileStorageContainerCustomPropertyDictionary] = None
    # Provides a user-visible description of the fileStorageContainer. Read-write.
    description: Optional[str] = None
    # The display name of the fileStorageContainer. Read-write.
    display_name: Optional[str] = None
    # The drive of the resource fileStorageContainer. Read-only.
    drive: Optional[Drive] = None
    # The externalGroupId property
    external_group_id: Optional[UUID] = None
    # The isItemVersioningEnabled property
    is_item_versioning_enabled: Optional[bool] = None
    # The itemMajorVersionLimit property
    item_major_version_limit: Optional[int] = None
    # Indicates the lock state of the fileStorageContainer. The possible values are unlocked and lockedReadOnly. Read-only.
    lock_state: Optional[SiteLockState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of users who own the fileStorageContainer. Read-only.
    owners: Optional[List[UserIdentity]] = None
    # Ownership type of the fileStorageContainer. The possible values are: tenantOwned. Read-only.
    ownership_type: Optional[FileStorageContainerOwnershipType] = None
    # The set of permissions for users in the fileStorageContainer. The permission for each user is set by the roles property. The possible values are reader, writer, manager, and owner. Read-write.
    permissions: Optional[List[Permission]] = None
    # Recycle bin of the fileStorageContainer. Read-only.
    recycle_bin: Optional[RecycleBin] = None
    # The settings property
    settings: Optional[FileStorageContainerSettings] = None
    # Status of the fileStorageContainer. Containers are created as inactive and require activation. Inactive containers are subjected to automatic deletion in 24 hours. The possible values are: inactive, active. Read-only.
    status: Optional[FileStorageContainerStatus] = None
    # Storage used in the fileStorageContainer, in bytes. Read-only.
    storage_used_in_bytes: Optional[int] = None
    # Data specific to the current user. Read-only.
    viewpoint: Optional[FileStorageContainerViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_label import AssignedLabel
        from .column_definition import ColumnDefinition
        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_ownership_type import FileStorageContainerOwnershipType
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission
        from .recycle_bin import RecycleBin
        from .site_lock_state import SiteLockState
        from .user_identity import UserIdentity

        from .assigned_label import AssignedLabel
        from .column_definition import ColumnDefinition
        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_ownership_type import FileStorageContainerOwnershipType
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission
        from .recycle_bin import RecycleBin
        from .site_lock_state import SiteLockState
        from .user_identity import UserIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedSensitivityLabel": lambda n : setattr(self, 'assigned_sensitivity_label', n.get_object_value(AssignedLabel)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ColumnDefinition)),
            "containerTypeId": lambda n : setattr(self, 'container_type_id', n.get_uuid_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(FileStorageContainerCustomPropertyDictionary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "externalGroupId": lambda n : setattr(self, 'external_group_id', n.get_uuid_value()),
            "isItemVersioningEnabled": lambda n : setattr(self, 'is_item_versioning_enabled', n.get_bool_value()),
            "itemMajorVersionLimit": lambda n : setattr(self, 'item_major_version_limit', n.get_int_value()),
            "lockState": lambda n : setattr(self, 'lock_state', n.get_enum_value(SiteLockState)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(UserIdentity)),
            "ownershipType": lambda n : setattr(self, 'ownership_type', n.get_enum_value(FileStorageContainerOwnershipType)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(Permission)),
            "recycleBin": lambda n : setattr(self, 'recycle_bin', n.get_object_value(RecycleBin)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(FileStorageContainerSettings)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FileStorageContainerStatus)),
            "storageUsedInBytes": lambda n : setattr(self, 'storage_used_in_bytes', n.get_int_value()),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(FileStorageContainerViewpoint)),
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
        from .assigned_label import AssignedLabel
        from .column_definition import ColumnDefinition
        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_ownership_type import FileStorageContainerOwnershipType
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission
        from .recycle_bin import RecycleBin
        from .site_lock_state import SiteLockState
        from .user_identity import UserIdentity

        writer.write_object_value("assignedSensitivityLabel", self.assigned_sensitivity_label)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_uuid_value("containerTypeId", self.container_type_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_uuid_value("externalGroupId", self.external_group_id)
        writer.write_bool_value("isItemVersioningEnabled", self.is_item_versioning_enabled)
        writer.write_int_value("itemMajorVersionLimit", self.item_major_version_limit)
        writer.write_enum_value("lockState", self.lock_state)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_enum_value("ownershipType", self.ownership_type)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("recycleBin", self.recycle_bin)
        writer.write_object_value("settings", self.settings)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("storageUsedInBytes", self.storage_used_in_bytes)
        writer.write_object_value("viewpoint", self.viewpoint)
    

