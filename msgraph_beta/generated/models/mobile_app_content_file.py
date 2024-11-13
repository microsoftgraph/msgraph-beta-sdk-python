from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

from .entity import Entity

@dataclass
class MobileAppContentFile(Entity, Parsable):
    """
    Contains properties for a single installer file that is associated with a given mobileAppContent version.
    """
    # Indicates the Azure Storage URI that the file is uploaded to. Created by the service upon receiving a valid mobileAppContentFile. Read-only. This property is read-only.
    azure_storage_uri: Optional[str] = None
    # Indicates the date and time when the Azure storage URI expires, in ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only. This property is read-only.
    azure_storage_uri_expiration_date_time: Optional[datetime.datetime] = None
    # Indicates created date and time associated with app content file, in ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # A value indicating whether the file is committed. A committed app content file has been fully uploaded and validated by the Intune service. TRUE means that app content file is committed, FALSE means that app content file is not committed. Defaults to FALSE. Read-only. This property is read-only.
    is_committed: Optional[bool] = None
    # Indicates whether this content file is a dependency for the main content file. TRUE means that the content file is a dependency, FALSE means that the content file is not a dependency and is the main content file. Defaults to FALSE.
    is_dependency: Optional[bool] = None
    # A value indicating whether the file is a framework file. To be deprecated.
    is_framework_file: Optional[bool] = None
    # Indicates the manifest information, containing file metadata.
    manifest: Optional[bytes] = None
    # Indicates the name of the file.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The size of the file prior to encryption. To be deprecated, please use sizeInBytes property instead.
    size: Optional[int] = None
    # The size of the file after encryption. To be deprecated, please use sizeEncryptedInBytes property instead.
    size_encrypted: Optional[int] = None
    # Indicates the size of the file after encryption, in bytes. Valid values 0 to 9.22337203685478E+18
    size_encrypted_in_bytes: Optional[int] = None
    # Indicates the original size of the file, in bytes. Valid values 0 to 9.22337203685478E+18
    size_in_bytes: Optional[int] = None
    # Contains properties for upload request states.
    upload_state: Optional[MobileAppContentFileUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppContentFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContentFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppContentFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

        from .entity import Entity
        from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

        fields: Dict[str, Callable[[Any], None]] = {
            "azureStorageUri": lambda n : setattr(self, 'azure_storage_uri', n.get_str_value()),
            "azureStorageUriExpirationDateTime": lambda n : setattr(self, 'azure_storage_uri_expiration_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isCommitted": lambda n : setattr(self, 'is_committed', n.get_bool_value()),
            "isDependency": lambda n : setattr(self, 'is_dependency', n.get_bool_value()),
            "isFrameworkFile": lambda n : setattr(self, 'is_framework_file', n.get_bool_value()),
            "manifest": lambda n : setattr(self, 'manifest', n.get_bytes_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sizeEncrypted": lambda n : setattr(self, 'size_encrypted', n.get_int_value()),
            "sizeEncryptedInBytes": lambda n : setattr(self, 'size_encrypted_in_bytes', n.get_int_value()),
            "sizeInBytes": lambda n : setattr(self, 'size_in_bytes', n.get_int_value()),
            "uploadState": lambda n : setattr(self, 'upload_state', n.get_enum_value(MobileAppContentFileUploadState)),
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
        from .entity import Entity
        from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

        writer.write_bool_value("isDependency", self.is_dependency)
        writer.write_bool_value("isFrameworkFile", self.is_framework_file)
        writer.write_bytes_value("manifest", self.manifest)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
        writer.write_int_value("sizeEncrypted", self.size_encrypted)
        writer.write_int_value("sizeEncryptedInBytes", self.size_encrypted_in_bytes)
        writer.write_int_value("sizeInBytes", self.size_in_bytes)
        writer.write_enum_value("uploadState", self.upload_state)
    

