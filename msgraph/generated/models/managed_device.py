from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_evaluation_status_details = lazy_import('msgraph.generated.models.assignment_filter_evaluation_status_details')
chassis_type = lazy_import('msgraph.generated.models.chassis_type')
chrome_o_s_device_property = lazy_import('msgraph.generated.models.chrome_o_s_device_property')
cloud_pc_remote_action_result = lazy_import('msgraph.generated.models.cloud_pc_remote_action_result')
compliance_state = lazy_import('msgraph.generated.models.compliance_state')
configuration_manager_client_enabled_features = lazy_import('msgraph.generated.models.configuration_manager_client_enabled_features')
configuration_manager_client_health_state = lazy_import('msgraph.generated.models.configuration_manager_client_health_state')
configuration_manager_client_information = lazy_import('msgraph.generated.models.configuration_manager_client_information')
detected_app = lazy_import('msgraph.generated.models.detected_app')
device_action_result = lazy_import('msgraph.generated.models.device_action_result')
device_category = lazy_import('msgraph.generated.models.device_category')
device_compliance_policy_state = lazy_import('msgraph.generated.models.device_compliance_policy_state')
device_configuration_state = lazy_import('msgraph.generated.models.device_configuration_state')
device_enrollment_type = lazy_import('msgraph.generated.models.device_enrollment_type')
device_health_attestation_state = lazy_import('msgraph.generated.models.device_health_attestation_state')
device_log_collection_response = lazy_import('msgraph.generated.models.device_log_collection_response')
device_management_exchange_access_state = lazy_import('msgraph.generated.models.device_management_exchange_access_state')
device_management_exchange_access_state_reason = lazy_import('msgraph.generated.models.device_management_exchange_access_state_reason')
device_registration_state = lazy_import('msgraph.generated.models.device_registration_state')
device_type = lazy_import('msgraph.generated.models.device_type')
entity = lazy_import('msgraph.generated.models.entity')
hardware_information = lazy_import('msgraph.generated.models.hardware_information')
join_type = lazy_import('msgraph.generated.models.join_type')
logged_on_user = lazy_import('msgraph.generated.models.logged_on_user')
lost_mode_state = lazy_import('msgraph.generated.models.lost_mode_state')
managed_device_architecture = lazy_import('msgraph.generated.models.managed_device_architecture')
managed_device_management_features = lazy_import('msgraph.generated.models.managed_device_management_features')
managed_device_mobile_app_configuration_state = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_state')
managed_device_owner_type = lazy_import('msgraph.generated.models.managed_device_owner_type')
managed_device_partner_reported_health_state = lazy_import('msgraph.generated.models.managed_device_partner_reported_health_state')
management_agent_type = lazy_import('msgraph.generated.models.management_agent_type')
management_state = lazy_import('msgraph.generated.models.management_state')
owner_type = lazy_import('msgraph.generated.models.owner_type')
security_baseline_state = lazy_import('msgraph.generated.models.security_baseline_state')
user = lazy_import('msgraph.generated.models.user')
windows_protection_state = lazy_import('msgraph.generated.models.windows_protection_state')

