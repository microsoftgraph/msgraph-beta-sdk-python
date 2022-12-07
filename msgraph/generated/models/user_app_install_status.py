from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
mobile_app_install_status = lazy_import('msgraph.generated.models.mobile_app_install_status')

class UserAppInstallStatus(entity.Entity):
    """
    Contains properties for the installation status for a user.
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
        Instantiates a new userAppInstallStatus and sets the default values.
        """
        super().__init__()
        # The navigation link to the mobile app.
        self._app: Optional[mobile_app.MobileApp] = None
        # The install state of the app on devices.
        self._device_statuses: Optional[List[mobile_app_install_status.MobileAppInstallStatus]] = None
        # Failed Device Count.
        self._failed_device_count: Optional[int] = None
        # Installed Device Count.
        self._installed_device_count: Optional[int] = None
        # Not installed device count.
        self._not_installed_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User name.
        self._user_name: Optional[str] = None
        # User Principal Name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAppInstallStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAppInstallStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserAppInstallStatus()
    
    @property
    def device_statuses(self,) -> Optional[List[mobile_app_install_status.MobileAppInstallStatus]]:
        """
        Gets the deviceStatuses property value. The install state of the app on devices.
        Returns: Optional[List[mobile_app_install_status.MobileAppInstallStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[mobile_app_install_status.MobileAppInstallStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. The install state of the app on devices.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def failed_device_count(self,) -> Optional[int]:
        """
        Gets the failedDeviceCount property value. Failed Device Count.
        Returns: Optional[int]
        """
        return self._failed_device_count
    
    @failed_device_count.setter
    def failed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedDeviceCount property value. Failed Device Count.
        Args:
            value: Value to set for the failedDeviceCount property.
        """
        self._failed_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(mobile_app.MobileApp)),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(mobile_app_install_status.MobileAppInstallStatus)),
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "installed_device_count": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "not_installed_device_count": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def installed_device_count(self,) -> Optional[int]:
        """
        Gets the installedDeviceCount property value. Installed Device Count.
        Returns: Optional[int]
        """
        return self._installed_device_count
    
    @installed_device_count.setter
    def installed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the installedDeviceCount property value. Installed Device Count.
        Args:
            value: Value to set for the installedDeviceCount property.
        """
        self._installed_device_count = value
    
    @property
    def not_installed_device_count(self,) -> Optional[int]:
        """
        Gets the notInstalledDeviceCount property value. Not installed device count.
        Returns: Optional[int]
        """
        return self._not_installed_device_count
    
    @not_installed_device_count.setter
    def not_installed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notInstalledDeviceCount property value. Not installed device count.
        Args:
            value: Value to set for the notInstalledDeviceCount property.
        """
        self._not_installed_device_count = value
    
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
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("installedDeviceCount", self.installed_device_count)
        writer.write_int_value("notInstalledDeviceCount", self.not_installed_device_count)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. User name.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. User name.
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

