from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_permission_action import AndroidPermissionAction
    from .android_profile_applicability import AndroidProfileApplicability
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

@dataclass
class AndroidManagedStoreAppConfiguration(ManagedDeviceMobileAppConfiguration):
    """
    Contains properties, inherited properties and actions for Android Enterprise mobile app configurations.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedStoreAppConfiguration"
    # Whether or not this AppConfig is an OEMConfig policy. This property is read-only.
    app_supports_oem_config: Optional[bool] = None
    # Setting to specify whether to allow ConnectedApps experience for this app.
    connected_apps_enabled: Optional[bool] = None
    # Android Enterprise app configuration package id.
    package_id: Optional[str] = None
    # Android Enterprise app configuration JSON payload.
    payload_json: Optional[str] = None
    # List of Android app permissions and corresponding permission actions.
    permission_actions: Optional[List[AndroidPermissionAction]] = None
    # Android profile applicability
    profile_applicability: Optional[AndroidProfileApplicability] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_permission_action import AndroidPermissionAction
        from .android_profile_applicability import AndroidProfileApplicability
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        from .android_permission_action import AndroidPermissionAction
        from .android_profile_applicability import AndroidProfileApplicability
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "appSupportsOemConfig": lambda n : setattr(self, 'app_supports_oem_config', n.get_bool_value()),
            "connectedAppsEnabled": lambda n : setattr(self, 'connected_apps_enabled', n.get_bool_value()),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "payloadJson": lambda n : setattr(self, 'payload_json', n.get_str_value()),
            "permissionActions": lambda n : setattr(self, 'permission_actions', n.get_collection_of_object_values(AndroidPermissionAction)),
            "profileApplicability": lambda n : setattr(self, 'profile_applicability', n.get_enum_value(AndroidProfileApplicability)),
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
        writer.write_bool_value("connectedAppsEnabled", self.connected_apps_enabled)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("payloadJson", self.payload_json)
        writer.write_collection_of_object_values("permissionActions", self.permission_actions)
        writer.write_enum_value("profileApplicability", self.profile_applicability)
    

