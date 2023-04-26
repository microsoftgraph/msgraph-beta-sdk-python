from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_local_credential, entity

from . import entity

class DeviceLocalCredentialInfo(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceLocalCredentialInfo and sets the default values.
        """
        super().__init__()
        # The credentials of the device's local administrator account backed up to Azure Active Directory.
        self._credentials: Optional[List[device_local_credential.DeviceLocalCredential]] = None
        # Display name of the device that the local credentials are associated with.
        self._device_name: Optional[str] = None
        # When the local administrator account credential was backed up to Azure Active Directory.
        self._last_backup_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # When the local administrator account credential will be refreshed and backed up to Azure Active Directory.
        self._refresh_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLocalCredentialInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLocalCredentialInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceLocalCredentialInfo()
    
    @property
    def credentials(self,) -> Optional[List[device_local_credential.DeviceLocalCredential]]:
        """
        Gets the credentials property value. The credentials of the device's local administrator account backed up to Azure Active Directory.
        Returns: Optional[List[device_local_credential.DeviceLocalCredential]]
        """
        return self._credentials
    
    @credentials.setter
    def credentials(self,value: Optional[List[device_local_credential.DeviceLocalCredential]] = None) -> None:
        """
        Sets the credentials property value. The credentials of the device's local administrator account backed up to Azure Active Directory.
        Args:
            value: Value to set for the credentials property.
        """
        self._credentials = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Display name of the device that the local credentials are associated with.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Display name of the device that the local credentials are associated with.
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_local_credential, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(device_local_credential.DeviceLocalCredential)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "lastBackupDateTime": lambda n : setattr(self, 'last_backup_date_time', n.get_datetime_value()),
            "refreshDateTime": lambda n : setattr(self, 'refresh_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_backup_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastBackupDateTime property value. When the local administrator account credential was backed up to Azure Active Directory.
        Returns: Optional[datetime]
        """
        return self._last_backup_date_time
    
    @last_backup_date_time.setter
    def last_backup_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastBackupDateTime property value. When the local administrator account credential was backed up to Azure Active Directory.
        Args:
            value: Value to set for the last_backup_date_time property.
        """
        self._last_backup_date_time = value
    
    @property
    def refresh_date_time(self,) -> Optional[datetime]:
        """
        Gets the refreshDateTime property value. When the local administrator account credential will be refreshed and backed up to Azure Active Directory.
        Returns: Optional[datetime]
        """
        return self._refresh_date_time
    
    @refresh_date_time.setter
    def refresh_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the refreshDateTime property value. When the local administrator account credential will be refreshed and backed up to Azure Active Directory.
        Args:
            value: Value to set for the refresh_date_time property.
        """
        self._refresh_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastBackupDateTime", self.last_backup_date_time)
        writer.write_datetime_value("refreshDateTime", self.refresh_date_time)
    

