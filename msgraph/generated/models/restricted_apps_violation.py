from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_device_reported_app = lazy_import('msgraph.generated.models.managed_device_reported_app')
policy_platform_type = lazy_import('msgraph.generated.models.policy_platform_type')
restricted_apps_state = lazy_import('msgraph.generated.models.restricted_apps_state')

class RestrictedAppsViolation(entity.Entity):
    """
    Violation of restricted apps configuration profile per device per user
    """
    def __init__(self,) -> None:
        """
        Instantiates a new restrictedAppsViolation and sets the default values.
        """
        super().__init__()
        # Device configuration profile unique identifier, must be Guid
        self._device_configuration_id: Optional[str] = None
        # Device configuration profile name
        self._device_configuration_name: Optional[str] = None
        # Device name
        self._device_name: Optional[str] = None
        # Managed device unique identifier, must be Guid
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types for policies.
        self._platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
        # List of violated restricted apps
        self._restricted_apps: Optional[List[managed_device_reported_app.ManagedDeviceReportedApp]] = None
        # Restricted apps state
        self._restricted_apps_state: Optional[restricted_apps_state.RestrictedAppsState] = None
        # User unique identifier, must be Guid
        self._user_id: Optional[str] = None
        # User name
        self._user_name: Optional[str] = None
    
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
    
    @property
    def device_configuration_id(self,) -> Optional[str]:
        """
        Gets the deviceConfigurationId property value. Device configuration profile unique identifier, must be Guid
        Returns: Optional[str]
        """
        return self._device_configuration_id
    
    @device_configuration_id.setter
    def device_configuration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceConfigurationId property value. Device configuration profile unique identifier, must be Guid
        Args:
            value: Value to set for the deviceConfigurationId property.
        """
        self._device_configuration_id = value
    
    @property
    def device_configuration_name(self,) -> Optional[str]:
        """
        Gets the deviceConfigurationName property value. Device configuration profile name
        Returns: Optional[str]
        """
        return self._device_configuration_name
    
    @device_configuration_name.setter
    def device_configuration_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceConfigurationName property value. Device configuration profile name
        Args:
            value: Value to set for the deviceConfigurationName property.
        """
        self._device_configuration_name = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_configuration_id": lambda n : setattr(self, 'device_configuration_id', n.get_str_value()),
            "device_configuration_name": lambda n : setattr(self, 'device_configuration_name', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "restricted_apps": lambda n : setattr(self, 'restricted_apps', n.get_collection_of_object_values(managed_device_reported_app.ManagedDeviceReportedApp)),
            "restricted_apps_state": lambda n : setattr(self, 'restricted_apps_state', n.get_enum_value(restricted_apps_state.RestrictedAppsState)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Managed device unique identifier, must be Guid
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Managed device unique identifier, must be Guid
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def platform_type(self,) -> Optional[policy_platform_type.PolicyPlatformType]:
        """
        Gets the platformType property value. Supported platform types for policies.
        Returns: Optional[policy_platform_type.PolicyPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[policy_platform_type.PolicyPlatformType] = None) -> None:
        """
        Sets the platformType property value. Supported platform types for policies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value
    
    @property
    def restricted_apps(self,) -> Optional[List[managed_device_reported_app.ManagedDeviceReportedApp]]:
        """
        Gets the restrictedApps property value. List of violated restricted apps
        Returns: Optional[List[managed_device_reported_app.ManagedDeviceReportedApp]]
        """
        return self._restricted_apps
    
    @restricted_apps.setter
    def restricted_apps(self,value: Optional[List[managed_device_reported_app.ManagedDeviceReportedApp]] = None) -> None:
        """
        Sets the restrictedApps property value. List of violated restricted apps
        Args:
            value: Value to set for the restrictedApps property.
        """
        self._restricted_apps = value
    
    @property
    def restricted_apps_state(self,) -> Optional[restricted_apps_state.RestrictedAppsState]:
        """
        Gets the restrictedAppsState property value. Restricted apps state
        Returns: Optional[restricted_apps_state.RestrictedAppsState]
        """
        return self._restricted_apps_state
    
    @restricted_apps_state.setter
    def restricted_apps_state(self,value: Optional[restricted_apps_state.RestrictedAppsState] = None) -> None:
        """
        Sets the restrictedAppsState property value. Restricted apps state
        Args:
            value: Value to set for the restrictedAppsState property.
        """
        self._restricted_apps_state = value
    
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
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User unique identifier, must be Guid
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User unique identifier, must be Guid
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. User name
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. User name
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

