from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_permission_action, android_profile_applicability, managed_device_mobile_app_configuration

from . import managed_device_mobile_app_configuration

@dataclass
class AndroidManagedStoreAppConfiguration(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration):
    odata_type = "#microsoft.graph.androidManagedStoreAppConfiguration"
    # Whether or not this AppConfig is an OEMConfig policy.
    app_supports_oem_config: Optional[bool] = None
    # Setting to specify whether to allow ConnectedApps experience for this app.
    connected_apps_enabled: Optional[bool] = None
    # Android Enterprise app configuration package id.
    package_id: Optional[str] = None
    # Android Enterprise app configuration JSON payload.
    payload_json: Optional[str] = None
    # List of Android app permissions and corresponding permission actions.
    permission_actions: Optional[List[android_permission_action.AndroidPermissionAction]] = None
    # Android profile applicability
    profile_applicability: Optional[android_profile_applicability.AndroidProfileApplicability] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_permission_action, android_profile_applicability, managed_device_mobile_app_configuration

        from . import android_permission_action, android_profile_applicability, managed_device_mobile_app_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "appSupportsOemConfig": lambda n : setattr(self, 'app_supports_oem_config', n.get_bool_value()),
            "connectedAppsEnabled": lambda n : setattr(self, 'connected_apps_enabled', n.get_bool_value()),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "payloadJson": lambda n : setattr(self, 'payload_json', n.get_str_value()),
            "permissionActions": lambda n : setattr(self, 'permission_actions', n.get_collection_of_object_values(android_permission_action.AndroidPermissionAction)),
            "profileApplicability": lambda n : setattr(self, 'profile_applicability', n.get_enum_value(android_profile_applicability.AndroidProfileApplicability)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("appSupportsOemConfig", self.app_supports_oem_config)
        writer.write_bool_value("connectedAppsEnabled", self.connected_apps_enabled)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("payloadJson", self.payload_json)
        writer.write_collection_of_object_values("permissionActions", self.permission_actions)
        writer.write_enum_value("profileApplicability", self.profile_applicability)
    

