from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_app_management_task, endpoint_security_configuration_applicable_platform, endpoint_security_configuration_profile_type, endpoint_security_configuration_type, key_value_pair, vulnerable_managed_device

from . import device_app_management_task

@dataclass
class SecurityConfigurationTask(device_app_management_task.DeviceAppManagementTask):
    odata_type = "#microsoft.graph.securityConfigurationTask"
    # The endpoint security configuration applicable platform.
    applicable_platform: Optional[endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform] = None
    # The endpoint security policy type.
    endpoint_security_policy: Optional[endpoint_security_configuration_type.EndpointSecurityConfigurationType] = None
    # The endpoint security policy profile type.
    endpoint_security_policy_profile: Optional[endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType] = None
    # Information about the mitigation.
    insights: Optional[str] = None
    # The intended settings and their values.
    intended_settings: Optional[List[key_value_pair.KeyValuePair]] = None
    # The number of vulnerable devices. Valid values 0 to 65536
    managed_device_count: Optional[int] = None
    # The vulnerable managed devices.
    managed_devices: Optional[List[vulnerable_managed_device.VulnerableManagedDevice]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_app_management_task, endpoint_security_configuration_applicable_platform, endpoint_security_configuration_profile_type, endpoint_security_configuration_type, key_value_pair, vulnerable_managed_device

        fields: Dict[str, Callable[[Any], None]] = {
            "applicablePlatform": lambda n : setattr(self, 'applicable_platform', n.get_enum_value(endpoint_security_configuration_applicable_platform.EndpointSecurityConfigurationApplicablePlatform)),
            "endpointSecurityPolicy": lambda n : setattr(self, 'endpoint_security_policy', n.get_enum_value(endpoint_security_configuration_type.EndpointSecurityConfigurationType)),
            "endpointSecurityPolicyProfile": lambda n : setattr(self, 'endpoint_security_policy_profile', n.get_enum_value(endpoint_security_configuration_profile_type.EndpointSecurityConfigurationProfileType)),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "intendedSettings": lambda n : setattr(self, 'intended_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(vulnerable_managed_device.VulnerableManagedDevice)),
            "managedDeviceCount": lambda n : setattr(self, 'managed_device_count', n.get_int_value()),
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
        writer.write_enum_value("applicablePlatform", self.applicable_platform)
        writer.write_enum_value("endpointSecurityPolicy", self.endpoint_security_policy)
        writer.write_enum_value("endpointSecurityPolicyProfile", self.endpoint_security_policy_profile)
        writer.write_str_value("insights", self.insights)
        writer.write_collection_of_object_values("intendedSettings", self.intended_settings)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_int_value("managedDeviceCount", self.managed_device_count)
    

