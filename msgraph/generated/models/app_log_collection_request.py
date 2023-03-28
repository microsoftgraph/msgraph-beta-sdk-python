from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_log_upload_state, entity

from . import entity

class AppLogCollectionRequest(entity.Entity):
    """
    Entity for AppLogCollectionRequest contains all logs values.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new appLogCollectionRequest and sets the default values.
        """
        super().__init__()
        # Time at which the upload log request reached a completed state if not completed yet NULL will be returned.
        self._completed_date_time: Optional[datetime] = None
        # List of log folders.
        self._custom_log_folders: Optional[List[str]] = None
        # Indicates error message if any during the upload process.
        self._error_message: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # AppLogUploadStatus
        self._status: Optional[app_log_upload_state.AppLogUploadState] = None
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Time at which the upload log request reached a completed state if not completed yet NULL will be returned.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Time at which the upload log request reached a completed state if not completed yet NULL will be returned.
        Args:
            value: Value to set for the completed_date_time property.
        """
        self._completed_date_time = value
    
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
            value: Value to set for the custom_log_folders property.
        """
        self._custom_log_folders = value
    
    @property
    def error_message(self,) -> Optional[str]:
        """
        Gets the errorMessage property value. Indicates error message if any during the upload process.
        Returns: Optional[str]
        """
        return self._error_message
    
    @error_message.setter
    def error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the errorMessage property value. Indicates error message if any during the upload process.
        Args:
            value: Value to set for the error_message property.
        """
        self._error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_log_upload_state, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "customLogFolders": lambda n : setattr(self, 'custom_log_folders', n.get_collection_of_primitive_values(str)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
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
    

