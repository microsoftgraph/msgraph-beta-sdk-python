from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_log_upload_state = lazy_import('msgraph.generated.models.app_log_upload_state')
entity = lazy_import('msgraph.generated.models.entity')

class AppLogCollectionRequest(entity.Entity):
    """
    AppLogCollectionRequest Entity.
    """
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Time at which the upload log request reached a terminal state
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Time at which the upload log request reached a terminal state
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appLogCollectionRequest and sets the default values.
        """
        super().__init__()
        # Time at which the upload log request reached a terminal state
        self._completed_date_time: Optional[datetime] = None
        # List of log folders.
        self._custom_log_folders: Optional[List[str]] = None
        # Error message if any during the upload process
        self._error_message: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # AppLogUploadStatus
        self._status: Optional[app_log_upload_state.AppLogUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppLogCollectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppLogCollectionRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppLogCollectionRequest()
    
    @property
    def custom_log_folders(self,) -> Optional[List[str]]:
        """
        Gets the customLogFolders property value. List of log folders.
        Returns: Optional[List[str]]
        """
        return self._custom_log_folders
    
    @custom_log_folders.setter
    def custom_log_folders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the customLogFolders property value. List of log folders.
        Args:
            value: Value to set for the customLogFolders property.
        """
        self._custom_log_folders = value
    
    @property
    def error_message(self,) -> Optional[str]:
        """
        Gets the errorMessage property value. Error message if any during the upload process
        Returns: Optional[str]
        """
        return self._error_message
    
    @error_message.setter
    def error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the errorMessage property value. Error message if any during the upload process
        Args:
            value: Value to set for the errorMessage property.
        """
        self._error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "custom_log_folders": lambda n : setattr(self, 'custom_log_folders', n.get_collection_of_primitive_values(str)),
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(app_log_upload_state.AppLogUploadState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_collection_of_primitive_values("customLogFolders", self.custom_log_folders)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[app_log_upload_state.AppLogUploadState]:
        """
        Gets the status property value. AppLogUploadStatus
        Returns: Optional[app_log_upload_state.AppLogUploadState]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[app_log_upload_state.AppLogUploadState] = None) -> None:
        """
        Sets the status property value. AppLogUploadStatus
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

