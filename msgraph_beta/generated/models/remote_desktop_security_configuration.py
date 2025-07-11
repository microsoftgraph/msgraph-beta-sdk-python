from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approved_client_app import ApprovedClientApp
    from .entity import Entity
    from .target_device_group import TargetDeviceGroup

from .entity import Entity

@dataclass
class RemoteDesktopSecurityConfiguration(Entity, Parsable):
    # The approvedClientApps property
    approved_client_apps: Optional[list[ApprovedClientApp]] = None
    # Determines if Microsoft Entra ID RDS authentication protocol for RDP is enabled.
    is_remote_desktop_protocol_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of target device groups that are associated with the RDS security configuration that will be enabled for SSO when a client connects to the target device over RDP using the new Microsoft Entra ID RDS authentication protocol.
    target_device_groups: Optional[list[TargetDeviceGroup]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteDesktopSecurityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteDesktopSecurityConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteDesktopSecurityConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approved_client_app import ApprovedClientApp
        from .entity import Entity
        from .target_device_group import TargetDeviceGroup

        from .approved_client_app import ApprovedClientApp
        from .entity import Entity
        from .target_device_group import TargetDeviceGroup

        fields: dict[str, Callable[[Any], None]] = {
            "approvedClientApps": lambda n : setattr(self, 'approved_client_apps', n.get_collection_of_object_values(ApprovedClientApp)),
            "isRemoteDesktopProtocolEnabled": lambda n : setattr(self, 'is_remote_desktop_protocol_enabled', n.get_bool_value()),
            "targetDeviceGroups": lambda n : setattr(self, 'target_device_groups', n.get_collection_of_object_values(TargetDeviceGroup)),
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
        writer.write_collection_of_object_values("approvedClientApps", self.approved_client_apps)
        writer.write_bool_value("isRemoteDesktopProtocolEnabled", self.is_remote_desktop_protocol_enabled)
        writer.write_collection_of_object_values("targetDeviceGroups", self.target_device_groups)
    

