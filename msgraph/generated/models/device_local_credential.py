from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class DeviceLocalCredential(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceLocalCredential and sets the default values.
        """
        super().__init__()
        # The name of the local admin account for which LAPS is enabled.
        self._account_name: Optional[str] = None
        # The SID of the local admin account for which LAPS is enabled.
        self._account_sid: Optional[str] = None
        # When the local adminstrator account credential for the device object was backed up to Azure Active Directory.
        self._backup_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The password for the local administrator account that is backed up to Azure Active Directory and returned as a base 64 encoded value.
        self._password_base64: Optional[str] = None
    
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. The name of the local admin account for which LAPS is enabled.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. The name of the local admin account for which LAPS is enabled.
        Args:
            value: Value to set for the account_name property.
        """
        self._account_name = value
    
    @property
    def account_sid(self,) -> Optional[str]:
        """
        Gets the accountSid property value. The SID of the local admin account for which LAPS is enabled.
        Returns: Optional[str]
        """
        return self._account_sid
    
    @account_sid.setter
    def account_sid(self,value: Optional[str] = None) -> None:
        """
        Sets the accountSid property value. The SID of the local admin account for which LAPS is enabled.
        Args:
            value: Value to set for the account_sid property.
        """
        self._account_sid = value
    
    @property
    def backup_date_time(self,) -> Optional[datetime]:
        """
        Gets the backupDateTime property value. When the local adminstrator account credential for the device object was backed up to Azure Active Directory.
        Returns: Optional[datetime]
        """
        return self._backup_date_time
    
    @backup_date_time.setter
    def backup_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the backupDateTime property value. When the local adminstrator account credential for the device object was backed up to Azure Active Directory.
        Args:
            value: Value to set for the backup_date_time property.
        """
        self._backup_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLocalCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLocalCredential
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceLocalCredential()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "accountSid": lambda n : setattr(self, 'account_sid', n.get_str_value()),
            "backupDateTime": lambda n : setattr(self, 'backup_date_time', n.get_datetime_value()),
            "passwordBase64": lambda n : setattr(self, 'password_base64', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password_base64(self,) -> Optional[str]:
        """
        Gets the passwordBase64 property value. The password for the local administrator account that is backed up to Azure Active Directory and returned as a base 64 encoded value.
        Returns: Optional[str]
        """
        return self._password_base64
    
    @password_base64.setter
    def password_base64(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordBase64 property value. The password for the local administrator account that is backed up to Azure Active Directory and returned as a base 64 encoded value.
        Args:
            value: Value to set for the password_base64 property.
        """
        self._password_base64 = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("accountSid", self.account_sid)
        writer.write_datetime_value("backupDateTime", self.backup_date_time)
        writer.write_str_value("passwordBase64", self.password_base64)
    

