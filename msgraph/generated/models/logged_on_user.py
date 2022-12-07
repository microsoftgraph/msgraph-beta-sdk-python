from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class LoggedOnUser(AdditionalDataHolder, Parsable):
    """
    Logged On User
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
        Instantiates a new loggedOnUser and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Date time when user logs on
        self._last_log_on_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # User id
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LoggedOnUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LoggedOnUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LoggedOnUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_log_on_date_time": lambda n : setattr(self, 'last_log_on_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        return fields
    
    @property
    def last_log_on_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastLogOnDateTime property value. Date time when user logs on
        Returns: Optional[datetime]
        """
        return self._last_log_on_date_time
    
    @last_log_on_date_time.setter
    def last_log_on_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastLogOnDateTime property value. Date time when user logs on
        Args:
            value: Value to set for the lastLogOnDateTime property.
        """
        self._last_log_on_date_time = value
    
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
        writer.write_datetime_value("lastLogOnDateTime", self.last_log_on_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User id
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User id
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

