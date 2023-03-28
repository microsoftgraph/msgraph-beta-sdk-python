from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import logon_type, user_account_security_type

class LogonUser(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new logonUser and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Domain of user account used to logon.
        self._account_domain: Optional[str] = None
        # Account name of user account used to logon.
        self._account_name: Optional[str] = None
        # User Account type, per Windows definition. Possible values are: unknown, standard, power, administrator.
        self._account_type: Optional[user_account_security_type.UserAccountSecurityType] = None
        # DateTime at which the earliest logon by this user account occurred (provider-determined period). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._first_seen_date_time: Optional[datetime] = None
        # DateTime at which the latest logon by this user account occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_seen_date_time: Optional[datetime] = None
        # User logon ID.
        self._logon_id: Optional[str] = None
        # Collection of the logon types observed for the logged on user from when first to last seen. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        self._logon_types: Optional[List[logon_type.LogonType]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def account_domain(self,) -> Optional[str]:
        """
        Gets the accountDomain property value. Domain of user account used to logon.
        Returns: Optional[str]
        """
        return self._account_domain
    
    @account_domain.setter
    def account_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the accountDomain property value. Domain of user account used to logon.
        Args:
            value: Value to set for the account_domain property.
        """
        self._account_domain = value
    
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. Account name of user account used to logon.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. Account name of user account used to logon.
        Args:
            value: Value to set for the account_name property.
        """
        self._account_name = value
    
    @property
    def account_type(self,) -> Optional[user_account_security_type.UserAccountSecurityType]:
        """
        Gets the accountType property value. User Account type, per Windows definition. Possible values are: unknown, standard, power, administrator.
        Returns: Optional[user_account_security_type.UserAccountSecurityType]
        """
        return self._account_type
    
    @account_type.setter
    def account_type(self,value: Optional[user_account_security_type.UserAccountSecurityType] = None) -> None:
        """
        Sets the accountType property value. User Account type, per Windows definition. Possible values are: unknown, standard, power, administrator.
        Args:
            value: Value to set for the account_type property.
        """
        self._account_type = value
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LogonUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LogonUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LogonUser()
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. DateTime at which the earliest logon by this user account occurred (provider-determined period). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. DateTime at which the earliest logon by this user account occurred (provider-determined period). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the first_seen_date_time property.
        """
        self._first_seen_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import logon_type, user_account_security_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accountDomain": lambda n : setattr(self, 'account_domain', n.get_str_value()),
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "accountType": lambda n : setattr(self, 'account_type', n.get_enum_value(user_account_security_type.UserAccountSecurityType)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "logonId": lambda n : setattr(self, 'logon_id', n.get_str_value()),
            "logonTypes": lambda n : setattr(self, 'logon_types', n.get_collection_of_enum_values(logon_type.LogonType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. DateTime at which the latest logon by this user account occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. DateTime at which the latest logon by this user account occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def logon_id(self,) -> Optional[str]:
        """
        Gets the logonId property value. User logon ID.
        Returns: Optional[str]
        """
        return self._logon_id
    
    @logon_id.setter
    def logon_id(self,value: Optional[str] = None) -> None:
        """
        Sets the logonId property value. User logon ID.
        Args:
            value: Value to set for the logon_id property.
        """
        self._logon_id = value
    
    @property
    def logon_types(self,) -> Optional[List[logon_type.LogonType]]:
        """
        Gets the logonTypes property value. Collection of the logon types observed for the logged on user from when first to last seen. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        Returns: Optional[List[logon_type.LogonType]]
        """
        return self._logon_types
    
    @logon_types.setter
    def logon_types(self,value: Optional[List[logon_type.LogonType]] = None) -> None:
        """
        Sets the logonTypes property value. Collection of the logon types observed for the logged on user from when first to last seen. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        Args:
            value: Value to set for the logon_types property.
        """
        self._logon_types = value
    
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
        writer.write_str_value("accountDomain", self.account_domain)
        writer.write_str_value("accountName", self.account_name)
        writer.write_enum_value("accountType", self.account_type)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("logonId", self.logon_id)
        writer.write_enum_value("logonTypes", self.logon_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

