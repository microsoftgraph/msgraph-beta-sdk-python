from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
operating_system_upgrade_eligibility = lazy_import('msgraph.generated.models.operating_system_upgrade_eligibility')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsWorkFromAnywhereDevice(entity.Entity):
    """
    The user experience analytics Device for work from anywhere report
    """
    @property
    def auto_pilot_profile_assigned(self,) -> Optional[bool]:
        """
        Gets the autoPilotProfileAssigned property value. The user experience analytics work from anywhere intune device's autopilotProfileAssigned.
        Returns: Optional[bool]
        """
        return self._auto_pilot_profile_assigned
    
    @auto_pilot_profile_assigned.setter
    def auto_pilot_profile_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoPilotProfileAssigned property value. The user experience analytics work from anywhere intune device's autopilotProfileAssigned.
        Args:
            value: Value to set for the autoPilotProfileAssigned property.
        """
        self._auto_pilot_profile_assigned = value
    
    @property
    def auto_pilot_registered(self,) -> Optional[bool]:
        """
        Gets the autoPilotRegistered property value. The user experience work from anywhere intune device's autopilotRegistered.
        Returns: Optional[bool]
        """
        return self._auto_pilot_registered
    
    @auto_pilot_registered.setter
    def auto_pilot_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoPilotRegistered property value. The user experience work from anywhere intune device's autopilotRegistered.
        Args:
            value: Value to set for the autoPilotRegistered property.
        """
        self._auto_pilot_registered = value
    
    @property
    def azure_ad_device_id(self,) -> Optional[str]:
        """
        Gets the azureAdDeviceId property value. The user experience work from anywhere azure Ad device Id.
        Returns: Optional[str]
        """
        return self._azure_ad_device_id
    
    @azure_ad_device_id.setter
    def azure_ad_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdDeviceId property value. The user experience work from anywhere azure Ad device Id.
        Args:
            value: Value to set for the azureAdDeviceId property.
        """
        self._azure_ad_device_id = value
    
    @property
    def azure_ad_join_type(self,) -> Optional[str]:
        """
        Gets the azureAdJoinType property value. The user experience work from anywhere device's azure Ad joinType.
        Returns: Optional[str]
        """
        return self._azure_ad_join_type
    
    @azure_ad_join_type.setter
    def azure_ad_join_type(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdJoinType property value. The user experience work from anywhere device's azure Ad joinType.
        Args:
            value: Value to set for the azureAdJoinType property.
        """
        self._azure_ad_join_type = value
    
    @property
    def azure_ad_registered(self,) -> Optional[bool]:
        """
        Gets the azureAdRegistered property value. The user experience work from anywhere device's azureAdRegistered.
        Returns: Optional[bool]
        """
        return self._azure_ad_registered
    
    @azure_ad_registered.setter
    def azure_ad_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureAdRegistered property value. The user experience work from anywhere device's azureAdRegistered.
        Args:
            value: Value to set for the azureAdRegistered property.
        """
        self._azure_ad_registered = value
    
    @property
    def cloud_identity_score(self,) -> Optional[float]:
        """
        Gets the cloudIdentityScore property value. The user experience work from anywhere per device cloud identity score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_identity_score
    
    @cloud_identity_score.setter
    def cloud_identity_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudIdentityScore property value. The user experience work from anywhere per device cloud identity score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudIdentityScore property.
        """
        self._cloud_identity_score = value
    
    @property
    def cloud_management_score(self,) -> Optional[float]:
        """
        Gets the cloudManagementScore property value. The user experience work from anywhere per device cloud management score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_management_score
    
    @cloud_management_score.setter
    def cloud_management_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudManagementScore property value. The user experience work from anywhere per device cloud management score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudManagementScore property.
        """
        self._cloud_management_score = value
    
    @property
    def cloud_provisioning_score(self,) -> Optional[float]:
        """
        Gets the cloudProvisioningScore property value. The user experience work from anywhere per device cloud provisioning score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_provisioning_score
    
    @cloud_provisioning_score.setter
    def cloud_provisioning_score(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudProvisioningScore property value. The user experience work from anywhere per device cloud provisioning score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloudProvisioningScore property.
        """
        self._cloud_provisioning_score = value
    
    @property
    def compliance_policy_set_to_intune(self,) -> Optional[bool]:
        """
        Gets the compliancePolicySetToIntune property value. The user experience work from anywhere device's compliancePolicySetToIntune.
        Returns: Optional[bool]
        """
        return self._compliance_policy_set_to_intune
    
    @compliance_policy_set_to_intune.setter
    def compliance_policy_set_to_intune(self,value: Optional[bool] = None) -> None:
        """
        Sets the compliancePolicySetToIntune property value. The user experience work from anywhere device's compliancePolicySetToIntune.
        Args:
            value: Value to set for the compliancePolicySetToIntune property.
        """
        self._compliance_policy_set_to_intune = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsWorkFromAnywhereDevice and sets the default values.
        """
        super().__init__()
        # The user experience analytics work from anywhere intune device's autopilotProfileAssigned.
        self._auto_pilot_profile_assigned: Optional[bool] = None
        # The user experience work from anywhere intune device's autopilotRegistered.
        self._auto_pilot_registered: Optional[bool] = None
        # The user experience work from anywhere azure Ad device Id.
        self._azure_ad_device_id: Optional[str] = None
        # The user experience work from anywhere device's azure Ad joinType.
        self._azure_ad_join_type: Optional[str] = None
        # The user experience work from anywhere device's azureAdRegistered.
        self._azure_ad_registered: Optional[bool] = None
        # The user experience work from anywhere per device cloud identity score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_identity_score: Optional[float] = None
        # The user experience work from anywhere per device cloud management score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_management_score: Optional[float] = None
        # The user experience work from anywhere per device cloud provisioning score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._cloud_provisioning_score: Optional[float] = None
        # The user experience work from anywhere device's compliancePolicySetToIntune.
        self._compliance_policy_set_to_intune: Optional[bool] = None
        # The user experience work from anywhere device Id.
        self._device_id: Optional[str] = None
        # The work from anywhere device's name.
        self._device_name: Optional[str] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The user experience work from anywhere device's Cloud Management Gateway for Configuration Manager is enabled.
        self._is_cloud_managed_gateway_enabled: Optional[bool] = None
        # The user experience work from anywhere management agent of the device.
        self._managed_by: Optional[str] = None
        # The user experience work from anywhere device's manufacturer.
        self._manufacturer: Optional[str] = None
        # The user experience work from anywhere device's model.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience work from anywhere device, Is OS check failed for device to upgrade to the latest version of windows.
        self._os_check_failed: Optional[bool] = None
        # The user experience work from anywhere device's OS Description.
        self._os_description: Optional[str] = None
        # The user experience work from anywhere device's OS Version.
        self._os_version: Optional[str] = None
        # The user experience work from anywhere device's otherWorkloadsSetToIntune.
        self._other_workloads_set_to_intune: Optional[bool] = None
        # The user experience work from anywhere device's ownership.
        self._ownership: Optional[str] = None
        # The user experience work from anywhere device, Is processor hardware 64-bit architecture check failed for device to upgrade to the latest version of windows.
        self._processor64_bit_check_failed: Optional[bool] = None
        # The user experience work from anywhere device, Is processor hardware core count check failed for device to upgrade to the latest version of windows.
        self._processor_core_count_check_failed: Optional[bool] = None
        # The user experience work from anywhere device, Is processor hardware family check failed for device to upgrade to the latest version of windows.
        self._processor_family_check_failed: Optional[bool] = None
        # The user experience work from anywhere device, Is processor hardware speed check failed for device to upgrade to the latest version of windows.
        self._processor_speed_check_failed: Optional[bool] = None
        # Is the user experience analytics work from anywhere device RAM hardware check failed for device to upgrade to the latest version of windows
        self._ram_check_failed: Optional[bool] = None
        # The user experience work from anywhere device, Is secure boot hardware check failed for device to upgrade to the latest version of windows.
        self._secure_boot_check_failed: Optional[bool] = None
        # The user experience work from anywhere device's serial number.
        self._serial_number: Optional[str] = None
        # The user experience work from anywhere device, Is storage hardware check failed for device to upgrade to the latest version of windows.
        self._storage_check_failed: Optional[bool] = None
        # The user experience work from anywhere device's tenantAttached.
        self._tenant_attached: Optional[bool] = None
        # The user experience work from anywhere device, Is Trusted Platform Module (TPM) hardware check failed for device to the latest version of upgrade to windows.
        self._tpm_check_failed: Optional[bool] = None
        # Work From Anywhere windows device upgrade eligibility status
        self._upgrade_eligibility: Optional[operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility] = None
        # The user experience work from anywhere per device windows score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._windows_score: Optional[float] = None
        # The user experience work from anywhere per device overall score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._work_from_anywhere_score: Optional[float] = None
    
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
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The user experience work from anywhere device Id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The user experience work from anywhere device Id.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The work from anywhere device's name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The work from anywhere device's name.
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
            "auto_pilot_profile_assigned": lambda n : setattr(self, 'auto_pilot_profile_assigned', n.get_bool_value()),
            "auto_pilot_registered": lambda n : setattr(self, 'auto_pilot_registered', n.get_bool_value()),
            "azure_ad_device_id": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "azure_ad_join_type": lambda n : setattr(self, 'azure_ad_join_type', n.get_str_value()),
            "azure_ad_registered": lambda n : setattr(self, 'azure_ad_registered', n.get_bool_value()),
            "cloud_identity_score": lambda n : setattr(self, 'cloud_identity_score', n.get_float_value()),
            "cloud_management_score": lambda n : setattr(self, 'cloud_management_score', n.get_float_value()),
            "cloud_provisioning_score": lambda n : setattr(self, 'cloud_provisioning_score', n.get_float_value()),
            "compliance_policy_set_to_intune": lambda n : setattr(self, 'compliance_policy_set_to_intune', n.get_bool_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "is_cloud_managed_gateway_enabled": lambda n : setattr(self, 'is_cloud_managed_gateway_enabled', n.get_bool_value()),
            "managed_by": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "os_check_failed": lambda n : setattr(self, 'os_check_failed', n.get_bool_value()),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "other_workloads_set_to_intune": lambda n : setattr(self, 'other_workloads_set_to_intune', n.get_bool_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "processor64_bit_check_failed": lambda n : setattr(self, 'processor64_bit_check_failed', n.get_bool_value()),
            "processor_core_count_check_failed": lambda n : setattr(self, 'processor_core_count_check_failed', n.get_bool_value()),
            "processor_family_check_failed": lambda n : setattr(self, 'processor_family_check_failed', n.get_bool_value()),
            "processor_speed_check_failed": lambda n : setattr(self, 'processor_speed_check_failed', n.get_bool_value()),
            "ram_check_failed": lambda n : setattr(self, 'ram_check_failed', n.get_bool_value()),
            "secure_boot_check_failed": lambda n : setattr(self, 'secure_boot_check_failed', n.get_bool_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "storage_check_failed": lambda n : setattr(self, 'storage_check_failed', n.get_bool_value()),
            "tenant_attached": lambda n : setattr(self, 'tenant_attached', n.get_bool_value()),
            "tpm_check_failed": lambda n : setattr(self, 'tpm_check_failed', n.get_bool_value()),
            "upgrade_eligibility": lambda n : setattr(self, 'upgrade_eligibility', n.get_enum_value(operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility)),
            "windows_score": lambda n : setattr(self, 'windows_score', n.get_float_value()),
            "work_from_anywhere_score": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_status(self,) -> Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]:
        """
        Gets the healthStatus property value. The healthStatus property
        Returns: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None) -> None:
        """
        Sets the healthStatus property value. The healthStatus property
        Args:
            value: Value to set for the healthStatus property.
        """
        self._health_status = value
    
    @property
    def is_cloud_managed_gateway_enabled(self,) -> Optional[bool]:
        """
        Gets the isCloudManagedGatewayEnabled property value. The user experience work from anywhere device's Cloud Management Gateway for Configuration Manager is enabled.
        Returns: Optional[bool]
        """
        return self._is_cloud_managed_gateway_enabled
    
    @is_cloud_managed_gateway_enabled.setter
    def is_cloud_managed_gateway_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCloudManagedGatewayEnabled property value. The user experience work from anywhere device's Cloud Management Gateway for Configuration Manager is enabled.
        Args:
            value: Value to set for the isCloudManagedGatewayEnabled property.
        """
        self._is_cloud_managed_gateway_enabled = value
    
    @property
    def managed_by(self,) -> Optional[str]:
        """
        Gets the managedBy property value. The user experience work from anywhere management agent of the device.
        Returns: Optional[str]
        """
        return self._managed_by
    
    @managed_by.setter
    def managed_by(self,value: Optional[str] = None) -> None:
        """
        Sets the managedBy property value. The user experience work from anywhere management agent of the device.
        Args:
            value: Value to set for the managedBy property.
        """
        self._managed_by = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The user experience work from anywhere device's manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience work from anywhere device's manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience work from anywhere device's model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience work from anywhere device's model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def os_check_failed(self,) -> Optional[bool]:
        """
        Gets the osCheckFailed property value. The user experience work from anywhere device, Is OS check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._os_check_failed
    
    @os_check_failed.setter
    def os_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the osCheckFailed property value. The user experience work from anywhere device, Is OS check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the osCheckFailed property.
        """
        self._os_check_failed = value
    
    @property
    def os_description(self,) -> Optional[str]:
        """
        Gets the osDescription property value. The user experience work from anywhere device's OS Description.
        Returns: Optional[str]
        """
        return self._os_description
    
    @os_description.setter
    def os_description(self,value: Optional[str] = None) -> None:
        """
        Sets the osDescription property value. The user experience work from anywhere device's OS Description.
        Args:
            value: Value to set for the osDescription property.
        """
        self._os_description = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The user experience work from anywhere device's OS Version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The user experience work from anywhere device's OS Version.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def other_workloads_set_to_intune(self,) -> Optional[bool]:
        """
        Gets the otherWorkloadsSetToIntune property value. The user experience work from anywhere device's otherWorkloadsSetToIntune.
        Returns: Optional[bool]
        """
        return self._other_workloads_set_to_intune
    
    @other_workloads_set_to_intune.setter
    def other_workloads_set_to_intune(self,value: Optional[bool] = None) -> None:
        """
        Sets the otherWorkloadsSetToIntune property value. The user experience work from anywhere device's otherWorkloadsSetToIntune.
        Args:
            value: Value to set for the otherWorkloadsSetToIntune property.
        """
        self._other_workloads_set_to_intune = value
    
    @property
    def ownership(self,) -> Optional[str]:
        """
        Gets the ownership property value. The user experience work from anywhere device's ownership.
        Returns: Optional[str]
        """
        return self._ownership
    
    @ownership.setter
    def ownership(self,value: Optional[str] = None) -> None:
        """
        Sets the ownership property value. The user experience work from anywhere device's ownership.
        Args:
            value: Value to set for the ownership property.
        """
        self._ownership = value
    
    @property
    def processor64_bit_check_failed(self,) -> Optional[bool]:
        """
        Gets the processor64BitCheckFailed property value. The user experience work from anywhere device, Is processor hardware 64-bit architecture check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._processor64_bit_check_failed
    
    @processor64_bit_check_failed.setter
    def processor64_bit_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the processor64BitCheckFailed property value. The user experience work from anywhere device, Is processor hardware 64-bit architecture check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the processor64BitCheckFailed property.
        """
        self._processor64_bit_check_failed = value
    
    @property
    def processor_core_count_check_failed(self,) -> Optional[bool]:
        """
        Gets the processorCoreCountCheckFailed property value. The user experience work from anywhere device, Is processor hardware core count check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._processor_core_count_check_failed
    
    @processor_core_count_check_failed.setter
    def processor_core_count_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the processorCoreCountCheckFailed property value. The user experience work from anywhere device, Is processor hardware core count check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the processorCoreCountCheckFailed property.
        """
        self._processor_core_count_check_failed = value
    
    @property
    def processor_family_check_failed(self,) -> Optional[bool]:
        """
        Gets the processorFamilyCheckFailed property value. The user experience work from anywhere device, Is processor hardware family check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._processor_family_check_failed
    
    @processor_family_check_failed.setter
    def processor_family_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the processorFamilyCheckFailed property value. The user experience work from anywhere device, Is processor hardware family check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the processorFamilyCheckFailed property.
        """
        self._processor_family_check_failed = value
    
    @property
    def processor_speed_check_failed(self,) -> Optional[bool]:
        """
        Gets the processorSpeedCheckFailed property value. The user experience work from anywhere device, Is processor hardware speed check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._processor_speed_check_failed
    
    @processor_speed_check_failed.setter
    def processor_speed_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the processorSpeedCheckFailed property value. The user experience work from anywhere device, Is processor hardware speed check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the processorSpeedCheckFailed property.
        """
        self._processor_speed_check_failed = value
    
    @property
    def ram_check_failed(self,) -> Optional[bool]:
        """
        Gets the ramCheckFailed property value. Is the user experience analytics work from anywhere device RAM hardware check failed for device to upgrade to the latest version of windows
        Returns: Optional[bool]
        """
        return self._ram_check_failed
    
    @ram_check_failed.setter
    def ram_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the ramCheckFailed property value. Is the user experience analytics work from anywhere device RAM hardware check failed for device to upgrade to the latest version of windows
        Args:
            value: Value to set for the ramCheckFailed property.
        """
        self._ram_check_failed = value
    
    @property
    def secure_boot_check_failed(self,) -> Optional[bool]:
        """
        Gets the secureBootCheckFailed property value. The user experience work from anywhere device, Is secure boot hardware check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._secure_boot_check_failed
    
    @secure_boot_check_failed.setter
    def secure_boot_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureBootCheckFailed property value. The user experience work from anywhere device, Is secure boot hardware check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the secureBootCheckFailed property.
        """
        self._secure_boot_check_failed = value
    
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
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. The user experience work from anywhere device's serial number.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. The user experience work from anywhere device's serial number.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def storage_check_failed(self,) -> Optional[bool]:
        """
        Gets the storageCheckFailed property value. The user experience work from anywhere device, Is storage hardware check failed for device to upgrade to the latest version of windows.
        Returns: Optional[bool]
        """
        return self._storage_check_failed
    
    @storage_check_failed.setter
    def storage_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageCheckFailed property value. The user experience work from anywhere device, Is storage hardware check failed for device to upgrade to the latest version of windows.
        Args:
            value: Value to set for the storageCheckFailed property.
        """
        self._storage_check_failed = value
    
    @property
    def tenant_attached(self,) -> Optional[bool]:
        """
        Gets the tenantAttached property value. The user experience work from anywhere device's tenantAttached.
        Returns: Optional[bool]
        """
        return self._tenant_attached
    
    @tenant_attached.setter
    def tenant_attached(self,value: Optional[bool] = None) -> None:
        """
        Sets the tenantAttached property value. The user experience work from anywhere device's tenantAttached.
        Args:
            value: Value to set for the tenantAttached property.
        """
        self._tenant_attached = value
    
    @property
    def tpm_check_failed(self,) -> Optional[bool]:
        """
        Gets the tpmCheckFailed property value. The user experience work from anywhere device, Is Trusted Platform Module (TPM) hardware check failed for device to the latest version of upgrade to windows.
        Returns: Optional[bool]
        """
        return self._tpm_check_failed
    
    @tpm_check_failed.setter
    def tpm_check_failed(self,value: Optional[bool] = None) -> None:
        """
        Sets the tpmCheckFailed property value. The user experience work from anywhere device, Is Trusted Platform Module (TPM) hardware check failed for device to the latest version of upgrade to windows.
        Args:
            value: Value to set for the tpmCheckFailed property.
        """
        self._tpm_check_failed = value
    
    @property
    def upgrade_eligibility(self,) -> Optional[operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility]:
        """
        Gets the upgradeEligibility property value. Work From Anywhere windows device upgrade eligibility status
        Returns: Optional[operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility]
        """
        return self._upgrade_eligibility
    
    @upgrade_eligibility.setter
    def upgrade_eligibility(self,value: Optional[operating_system_upgrade_eligibility.OperatingSystemUpgradeEligibility] = None) -> None:
        """
        Sets the upgradeEligibility property value. Work From Anywhere windows device upgrade eligibility status
        Args:
            value: Value to set for the upgradeEligibility property.
        """
        self._upgrade_eligibility = value
    
    @property
    def windows_score(self,) -> Optional[float]:
        """
        Gets the windowsScore property value. The user experience work from anywhere per device windows score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._windows_score
    
    @windows_score.setter
    def windows_score(self,value: Optional[float] = None) -> None:
        """
        Sets the windowsScore property value. The user experience work from anywhere per device windows score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the windowsScore property.
        """
        self._windows_score = value
    
    @property
    def work_from_anywhere_score(self,) -> Optional[float]:
        """
        Gets the workFromAnywhereScore property value. The user experience work from anywhere per device overall score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._work_from_anywhere_score
    
    @work_from_anywhere_score.setter
    def work_from_anywhere_score(self,value: Optional[float] = None) -> None:
        """
        Sets the workFromAnywhereScore property value. The user experience work from anywhere per device overall score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the workFromAnywhereScore property.
        """
        self._work_from_anywhere_score = value
    

