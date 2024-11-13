from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget
    from .open_id_connect_setting import OpenIdConnectSetting

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class ExternalAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalAuthenticationMethodConfiguration"
    # appId for the app registration in Microsoft Entra ID representing the integration with the external provider.
    app_id: Optional[str] = None
    # Display name for the external authentication method. This name is shown to users during sign-in.
    display_name: Optional[str] = None
    # A collection of groups that are enabled to use an authentication method as part of an authentication method policy in Microsoft Entra ID.
    include_targets: Optional[List[AuthenticationMethodTarget]] = None
    # The openIdConnectSetting property
    open_id_connect_setting: Optional[OpenIdConnectSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .open_id_connect_setting import OpenIdConnectSetting

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .open_id_connect_setting import OpenIdConnectSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "openIdConnectSetting": lambda n : setattr(self, 'open_id_connect_setting', n.get_object_value(OpenIdConnectSetting)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .open_id_connect_setting import OpenIdConnectSetting

        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_object_value("openIdConnectSetting", self.open_id_connect_setting)
    

