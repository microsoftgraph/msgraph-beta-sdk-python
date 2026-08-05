from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_info import AuthenticationInfo
    from .connection_info import ConnectionInfo

from .connection_info import ConnectionInfo

@dataclass
class ExternalSapAcConnectionInfo(ConnectionInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalSapAcConnectionInfo"
    # The authenticationInfo property
    authentication_info: Optional[AuthenticationInfo] = None
    # The keyVaultName property
    key_vault_name: Optional[str] = None
    # The resourceGroup property
    resource_group: Optional[str] = None
    # The subscriptionId property
    subscription_id: Optional[str] = None
    # The systemId property
    system_id: Optional[str] = None
    # The userIdentifier property
    user_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalSapAcConnectionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalSapAcConnectionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalSapAcConnectionInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_info import AuthenticationInfo
        from .connection_info import ConnectionInfo

        from .authentication_info import AuthenticationInfo
        from .connection_info import ConnectionInfo

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationInfo": lambda n : setattr(self, 'authentication_info', n.get_object_value(AuthenticationInfo)),
            "keyVaultName": lambda n : setattr(self, 'key_vault_name', n.get_str_value()),
            "resourceGroup": lambda n : setattr(self, 'resource_group', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "systemId": lambda n : setattr(self, 'system_id', n.get_str_value()),
            "userIdentifier": lambda n : setattr(self, 'user_identifier', n.get_str_value()),
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
        writer.write_object_value("authenticationInfo", self.authentication_info)
        writer.write_str_value("keyVaultName", self.key_vault_name)
        writer.write_str_value("resourceGroup", self.resource_group)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("systemId", self.system_id)
        writer.write_str_value("userIdentifier", self.user_identifier)
    

