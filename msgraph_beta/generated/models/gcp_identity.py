from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .gcp_cloud_function import GcpCloudFunction
    from .gcp_group import GcpGroup
    from .gcp_service_account import GcpServiceAccount
    from .gcp_user import GcpUser

from .authorization_system_identity import AuthorizationSystemIdentity

@dataclass
class GcpIdentity(AuthorizationSystemIdentity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpIdentity"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpCloudFunction".casefold():
            from .gcp_cloud_function import GcpCloudFunction

            return GcpCloudFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpGroup".casefold():
            from .gcp_group import GcpGroup

            return GcpGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpServiceAccount".casefold():
            from .gcp_service_account import GcpServiceAccount

            return GcpServiceAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpUser".casefold():
            from .gcp_user import GcpUser

            return GcpUser()
        return GcpIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        fields: Dict[str, Callable[[Any], None]] = {
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
    

