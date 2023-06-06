from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method, device, microsoft_authenticator_authentication_method_client_app_name

from . import authentication_method

@dataclass
class MicrosoftAuthenticatorAuthenticationMethod(authentication_method.AuthenticationMethod):
    odata_type = "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod"
    # The app that the user has registered to use to approve push notifications. The possible values are: microsoftAuthenticator, outlookMobile, unknownFutureValue.
    client_app_name: Optional[microsoft_authenticator_authentication_method_client_app_name.MicrosoftAuthenticatorAuthenticationMethodClientAppName] = None
    # The date and time that this app was registered. This property is null if the device is not registered for passwordless Phone Sign-In.
    created_date_time: Optional[datetime] = None
    # The registered device on which Microsoft Authenticator resides. This property is null if the device is not registered for passwordless Phone Sign-In.
    device: Optional[device.Device] = None
    # Tags containing app metadata.
    device_tag: Optional[str] = None
    # The name of the device on which this app is registered.
    display_name: Optional[str] = None
    # Numerical version of this instance of the Authenticator app.
    phone_app_version: Optional[str] = None
    
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
    

