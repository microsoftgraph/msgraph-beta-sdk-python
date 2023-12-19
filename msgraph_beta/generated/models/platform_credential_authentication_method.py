from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .device import Device
    from .platform_credential_authentication_method_key_strength import PlatformCredentialAuthenticationMethod_keyStrength
    from .platform_credential_authentication_method_platform import PlatformCredentialAuthenticationMethod_platform

from .authentication_method import AuthenticationMethod

@dataclass
class PlatformCredentialAuthenticationMethod(AuthenticationMethod):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.platformCredentialAuthenticationMethod"
    # The date and time that this Platform Credential Key was registered.
    created_date_time: Optional[datetime.datetime] = None
    # The registered device on which this Platform Credential resides. Supports $expand. When you get a user's Platform Credential registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/platformCredentialAuthenticationMethod/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
    device: Optional[Device] = None
    # The name of the device on which Platform Credential is registered.
    display_name: Optional[str] = None
    # Key strength of this Platform Credential key. Possible values are: normal, weak, unknown.
    key_strength: Optional[PlatformCredentialAuthenticationMethod_keyStrength] = None
    # Platform on which this Platform Credential key is present. Possible values are: unknown, windows, macOS,iOS, android, linux.
    platform: Optional[PlatformCredentialAuthenticationMethod_platform] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlatformCredentialAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlatformCredentialAuthenticationMethod
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlatformCredentialAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .device import Device
        from .platform_credential_authentication_method_key_strength import PlatformCredentialAuthenticationMethod_keyStrength
        from .platform_credential_authentication_method_platform import PlatformCredentialAuthenticationMethod_platform

        from .authentication_method import AuthenticationMethod
        from .device import Device
        from .platform_credential_authentication_method_key_strength import PlatformCredentialAuthenticationMethod_keyStrength
        from .platform_credential_authentication_method_platform import PlatformCredentialAuthenticationMethod_platform

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "keyStrength": lambda n : setattr(self, 'key_strength', n.get_enum_value(PlatformCredentialAuthenticationMethod_keyStrength)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(PlatformCredentialAuthenticationMethod_platform)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("keyStrength", self.key_strength)
        writer.write_enum_value("platform", self.platform)
    

