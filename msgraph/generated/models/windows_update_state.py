from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_update_status = lazy_import('msgraph.generated.models.windows_update_status')

class WindowsUpdateState(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsUpdateState and sets the default values.
        """
        super().__init__()
        # Device display name.
        self._device_display_name: Optional[str] = None
        # The id of the device.
        self._device_id: Optional[str] = None
        # The current feature update version of the device.
        self._feature_update_version: Optional[str] = None
        # The date time that the Windows Update Agent did a successful scan.
        self._last_scan_date_time: Optional[datetime] = None
        # Last date time that the device sync with with Microsoft Intune.
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Quality Update Version of the device.
        self._quality_update_version: Optional[str] = None
        # Windows update for business configuration device states
        self._status: Optional[windows_update_status.WindowsUpdateStatus] = None
        # The id of the user.
        self._user_id: Optional[str] = None
        # User principal name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateState()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Device display name.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Device display name.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def feature_update_version(self,) -> Optional[str]:
        """
        Gets the featureUpdateVersion property value. The current feature update version of the device.
        Returns: Optional[str]
        """
        return self._feature_update_version
    
    @feature_update_version.setter
    def feature_update_version(self,value: Optional[str] = None) -> None:
        """
        Sets the featureUpdateVersion property value. The current feature update version of the device.
        Args:
            value: Value to set for the featureUpdateVersion property.
        """
        self._feature_update_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "feature_update_version": lambda n : setattr(self, 'feature_update_version', n.get_str_value()),
            "last_scan_date_time": lambda n : setattr(self, 'last_scan_date_time', n.get_datetime_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "quality_update_version": lambda n : setattr(self, 'quality_update_version', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(windows_update_status.WindowsUpdateStatus)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_scan_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastScanDateTime property value. The date time that the Windows Update Agent did a successful scan.
        Returns: Optional[datetime]
        """
        return self._last_scan_date_time
    
    @last_scan_date_time.setter
    def last_scan_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastScanDateTime property value. The date time that the Windows Update Agent did a successful scan.
        Args:
            value: Value to set for the lastScanDateTime property.
        """
        self._last_scan_date_time = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last date time that the device sync with with Microsoft Intune.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last date time that the device sync with with Microsoft Intune.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def quality_update_version(self,) -> Optional[str]:
        """
        Gets the qualityUpdateVersion property value. The Quality Update Version of the device.
        Returns: Optional[str]
        """
        return self._quality_update_version
    
    @quality_update_version.setter
    def quality_update_version(self,value: Optional[str] = None) -> None:
        """
        Sets the qualityUpdateVersion property value. The Quality Update Version of the device.
        Args:
            value: Value to set for the qualityUpdateVersion property.
        """
        self._quality_update_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("featureUpdateVersion", self.feature_update_version)
        writer.write_datetime_value("lastScanDateTime", self.last_scan_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("qualityUpdateVersion", self.quality_update_version)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def status(self,) -> Optional[windows_update_status.WindowsUpdateStatus]:
        """
        Gets the status property value. Windows update for business configuration device states
        Returns: Optional[windows_update_status.WindowsUpdateStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[windows_update_status.WindowsUpdateStatus] = None) -> None:
        """
        Sets the status property value. Windows update for business configuration device states
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The id of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The id of the user.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

