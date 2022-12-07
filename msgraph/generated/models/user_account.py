from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

account_status = lazy_import('msgraph.generated.models.account_status')

class UserAccount(AdditionalDataHolder, Parsable):
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
        Instantiates a new userAccount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The displayName property
        self._display_name: Optional[str] = None
        # The lastSeenDateTime property
        self._last_seen_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The service property
        self._service: Optional[str] = None
        # The signinName property
        self._signin_name: Optional[str] = None
        # The status property
        self._status: Optional[account_status.AccountStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAccount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserAccount()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "signin_name": lambda n : setattr(self, 'signin_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(account_status.AccountStatus)),
        }
        return fields
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The lastSeenDateTime property
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The lastSeenDateTime property
        Args:
            value: Value to set for the lastSeenDateTime property.
        """
        self._last_seen_date_time = value
    
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
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. The riskScore property
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. The riskScore property
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_str_value("service", self.service)
        writer.write_str_value("signinName", self.signin_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The service property
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The service property
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def signin_name(self,) -> Optional[str]:
        """
        Gets the signinName property value. The signinName property
        Returns: Optional[str]
        """
        return self._signin_name
    
    @signin_name.setter
    def signin_name(self,value: Optional[str] = None) -> None:
        """
        Sets the signinName property value. The signinName property
        Args:
            value: Value to set for the signinName property.
        """
        self._signin_name = value
    
    @property
    def status(self,) -> Optional[account_status.AccountStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[account_status.AccountStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[account_status.AccountStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

