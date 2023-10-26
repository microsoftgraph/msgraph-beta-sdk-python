from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .authentication_method_key_strength import AuthenticationMethodKeyStrength
    from .authentication_method_platform import AuthenticationMethodPlatform
    from .device import Device

from .authentication_method import AuthenticationMethod

@dataclass
class PlatformCredentialAuthenticationMethod(AuthenticationMethod):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.platformCredentialAuthenticationMethod"
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The device property
    device: Optional[Device] = None
    # The displayName property
    display_name: Optional[str] = None
    # The keyStrength property
    key_strength: Optional[AuthenticationMethodKeyStrength] = None
    # The platform property
    platform: Optional[AuthenticationMethodPlatform] = None
    
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
        from .authentication_method_key_strength import AuthenticationMethodKeyStrength
        from .authentication_method_platform import AuthenticationMethodPlatform
        from .device import Device

        from .authentication_method import AuthenticationMethod
        from .authentication_method_key_strength import AuthenticationMethodKeyStrength
        from .authentication_method_platform import AuthenticationMethodPlatform
        from .device import Device

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "keyStrength": lambda n : setattr(self, 'key_strength', n.get_enum_value(AuthenticationMethodKeyStrength)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(AuthenticationMethodPlatform)),
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
    

