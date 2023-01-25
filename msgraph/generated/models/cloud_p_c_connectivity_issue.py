from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPCConnectivityIssue(entity.Entity):
    """
    The user experience analyte connectivity issue entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPCConnectivityIssue and sets the default values.
        """
        super().__init__()
        # The Intune DeviceId of the device the connection is associated with.
        self._device_id: Optional[str] = None
        # The error code of the connectivity issue.
        self._error_code: Optional[str] = None
        # The time that the connection initiated. The time is shown in ISO 8601 format and Coordinated Universal Time (UTC) time.
        self._error_date_time: Optional[datetime] = None
        # The detailed description of what went wrong.
        self._error_description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The recommended action to fix the corresponding error.
        self._recommended_action: Optional[str] = None
        # The unique id of user who initialize the connection.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPCConnectivityIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPCConnectivityIssue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPCConnectivityIssue()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The Intune DeviceId of the device the connection is associated with.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The Intune DeviceId of the device the connection is associated with.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. The error code of the connectivity issue.
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. The error code of the connectivity issue.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def error_date_time(self,) -> Optional[datetime]:
        """
        Gets the errorDateTime property value. The time that the connection initiated. The time is shown in ISO 8601 format and Coordinated Universal Time (UTC) time.
        Returns: Optional[datetime]
        """
        return self._error_date_time
    
    @error_date_time.setter
    def error_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the errorDateTime property value. The time that the connection initiated. The time is shown in ISO 8601 format and Coordinated Universal Time (UTC) time.
        Args:
            value: Value to set for the errorDateTime property.
        """
        self._error_date_time = value
    
    @property
    def error_description(self,) -> Optional[str]:
        """
        Gets the errorDescription property value. The detailed description of what went wrong.
        Returns: Optional[str]
        """
        return self._error_description
    
    @error_description.setter
    def error_description(self,value: Optional[str] = None) -> None:
        """
        Sets the errorDescription property value. The detailed description of what went wrong.
        Args:
            value: Value to set for the errorDescription property.
        """
        self._error_description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "error_date_time": lambda n : setattr(self, 'error_date_time', n.get_datetime_value()),
            "error_description": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "recommended_action": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recommended_action(self,) -> Optional[str]:
        """
        Gets the recommendedAction property value. The recommended action to fix the corresponding error.
        Returns: Optional[str]
        """
        return self._recommended_action
    
    @recommended_action.setter
    def recommended_action(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedAction property value. The recommended action to fix the corresponding error.
        Args:
            value: Value to set for the recommendedAction property.
        """
        self._recommended_action = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_datetime_value("errorDateTime", self.error_date_time)
        writer.write_str_value("errorDescription", self.error_description)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The unique id of user who initialize the connection.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The unique id of user who initialize the connection.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

