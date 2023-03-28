from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ClassificationInnerError(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new classificationInnerError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The activityId property
        self._activity_id: Optional[str] = None
        # The clientRequestId property
        self._client_request_id: Optional[str] = None
        # The code property
        self._code: Optional[str] = None
        # The errorDateTime property
        self._error_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def activity_id(self,) -> Optional[str]:
        """
        Gets the activityId property value. The activityId property
        Returns: Optional[str]
        """
        return self._activity_id
    
    @activity_id.setter
    def activity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the activityId property value. The activityId property
        Args:
            value: Value to set for the activity_id property.
        """
        self._activity_id = value
    
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
    def client_request_id(self,) -> Optional[str]:
        """
        Gets the clientRequestId property value. The clientRequestId property
        Returns: Optional[str]
        """
        return self._client_request_id
    
    @client_request_id.setter
    def client_request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientRequestId property value. The clientRequestId property
        Args:
            value: Value to set for the client_request_id property.
        """
        self._client_request_id = value
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code property
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code property
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassificationInnerError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationInnerError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClassificationInnerError()
    
    @property
    def error_date_time(self,) -> Optional[datetime]:
        """
        Gets the errorDateTime property value. The errorDateTime property
        Returns: Optional[datetime]
        """
        return self._error_date_time
    
    @error_date_time.setter
    def error_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the errorDateTime property value. The errorDateTime property
        Args:
            value: Value to set for the error_date_time property.
        """
        self._error_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "activityId": lambda n : setattr(self, 'activity_id', n.get_str_value()),
            "clientRequestId": lambda n : setattr(self, 'client_request_id', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "errorDateTime": lambda n : setattr(self, 'error_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("activityId", self.activity_id)
        writer.write_str_value("clientRequestId", self.client_request_id)
        writer.write_str_value("code", self.code)
        writer.write_datetime_value("errorDateTime", self.error_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

