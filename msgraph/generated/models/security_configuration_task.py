from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_app_management_task = lazy_import('msgraph.generated.models.device_app_management_task')
endpoint_security_configuration_applicable_platform = lazy_import('msgraph.generated.models.endpoint_security_configuration_applicable_platform')
endpoint_security_configuration_profile_type = lazy_import('msgraph.generated.models.endpoint_security_configuration_profile_type')
endpoint_security_configuration_type = lazy_import('msgraph.generated.models.endpoint_security_configuration_type')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
vulnerable_managed_device = lazy_import('msgraph.generated.models.vulnerable_managed_device')

class SecurityConfigurationTask(device_app_management_task.DeviceAppManagementTask):
    @property
    def applicable_platform(self,) -> Optional[endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform]:
        """
        Gets the applicablePlatform property value. The endpoint security configuration applicable platform.
        Returns: Optional[endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform]
        """
        return self._applicable_platform
    
    @applicable_platform.setter
    def applicable_platform(self,value: Optional[endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform] = None) -> None:
        """
        Sets the applicablePlatform property value. The endpoint security configuration applicable platform.
        Args:
            value: Value to set for the applicablePlatform property.
        """
        self._applicable_platform = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SecurityConfigurationTask and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.securityConfigurationTask"
        # The endpoint security configuration applicable platform.
        self._applicable_platform: Optional[endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform] = None
        # The endpoint security policy type.
        self._endpoint_security_policy: Optional[endpoint_security_configuration_type.EndpointSecurityConfigurationType] = None
        # The endpoint security policy profile type.
        self._endpoint_security_policy_profile: Optional[endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType] = None
        # Information about the mitigation.
        self._insights: Optional[str] = None
        # The intended settings and their values.
        self._intended_settings: Optional[List[key_value_pair.KeyValuePair]] = None
        # The number of vulnerable devices.
        self._managed_device_count: Optional[int] = None
        # The vulnerable managed devices.
        self._managed_devices: Optional[List[vulnerable_managed_device.VulnerableManagedDevice]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityConfigurationTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityConfigurationTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityConfigurationTask()
    
    @property
    def endpoint_security_policy(self,) -> Optional[endpoint_security_configuration_type.EndpointSecurityConfigurationType]:
        """
        Gets the endpointSecurityPolicy property value. The endpoint security policy type.
        Returns: Optional[endpoint_security_configuration_type.EndpointSecurityConfigurationType]
        """
        return self._endpoint_security_policy
    
    @endpoint_security_policy.setter
    def endpoint_security_policy(self,value: Optional[endpoint_security_configuration_type.EndpointSecurityConfigurationType] = None) -> None:
        """
        Sets the endpointSecurityPolicy property value. The endpoint security policy type.
        Args:
            value: Value to set for the endpointSecurityPolicy property.
        """
        self._endpoint_security_policy = value
    
    @property
    def endpoint_security_policy_profile(self,) -> Optional[endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType]:
        """
        Gets the endpointSecurityPolicyProfile property value. The endpoint security policy profile type.
        Returns: Optional[endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType]
        """
        return self._endpoint_security_policy_profile
    
    @endpoint_security_policy_profile.setter
    def endpoint_security_policy_profile(self,value: Optional[endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType] = None) -> None:
        """
        Sets the endpointSecurityPolicyProfile property value. The endpoint security policy profile type.
        Args:
            value: Value to set for the endpointSecurityPolicyProfile property.
        """
        self._endpoint_security_policy_profile = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_platform": lambda n : setattr(self, 'applicable_platform', n.get_enum_value(endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform)),
            "endpoint_security_policy": lambda n : setattr(self, 'endpoint_security_policy', n.get_enum_value(endpoint_security_configuration_type.EndpointSecurityConfigurationType)),
            "endpoint_security_policy_profile": lambda n : setattr(self, 'endpoint_security_policy_profile', n.get_enum_value(endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType)),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "intended_settings": lambda n : setattr(self, 'intended_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "managed_device_count": lambda n : setattr(self, 'managed_device_count', n.get_int_value()),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(vulnerable_managed_device.VulnerableManagedDevice)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def insights(self,) -> Optional[str]:
        """
        Gets the insights property value. Information about the mitigation.
        Returns: Optional[str]
        """
        return self._insights
    
    @insights.setter
    def insights(self,value: Optional[str] = None) -> None:
        """
        Sets the insights property value. Information about the mitigation.
        Args:
            value: Value to set for the insights property.
        """
        self._insights = value
    
    @property
    def intended_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the intendedSettings property value. The intended settings and their values.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._intended_settings
    
    @intended_settings.setter
    def intended_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the intendedSettings property value. The intended settings and their values.
        Args:
            value: Value to set for the intendedSettings property.
        """
        self._intended_settings = value
    
    @property
    def managed_device_count(self,) -> Optional[int]:
        """
        Gets the managedDeviceCount property value. The number of vulnerable devices.
        Returns: Optional[int]
        """
        return self._managed_device_count
    
    @managed_device_count.setter
    def managed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the managedDeviceCount property value. The number of vulnerable devices.
        Args:
            value: Value to set for the managedDeviceCount property.
        """
        self._managed_device_count = value
    
    @property
    def managed_devices(self,) -> Optional[List[vulnerable_managed_device.VulnerableManagedDevice]]:
        """
        Gets the managedDevices property value. The vulnerable managed devices.
        Returns: Optional[List[vulnerable_managed_device.VulnerableManagedDevice]]
        """
        return self._managed_devices
    
    @managed_devices.setter
    def managed_devices(self,value: Optional[List[vulnerable_managed_device.VulnerableManagedDevice]] = None) -> None:
        """
        Sets the managedDevices property value. The vulnerable managed devices.
        Args:
            value: Value to set for the managedDevices property.
        """
        self._managed_devices = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("applicablePlatform", self.applicable_platform)
        writer.write_enum_value("endpointSecurityPolicy", self.endpoint_security_policy)
        writer.write_enum_value("endpointSecurityPolicyProfile", self.endpoint_security_policy_profile)
        writer.write_str_value("insights", self.insights)
        writer.write_collection_of_object_values("intendedSettings", self.intended_settings)
        writer.write_int_value("managedDeviceCount", self.managed_device_count)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
    

