from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_app_management_task_status = lazy_import('msgraph.generated.models.device_app_management_task_status')

class UpdateStatusPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateStatus method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updateStatusPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The note property
        self._note: Optional[str] = None
        # Device app management task status.
        self._status: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateStatusPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_app_management_task_status.DeviceAppManagementTaskStatus)),
        }
        return fields
    
    @property
    def note(self,) -> Optional[str]:
        """
        Gets the note property value. The note property
        Returns: Optional[str]
        """
        return self._note
    
    @note.setter
    def note(self,value: Optional[str] = None) -> None:
        """
        Sets the note property value. The note property
        Args:
            value: Value to set for the note property.
        """
        self._note = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("note", self.note)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[device_app_management_task_status.DeviceAppManagementTaskStatus]:
        """
        Gets the status property value. Device app management task status.
        Returns: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_app_management_task_status.DeviceAppManagementTaskStatus] = None) -> None:
        """
        Sets the status property value. Device app management task status.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

