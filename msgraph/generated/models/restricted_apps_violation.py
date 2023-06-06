from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, managed_device_reported_app, policy_platform_type, restricted_apps_state

from . import entity

@dataclass
class RestrictedAppsViolation(entity.Entity):
    """
    Violation of restricted apps configuration profile per device per user
    """
    # Device configuration profile unique identifier, must be Guid
    device_configuration_id: Optional[str] = None
    # Device configuration profile name
    device_configuration_name: Optional[str] = None
    # Device name
    device_name: Optional[str] = None
    # Managed device unique identifier, must be Guid
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
    # List of violated restricted apps
    restricted_apps: Optional[List[managed_device_reported_app.ManagedDeviceReportedApp]] = None
    # Restricted apps state
    restricted_apps_state: Optional[restricted_apps_state.RestrictedAppsState] = None
    # User unique identifier, must be Guid
    user_id: Optional[str] = None
    # User name
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RestrictedAppsViolation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RestrictedAppsViolation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RestrictedAppsViolation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, managed_device_reported_app, policy_platform_type, restricted_apps_state

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceConfigurationId": lambda n : setattr(self, 'device_configuration_id', n.get_str_value()),
            "deviceConfigurationName": lambda n : setattr(self, 'device_configuration_name', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "restrictedApps": lambda n : setattr(self, 'restricted_apps', n.get_collection_of_object_values(managed_device_reported_app.ManagedDeviceReportedApp)),
            "restrictedAppsState": lambda n : setattr(self, 'restricted_apps_state', n.get_enum_value(restricted_apps_state.RestrictedAppsState)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("deviceConfigurationId", self.device_configuration_id)
        writer.write_str_value("deviceConfigurationName", self.device_configuration_name)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_collection_of_object_values("restrictedApps", self.restricted_apps)
        writer.write_enum_value("restrictedAppsState", self.restricted_apps_state)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
    