class ManagedDevice(entity.Entity):
    """
    Devices that are managed or pre-enrolled through Intune
    """
    @property
    def aad_registered(self,) -> Optional[bool]:
        """
        Gets the aadRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Returns: Optional[bool]
        """
        return self._aad_registered
    
    @aad_registered.setter
    def aad_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the aadRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Args:
            value: Value to set for the aadRegistered property.
        """
        self._aad_registered = value
    
    @property
    def activation_lock_bypass_code(self,) -> Optional[str]:
        """
        Gets the activationLockBypassCode property value. Code that allows the Activation Lock on a device to be bypassed. This property is read-only.
        Returns: Optional[str]
        """
        return self._activation_lock_bypass_code
    
    @activation_lock_bypass_code.setter
    def activation_lock_bypass_code(self,value: Optional[str] = None) -> None:
        """
        Sets the activationLockBypassCode property value. Code that allows the Activation Lock on a device to be bypassed. This property is read-only.
        Args:
            value: Value to set for the activationLockBypassCode property.
        """
        self._activation_lock_bypass_code = value
    
    @property
    def android_security_patch_level(self,) -> Optional[str]:
        """
        Gets the androidSecurityPatchLevel property value. Android security patch level. This property is read-only.
        Returns: Optional[str]
        """
        return self._android_security_patch_level
    
    @android_security_patch_level.setter
    def android_security_patch_level(self,value: Optional[str] = None) -> None:
        """
        Sets the androidSecurityPatchLevel property value. Android security patch level. This property is read-only.
        Args:
            value: Value to set for the androidSecurityPatchLevel property.
        """
        self._android_security_patch_level = value
    
    @property
    def assignment_filter_evaluation_status_details(self,) -> Optional[List[assignment_filter_evaluation_status_details.AssignmentFilterEvaluationStatusDetails]]:
        """
        Gets the assignmentFilterEvaluationStatusDetails property value. Managed device mobile app configuration states for this device.
        Returns: Optional[List[assignment_filter_evaluation_status_details.AssignmentFilterEvaluationStatusDetails]]
        """
        return self._assignment_filter_evaluation_status_details
    
    @assignment_filter_evaluation_status_details.setter
    def assignment_filter_evaluation_status_details(self,value: Optional[List[assignment_filter_evaluation_status_details.AssignmentFilterEvaluationStatusDetails]] = None) -> None:
        """
        Sets the assignmentFilterEvaluationStatusDetails property value. Managed device mobile app configuration states for this device.
        Args:
            value: Value to set for the assignmentFilterEvaluationStatusDetails property.
        """
        self._assignment_filter_evaluation_status_details = value
    
    @property
    def autopilot_enrolled(self,) -> Optional[bool]:
        """
        Gets the autopilotEnrolled property value. Reports if the managed device is enrolled via auto-pilot. This property is read-only.
        Returns: Optional[bool]
        """
        return self._autopilot_enrolled
    
    @autopilot_enrolled.setter
    def autopilot_enrolled(self,value: Optional[bool] = None) -> None:
        """
        Sets the autopilotEnrolled property value. Reports if the managed device is enrolled via auto-pilot. This property is read-only.
        Args:
            value: Value to set for the autopilotEnrolled property.
        """
        self._autopilot_enrolled = value
    
    @property
    def azure_active_directory_device_id(self,) -> Optional[str]:
        """
        Gets the azureActiveDirectoryDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Returns: Optional[str]
        """
        return self._azure_active_directory_device_id
    
    @azure_active_directory_device_id.setter
    def azure_active_directory_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureActiveDirectoryDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Args:
            value: Value to set for the azureActiveDirectoryDeviceId property.
        """
        self._azure_active_directory_device_id = value
    
    @property
    def azure_a_d_device_id(self,) -> Optional[str]:
        """
        Gets the azureADDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Returns: Optional[str]
        """
        return self._azure_a_d_device_id
    
    @azure_a_d_device_id.setter
    def azure_a_d_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureADDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Args:
            value: Value to set for the azureADDeviceId property.
        """
        self._azure_a_d_device_id = value
    
    @property
    def azure_a_d_registered(self,) -> Optional[bool]:
        """
        Gets the azureADRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Returns: Optional[bool]
        """
        return self._azure_a_d_registered
    
    @azure_a_d_registered.setter
    def azure_a_d_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureADRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Args:
            value: Value to set for the azureADRegistered property.
        """
        self._azure_a_d_registered = value
    
    @property
    def bootstrap_token_escrowed(self,) -> Optional[bool]:
        """
        Gets the bootstrapTokenEscrowed property value. Reports if the managed device has an escrowed Bootstrap Token. This is only for macOS devices. To get, include BootstrapTokenEscrowed in the select clause and query with a device id. If FALSE, no bootstrap token is escrowed. If TRUE, the device has escrowed a bootstrap token with Intune. This property is read-only.
        Returns: Optional[bool]
        """
        return self._bootstrap_token_escrowed
    
    @bootstrap_token_escrowed.setter
    def bootstrap_token_escrowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the bootstrapTokenEscrowed property value. Reports if the managed device has an escrowed Bootstrap Token. This is only for macOS devices. To get, include BootstrapTokenEscrowed in the select clause and query with a device id. If FALSE, no bootstrap token is escrowed. If TRUE, the device has escrowed a bootstrap token with Intune. This property is read-only.
        Args:
            value: Value to set for the bootstrapTokenEscrowed property.
        """
        self._bootstrap_token_escrowed = value
    
    @property
    def chassis_type(self,) -> Optional[chassis_type.ChassisType]:
        """
        Gets the chassisType property value. Chassis type.
        Returns: Optional[chassis_type.ChassisType]
        """
        return self._chassis_type
    
    @chassis_type.setter
    def chassis_type(self,value: Optional[chassis_type.ChassisType] = None) -> None:
        """
        Sets the chassisType property value. Chassis type.
        Args:
            value: Value to set for the chassisType property.
        """
        self._chassis_type = value
    
    @property
    def chrome_o_s_device_info(self,) -> Optional[List[chrome_o_s_device_property.ChromeOSDeviceProperty]]:
        """
        Gets the chromeOSDeviceInfo property value. List of properties of the ChromeOS Device.
        Returns: Optional[List[chrome_o_s_device_property.ChromeOSDeviceProperty]]
        """
        return self._chrome_o_s_device_info
    
    @chrome_o_s_device_info.setter
    def chrome_o_s_device_info(self,value: Optional[List[chrome_o_s_device_property.ChromeOSDeviceProperty]] = None) -> None:
        """
        Sets the chromeOSDeviceInfo property value. List of properties of the ChromeOS Device.
        Args:
            value: Value to set for the chromeOSDeviceInfo property.
        """
        self._chrome_o_s_device_info = value
    
    @property
    def cloud_pc_remote_action_results(self,) -> Optional[List[cloud_pc_remote_action_result.CloudPcRemoteActionResult]]:
        """
        Gets the cloudPcRemoteActionResults property value. The cloudPcRemoteActionResults property
        Returns: Optional[List[cloud_pc_remote_action_result.CloudPcRemoteActionResult]]
        """
        return self._cloud_pc_remote_action_results
    
    @cloud_pc_remote_action_results.setter
    def cloud_pc_remote_action_results(self,value: Optional[List[cloud_pc_remote_action_result.CloudPcRemoteActionResult]] = None) -> None:
        """
        Sets the cloudPcRemoteActionResults property value. The cloudPcRemoteActionResults property
        Args:
            value: Value to set for the cloudPcRemoteActionResults property.
        """
        self._cloud_pc_remote_action_results = value
    
    @property
    def compliance_grace_period_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._compliance_grace_period_expiration_date_time
    
    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires. This property is read-only.
        Args:
            value: Value to set for the complianceGracePeriodExpirationDateTime property.
        """
        self._compliance_grace_period_expiration_date_time = value
    
    @property
    def compliance_state(self,) -> Optional[compliance_state.ComplianceState]:
        """
        Gets the complianceState property value. Compliance state.
        Returns: Optional[compliance_state.ComplianceState]
        """
        return self._compliance_state
    
    @compliance_state.setter
    def compliance_state(self,value: Optional[compliance_state.ComplianceState] = None) -> None:
        """
        Sets the complianceState property value. Compliance state.
        Args:
            value: Value to set for the complianceState property.
        """
        self._compliance_state = value
    
    @property
    def configuration_manager_client_enabled_features(self,) -> Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures]:
        """
        Gets the configurationManagerClientEnabledFeatures property value. ConfigrMgr client enabled features. This property is read-only.
        Returns: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures]
        """
        return self._configuration_manager_client_enabled_features
    
    @configuration_manager_client_enabled_features.setter
    def configuration_manager_client_enabled_features(self,value: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures] = None) -> None:
        """
        Sets the configurationManagerClientEnabledFeatures property value. ConfigrMgr client enabled features. This property is read-only.
        Args:
            value: Value to set for the configurationManagerClientEnabledFeatures property.
        """
        self._configuration_manager_client_enabled_features = value
    
    @property
    def configuration_manager_client_health_state(self,) -> Optional[configuration_manager_client_health_state.ConfigurationManagerClientHealthState]:
        """
        Gets the configurationManagerClientHealthState property value. Configuration manager client health state, valid only for devices managed by MDM/ConfigMgr Agent
        Returns: Optional[configuration_manager_client_health_state.ConfigurationManagerClientHealthState]
        """
        return self._configuration_manager_client_health_state
    
    @configuration_manager_client_health_state.setter
    def configuration_manager_client_health_state(self,value: Optional[configuration_manager_client_health_state.ConfigurationManagerClientHealthState] = None) -> None:
        """
        Sets the configurationManagerClientHealthState property value. Configuration manager client health state, valid only for devices managed by MDM/ConfigMgr Agent
        Args:
            value: Value to set for the configurationManagerClientHealthState property.
        """
        self._configuration_manager_client_health_state = value
    
    @property
    def configuration_manager_client_information(self,) -> Optional[configuration_manager_client_information.ConfigurationManagerClientInformation]:
        """
        Gets the configurationManagerClientInformation property value. Configuration manager client information, valid only for devices managed, duel-managed or tri-managed by ConfigMgr Agent
        Returns: Optional[configuration_manager_client_information.ConfigurationManagerClientInformation]
        """
        return self._configuration_manager_client_information
    
    @configuration_manager_client_information.setter
    def configuration_manager_client_information(self,value: Optional[configuration_manager_client_information.ConfigurationManagerClientInformation] = None) -> None:
        """
        Sets the configurationManagerClientInformation property value. Configuration manager client information, valid only for devices managed, duel-managed or tri-managed by ConfigMgr Agent
        Args:
            value: Value to set for the configurationManagerClientInformation property.
        """
        self._configuration_manager_client_information = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedDevice and sets the default values.
        """
        super().__init__()
        # Whether the device is Azure Active Directory registered. This property is read-only.
        self._aad_registered: Optional[bool] = None
        # Code that allows the Activation Lock on a device to be bypassed. This property is read-only.
        self._activation_lock_bypass_code: Optional[str] = None
        # Android security patch level. This property is read-only.
        self._android_security_patch_level: Optional[str] = None
        # Managed device mobile app configuration states for this device.
        self._assignment_filter_evaluation_status_details: Optional[List[assignment_filter_evaluation_status_details.AssignmentFilterEvaluationStatusDetails]] = None
        # Reports if the managed device is enrolled via auto-pilot. This property is read-only.
        self._autopilot_enrolled: Optional[bool] = None
        # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        self._azure_active_directory_device_id: Optional[str] = None
        # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        self._azure_a_d_device_id: Optional[str] = None
        # Whether the device is Azure Active Directory registered. This property is read-only.
        self._azure_a_d_registered: Optional[bool] = None
        # Reports if the managed device has an escrowed Bootstrap Token. This is only for macOS devices. To get, include BootstrapTokenEscrowed in the select clause and query with a device id. If FALSE, no bootstrap token is escrowed. If TRUE, the device has escrowed a bootstrap token with Intune. This property is read-only.
        self._bootstrap_token_escrowed: Optional[bool] = None
        # Chassis type.
        self._chassis_type: Optional[chassis_type.ChassisType] = None
        # List of properties of the ChromeOS Device.
        self._chrome_o_s_device_info: Optional[List[chrome_o_s_device_property.ChromeOSDeviceProperty]] = None
        # The cloudPcRemoteActionResults property
        self._cloud_pc_remote_action_results: Optional[List[cloud_pc_remote_action_result.CloudPcRemoteActionResult]] = None
        # The DateTime when device compliance grace period expires. This property is read-only.
        self._compliance_grace_period_expiration_date_time: Optional[datetime] = None
        # Compliance state.
        self._compliance_state: Optional[compliance_state.ComplianceState] = None
        # ConfigrMgr client enabled features. This property is read-only.
        self._configuration_manager_client_enabled_features: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures] = None
        # Configuration manager client health state, valid only for devices managed by MDM/ConfigMgr Agent
        self._configuration_manager_client_health_state: Optional[configuration_manager_client_health_state.ConfigurationManagerClientHealthState] = None
        # Configuration manager client information, valid only for devices managed, duel-managed or tri-managed by ConfigMgr Agent
        self._configuration_manager_client_information: Optional[configuration_manager_client_information.ConfigurationManagerClientInformation] = None
        # All applications currently installed on the device
        self._detected_apps: Optional[List[detected_app.DetectedApp]] = None
        # List of ComplexType deviceActionResult objects. This property is read-only.
        self._device_action_results: Optional[List[device_action_result.DeviceActionResult]] = None
        # Device category
        self._device_category: Optional[device_category.DeviceCategory] = None
        # Device category display name. This property is read-only.
        self._device_category_display_name: Optional[str] = None
        # Device compliance policy states for this device.
        self._device_compliance_policy_states: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]] = None
        # Device configuration states for this device.
        self._device_configuration_states: Optional[List[device_configuration_state.DeviceConfigurationState]] = None
        # Possible ways of adding a mobile device to management.
        self._device_enrollment_type: Optional[device_enrollment_type.DeviceEnrollmentType] = None
        # Indicates whether the device is DFCI managed. When TRUE the device is DFCI managed. When FALSE, the device is not DFCI managed. The default value is FALSE.
        self._device_firmware_configuration_interface_managed: Optional[bool] = None
        # The device health attestation state. This property is read-only.
        self._device_health_attestation_state: Optional[device_health_attestation_state.DeviceHealthAttestationState] = None
        # Name of the device. This property is read-only.
        self._device_name: Optional[str] = None
        # Device registration status.
        self._device_registration_state: Optional[device_registration_state.DeviceRegistrationState] = None
        # Device type.
        self._device_type: Optional[device_type.DeviceType] = None
        # Whether the device is Exchange ActiveSync activated. This property is read-only.
        self._eas_activated: Optional[bool] = None
        # Exchange ActivationSync activation time of the device. This property is read-only.
        self._eas_activation_date_time: Optional[datetime] = None
        # Exchange ActiveSync Id of the device. This property is read-only.
        self._eas_device_id: Optional[str] = None
        # Email(s) for the user associated with the device. This property is read-only.
        self._email_address: Optional[str] = None
        # Enrollment time of the device. This property is read-only.
        self._enrolled_date_time: Optional[datetime] = None
        # Name of the enrollment profile assigned to the device. Default value is empty string, indicating no enrollment profile was assgined. This property is read-only.
        self._enrollment_profile_name: Optional[str] = None
        # Ethernet MAC. This property is read-only.
        self._ethernet_mac_address: Optional[str] = None
        # Device Exchange Access State.
        self._exchange_access_state: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState] = None
        # Device Exchange Access State Reason.
        self._exchange_access_state_reason: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason] = None
        # Last time the device contacted Exchange. This property is read-only.
        self._exchange_last_successful_sync_date_time: Optional[datetime] = None
        # Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        self._free_storage_space_in_bytes: Optional[int] = None
        # The hardward details for the device.  Includes information such as storage space, manufacturer, serial number, etc. Return default value in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._hardware_information: Optional[hardware_information.HardwareInformation] = None
        # Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._iccid: Optional[str] = None
        # IMEI. This property is read-only.
        self._imei: Optional[str] = None
        # Device encryption status. This property is read-only.
        self._is_encrypted: Optional[bool] = None
        # Device supervised status. This property is read-only.
        self._is_supervised: Optional[bool] = None
        # whether the device is jail broken or rooted. This property is read-only.
        self._jail_broken: Optional[str] = None
        # Device enrollment join type.
        self._join_type: Optional[join_type.JoinType] = None
        # The date and time that the device last completed a successful sync with Intune. This property is read-only.
        self._last_sync_date_time: Optional[datetime] = None
        # List of log collection requests
        self._log_collection_requests: Optional[List[device_log_collection_response.DeviceLogCollectionResponse]] = None
        # State of lost mode, indicating if lost mode is enabled or disabled
        self._lost_mode_state: Optional[lost_mode_state.LostModeState] = None
        # Managed device mobile app configuration states for this device.
        self._managed_device_mobile_app_configuration_states: Optional[List[managed_device_mobile_app_configuration_state.ManagedDeviceMobileAppConfigurationState]] = None
        # Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        self._managed_device_name: Optional[str] = None
        # Owner type of device.
        self._managed_device_owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
        # Management agent type.
        self._management_agent: Optional[management_agent_type.ManagementAgentType] = None
        # Reports device management certificate expiration date. This property is read-only.
        self._management_certificate_expiration_date: Optional[datetime] = None
        # Device management features.
        self._management_features: Optional[managed_device_management_features.ManagedDeviceManagementFeatures] = None
        # Management state of device in Microsoft Intune.
        self._management_state: Optional[management_state.ManagementState] = None
        # Manufacturer of the device. This property is read-only.
        self._manufacturer: Optional[str] = None
        # MEID. This property is read-only.
        self._meid: Optional[str] = None
        # Model of the device. This property is read-only.
        self._model: Optional[str] = None
        # Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Operating system of the device. Windows, iOS, etc. This property is read-only.
        self._operating_system: Optional[str] = None
        # Operating system version of the device. This property is read-only.
        self._os_version: Optional[str] = None
        # Owner type of device.
        self._owner_type: Optional[owner_type.OwnerType] = None
        # Available health states for the Device Health API
        self._partner_reported_threat_state: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState] = None
        # Phone number of the device. This property is read-only.
        self._phone_number: Optional[str] = None
        # Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        self._physical_memory_in_bytes: Optional[int] = None
        # Reports the DateTime the preferMdmOverGroupPolicy setting was set.  When set, the Intune MDM settings will override Group Policy settings if there is a conflict. Read Only. This property is read-only.
        self._prefer_mdm_over_group_policy_applied_date_time: Optional[datetime] = None
        # Processor architecture
        self._processor_architecture: Optional[managed_device_architecture.ManagedDeviceArchitecture] = None
        # An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        self._remote_assistance_session_error_details: Optional[str] = None
        # Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        self._remote_assistance_session_url: Optional[str] = None
        # Reports if the managed iOS device is user approval enrollment. This property is read-only.
        self._require_user_enrollment_approval: Optional[bool] = None
        # Indicates the time after when a device will be auto retired because of scheduled action. This property is read-only.
        self._retire_after_date_time: Optional[datetime] = None
        # List of Scope Tag IDs for this Device instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Security baseline states for this device.
        self._security_baseline_states: Optional[List[security_baseline_state.SecurityBaselineState]] = None
        # SerialNumber. This property is read-only.
        self._serial_number: Optional[str] = None
        # Device sku family
        self._sku_family: Optional[str] = None
        # Device sku number, see also: https://learn.microsoft.com/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo. Valid values 0 to 2147483647. This property is read-only.
        self._sku_number: Optional[int] = None
        # Specification version. This property is read-only.
        self._specification_version: Optional[str] = None
        # Subscriber Carrier. This property is read-only.
        self._subscriber_carrier: Optional[str] = None
        # Total Storage in Bytes. This property is read-only.
        self._total_storage_space_in_bytes: Optional[int] = None
        # Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._udid: Optional[str] = None
        # User display name. This property is read-only.
        self._user_display_name: Optional[str] = None
        # Unique Identifier for the user associated with the device. This property is read-only.
        self._user_id: Optional[str] = None
        # Device user principal name. This property is read-only.
        self._user_principal_name: Optional[str] = None
        # The primary users associated with the managed device.
        self._users: Optional[List[user.User]] = None
        # Indicates the last logged on users of a device. This property is read-only.
        self._users_logged_on: Optional[List[logged_on_user.LoggedOnUser]] = None
        # Wi-Fi MAC. This property is read-only.
        self._wi_fi_mac_address: Optional[str] = None
        # Count of active malware for this windows device. This property is read-only.
        self._windows_active_malware_count: Optional[int] = None
        # The device protection status. This property is read-only.
        self._windows_protection_state: Optional[windows_protection_state.WindowsProtectionState] = None
        # Count of remediated malware for this windows device. This property is read-only.
        self._windows_remediated_malware_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDevice()
    
    @property
    def detected_apps(self,) -> Optional[List[detected_app.DetectedApp]]:
        """
        Gets the detectedApps property value. All applications currently installed on the device
        Returns: Optional[List[detected_app.DetectedApp]]
        """
        return self._detected_apps
    
    @detected_apps.setter
    def detected_apps(self,value: Optional[List[detected_app.DetectedApp]] = None) -> None:
        """
        Sets the detectedApps property value. All applications currently installed on the device
        Args:
            value: Value to set for the detectedApps property.
        """
        self._detected_apps = value
    
    @property
    def device_action_results(self,) -> Optional[List[device_action_result.DeviceActionResult]]:
        """
        Gets the deviceActionResults property value. List of ComplexType deviceActionResult objects. This property is read-only.
        Returns: Optional[List[device_action_result.DeviceActionResult]]
        """
        return self._device_action_results
    
    @device_action_results.setter
    def device_action_results(self,value: Optional[List[device_action_result.DeviceActionResult]] = None) -> None:
        """
        Sets the deviceActionResults property value. List of ComplexType deviceActionResult objects. This property is read-only.
        Args:
            value: Value to set for the deviceActionResults property.
        """
        self._device_action_results = value
    
    @property
    def device_category(self,) -> Optional[device_category.DeviceCategory]:
        """
        Gets the deviceCategory property value. Device category
        Returns: Optional[device_category.DeviceCategory]
        """
        return self._device_category
    
    @device_category.setter
    def device_category(self,value: Optional[device_category.DeviceCategory] = None) -> None:
        """
        Sets the deviceCategory property value. Device category
        Args:
            value: Value to set for the deviceCategory property.
        """
        self._device_category = value
    
    @property
    def device_category_display_name(self,) -> Optional[str]:
        """
        Gets the deviceCategoryDisplayName property value. Device category display name. This property is read-only.
        Returns: Optional[str]
        """
        return self._device_category_display_name
    
    @device_category_display_name.setter
    def device_category_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceCategoryDisplayName property value. Device category display name. This property is read-only.
        Args:
            value: Value to set for the deviceCategoryDisplayName property.
        """
        self._device_category_display_name = value
    
    @property
    def device_compliance_policy_states(self,) -> Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]]:
        """
        Gets the deviceCompliancePolicyStates property value. Device compliance policy states for this device.
        Returns: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]]
        """
        return self._device_compliance_policy_states
    
    @device_compliance_policy_states.setter
    def device_compliance_policy_states(self,value: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]] = None) -> None:
        """
        Sets the deviceCompliancePolicyStates property value. Device compliance policy states for this device.
        Args:
            value: Value to set for the deviceCompliancePolicyStates property.
        """
        self._device_compliance_policy_states = value
    
    @property
    def device_configuration_states(self,) -> Optional[List[device_configuration_state.DeviceConfigurationState]]:
        """
        Gets the deviceConfigurationStates property value. Device configuration states for this device.
        Returns: Optional[List[device_configuration_state.DeviceConfigurationState]]
        """
        return self._device_configuration_states
    
    @device_configuration_states.setter
    def device_configuration_states(self,value: Optional[List[device_configuration_state.DeviceConfigurationState]] = None) -> None:
        """
        Sets the deviceConfigurationStates property value. Device configuration states for this device.
        Args:
            value: Value to set for the deviceConfigurationStates property.
        """
        self._device_configuration_states = value
    
    @property
    def device_enrollment_type(self,) -> Optional[device_enrollment_type.DeviceEnrollmentType]:
        """
        Gets the deviceEnrollmentType property value. Possible ways of adding a mobile device to management.
        Returns: Optional[device_enrollment_type.DeviceEnrollmentType]
        """
        return self._device_enrollment_type
    
    @device_enrollment_type.setter
    def device_enrollment_type(self,value: Optional[device_enrollment_type.DeviceEnrollmentType] = None) -> None:
        """
        Sets the deviceEnrollmentType property value. Possible ways of adding a mobile device to management.
        Args:
            value: Value to set for the deviceEnrollmentType property.
        """
        self._device_enrollment_type = value
    
    @property
    def device_firmware_configuration_interface_managed(self,) -> Optional[bool]:
        """
        Gets the deviceFirmwareConfigurationInterfaceManaged property value. Indicates whether the device is DFCI managed. When TRUE the device is DFCI managed. When FALSE, the device is not DFCI managed. The default value is FALSE.
        Returns: Optional[bool]
        """
        return self._device_firmware_configuration_interface_managed
    
    @device_firmware_configuration_interface_managed.setter
    def device_firmware_configuration_interface_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceFirmwareConfigurationInterfaceManaged property value. Indicates whether the device is DFCI managed. When TRUE the device is DFCI managed. When FALSE, the device is not DFCI managed. The default value is FALSE.
        Args:
            value: Value to set for the deviceFirmwareConfigurationInterfaceManaged property.
        """
        self._device_firmware_configuration_interface_managed = value
    
    @property
    def device_health_attestation_state(self,) -> Optional[device_health_attestation_state.DeviceHealthAttestationState]:
        """
        Gets the deviceHealthAttestationState property value. The device health attestation state. This property is read-only.
        Returns: Optional[device_health_attestation_state.DeviceHealthAttestationState]
        """
        return self._device_health_attestation_state
    
    @device_health_attestation_state.setter
    def device_health_attestation_state(self,value: Optional[device_health_attestation_state.DeviceHealthAttestationState] = None) -> None:
        """
        Sets the deviceHealthAttestationState property value. The device health attestation state. This property is read-only.
        Args:
            value: Value to set for the deviceHealthAttestationState property.
        """
        self._device_health_attestation_state = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Name of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Name of the device. This property is read-only.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_registration_state(self,) -> Optional[device_registration_state.DeviceRegistrationState]:
        """
        Gets the deviceRegistrationState property value. Device registration status.
        Returns: Optional[device_registration_state.DeviceRegistrationState]
        """
        return self._device_registration_state
    
    @device_registration_state.setter
    def device_registration_state(self,value: Optional[device_registration_state.DeviceRegistrationState] = None) -> None:
        """
        Sets the deviceRegistrationState property value. Device registration status.
        Args:
            value: Value to set for the deviceRegistrationState property.
        """
        self._device_registration_state = value
    
    @property
    def device_type(self,) -> Optional[device_type.DeviceType]:
        """
        Gets the deviceType property value. Device type.
        Returns: Optional[device_type.DeviceType]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[device_type.DeviceType] = None) -> None:
        """
        Sets the deviceType property value. Device type.
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    @property
    def eas_activated(self,) -> Optional[bool]:
        """
        Gets the easActivated property value. Whether the device is Exchange ActiveSync activated. This property is read-only.
        Returns: Optional[bool]
        """
        return self._eas_activated
    
    @eas_activated.setter
    def eas_activated(self,value: Optional[bool] = None) -> None:
        """
        Sets the easActivated property value. Whether the device is Exchange ActiveSync activated. This property is read-only.
        Args:
            value: Value to set for the easActivated property.
        """
        self._eas_activated = value
    
    @property
    def eas_activation_date_time(self,) -> Optional[datetime]:
        """
        Gets the easActivationDateTime property value. Exchange ActivationSync activation time of the device. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._eas_activation_date_time
    
    @eas_activation_date_time.setter
    def eas_activation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the easActivationDateTime property value. Exchange ActivationSync activation time of the device. This property is read-only.
        Args:
            value: Value to set for the easActivationDateTime property.
        """
        self._eas_activation_date_time = value
    
    @property
    def eas_device_id(self,) -> Optional[str]:
        """
        Gets the easDeviceId property value. Exchange ActiveSync Id of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._eas_device_id
    
    @eas_device_id.setter
    def eas_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the easDeviceId property value. Exchange ActiveSync Id of the device. This property is read-only.
        Args:
            value: Value to set for the easDeviceId property.
        """
        self._eas_device_id = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Email(s) for the user associated with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Email(s) for the user associated with the device. This property is read-only.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    @property
    def enrolled_date_time(self,) -> Optional[datetime]:
        """
        Gets the enrolledDateTime property value. Enrollment time of the device. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._enrolled_date_time
    
    @enrolled_date_time.setter
    def enrolled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the enrolledDateTime property value. Enrollment time of the device. This property is read-only.
        Args:
            value: Value to set for the enrolledDateTime property.
        """
        self._enrolled_date_time = value
    
    @property
    def enrollment_profile_name(self,) -> Optional[str]:
        """
        Gets the enrollmentProfileName property value. Name of the enrollment profile assigned to the device. Default value is empty string, indicating no enrollment profile was assgined. This property is read-only.
        Returns: Optional[str]
        """
        return self._enrollment_profile_name
    
    @enrollment_profile_name.setter
    def enrollment_profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentProfileName property value. Name of the enrollment profile assigned to the device. Default value is empty string, indicating no enrollment profile was assgined. This property is read-only.
        Args:
            value: Value to set for the enrollmentProfileName property.
        """
        self._enrollment_profile_name = value
    
    @property
    def ethernet_mac_address(self,) -> Optional[str]:
        """
        Gets the ethernetMacAddress property value. Ethernet MAC. This property is read-only.
        Returns: Optional[str]
        """
        return self._ethernet_mac_address
    
    @ethernet_mac_address.setter
    def ethernet_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ethernetMacAddress property value. Ethernet MAC. This property is read-only.
        Args:
            value: Value to set for the ethernetMacAddress property.
        """
        self._ethernet_mac_address = value
    
    @property
    def exchange_access_state(self,) -> Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState]:
        """
        Gets the exchangeAccessState property value. Device Exchange Access State.
        Returns: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState]
        """
        return self._exchange_access_state
    
    @exchange_access_state.setter
    def exchange_access_state(self,value: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState] = None) -> None:
        """
        Sets the exchangeAccessState property value. Device Exchange Access State.
        Args:
            value: Value to set for the exchangeAccessState property.
        """
        self._exchange_access_state = value
    
    @property
    def exchange_access_state_reason(self,) -> Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason]:
        """
        Gets the exchangeAccessStateReason property value. Device Exchange Access State Reason.
        Returns: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason]
        """
        return self._exchange_access_state_reason
    
    @exchange_access_state_reason.setter
    def exchange_access_state_reason(self,value: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason] = None) -> None:
        """
        Sets the exchangeAccessStateReason property value. Device Exchange Access State Reason.
        Args:
            value: Value to set for the exchangeAccessStateReason property.
        """
        self._exchange_access_state_reason = value
    
    @property
    def exchange_last_successful_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the exchangeLastSuccessfulSyncDateTime property value. Last time the device contacted Exchange. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._exchange_last_successful_sync_date_time
    
    @exchange_last_successful_sync_date_time.setter
    def exchange_last_successful_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the exchangeLastSuccessfulSyncDateTime property value. Last time the device contacted Exchange. This property is read-only.
        Args:
            value: Value to set for the exchangeLastSuccessfulSyncDateTime property.
        """
        self._exchange_last_successful_sync_date_time = value
    
    @property
    def free_storage_space_in_bytes(self,) -> Optional[int]:
        """
        Gets the freeStorageSpaceInBytes property value. Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        Returns: Optional[int]
        """
        return self._free_storage_space_in_bytes
    
    @free_storage_space_in_bytes.setter
    def free_storage_space_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the freeStorageSpaceInBytes property value. Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        Args:
            value: Value to set for the freeStorageSpaceInBytes property.
        """
        self._free_storage_space_in_bytes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aad_registered": lambda n : setattr(self, 'aad_registered', n.get_bool_value()),
            "activation_lock_bypass_code": lambda n : setattr(self, 'activation_lock_bypass_code', n.get_str_value()),
            "android_security_patch_level": lambda n : setattr(self, 'android_security_patch_level', n.get_str_value()),
            "assignment_filter_evaluation_status_details": lambda n : setattr(self, 'assignment_filter_evaluation_status_details', n.get_collection_of_object_values(assignment_filter_evaluation_status_details.AssignmentFilterEvaluationStatusDetails)),
            "autopilot_enrolled": lambda n : setattr(self, 'autopilot_enrolled', n.get_bool_value()),
            "azure_active_directory_device_id": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "azure_a_d_device_id": lambda n : setattr(self, 'azure_a_d_device_id', n.get_str_value()),
            "azure_a_d_registered": lambda n : setattr(self, 'azure_a_d_registered', n.get_bool_value()),
            "bootstrap_token_escrowed": lambda n : setattr(self, 'bootstrap_token_escrowed', n.get_bool_value()),
            "chassis_type": lambda n : setattr(self, 'chassis_type', n.get_enum_value(chassis_type.ChassisType)),
            "chrome_o_s_device_info": lambda n : setattr(self, 'chrome_o_s_device_info', n.get_collection_of_object_values(chrome_o_s_device_property.ChromeOSDeviceProperty)),
            "cloud_pc_remote_action_results": lambda n : setattr(self, 'cloud_pc_remote_action_results', n.get_collection_of_object_values(cloud_pc_remote_action_result.CloudPcRemoteActionResult)),
            "compliance_grace_period_expiration_date_time": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "compliance_state": lambda n : setattr(self, 'compliance_state', n.get_enum_value(compliance_state.ComplianceState)),
            "configuration_manager_client_enabled_features": lambda n : setattr(self, 'configuration_manager_client_enabled_features', n.get_object_value(configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures)),
            "configuration_manager_client_health_state": lambda n : setattr(self, 'configuration_manager_client_health_state', n.get_object_value(configuration_manager_client_health_state.ConfigurationManagerClientHealthState)),
            "configuration_manager_client_information": lambda n : setattr(self, 'configuration_manager_client_information', n.get_object_value(configuration_manager_client_information.ConfigurationManagerClientInformation)),
            "detected_apps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(detected_app.DetectedApp)),
            "device_action_results": lambda n : setattr(self, 'device_action_results', n.get_collection_of_object_values(device_action_result.DeviceActionResult)),
            "device_category": lambda n : setattr(self, 'device_category', n.get_object_value(device_category.DeviceCategory)),
            "device_category_display_name": lambda n : setattr(self, 'device_category_display_name', n.get_str_value()),
            "device_compliance_policy_states": lambda n : setattr(self, 'device_compliance_policy_states', n.get_collection_of_object_values(device_compliance_policy_state.DeviceCompliancePolicyState)),
            "device_configuration_states": lambda n : setattr(self, 'device_configuration_states', n.get_collection_of_object_values(device_configuration_state.DeviceConfigurationState)),
            "device_enrollment_type": lambda n : setattr(self, 'device_enrollment_type', n.get_enum_value(device_enrollment_type.DeviceEnrollmentType)),
            "device_firmware_configuration_interface_managed": lambda n : setattr(self, 'device_firmware_configuration_interface_managed', n.get_bool_value()),
            "device_health_attestation_state": lambda n : setattr(self, 'device_health_attestation_state', n.get_object_value(device_health_attestation_state.DeviceHealthAttestationState)),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_registration_state": lambda n : setattr(self, 'device_registration_state', n.get_enum_value(device_registration_state.DeviceRegistrationState)),
            "device_type": lambda n : setattr(self, 'device_type', n.get_enum_value(device_type.DeviceType)),
            "eas_activated": lambda n : setattr(self, 'eas_activated', n.get_bool_value()),
            "eas_activation_date_time": lambda n : setattr(self, 'eas_activation_date_time', n.get_datetime_value()),
            "eas_device_id": lambda n : setattr(self, 'eas_device_id', n.get_str_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "enrolled_date_time": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "enrollment_profile_name": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "ethernet_mac_address": lambda n : setattr(self, 'ethernet_mac_address', n.get_str_value()),
            "exchange_access_state": lambda n : setattr(self, 'exchange_access_state', n.get_enum_value(device_management_exchange_access_state.DeviceManagementExchangeAccessState)),
            "exchange_access_state_reason": lambda n : setattr(self, 'exchange_access_state_reason', n.get_enum_value(device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason)),
            "exchange_last_successful_sync_date_time": lambda n : setattr(self, 'exchange_last_successful_sync_date_time', n.get_datetime_value()),
            "free_storage_space_in_bytes": lambda n : setattr(self, 'free_storage_space_in_bytes', n.get_int_value()),
            "hardware_information": lambda n : setattr(self, 'hardware_information', n.get_object_value(hardware_information.HardwareInformation)),
            "iccid": lambda n : setattr(self, 'iccid', n.get_str_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "is_encrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "is_supervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "jail_broken": lambda n : setattr(self, 'jail_broken', n.get_str_value()),
            "join_type": lambda n : setattr(self, 'join_type', n.get_enum_value(join_type.JoinType)),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "log_collection_requests": lambda n : setattr(self, 'log_collection_requests', n.get_collection_of_object_values(device_log_collection_response.DeviceLogCollectionResponse)),
            "lost_mode_state": lambda n : setattr(self, 'lost_mode_state', n.get_enum_value(lost_mode_state.LostModeState)),
            "managed_device_mobile_app_configuration_states": lambda n : setattr(self, 'managed_device_mobile_app_configuration_states', n.get_collection_of_object_values(managed_device_mobile_app_configuration_state.ManagedDeviceMobileAppConfigurationState)),
            "managed_device_name": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managed_device_owner_type": lambda n : setattr(self, 'managed_device_owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
            "management_agent": lambda n : setattr(self, 'management_agent', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "management_certificate_expiration_date": lambda n : setattr(self, 'management_certificate_expiration_date', n.get_datetime_value()),
            "management_features": lambda n : setattr(self, 'management_features', n.get_enum_value(managed_device_management_features.ManagedDeviceManagementFeatures)),
            "management_state": lambda n : setattr(self, 'management_state', n.get_enum_value(management_state.ManagementState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "owner_type": lambda n : setattr(self, 'owner_type', n.get_enum_value(owner_type.OwnerType)),
            "partner_reported_threat_state": lambda n : setattr(self, 'partner_reported_threat_state', n.get_enum_value(managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState)),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "physical_memory_in_bytes": lambda n : setattr(self, 'physical_memory_in_bytes', n.get_int_value()),
            "prefer_mdm_over_group_policy_applied_date_time": lambda n : setattr(self, 'prefer_mdm_over_group_policy_applied_date_time', n.get_datetime_value()),
            "processor_architecture": lambda n : setattr(self, 'processor_architecture', n.get_enum_value(managed_device_architecture.ManagedDeviceArchitecture)),
            "remote_assistance_session_error_details": lambda n : setattr(self, 'remote_assistance_session_error_details', n.get_str_value()),
            "remote_assistance_session_url": lambda n : setattr(self, 'remote_assistance_session_url', n.get_str_value()),
            "require_user_enrollment_approval": lambda n : setattr(self, 'require_user_enrollment_approval', n.get_bool_value()),
            "retire_after_date_time": lambda n : setattr(self, 'retire_after_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "security_baseline_states": lambda n : setattr(self, 'security_baseline_states', n.get_collection_of_object_values(security_baseline_state.SecurityBaselineState)),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "sku_family": lambda n : setattr(self, 'sku_family', n.get_str_value()),
            "sku_number": lambda n : setattr(self, 'sku_number', n.get_int_value()),
            "specification_version": lambda n : setattr(self, 'specification_version', n.get_str_value()),
            "subscriber_carrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "total_storage_space_in_bytes": lambda n : setattr(self, 'total_storage_space_in_bytes', n.get_int_value()),
            "udid": lambda n : setattr(self, 'udid', n.get_str_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(user.User)),
            "users_logged_on": lambda n : setattr(self, 'users_logged_on', n.get_collection_of_object_values(logged_on_user.LoggedOnUser)),
            "wi_fi_mac_address": lambda n : setattr(self, 'wi_fi_mac_address', n.get_str_value()),
            "windows_active_malware_count": lambda n : setattr(self, 'windows_active_malware_count', n.get_int_value()),
            "windows_protection_state": lambda n : setattr(self, 'windows_protection_state', n.get_object_value(windows_protection_state.WindowsProtectionState)),
            "windows_remediated_malware_count": lambda n : setattr(self, 'windows_remediated_malware_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hardware_information(self,) -> Optional[hardware_information.HardwareInformation]:
        """
        Gets the hardwareInformation property value. The hardward details for the device.  Includes information such as storage space, manufacturer, serial number, etc. Return default value in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[hardware_information.HardwareInformation]
        """
        return self._hardware_information
    
    @hardware_information.setter
    def hardware_information(self,value: Optional[hardware_information.HardwareInformation] = None) -> None:
        """
        Sets the hardwareInformation property value. The hardward details for the device.  Includes information such as storage space, manufacturer, serial number, etc. Return default value in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the hardwareInformation property.
        """
        self._hardware_information = value
    
    @property
    def iccid(self,) -> Optional[str]:
        """
        Gets the iccid property value. Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._iccid
    
    @iccid.setter
    def iccid(self,value: Optional[str] = None) -> None:
        """
        Sets the iccid property value. Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the iccid property.
        """
        self._iccid = value
    
    @property
    def imei(self,) -> Optional[str]:
        """
        Gets the imei property value. IMEI. This property is read-only.
        Returns: Optional[str]
        """
        return self._imei
    
    @imei.setter
    def imei(self,value: Optional[str] = None) -> None:
        """
        Sets the imei property value. IMEI. This property is read-only.
        Args:
            value: Value to set for the imei property.
        """
        self._imei = value
    
    @property
    def is_encrypted(self,) -> Optional[bool]:
        """
        Gets the isEncrypted property value. Device encryption status. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_encrypted
    
    @is_encrypted.setter
    def is_encrypted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEncrypted property value. Device encryption status. This property is read-only.
        Args:
            value: Value to set for the isEncrypted property.
        """
        self._is_encrypted = value
    
    @property
    def is_supervised(self,) -> Optional[bool]:
        """
        Gets the isSupervised property value. Device supervised status. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_supervised
    
    @is_supervised.setter
    def is_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSupervised property value. Device supervised status. This property is read-only.
        Args:
            value: Value to set for the isSupervised property.
        """
        self._is_supervised = value
    
    @property
    def jail_broken(self,) -> Optional[str]:
        """
        Gets the jailBroken property value. whether the device is jail broken or rooted. This property is read-only.
        Returns: Optional[str]
        """
        return self._jail_broken
    
    @jail_broken.setter
    def jail_broken(self,value: Optional[str] = None) -> None:
        """
        Sets the jailBroken property value. whether the device is jail broken or rooted. This property is read-only.
        Args:
            value: Value to set for the jailBroken property.
        """
        self._jail_broken = value
    
    @property
    def join_type(self,) -> Optional[join_type.JoinType]:
        """
        Gets the joinType property value. Device enrollment join type.
        Returns: Optional[join_type.JoinType]
        """
        return self._join_type
    
    @join_type.setter
    def join_type(self,value: Optional[join_type.JoinType] = None) -> None:
        """
        Sets the joinType property value. Device enrollment join type.
        Args:
            value: Value to set for the joinType property.
        """
        self._join_type = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The date and time that the device last completed a successful sync with Intune. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The date and time that the device last completed a successful sync with Intune. This property is read-only.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def log_collection_requests(self,) -> Optional[List[device_log_collection_response.DeviceLogCollectionResponse]]:
        """
        Gets the logCollectionRequests property value. List of log collection requests
        Returns: Optional[List[device_log_collection_response.DeviceLogCollectionResponse]]
        """
        return self._log_collection_requests
    
    @log_collection_requests.setter
    def log_collection_requests(self,value: Optional[List[device_log_collection_response.DeviceLogCollectionResponse]] = None) -> None:
        """
        Sets the logCollectionRequests property value. List of log collection requests
        Args:
            value: Value to set for the logCollectionRequests property.
        """
        self._log_collection_requests = value
    
    @property
    def lost_mode_state(self,) -> Optional[lost_mode_state.LostModeState]:
        """
        Gets the lostModeState property value. State of lost mode, indicating if lost mode is enabled or disabled
        Returns: Optional[lost_mode_state.LostModeState]
        """
        return self._lost_mode_state
    
    @lost_mode_state.setter
    def lost_mode_state(self,value: Optional[lost_mode_state.LostModeState] = None) -> None:
        """
        Sets the lostModeState property value. State of lost mode, indicating if lost mode is enabled or disabled
        Args:
            value: Value to set for the lostModeState property.
        """
        self._lost_mode_state = value
    
    @property
    def managed_device_mobile_app_configuration_states(self,) -> Optional[List[managed_device_mobile_app_configuration_state.ManagedDeviceMobileAppConfigurationState]]:
        """
        Gets the managedDeviceMobileAppConfigurationStates property value. Managed device mobile app configuration states for this device.
        Returns: Optional[List[managed_device_mobile_app_configuration_state.ManagedDeviceMobileAppConfigurationState]]
        """
        return self._managed_device_mobile_app_configuration_states
    
    @managed_device_mobile_app_configuration_states.setter
    def managed_device_mobile_app_configuration_states(self,value: Optional[List[managed_device_mobile_app_configuration_state.ManagedDeviceMobileAppConfigurationState]] = None) -> None:
        """
        Sets the managedDeviceMobileAppConfigurationStates property value. Managed device mobile app configuration states for this device.
        Args:
            value: Value to set for the managedDeviceMobileAppConfigurationStates property.
        """
        self._managed_device_mobile_app_configuration_states = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        Args:
            value: Value to set for the managedDeviceName property.
        """
        self._managed_device_name = value
    
    @property
    def managed_device_owner_type(self,) -> Optional[managed_device_owner_type.ManagedDeviceOwnerType]:
        """
        Gets the managedDeviceOwnerType property value. Owner type of device.
        Returns: Optional[managed_device_owner_type.ManagedDeviceOwnerType]
        """
        return self._managed_device_owner_type
    
    @managed_device_owner_type.setter
    def managed_device_owner_type(self,value: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None) -> None:
        """
        Sets the managedDeviceOwnerType property value. Owner type of device.
        Args:
            value: Value to set for the managedDeviceOwnerType property.
        """
        self._managed_device_owner_type = value
    
    @property
    def management_agent(self,) -> Optional[management_agent_type.ManagementAgentType]:
        """
        Gets the managementAgent property value. Management agent type.
        Returns: Optional[management_agent_type.ManagementAgentType]
        """
        return self._management_agent
    
    @management_agent.setter
    def management_agent(self,value: Optional[management_agent_type.ManagementAgentType] = None) -> None:
        """
        Sets the managementAgent property value. Management agent type.
        Args:
            value: Value to set for the managementAgent property.
        """
        self._management_agent = value
    
    @property
    def management_certificate_expiration_date(self,) -> Optional[datetime]:
        """
        Gets the managementCertificateExpirationDate property value. Reports device management certificate expiration date. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._management_certificate_expiration_date
    
    @management_certificate_expiration_date.setter
    def management_certificate_expiration_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the managementCertificateExpirationDate property value. Reports device management certificate expiration date. This property is read-only.
        Args:
            value: Value to set for the managementCertificateExpirationDate property.
        """
        self._management_certificate_expiration_date = value
    
    @property
    def management_features(self,) -> Optional[managed_device_management_features.ManagedDeviceManagementFeatures]:
        """
        Gets the managementFeatures property value. Device management features.
        Returns: Optional[managed_device_management_features.ManagedDeviceManagementFeatures]
        """
        return self._management_features
    
    @management_features.setter
    def management_features(self,value: Optional[managed_device_management_features.ManagedDeviceManagementFeatures] = None) -> None:
        """
        Sets the managementFeatures property value. Device management features.
        Args:
            value: Value to set for the managementFeatures property.
        """
        self._management_features = value
    
    @property
    def management_state(self,) -> Optional[management_state.ManagementState]:
        """
        Gets the managementState property value. Management state of device in Microsoft Intune.
        Returns: Optional[management_state.ManagementState]
        """
        return self._management_state
    
    @management_state.setter
    def management_state(self,value: Optional[management_state.ManagementState] = None) -> None:
        """
        Sets the managementState property value. Management state of device in Microsoft Intune.
        Args:
            value: Value to set for the managementState property.
        """
        self._management_state = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer of the device. This property is read-only.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def meid(self,) -> Optional[str]:
        """
        Gets the meid property value. MEID. This property is read-only.
        Returns: Optional[str]
        """
        return self._meid
    
    @meid.setter
    def meid(self,value: Optional[str] = None) -> None:
        """
        Sets the meid property value. MEID. This property is read-only.
        Args:
            value: Value to set for the meid property.
        """
        self._meid = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model of the device. This property is read-only.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. Operating system of the device. Windows, iOS, etc. This property is read-only.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. Operating system of the device. Windows, iOS, etc. This property is read-only.
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Operating system version of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Operating system version of the device. This property is read-only.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def owner_type(self,) -> Optional[owner_type.OwnerType]:
        """
        Gets the ownerType property value. Owner type of device.
        Returns: Optional[owner_type.OwnerType]
        """
        return self._owner_type
    
    @owner_type.setter
    def owner_type(self,value: Optional[owner_type.OwnerType] = None) -> None:
        """
        Sets the ownerType property value. Owner type of device.
        Args:
            value: Value to set for the ownerType property.
        """
        self._owner_type = value
    
    @property
    def partner_reported_threat_state(self,) -> Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState]:
        """
        Gets the partnerReportedThreatState property value. Available health states for the Device Health API
        Returns: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState]
        """
        return self._partner_reported_threat_state
    
    @partner_reported_threat_state.setter
    def partner_reported_threat_state(self,value: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState] = None) -> None:
        """
        Sets the partnerReportedThreatState property value. Available health states for the Device Health API
        Args:
            value: Value to set for the partnerReportedThreatState property.
        """
        self._partner_reported_threat_state = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. Phone number of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. Phone number of the device. This property is read-only.
        Args:
            value: Value to set for the phoneNumber property.
        """
        self._phone_number = value
    
    @property
    def physical_memory_in_bytes(self,) -> Optional[int]:
        """
        Gets the physicalMemoryInBytes property value. Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        Returns: Optional[int]
        """
        return self._physical_memory_in_bytes
    
    @physical_memory_in_bytes.setter
    def physical_memory_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the physicalMemoryInBytes property value. Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        Args:
            value: Value to set for the physicalMemoryInBytes property.
        """
        self._physical_memory_in_bytes = value
    
    @property
    def prefer_mdm_over_group_policy_applied_date_time(self,) -> Optional[datetime]:
        """
        Gets the preferMdmOverGroupPolicyAppliedDateTime property value. Reports the DateTime the preferMdmOverGroupPolicy setting was set.  When set, the Intune MDM settings will override Group Policy settings if there is a conflict. Read Only. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._prefer_mdm_over_group_policy_applied_date_time
    
    @prefer_mdm_over_group_policy_applied_date_time.setter
    def prefer_mdm_over_group_policy_applied_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the preferMdmOverGroupPolicyAppliedDateTime property value. Reports the DateTime the preferMdmOverGroupPolicy setting was set.  When set, the Intune MDM settings will override Group Policy settings if there is a conflict. Read Only. This property is read-only.
        Args:
            value: Value to set for the preferMdmOverGroupPolicyAppliedDateTime property.
        """
        self._prefer_mdm_over_group_policy_applied_date_time = value
    
    @property
    def processor_architecture(self,) -> Optional[managed_device_architecture.ManagedDeviceArchitecture]:
        """
        Gets the processorArchitecture property value. Processor architecture
        Returns: Optional[managed_device_architecture.ManagedDeviceArchitecture]
        """
        return self._processor_architecture
    
    @processor_architecture.setter
    def processor_architecture(self,value: Optional[managed_device_architecture.ManagedDeviceArchitecture] = None) -> None:
        """
        Sets the processorArchitecture property value. Processor architecture
        Args:
            value: Value to set for the processorArchitecture property.
        """
        self._processor_architecture = value
    
    @property
    def remote_assistance_session_error_details(self,) -> Optional[str]:
        """
        Gets the remoteAssistanceSessionErrorDetails property value. An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        Returns: Optional[str]
        """
        return self._remote_assistance_session_error_details
    
    @remote_assistance_session_error_details.setter
    def remote_assistance_session_error_details(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteAssistanceSessionErrorDetails property value. An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        Args:
            value: Value to set for the remoteAssistanceSessionErrorDetails property.
        """
        self._remote_assistance_session_error_details = value
    
    @property
    def remote_assistance_session_url(self,) -> Optional[str]:
        """
        Gets the remoteAssistanceSessionUrl property value. Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._remote_assistance_session_url
    
    @remote_assistance_session_url.setter
    def remote_assistance_session_url(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteAssistanceSessionUrl property value. Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        Args:
            value: Value to set for the remoteAssistanceSessionUrl property.
        """
        self._remote_assistance_session_url = value
    
    @property
    def require_user_enrollment_approval(self,) -> Optional[bool]:
        """
        Gets the requireUserEnrollmentApproval property value. Reports if the managed iOS device is user approval enrollment. This property is read-only.
        Returns: Optional[bool]
        """
        return self._require_user_enrollment_approval
    
    @require_user_enrollment_approval.setter
    def require_user_enrollment_approval(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireUserEnrollmentApproval property value. Reports if the managed iOS device is user approval enrollment. This property is read-only.
        Args:
            value: Value to set for the requireUserEnrollmentApproval property.
        """
        self._require_user_enrollment_approval = value
    
    @property
    def retire_after_date_time(self,) -> Optional[datetime]:
        """
        Gets the retireAfterDateTime property value. Indicates the time after when a device will be auto retired because of scheduled action. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._retire_after_date_time
    
    @retire_after_date_time.setter
    def retire_after_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the retireAfterDateTime property value. Indicates the time after when a device will be auto retired because of scheduled action. This property is read-only.
        Args:
            value: Value to set for the retireAfterDateTime property.
        """
        self._retire_after_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tag IDs for this Device instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tag IDs for this Device instance.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    @property
    def security_baseline_states(self,) -> Optional[List[security_baseline_state.SecurityBaselineState]]:
        """
        Gets the securityBaselineStates property value. Security baseline states for this device.
        Returns: Optional[List[security_baseline_state.SecurityBaselineState]]
        """
        return self._security_baseline_states
    
    @security_baseline_states.setter
    def security_baseline_states(self,value: Optional[List[security_baseline_state.SecurityBaselineState]] = None) -> None:
        """
        Sets the securityBaselineStates property value. Security baseline states for this device.
        Args:
            value: Value to set for the securityBaselineStates property.
        """
        self._security_baseline_states = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignmentFilterEvaluationStatusDetails", self.assignment_filter_evaluation_status_details)
        writer.write_enum_value("chassisType", self.chassis_type)
        writer.write_collection_of_object_values("chromeOSDeviceInfo", self.chrome_o_s_device_info)
        writer.write_collection_of_object_values("cloudPcRemoteActionResults", self.cloud_pc_remote_action_results)
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_object_value("configurationManagerClientHealthState", self.configuration_manager_client_health_state)
        writer.write_object_value("configurationManagerClientInformation", self.configuration_manager_client_information)
        writer.write_collection_of_object_values("detectedApps", self.detected_apps)
        writer.write_object_value("deviceCategory", self.device_category)
        writer.write_collection_of_object_values("deviceCompliancePolicyStates", self.device_compliance_policy_states)
        writer.write_collection_of_object_values("deviceConfigurationStates", self.device_configuration_states)
        writer.write_enum_value("deviceEnrollmentType", self.device_enrollment_type)
        writer.write_bool_value("deviceFirmwareConfigurationInterfaceManaged", self.device_firmware_configuration_interface_managed)
        writer.write_enum_value("deviceRegistrationState", self.device_registration_state)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_enum_value("exchangeAccessState", self.exchange_access_state)
        writer.write_enum_value("exchangeAccessStateReason", self.exchange_access_state_reason)
        writer.write_enum_value("joinType", self.join_type)
        writer.write_collection_of_object_values("logCollectionRequests", self.log_collection_requests)
        writer.write_enum_value("lostModeState", self.lost_mode_state)
        writer.write_collection_of_object_values("managedDeviceMobileAppConfigurationStates", self.managed_device_mobile_app_configuration_states)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_enum_value("managedDeviceOwnerType", self.managed_device_owner_type)
        writer.write_enum_value("managementAgent", self.management_agent)
        writer.write_enum_value("managementFeatures", self.management_features)
        writer.write_enum_value("managementState", self.management_state)
        writer.write_str_value("notes", self.notes)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_enum_value("partnerReportedThreatState", self.partner_reported_threat_state)
        writer.write_enum_value("processorArchitecture", self.processor_architecture)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("securityBaselineStates", self.security_baseline_states)
        writer.write_str_value("skuFamily", self.sku_family)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_object_value("windowsProtectionState", self.windows_protection_state)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. SerialNumber. This property is read-only.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. SerialNumber. This property is read-only.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def sku_family(self,) -> Optional[str]:
        """
        Gets the skuFamily property value. Device sku family
        Returns: Optional[str]
        """
        return self._sku_family
    
    @sku_family.setter
    def sku_family(self,value: Optional[str] = None) -> None:
        """
        Sets the skuFamily property value. Device sku family
        Args:
            value: Value to set for the skuFamily property.
        """
        self._sku_family = value
    
    @property
    def sku_number(self,) -> Optional[int]:
        """
        Gets the skuNumber property value. Device sku number, see also: https://learn.microsoft.com/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo. Valid values 0 to 2147483647. This property is read-only.
        Returns: Optional[int]
        """
        return self._sku_number
    
    @sku_number.setter
    def sku_number(self,value: Optional[int] = None) -> None:
        """
        Sets the skuNumber property value. Device sku number, see also: https://learn.microsoft.com/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo. Valid values 0 to 2147483647. This property is read-only.
        Args:
            value: Value to set for the skuNumber property.
        """
        self._sku_number = value
    
    @property
    def specification_version(self,) -> Optional[str]:
        """
        Gets the specificationVersion property value. Specification version. This property is read-only.
        Returns: Optional[str]
        """
        return self._specification_version
    
    @specification_version.setter
    def specification_version(self,value: Optional[str] = None) -> None:
        """
        Sets the specificationVersion property value. Specification version. This property is read-only.
        Args:
            value: Value to set for the specificationVersion property.
        """
        self._specification_version = value
    
    @property
    def subscriber_carrier(self,) -> Optional[str]:
        """
        Gets the subscriberCarrier property value. Subscriber Carrier. This property is read-only.
        Returns: Optional[str]
        """
        return self._subscriber_carrier
    
    @subscriber_carrier.setter
    def subscriber_carrier(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriberCarrier property value. Subscriber Carrier. This property is read-only.
        Args:
            value: Value to set for the subscriberCarrier property.
        """
        self._subscriber_carrier = value
    
    @property
    def total_storage_space_in_bytes(self,) -> Optional[int]:
        """
        Gets the totalStorageSpaceInBytes property value. Total Storage in Bytes. This property is read-only.
        Returns: Optional[int]
        """
        return self._total_storage_space_in_bytes
    
    @total_storage_space_in_bytes.setter
    def total_storage_space_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the totalStorageSpaceInBytes property value. Total Storage in Bytes. This property is read-only.
        Args:
            value: Value to set for the totalStorageSpaceInBytes property.
        """
        self._total_storage_space_in_bytes = value
    
    @property
    def udid(self,) -> Optional[str]:
        """
        Gets the udid property value. Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._udid
    
    @udid.setter
    def udid(self,value: Optional[str] = None) -> None:
        """
        Sets the udid property value. Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the udid property.
        """
        self._udid = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. User display name. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. User display name. This property is read-only.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Unique Identifier for the user associated with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Unique Identifier for the user associated with the device. This property is read-only.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. Device user principal name. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. Device user principal name. This property is read-only.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def users(self,) -> Optional[List[user.User]]:
        """
        Gets the users property value. The primary users associated with the managed device.
        Returns: Optional[List[user.User]]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the users property value. The primary users associated with the managed device.
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    
    @property
    def users_logged_on(self,) -> Optional[List[logged_on_user.LoggedOnUser]]:
        """
        Gets the usersLoggedOn property value. Indicates the last logged on users of a device. This property is read-only.
        Returns: Optional[List[logged_on_user.LoggedOnUser]]
        """
        return self._users_logged_on
    
    @users_logged_on.setter
    def users_logged_on(self,value: Optional[List[logged_on_user.LoggedOnUser]] = None) -> None:
        """
        Sets the usersLoggedOn property value. Indicates the last logged on users of a device. This property is read-only.
        Args:
            value: Value to set for the usersLoggedOn property.
        """
        self._users_logged_on = value
    
    @property
    def wi_fi_mac_address(self,) -> Optional[str]:
        """
        Gets the wiFiMacAddress property value. Wi-Fi MAC. This property is read-only.
        Returns: Optional[str]
        """
        return self._wi_fi_mac_address
    
    @wi_fi_mac_address.setter
    def wi_fi_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the wiFiMacAddress property value. Wi-Fi MAC. This property is read-only.
        Args:
            value: Value to set for the wiFiMacAddress property.
        """
        self._wi_fi_mac_address = value
    
    @property
    def windows_active_malware_count(self,) -> Optional[int]:
        """
        Gets the windowsActiveMalwareCount property value. Count of active malware for this windows device. This property is read-only.
        Returns: Optional[int]
        """
        return self._windows_active_malware_count
    
    @windows_active_malware_count.setter
    def windows_active_malware_count(self,value: Optional[int] = None) -> None:
        """
        Sets the windowsActiveMalwareCount property value. Count of active malware for this windows device. This property is read-only.
        Args:
            value: Value to set for the windowsActiveMalwareCount property.
        """
        self._windows_active_malware_count = value
    
    @property
    def windows_protection_state(self,) -> Optional[windows_protection_state.WindowsProtectionState]:
        """
        Gets the windowsProtectionState property value. The device protection status. This property is read-only.
        Returns: Optional[windows_protection_state.WindowsProtectionState]
        """
        return self._windows_protection_state
    
    @windows_protection_state.setter
    def windows_protection_state(self,value: Optional[windows_protection_state.WindowsProtectionState] = None) -> None:
        """
        Sets the windowsProtectionState property value. The device protection status. This property is read-only.
        Args:
            value: Value to set for the windowsProtectionState property.
        """
        self._windows_protection_state = value
    
    @property
    def windows_remediated_malware_count(self,) -> Optional[int]:
        """
        Gets the windowsRemediatedMalwareCount property value. Count of remediated malware for this windows device. This property is read-only.
        Returns: Optional[int]
        """
        return self._windows_remediated_malware_count
    
    @windows_remediated_malware_count.setter
    def windows_remediated_malware_count(self,value: Optional[int] = None) -> None:
        """
        Sets the windowsRemediatedMalwareCount property value. Count of remediated malware for this windows device. This property is read-only.
        Args:
            value: Value to set for the windowsRemediatedMalwareCount property.
        """
        self._windows_remediated_malware_count = value
    

