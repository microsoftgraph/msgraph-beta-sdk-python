from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method, device, microsoft_authenticator_authentication_method_client_app_name

from . import authentication_method

class MicrosoftAuthenticatorAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftAuthenticatorAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod"
        # The app that the user has registered to use to approve push notifications. The possible values are: microsoftAuthenticator, outlookMobile, unknownFutureValue.
        self._client_app_name: Optional[microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName] = None
        # The date and time that this app was registered. This property is null if the device is not registered for passwordless Phone Sign-In.
        self._created_date_time: Optional[datetime] = None
        # The registered device on which Microsoft Authenticator resides. This property is null if the device is not registered for passwordless Phone Sign-In.
        self._device: Optional[device.Device] = None
        # Tags containing app metadata.
        self._device_tag: Optional[str] = None
        # The name of the device on which this app is registered.
        self._display_name: Optional[str] = None
        # Numerical version of this instance of the Authenticator app.
        self._phone_app_version: Optional[str] = None
    
    @property
    def client_app_name(self,) -> Optional[microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName]:
        """
        Gets the clientAppName property value. The app that the user has registered to use to approve push notifications. The possible values are: microsoftAuthenticator, outlookMobile, unknownFutureValue.
        Returns: Optional[microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName]
        """
        return self._client_app_name
    
    @client_app_name.setter
    def client_app_name(self,value: Optional[microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName] = None) -> None:
        """
        Sets the clientAppName property value. The app that the user has registered to use to approve push notifications. The possible values are: microsoftAuthenticator, outlookMobile, unknownFutureValue.
        Args:
            value: Value to set for the client_app_name property.
        """
        self._client_app_name = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time that this app was registered. This property is null if the device is not registered for passwordless Phone Sign-In.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time that this app was registered. This property is null if the device is not registered for passwordless Phone Sign-In.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAuthenticatorAuthenticationMethod()
    
    @property
    def device(self,) -> Optional[device.Device]:
        """
        Gets the device property value. The registered device on which Microsoft Authenticator resides. This property is null if the device is not registered for passwordless Phone Sign-In.
        Returns: Optional[device.Device]
        """
        return self._device
    
    @device.setter
    def device(self,value: Optional[device.Device] = None) -> None:
        """
        Sets the device property value. The registered device on which Microsoft Authenticator resides. This property is null if the device is not registered for passwordless Phone Sign-In.
        Args:
            value: Value to set for the device property.
        """
        self._device = value
    
    @property
    def device_tag(self,) -> Optional[str]:
        """
        Gets the deviceTag property value. Tags containing app metadata.
        Returns: Optional[str]
        """
        return self._device_tag
    
    @device_tag.setter
    def device_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceTag property value. Tags containing app metadata.
        Args:
            value: Value to set for the device_tag property.
        """
        self._device_tag = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the device on which this app is registered.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the device on which this app is registered.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method, device, microsoft_authenticator_authentication_method_client_app_name

        fields: Dict[str, Callable[[Any], None]] = {
            "clientAppName": lambda n : setattr(self, 'client_app_name', n.get_enum_value(microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(device.Device)),
            "deviceTag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "phoneAppVersion": lambda n : setattr(self, 'phone_app_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def phone_app_version(self,) -> Optional[str]:
        """
        Gets the phoneAppVersion property value. Numerical version of this instance of the Authenticator app.
        Returns: Optional[str]
        """
        return self._phone_app_version
    
    @phone_app_version.setter
    def phone_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneAppVersion property value. Numerical version of this instance of the Authenticator app.
        Args:
            value: Value to set for the phone_app_version property.
        """
        self._phone_app_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("clientAppName", self.client_app_name)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("phoneAppVersion", self.phone_app_version)
    

