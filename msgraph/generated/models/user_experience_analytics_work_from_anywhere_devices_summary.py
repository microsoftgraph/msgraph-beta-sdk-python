from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_experience_analytics_autopilot_devices_summary = lazy_import('msgraph.generated.models.user_experience_analytics_autopilot_devices_summary')
user_experience_analytics_cloud_identity_devices_summary = lazy_import('msgraph.generated.models.user_experience_analytics_cloud_identity_devices_summary')
user_experience_analytics_cloud_management_devices_summary = lazy_import('msgraph.generated.models.user_experience_analytics_cloud_management_devices_summary')
user_experience_analytics_windows10_devices_summary = lazy_import('msgraph.generated.models.user_experience_analytics_windows10_devices_summary')

class UserExperienceAnalyticsWorkFromAnywhereDevicesSummary(AdditionalDataHolder, Parsable):
    """
    The user experience analytics Work From Anywhere metrics devices summary.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def autopilot_devices_summary(self,) -> Optional[user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary]:
        """
        Gets the autopilotDevicesSummary property value. The value of work from anywhere autopilot devices summary.
        Returns: Optional[user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary]
        """
        return self._autopilot_devices_summary
    
    @autopilot_devices_summary.setter
    def autopilot_devices_summary(self,value: Optional[user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary] = None) -> None:
        """
        Sets the autopilotDevicesSummary property value. The value of work from anywhere autopilot devices summary.
        Args:
            value: Value to set for the autopilotDevicesSummary property.
        """
        self._autopilot_devices_summary = value
    
    @property
    def cloud_identity_devices_summary(self,) -> Optional[user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary]:
        """
        Gets the cloudIdentityDevicesSummary property value. The user experience analytics work from anywhere Cloud Identity devices summary.
        Returns: Optional[user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary]
        """
        return self._cloud_identity_devices_summary
    
    @cloud_identity_devices_summary.setter
    def cloud_identity_devices_summary(self,value: Optional[user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary] = None) -> None:
        """
        Sets the cloudIdentityDevicesSummary property value. The user experience analytics work from anywhere Cloud Identity devices summary.
        Args:
            value: Value to set for the cloudIdentityDevicesSummary property.
        """
        self._cloud_identity_devices_summary = value
    
    @property
    def cloud_management_devices_summary(self,) -> Optional[user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary]:
        """
        Gets the cloudManagementDevicesSummary property value. The user experience work from anywhere Cloud management devices summary.
        Returns: Optional[user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary]
        """
        return self._cloud_management_devices_summary
    
    @cloud_management_devices_summary.setter
    def cloud_management_devices_summary(self,value: Optional[user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary] = None) -> None:
        """
        Sets the cloudManagementDevicesSummary property value. The user experience work from anywhere Cloud management devices summary.
        Args:
            value: Value to set for the cloudManagementDevicesSummary property.
        """
        self._cloud_management_devices_summary = value
    
    @property
    def co_managed_devices(self,) -> Optional[int]:
        """
        Gets the coManagedDevices property value. Total number of co-managed devices. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._co_managed_devices
    
    @co_managed_devices.setter
    def co_managed_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the coManagedDevices property value. Total number of co-managed devices. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the coManagedDevices property.
        """
        self._co_managed_devices = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsWorkFromAnywhereDevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The value of work from anywhere autopilot devices summary.
        self._autopilot_devices_summary: Optional[user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary] = None
        # The user experience analytics work from anywhere Cloud Identity devices summary.
        self._cloud_identity_devices_summary: Optional[user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary] = None
        # The user experience work from anywhere Cloud management devices summary.
        self._cloud_management_devices_summary: Optional[user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary] = None
        # Total number of co-managed devices. Valid values -2147483648 to 2147483647
        self._co_managed_devices: Optional[int] = None
        # The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        self._devices_not_autopilot_registered: Optional[int] = None
        # The count of intune devices not autopilot profile assigned. Valid values -2147483648 to 2147483647
        self._devices_without_autopilot_profile_assigned: Optional[int] = None
        # The count of devices that are not cloud identity. Valid values -2147483648 to 2147483647
        self._devices_without_cloud_identity: Optional[int] = None
        # The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        self._intune_devices: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total count of tenant attach devices. Valid values -2147483648 to 2147483647
        self._tenant_attach_devices: Optional[int] = None
        # The total count of devices. Valid values -2147483648 to 2147483647
        self._total_devices: Optional[int] = None
        # The count of Windows 10 devices that have unsupported OS versions. Valid values -2147483648 to 2147483647
        self._unsupported_o_sversion_devices: Optional[int] = None
        # The count of windows 10 devices. Valid values -2147483648 to 2147483647
        self._windows10_devices: Optional[int] = None
        # The user experience analytics work from anywhere Windows 10 devices summary.
        self._windows10_devices_summary: Optional[user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary] = None
        # The count of windows 10 devices that are Intune and Comanaged. Valid values -2147483648 to 2147483647
        self._windows10_devices_without_tenant_attach: Optional[int] = None
    
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
    
    @property
    def devices_not_autopilot_registered(self,) -> Optional[int]:
        """
        Gets the devicesNotAutopilotRegistered property value. The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._devices_not_autopilot_registered
    
    @devices_not_autopilot_registered.setter
    def devices_not_autopilot_registered(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesNotAutopilotRegistered property value. The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the devicesNotAutopilotRegistered property.
        """
        self._devices_not_autopilot_registered = value
    
    @property
    def devices_without_autopilot_profile_assigned(self,) -> Optional[int]:
        """
        Gets the devicesWithoutAutopilotProfileAssigned property value. The count of intune devices not autopilot profile assigned. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._devices_without_autopilot_profile_assigned
    
    @devices_without_autopilot_profile_assigned.setter
    def devices_without_autopilot_profile_assigned(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesWithoutAutopilotProfileAssigned property value. The count of intune devices not autopilot profile assigned. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the devicesWithoutAutopilotProfileAssigned property.
        """
        self._devices_without_autopilot_profile_assigned = value
    
    @property
    def devices_without_cloud_identity(self,) -> Optional[int]:
        """
        Gets the devicesWithoutCloudIdentity property value. The count of devices that are not cloud identity. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._devices_without_cloud_identity
    
    @devices_without_cloud_identity.setter
    def devices_without_cloud_identity(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesWithoutCloudIdentity property value. The count of devices that are not cloud identity. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the devicesWithoutCloudIdentity property.
        """
        self._devices_without_cloud_identity = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "autopilot_devices_summary": lambda n : setattr(self, 'autopilot_devices_summary', n.get_object_value(user_experience_analytics_autopilot_devices_summary.UserExperienceAnalyticsAutopilotDevicesSummary)),
            "cloud_identity_devices_summary": lambda n : setattr(self, 'cloud_identity_devices_summary', n.get_object_value(user_experience_analytics_cloud_identity_devices_summary.UserExperienceAnalyticsCloudIdentityDevicesSummary)),
            "cloud_management_devices_summary": lambda n : setattr(self, 'cloud_management_devices_summary', n.get_object_value(user_experience_analytics_cloud_management_devices_summary.UserExperienceAnalyticsCloudManagementDevicesSummary)),
            "co_managed_devices": lambda n : setattr(self, 'co_managed_devices', n.get_int_value()),
            "devices_not_autopilot_registered": lambda n : setattr(self, 'devices_not_autopilot_registered', n.get_int_value()),
            "devices_without_autopilot_profile_assigned": lambda n : setattr(self, 'devices_without_autopilot_profile_assigned', n.get_int_value()),
            "devices_without_cloud_identity": lambda n : setattr(self, 'devices_without_cloud_identity', n.get_int_value()),
            "intune_devices": lambda n : setattr(self, 'intune_devices', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_attach_devices": lambda n : setattr(self, 'tenant_attach_devices', n.get_int_value()),
            "total_devices": lambda n : setattr(self, 'total_devices', n.get_int_value()),
            "unsupported_o_sversion_devices": lambda n : setattr(self, 'unsupported_o_sversion_devices', n.get_int_value()),
            "windows10_devices": lambda n : setattr(self, 'windows10_devices', n.get_int_value()),
            "windows10_devices_summary": lambda n : setattr(self, 'windows10_devices_summary', n.get_object_value(user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary)),
            "windows10_devices_without_tenant_attach": lambda n : setattr(self, 'windows10_devices_without_tenant_attach', n.get_int_value()),
        }
        return fields
    
    @property
    def intune_devices(self,) -> Optional[int]:
        """
        Gets the intuneDevices property value. The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._intune_devices
    
    @intune_devices.setter
    def intune_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the intuneDevices property value. The count of intune devices that are not autopilot registerd. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the intuneDevices property.
        """
        self._intune_devices = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
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
    
    @property
    def tenant_attach_devices(self,) -> Optional[int]:
        """
        Gets the tenantAttachDevices property value. Total count of tenant attach devices. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._tenant_attach_devices
    
    @tenant_attach_devices.setter
    def tenant_attach_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the tenantAttachDevices property value. Total count of tenant attach devices. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the tenantAttachDevices property.
        """
        self._tenant_attach_devices = value
    
    @property
    def total_devices(self,) -> Optional[int]:
        """
        Gets the totalDevices property value. The total count of devices. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._total_devices
    
    @total_devices.setter
    def total_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDevices property value. The total count of devices. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the totalDevices property.
        """
        self._total_devices = value
    
    @property
    def unsupported_o_sversion_devices(self,) -> Optional[int]:
        """
        Gets the unsupportedOSversionDevices property value. The count of Windows 10 devices that have unsupported OS versions. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._unsupported_o_sversion_devices
    
    @unsupported_o_sversion_devices.setter
    def unsupported_o_sversion_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the unsupportedOSversionDevices property value. The count of Windows 10 devices that have unsupported OS versions. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the unsupportedOSversionDevices property.
        """
        self._unsupported_o_sversion_devices = value
    
    @property
    def windows10_devices(self,) -> Optional[int]:
        """
        Gets the windows10Devices property value. The count of windows 10 devices. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._windows10_devices
    
    @windows10_devices.setter
    def windows10_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the windows10Devices property value. The count of windows 10 devices. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the windows10Devices property.
        """
        self._windows10_devices = value
    
    @property
    def windows10_devices_summary(self,) -> Optional[user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary]:
        """
        Gets the windows10DevicesSummary property value. The user experience analytics work from anywhere Windows 10 devices summary.
        Returns: Optional[user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary]
        """
        return self._windows10_devices_summary
    
    @windows10_devices_summary.setter
    def windows10_devices_summary(self,value: Optional[user_experience_analytics_windows10_devices_summary.UserExperienceAnalyticsWindows10DevicesSummary] = None) -> None:
        """
        Sets the windows10DevicesSummary property value. The user experience analytics work from anywhere Windows 10 devices summary.
        Args:
            value: Value to set for the windows10DevicesSummary property.
        """
        self._windows10_devices_summary = value
    
    @property
    def windows10_devices_without_tenant_attach(self,) -> Optional[int]:
        """
        Gets the windows10DevicesWithoutTenantAttach property value. The count of windows 10 devices that are Intune and Comanaged. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._windows10_devices_without_tenant_attach
    
    @windows10_devices_without_tenant_attach.setter
    def windows10_devices_without_tenant_attach(self,value: Optional[int] = None) -> None:
        """
        Sets the windows10DevicesWithoutTenantAttach property value. The count of windows 10 devices that are Intune and Comanaged. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the windows10DevicesWithoutTenantAttach property.
        """
        self._windows10_devices_without_tenant_attach = value
    

