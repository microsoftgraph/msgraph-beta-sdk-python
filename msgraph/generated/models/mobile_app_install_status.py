from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
resultant_app_state = lazy_import('msgraph.generated.models.resultant_app_state')
resultant_app_state_detail = lazy_import('msgraph.generated.models.resultant_app_state_detail')

class MobileAppInstallStatus(entity.Entity):
    """
    Contains properties for the installation state of a mobile app for a device.
    """
    @property
    def app(self,) -> Optional[mobile_app.MobileApp]:
        """
        Gets the app property value. The navigation link to the mobile app.
        Returns: Optional[mobile_app.MobileApp]
        """
        return self._app
    
    @app.setter
    def app(self,value: Optional[mobile_app.MobileApp] = None) -> None:
        """
        Sets the app property value. The navigation link to the mobile app.
        Args:
            value: Value to set for the app property.
        """
        self._app = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppInstallStatus and sets the default values.
        """
        super().__init__()
        # The navigation link to the mobile app.
        self._app: Optional[mobile_app.MobileApp] = None
        # Device ID
        self._device_id: Optional[str] = None
        # Device name
        self._device_name: Optional[str] = None
        # Human readable version of the application
        self._display_version: Optional[str] = None
        # The error code for install or uninstall failures.
        self._error_code: Optional[int] = None
        # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        self._install_state: Optional[resultant_app_state.ResultantAppState] = None
        # Enum indicating additional details regarding why an application has a particular install state.
        self._install_state_detail: Optional[resultant_app_state_detail.ResultantAppStateDetail] = None
        # Last sync date time
        self._last_sync_date_time: Optional[datetime] = None
        # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        self._mobile_app_install_status_value: Optional[resultant_app_state.ResultantAppState] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # OS Description
        self._os_description: Optional[str] = None
        # OS Version
        self._os_version: Optional[str] = None
        # Device User Name
        self._user_name: Optional[str] = None
        # User Principal Name
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppInstallStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppInstallStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppInstallStatus()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Device ID
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Device ID
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def display_version(self,) -> Optional[str]:
        """
        Gets the displayVersion property value. Human readable version of the application
        Returns: Optional[str]
        """
        return self._display_version
    
    @display_version.setter
    def display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the displayVersion property value. Human readable version of the application
        Args:
            value: Value to set for the displayVersion property.
        """
        self._display_version = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. The error code for install or uninstall failures.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. The error code for install or uninstall failures.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(mobile_app.MobileApp)),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "display_version": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "install_state": lambda n : setattr(self, 'install_state', n.get_enum_value(resultant_app_state.ResultantAppState)),
            "install_state_detail": lambda n : setattr(self, 'install_state_detail', n.get_enum_value(resultant_app_state_detail.ResultantAppStateDetail)),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "mobile_app_install_status_value": lambda n : setattr(self, 'mobile_app_install_status_value', n.get_enum_value(resultant_app_state.ResultantAppState)),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_state(self,) -> Optional[resultant_app_state.ResultantAppState]:
        """
        Gets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Returns: Optional[resultant_app_state.ResultantAppState]
        """
        return self._install_state
    
    @install_state.setter
    def install_state(self,value: Optional[resultant_app_state.ResultantAppState] = None) -> None:
        """
        Sets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Args:
            value: Value to set for the installState property.
        """
        self._install_state = value
    
    @property
    def install_state_detail(self,) -> Optional[resultant_app_state_detail.ResultantAppStateDetail]:
        """
        Gets the installStateDetail property value. Enum indicating additional details regarding why an application has a particular install state.
        Returns: Optional[resultant_app_state_detail.ResultantAppStateDetail]
        """
        return self._install_state_detail
    
    @install_state_detail.setter
    def install_state_detail(self,value: Optional[resultant_app_state_detail.ResultantAppStateDetail] = None) -> None:
        """
        Sets the installStateDetail property value. Enum indicating additional details regarding why an application has a particular install state.
        Args:
            value: Value to set for the installStateDetail property.
        """
        self._install_state_detail = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last sync date time
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last sync date time
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def mobile_app_install_status_value(self,) -> Optional[resultant_app_state.ResultantAppState]:
        """
        Gets the mobileAppInstallStatusValue property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Returns: Optional[resultant_app_state.ResultantAppState]
        """
        return self._mobile_app_install_status_value
    
    @mobile_app_install_status_value.setter
    def mobile_app_install_status_value(self,value: Optional[resultant_app_state.ResultantAppState] = None) -> None:
        """
        Sets the mobileAppInstallStatusValue property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Args:
            value: Value to set for the mobileAppInstallStatusValue property.
        """
        self._mobile_app_install_status_value = value
    
    @property
    def os_description(self,) -> Optional[str]:
        """
        Gets the osDescription property value. OS Description
        Returns: Optional[str]
        """
        return self._os_description
    
    @os_description.setter
    def os_description(self,value: Optional[str] = None) -> None:
        """
        Sets the osDescription property value. OS Description
        Args:
            value: Value to set for the osDescription property.
        """
        self._os_description = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. OS Version
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. OS Version
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("app", self.app)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_enum_value("installState", self.install_state)
        writer.write_enum_value("installStateDetail", self.install_state_detail)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("mobileAppInstallStatusValue", self.mobile_app_install_status_value)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. Device User Name
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. Device User Name
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

