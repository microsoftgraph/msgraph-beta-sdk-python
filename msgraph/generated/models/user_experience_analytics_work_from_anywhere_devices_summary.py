from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import user_experience_analytics_autopilot_devices_summary, user_experience_analytics_cloud_identity_devices_summary, user_experience_analytics_cloud_management_devices_summary, user_experience_analytics_windows10_devices_summary

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereDevicesSummary(AdditionalDataHolder, Parsable):
    """
    The user experience analytics Work From Anywhere metrics devices summary.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The value of work from anywhere autopilot devices summary.
    autopilot_devices_summary: Optional[user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary] = None
    # The user experience analytics work from anywhere Cloud Identity devices summary.
    cloud_identity_devices_summary: Optional[user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary] = None
    # The user experience work from anywhere Cloud management devices summary.
    cloud_management_devices_summary: Optional[user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary] = None
    # Total number of co-managed devices. Valid values -2147483648 to 2147483647
    co_managed_devices: Optional[int] = None
    # The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
    devices_not_autopilot_registered: Optional[int] = None
    # The count of intune devices not autopilot profile assigned. Valid values -2147483648 to 2147483647
    devices_without_autopilot_profile_assigned: Optional[int] = None
    # The count of devices that are not cloud identity. Valid values -2147483648 to 2147483647
    devices_without_cloud_identity: Optional[int] = None
    # The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
    intune_devices: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total count of tenant attach devices. Valid values -2147483648 to 2147483647
    tenant_attach_devices: Optional[int] = None
    # The total count of devices. Valid values -2147483648 to 2147483647
    total_devices: Optional[int] = None
    # The count of Windows 10 devices that have unsupported OS versions. Valid values -2147483648 to 2147483647
    unsupported_o_sversion_devices: Optional[int] = None
    # The count of windows 10 devices. Valid values -2147483648 to 2147483647
    windows10_devices: Optional[int] = None
    # The user experience analytics work from anywhere Windows 10 devices summary.
    windows10_devices_summary: Optional[user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary] = None
    # The count of windows 10 devices that are Intune and Comanaged. Valid values -2147483648 to 2147483647
    windows10_devices_without_tenant_attach: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereDevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWorkFromAnywhereDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import user_experience_analytics_autopilot_devices_summary, user_experience_analytics_cloud_identity_devices_summary, user_experience_analytics_cloud_management_devices_summary, user_experience_analytics_windows10_devices_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "autopilotDevicesSummary": lambda n : setattr(self, 'autopilot_devices_summary', n.get_object_value(user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary)),
            "cloudIdentityDevicesSummary": lambda n : setattr(self, 'cloud_identity_devices_summary', n.get_object_value(user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary)),
            "cloudManagementDevicesSummary": lambda n : setattr(self, 'cloud_management_devices_summary', n.get_object_value(user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary)),
            "coManagedDevices": lambda n : setattr(self, 'co_managed_devices', n.get_int_value()),
            "devicesNotAutopilotRegistered": lambda n : setattr(self, 'devices_not_autopilot_registered', n.get_int_value()),
            "devicesWithoutAutopilotProfileAssigned": lambda n : setattr(self, 'devices_without_autopilot_profile_assigned', n.get_int_value()),
            "devicesWithoutCloudIdentity": lambda n : setattr(self, 'devices_without_cloud_identity', n.get_int_value()),
            "intuneDevices": lambda n : setattr(self, 'intune_devices', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantAttachDevices": lambda n : setattr(self, 'tenant_attach_devices', n.get_int_value()),
            "totalDevices": lambda n : setattr(self, 'total_devices', n.get_int_value()),
            "unsupportedOSversionDevices": lambda n : setattr(self, 'unsupported_o_sversion_devices', n.get_int_value()),
            "windows10Devices": lambda n : setattr(self, 'windows10_devices', n.get_int_value()),
            "windows10DevicesSummary": lambda n : setattr(self, 'windows10_devices_summary', n.get_object_value(user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary)),
            "windows10DevicesWithoutTenantAttach": lambda n : setattr(self, 'windows10_devices_without_tenant_attach', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("autopilotDevicesSummary", self.autopilot_devices_summary)
        writer.write_object_value("cloudIdentityDevicesSummary", self.cloud_identity_devices_summary)
        writer.write_object_value("cloudManagementDevicesSummary", self.cloud_management_devices_summary)
        writer.write_int_value("coManagedDevices", self.co_managed_devices)
        writer.write_int_value("devicesNotAutopilotRegistered", self.devices_not_autopilot_registered)
        writer.write_int_value("devicesWithoutAutopilotProfileAssigned", self.devices_without_autopilot_profile_assigned)
        writer.write_int_value("devicesWithoutCloudIdentity", self.devices_without_cloud_identity)
        writer.write_int_value("intuneDevices", self.intune_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("tenantAttachDevices", self.tenant_attach_devices)
        writer.write_int_value("totalDevices", self.total_devices)
        writer.write_int_value("unsupportedOSversionDevices", self.unsupported_o_sversion_devices)
        writer.write_int_value("windows10Devices", self.windows10_devices)
        writer.write_object_value("windows10DevicesSummary", self.windows10_devices_summary)
        writer.write_int_value("windows10DevicesWithoutTenantAttach", self.windows10_devices_without_tenant_attach)
        writer.write_additional_data_value(self.additional_data)
    

