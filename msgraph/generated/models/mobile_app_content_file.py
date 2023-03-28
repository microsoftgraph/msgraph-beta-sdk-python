from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, mobile_app_content_file_upload_state

from . import entity

class MobileAppContentFile(entity.Entity):
    """
    Contains properties for a single installer file that is associated with a given mobileAppContent version.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppContentFile and sets the default values.
        """
        super().__init__()
        # The Azure Storage URI.
        self._azure_storage_uri: Optional[str] = None
        # The time the Azure storage Uri expires.
        self._azure_storage_uri_expiration_date_time: Optional[datetime] = None
        # The time the file was created.
        self._created_date_time: Optional[datetime] = None
        # A value indicating whether the file is committed.
        self._is_committed: Optional[bool] = None
        # Whether the content file is a dependency for the main content file.
        self._is_dependency: Optional[bool] = None
        # A value indicating whether the file is a framework file.
        self._is_framework_file: Optional[bool] = None
        # The manifest information.
        self._manifest: Optional[bytes] = None
        # the file name.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The size of the file prior to encryption.
        self._size: Optional[int] = None
        # The size of the file after encryption.
        self._size_encrypted: Optional[int] = None
        # Contains properties for upload request states.
        self._upload_state: Optional[mobile_app_content_file_upload_state.MobileAppContentFileUploadState] = None
    
    @property
    def azure_storage_uri(self,) -> Optional[str]:
        """
        Gets the azureStorageUri property value. The Azure Storage URI.
        Returns: Optional[str]
        """
        return self._azure_storage_uri
    
    @azure_storage_uri.setter
    def azure_storage_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the azureStorageUri property value. The Azure Storage URI.
        Args:
            value: Value to set for the azure_storage_uri property.
        """
        self._azure_storage_uri = value
    
    @property
    def azure_storage_uri_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the azureStorageUriExpirationDateTime property value. The time the Azure storage Uri expires.
        Returns: Optional[datetime]
        """
        return self._azure_storage_uri_expiration_date_time
    
    @azure_storage_uri_expiration_date_time.setter
    def azure_storage_uri_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the azureStorageUriExpirationDateTime property value. The time the Azure storage Uri expires.
        Args:
            value: Value to set for the azure_storage_uri_expiration_date_time property.
        """
        self._azure_storage_uri_expiration_date_time = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time the file was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time the file was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppContentFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContentFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppContentFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, mobile_app_content_file_upload_state

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
            "uploadState": lambda n : setattr(self, 'upload_state', n.get_enum_value(mobile_app_content_file_upload_state.MobileAppContentFileUploadState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_committed(self,) -> Optional[bool]:
        """
        Gets the isCommitted property value. A value indicating whether the file is committed.
        Returns: Optional[bool]
        """
        return self._is_committed
    
    @is_committed.setter
    def is_committed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCommitted property value. A value indicating whether the file is committed.
        Args:
            value: Value to set for the is_committed property.
        """
        self._is_committed = value
    
    @property
    def is_dependency(self,) -> Optional[bool]:
        """
        Gets the isDependency property value. Whether the content file is a dependency for the main content file.
        Returns: Optional[bool]
        """
        return self._is_dependency
    
    @is_dependency.setter
    def is_dependency(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDependency property value. Whether the content file is a dependency for the main content file.
        Args:
            value: Value to set for the is_dependency property.
        """
        self._is_dependency = value
    
    @property
    def is_framework_file(self,) -> Optional[bool]:
        """
        Gets the isFrameworkFile property value. A value indicating whether the file is a framework file.
        Returns: Optional[bool]
        """
        return self._is_framework_file
    
    @is_framework_file.setter
    def is_framework_file(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFrameworkFile property value. A value indicating whether the file is a framework file.
        Args:
            value: Value to set for the is_framework_file property.
        """
        self._is_framework_file = value
    
    @property
    def manifest(self,) -> Optional[bytes]:
        """
        Gets the manifest property value. The manifest information.
        Returns: Optional[bytes]
        """
        return self._manifest
    
    @manifest.setter
    def manifest(self,value: Optional[bytes] = None) -> None:
        """
        Sets the manifest property value. The manifest information.
        Args:
            value: Value to set for the manifest property.
        """
        self._manifest = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. the file name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. the file name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureStorageUri", self.azure_storage_uri)
        writer.write_datetime_value("azureStorageUriExpirationDateTime", self.azure_storage_uri_expiration_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isCommitted", self.is_committed)
        writer.write_bool_value("isDependency", self.is_dependency)
        writer.write_bool_value("isFrameworkFile", self.is_framework_file)
        writer.write_object_value("manifest", self.manifest)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
        writer.write_int_value("sizeEncrypted", self.size_encrypted)
        writer.write_enum_value("uploadState", self.upload_state)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size of the file prior to encryption.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size of the file prior to encryption.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def size_encrypted(self,) -> Optional[int]:
        """
        Gets the sizeEncrypted property value. The size of the file after encryption.
        Returns: Optional[int]
        """
        return self._size_encrypted
    
    @size_encrypted.setter
    def size_encrypted(self,value: Optional[int] = None) -> None:
        """
        Sets the sizeEncrypted property value. The size of the file after encryption.
        Args:
            value: Value to set for the size_encrypted property.
        """
        self._size_encrypted = value
    
    @property
    def upload_state(self,) -> Optional[mobile_app_content_file_upload_state.MobileAppContentFileUploadState]:
        """
        Gets the uploadState property value. Contains properties for upload request states.
        Returns: Optional[mobile_app_content_file_upload_state.MobileAppContentFileUploadState]
        """
        return self._upload_state
    
    @upload_state.setter
    def upload_state(self,value: Optional[mobile_app_content_file_upload_state.MobileAppContentFileUploadState] = None) -> None:
        """
        Sets the uploadState property value. Contains properties for upload request states.
        Args:
            value: Value to set for the upload_state property.
        """
        self._upload_state = value
    

