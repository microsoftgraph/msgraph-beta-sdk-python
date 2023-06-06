from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, operating_system_upgrade_eligibility, user_experience_analytics_health_state

from . import entity

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereDevice(entity.Entity):
    """
    The user experience analytics Device for work from anywhere report
    """
    # The user experience analytics work from anywhere intune device's autopilotProfileAssigned.
    auto_pilot_profile_assigned: Optional[bool] = None
    # The user experience work from anywhere intune device's autopilotRegistered.
    auto_pilot_registered: Optional[bool] = None
    # The user experience work from anywhere azure Ad device Id.
    azure_ad_device_id: Optional[str] = None
    # The user experience work from anywhere device's azure Ad joinType.
    azure_ad_join_type: Optional[str] = None
    # The user experience work from anywhere device's azureAdRegistered.
    azure_ad_registered: Optional[bool] = None
    # The user experience work from anywhere per device cloud identity score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_identity_score: Optional[float] = None
    # The user experience work from anywhere per device cloud management score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_management_score: Optional[float] = None
    # The user experience work from anywhere per device cloud provisioning score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_provisioning_score: Optional[float] = None
    # The user experience work from anywhere device's compliancePolicySetToIntune.
    compliance_policy_set_to_intune: Optional[bool] = None
    # The user experience work from anywhere device Id.
    device_id: Optional[str] = None
    # The work from anywhere device's name.
    device_name: Optional[str] = None
    # The healthStatus property
    health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
    # The user experience work from anywhere device's Cloud Management Gateway for Configuration Manager is enabled.
    is_cloud_managed_gateway_enabled: Optional[bool] = None
    # The user experience work from anywhere management agent of the device.
    managed_by: Optional[str] = None
    # The user experience work from anywhere device's manufacturer.
    manufacturer: Optional[str] = None
    # The user experience work from anywhere device's model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience work from anywhere device, Is OS check failed for device to upgrade to the latest version of windows.
    os_check_failed: Optional[bool] = None
    # The user experience work from anywhere device's OS Description.
    os_description: Optional[str] = None
    # The user experience work from anywhere device's OS Version.
    os_version: Optional[str] = None
    # The user experience work from anywhere device's otherWorkloadsSetToIntune.
    other_workloads_set_to_intune: Optional[bool] = None
    # The user experience work from anywhere device's ownership.
    ownership: Optional[str] = None
    # The user experience work from anywhere device, Is processor hardware core count check failed for device to upgrade to the latest version of windows.
    processor_core_count_check_failed: Optional[bool] = None
    # The user experience work from anywhere device, Is processor hardware family check failed for device to upgrade to the latest version of windows.
    processor_family_check_failed: Optional[bool] = None
    # The user experience work from anywhere device, Is processor hardware speed check failed for device to upgrade to the latest version of windows.
    processor_speed_check_failed: Optional[bool] = None
    # The user experience work from anywhere device, Is processor hardware 64-bit architecture check failed for device to upgrade to the latest version of windows.
    processor64_bit_check_failed: Optional[bool] = None
    # Is the user experience analytics work from anywhere device RAM hardware check failed for device to upgrade to the latest version of windows
    ram_check_failed: Optional[bool] = None
    # The user experience work from anywhere device, Is secure boot hardware check failed for device to upgrade to the latest version of windows.
    secure_boot_check_failed: Optional[bool] = None
    # The user experience work from anywhere device's serial number.
    serial_number: Optional[str] = None
    # The user experience work from anywhere device, Is storage hardware check failed for device to upgrade to the latest version of windows.
    storage_check_failed: Optional[bool] = None
    # The user experience work from anywhere device's tenantAttached.
    tenant_attached: Optional[bool] = None
    # The user experience work from anywhere device, Is Trusted Platform Module (TPM) hardware check failed for device to the latest version of upgrade to windows.
    tpm_check_failed: Optional[bool] = None
    # Work From Anywhere windows device upgrade eligibility status
    upgrade_eligibility: Optional[operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility] = None
    # The user experience work from anywhere per device windows score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    windows_score: Optional[float] = None
    # The user experience work from anywhere per device overall score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsWorkFromAnywhereDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, operating_system_upgrade_eligibility, user_experience_analytics_health_state

        fields: Dict[str, Callable[[Any], None]] = {
            "autoPilotProfileAssigned": lambda n : setattr(self, 'auto_pilot_profile_assigned', n.get_bool_value()),
            "autoPilotRegistered": lambda n : setattr(self, 'auto_pilot_registered', n.get_bool_value()),
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "azureAdJoinType": lambda n : setattr(self, 'azure_ad_join_type', n.get_str_value()),
            "azureAdRegistered": lambda n : setattr(self, 'azure_ad_registered', n.get_bool_value()),
            "cloudIdentityScore": lambda n : setattr(self, 'cloud_identity_score', n.get_float_value()),
            "cloudManagementScore": lambda n : setattr(self, 'cloud_management_score', n.get_float_value()),
            "cloudProvisioningScore": lambda n : setattr(self, 'cloud_provisioning_score', n.get_float_value()),
            "compliancePolicySetToIntune": lambda n : setattr(self, 'compliance_policy_set_to_intune', n.get_bool_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "isCloudManagedGatewayEnabled": lambda n : setattr(self, 'is_cloud_managed_gateway_enabled', n.get_bool_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "osCheckFailed": lambda n : setattr(self, 'os_check_failed', n.get_bool_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "otherWorkloadsSetToIntune": lambda n : setattr(self, 'other_workloads_set_to_intune', n.get_bool_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "processor64BitCheckFailed": lambda n : setattr(self, 'processor64_bit_check_failed', n.get_bool_value()),
            "processorCoreCountCheckFailed": lambda n : setattr(self, 'processor_core_count_check_failed', n.get_bool_value()),
            "processorFamilyCheckFailed": lambda n : setattr(self, 'processor_family_check_failed', n.get_bool_value()),
            "processorSpeedCheckFailed": lambda n : setattr(self, 'processor_speed_check_failed', n.get_bool_value()),
            "ramCheckFailed": lambda n : setattr(self, 'ram_check_failed', n.get_bool_value()),
            "secureBootCheckFailed": lambda n : setattr(self, 'secure_boot_check_failed', n.get_bool_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "storageCheckFailed": lambda n : setattr(self, 'storage_check_failed', n.get_bool_value()),
            "tenantAttached": lambda n : setattr(self, 'tenant_attached', n.get_bool_value()),
            "tpmCheckFailed": lambda n : setattr(self, 'tpm_check_failed', n.get_bool_value()),
            "upgradeEligibility": lambda n : setattr(self, 'upgrade_eligibility', n.get_enum_value(operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility)),
            "windowsScore": lambda n : setattr(self, 'windows_score', n.get_float_value()),
            "workFromAnywhereScore": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
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
        writer.write_bool_value("autoPilotProfileAssigned", self.auto_pilot_profile_assigned)
        writer.write_bool_value("autoPilotRegistered", self.auto_pilot_registered)
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_str_value("azureAdJoinType", self.azure_ad_join_type)
        writer.write_bool_value("azureAdRegistered", self.azure_ad_registered)
        writer.write_float_value("cloudIdentityScore", self.cloud_identity_score)
        writer.write_float_value("cloudManagementScore", self.cloud_management_score)
        writer.write_float_value("cloudProvisioningScore", self.cloud_provisioning_score)
        writer.write_bool_value("compliancePolicySetToIntune", self.compliance_policy_set_to_intune)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_bool_value("isCloudManagedGatewayEnabled", self.is_cloud_managed_gateway_enabled)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_bool_value("osCheckFailed", self.os_check_failed)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_bool_value("otherWorkloadsSetToIntune", self.other_workloads_set_to_intune)
        writer.write_str_value("ownership", self.ownership)
        writer.write_bool_value("processor64BitCheckFailed", self.processor64_bit_check_failed)
        writer.write_bool_value("processorCoreCountCheckFailed", self.processor_core_count_check_failed)
        writer.write_bool_value("processorFamilyCheckFailed", self.processor_family_check_failed)
        writer.write_bool_value("processorSpeedCheckFailed", self.processor_speed_check_failed)
        writer.write_bool_value("ramCheckFailed", self.ram_check_failed)
        writer.write_bool_value("secureBootCheckFailed", self.secure_boot_check_failed)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_bool_value("storageCheckFailed", self.storage_check_failed)
        writer.write_bool_value("tenantAttached", self.tenant_attached)
        writer.write_bool_value("tpmCheckFailed", self.tpm_check_failed)
        writer.write_enum_value("upgradeEligibility", self.upgrade_eligibility)
        writer.write_float_value("windowsScore", self.windows_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    

