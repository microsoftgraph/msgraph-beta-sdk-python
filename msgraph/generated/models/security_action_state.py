from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

operation_status = lazy_import('msgraph.generated.models.operation_status')

class SecurityActionState(AdditionalDataHolder, Parsable):
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
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The Application ID of the calling application that submitted an update (PATCH) to the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The Application ID of the calling application that submitted an update (PATCH) to the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new securityActionState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Application ID of the calling application that submitted an update (PATCH) to the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        self._app_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Status of the securityAction in this update. Possible values are: NotStarted, Running, Completed, Failed.
        self._status: Optional[operation_status.OperationStatus] = None
        # Timestamp when the actionState was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._updated_date_time: Optional[datetime] = None
        # The user principal name of the signed-in user that submitted an update (PATCH) to the action. The user should be extracted from the auth token and not entered manually by the calling application.
        self._user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityActionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityActionState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityActionState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(operation_status.OperationStatus)),
            "updated_date_time": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the status property value. Status of the securityAction in this update. Possible values are: NotStarted, Running, Completed, Failed.
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the status property value. Status of the securityAction in this update. Possible values are: NotStarted, Running, Completed, Failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the updatedDateTime property value. Timestamp when the actionState was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._updated_date_time
    
    @updated_date_time.setter
    def updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedDateTime property value. Timestamp when the actionState was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the updatedDateTime property.
        """
        self._updated_date_time = value
    
    @property
    def user(self,) -> Optional[str]:
        """
        Gets the user property value. The user principal name of the signed-in user that submitted an update (PATCH) to the action. The user should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[str] = None) -> None:
        """
        Sets the user property value. The user principal name of the signed-in user that submitted an update (PATCH) to the action. The user should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

