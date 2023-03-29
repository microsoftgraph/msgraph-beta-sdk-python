from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_autopilot_policy_status_detail, enrollment_state, entity, windows_autopilot_deployment_state, windows_autopilot_enrollment_type

from . import entity

class DeviceManagementAutopilotEvent(entity.Entity):
    """
    Represents an Autopilot flow event.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementAutopilotEvent and sets the default values.
        """
        super().__init__()
        # Time spent in user ESP.
        self._account_setup_duration: Optional[timedelta] = None
        # Deployment states for Autopilot devices
        self._account_setup_status: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None
        # Autopilot deployment duration including enrollment.
        self._deployment_duration: Optional[timedelta] = None
        # Deployment end time.
        self._deployment_end_date_time: Optional[datetime] = None
        # Deployment start time.
        self._deployment_start_date_time: Optional[datetime] = None
        # Deployment states for Autopilot devices
        self._deployment_state: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None
        # Total deployment duration from enrollment to Desktop screen.
        self._deployment_total_duration: Optional[timedelta] = None
        # Device id associated with the object
        self._device_id: Optional[str] = None
        # Time spent in device enrollment.
        self._device_preparation_duration: Optional[timedelta] = None
        # Device registration date.
        self._device_registered_date_time: Optional[datetime] = None
        # Device serial number.
        self._device_serial_number: Optional[str] = None
        # Time spent in device ESP.
        self._device_setup_duration: Optional[timedelta] = None
        # Deployment states for Autopilot devices
        self._device_setup_status: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None
        # Enrollment failure details.
        self._enrollment_failure_details: Optional[str] = None
        # Device enrollment start date.
        self._enrollment_start_date_time: Optional[datetime] = None
        # The enrollmentState property
        self._enrollment_state: Optional[enrollment_state.EnrollmentState] = None
        # The enrollmentType property
        self._enrollment_type: Optional[windows_autopilot_enrollment_type.WindowsAutopilotEnrollmentType] = None
        # Time when the event occurred .
        self._event_date_time: Optional[datetime] = None
        # Managed device name.
        self._managed_device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device operating system version.
        self._os_version: Optional[str] = None
        # Policy and application status details for this device.
        self._policy_status_details: Optional[List[device_management_autopilot_policy_status_detail.DeviceManagementAutopilotPolicyStatusDetail]] = None
        # Count of applications targeted.
        self._targeted_app_count: Optional[int] = None
        # Count of policies targeted.
        self._targeted_policy_count: Optional[int] = None
        # User principal name used to enroll the device.
        self._user_principal_name: Optional[str] = None
        # Autopilot profile name.
        self._windows_autopilot_deployment_profile_display_name: Optional[str] = None
        # Enrollment Status Page profile name
        self._windows10_enrollment_completion_page_configuration_display_name: Optional[str] = None
        # Enrollment Status Page profile ID
        self._windows10_enrollment_completion_page_configuration_id: Optional[str] = None
    
    @property
    def account_setup_duration(self,) -> Optional[timedelta]:
        """
        Gets the accountSetupDuration property value. Time spent in user ESP.
        Returns: Optional[timedelta]
        """
        return self._account_setup_duration
    
    @account_setup_duration.setter
    def account_setup_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the accountSetupDuration property value. Time spent in user ESP.
        Args:
            value: Value to set for the account_setup_duration property.
        """
        self._account_setup_duration = value
    
    @property
    def account_setup_status(self,) -> Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]:
        """
        Gets the accountSetupStatus property value. Deployment states for Autopilot devices
        Returns: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]
        """
        return self._account_setup_status
    
    @account_setup_status.setter
    def account_setup_status(self,value: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None) -> None:
        """
        Sets the accountSetupStatus property value. Deployment states for Autopilot devices
        Args:
            value: Value to set for the account_setup_status property.
        """
        self._account_setup_status = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementAutopilotEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAutopilotEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementAutopilotEvent()
    
    @property
    def deployment_duration(self,) -> Optional[timedelta]:
        """
        Gets the deploymentDuration property value. Autopilot deployment duration including enrollment.
        Returns: Optional[timedelta]
        """
        return self._deployment_duration
    
    @deployment_duration.setter
    def deployment_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the deploymentDuration property value. Autopilot deployment duration including enrollment.
        Args:
            value: Value to set for the deployment_duration property.
        """
        self._deployment_duration = value
    
    @property
    def deployment_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the deploymentEndDateTime property value. Deployment end time.
        Returns: Optional[datetime]
        """
        return self._deployment_end_date_time
    
    @deployment_end_date_time.setter
    def deployment_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deploymentEndDateTime property value. Deployment end time.
        Args:
            value: Value to set for the deployment_end_date_time property.
        """
        self._deployment_end_date_time = value
    
    @property
    def deployment_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the deploymentStartDateTime property value. Deployment start time.
        Returns: Optional[datetime]
        """
        return self._deployment_start_date_time
    
    @deployment_start_date_time.setter
    def deployment_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deploymentStartDateTime property value. Deployment start time.
        Args:
            value: Value to set for the deployment_start_date_time property.
        """
        self._deployment_start_date_time = value
    
    @property
    def deployment_state(self,) -> Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]:
        """
        Gets the deploymentState property value. Deployment states for Autopilot devices
        Returns: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]
        """
        return self._deployment_state
    
    @deployment_state.setter
    def deployment_state(self,value: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None) -> None:
        """
        Sets the deploymentState property value. Deployment states for Autopilot devices
        Args:
            value: Value to set for the deployment_state property.
        """
        self._deployment_state = value
    
    @property
    def deployment_total_duration(self,) -> Optional[timedelta]:
        """
        Gets the deploymentTotalDuration property value. Total deployment duration from enrollment to Desktop screen.
        Returns: Optional[timedelta]
        """
        return self._deployment_total_duration
    
    @deployment_total_duration.setter
    def deployment_total_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the deploymentTotalDuration property value. Total deployment duration from enrollment to Desktop screen.
        Args:
            value: Value to set for the deployment_total_duration property.
        """
        self._deployment_total_duration = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Device id associated with the object
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Device id associated with the object
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_preparation_duration(self,) -> Optional[timedelta]:
        """
        Gets the devicePreparationDuration property value. Time spent in device enrollment.
        Returns: Optional[timedelta]
        """
        return self._device_preparation_duration
    
    @device_preparation_duration.setter
    def device_preparation_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the devicePreparationDuration property value. Time spent in device enrollment.
        Args:
            value: Value to set for the device_preparation_duration property.
        """
        self._device_preparation_duration = value
    
    @property
    def device_registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the deviceRegisteredDateTime property value. Device registration date.
        Returns: Optional[datetime]
        """
        return self._device_registered_date_time
    
    @device_registered_date_time.setter
    def device_registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deviceRegisteredDateTime property value. Device registration date.
        Args:
            value: Value to set for the device_registered_date_time property.
        """
        self._device_registered_date_time = value
    
    @property
    def device_serial_number(self,) -> Optional[str]:
        """
        Gets the deviceSerialNumber property value. Device serial number.
        Returns: Optional[str]
        """
        return self._device_serial_number
    
    @device_serial_number.setter
    def device_serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceSerialNumber property value. Device serial number.
        Args:
            value: Value to set for the device_serial_number property.
        """
        self._device_serial_number = value
    
    @property
    def device_setup_duration(self,) -> Optional[timedelta]:
        """
        Gets the deviceSetupDuration property value. Time spent in device ESP.
        Returns: Optional[timedelta]
        """
        return self._device_setup_duration
    
    @device_setup_duration.setter
    def device_setup_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the deviceSetupDuration property value. Time spent in device ESP.
        Args:
            value: Value to set for the device_setup_duration property.
        """
        self._device_setup_duration = value
    
    @property
    def device_setup_status(self,) -> Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]:
        """
        Gets the deviceSetupStatus property value. Deployment states for Autopilot devices
        Returns: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState]
        """
        return self._device_setup_status
    
    @device_setup_status.setter
    def device_setup_status(self,value: Optional[windows_autopilot_deployment_state.WindowsAutopilotDeploymentState] = None) -> None:
        """
        Sets the deviceSetupStatus property value. Deployment states for Autopilot devices
        Args:
            value: Value to set for the device_setup_status property.
        """
        self._device_setup_status = value
    
    @property
    def enrollment_failure_details(self,) -> Optional[str]:
        """
        Gets the enrollmentFailureDetails property value. Enrollment failure details.
        Returns: Optional[str]
        """
        return self._enrollment_failure_details
    
    @enrollment_failure_details.setter
    def enrollment_failure_details(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentFailureDetails property value. Enrollment failure details.
        Args:
            value: Value to set for the enrollment_failure_details property.
        """
        self._enrollment_failure_details = value
    
    @property
    def enrollment_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the enrollmentStartDateTime property value. Device enrollment start date.
        Returns: Optional[datetime]
        """
        return self._enrollment_start_date_time
    
    @enrollment_start_date_time.setter
    def enrollment_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the enrollmentStartDateTime property value. Device enrollment start date.
        Args:
            value: Value to set for the enrollment_start_date_time property.
        """
        self._enrollment_start_date_time = value
    
    @property
    def enrollment_state(self,) -> Optional[enrollment_state.EnrollmentState]:
        """
        Gets the enrollmentState property value. The enrollmentState property
        Returns: Optional[enrollment_state.EnrollmentState]
        """
        return self._enrollment_state
    
    @enrollment_state.setter
    def enrollment_state(self,value: Optional[enrollment_state.EnrollmentState] = None) -> None:
        """
        Sets the enrollmentState property value. The enrollmentState property
        Args:
            value: Value to set for the enrollment_state property.
        """
        self._enrollment_state = value
    
    @property
    def enrollment_type(self,) -> Optional[windows_autopilot_enrollment_type.WindowsAutopilotEnrollmentType]:
        """
        Gets the enrollmentType property value. The enrollmentType property
        Returns: Optional[windows_autopilot_enrollment_type.WindowsAutopilotEnrollmentType]
        """
        return self._enrollment_type
    
    @enrollment_type.setter
    def enrollment_type(self,value: Optional[windows_autopilot_enrollment_type.WindowsAutopilotEnrollmentType] = None) -> None:
        """
        Sets the enrollmentType property value. The enrollmentType property
        Args:
            value: Value to set for the enrollment_type property.
        """
        self._enrollment_type = value
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Time when the event occurred .
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Time when the event occurred .
        Args:
            value: Value to set for the event_date_time property.
        """
        self._event_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_autopilot_policy_status_detail, enrollment_state, entity, windows_autopilot_deployment_state, windows_autopilot_enrollment_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accountSetupDuration": lambda n : setattr(self, 'account_setup_duration', n.get_timedelta_value()),
            "accountSetupStatus": lambda n : setattr(self, 'account_setup_status', n.get_enum_value(windows_autopilot_deployment_state.WindowsAutopilotDeploymentState)),
            "deploymentDuration": lambda n : setattr(self, 'deployment_duration', n.get_timedelta_value()),
            "deploymentEndDateTime": lambda n : setattr(self, 'deployment_end_date_time', n.get_datetime_value()),
            "deploymentStartDateTime": lambda n : setattr(self, 'deployment_start_date_time', n.get_datetime_value()),
            "deploymentState": lambda n : setattr(self, 'deployment_state', n.get_enum_value(windows_autopilot_deployment_state.WindowsAutopilotDeploymentState)),
            "deploymentTotalDuration": lambda n : setattr(self, 'deployment_total_duration', n.get_timedelta_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "devicePreparationDuration": lambda n : setattr(self, 'device_preparation_duration', n.get_timedelta_value()),
            "deviceRegisteredDateTime": lambda n : setattr(self, 'device_registered_date_time', n.get_datetime_value()),
            "deviceSerialNumber": lambda n : setattr(self, 'device_serial_number', n.get_str_value()),
            "deviceSetupDuration": lambda n : setattr(self, 'device_setup_duration', n.get_timedelta_value()),
            "deviceSetupStatus": lambda n : setattr(self, 'device_setup_status', n.get_enum_value(windows_autopilot_deployment_state.WindowsAutopilotDeploymentState)),
            "enrollmentFailureDetails": lambda n : setattr(self, 'enrollment_failure_details', n.get_str_value()),
            "enrollmentStartDateTime": lambda n : setattr(self, 'enrollment_start_date_time', n.get_datetime_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(windows_autopilot_enrollment_type.WindowsAutopilotEnrollmentType)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policyStatusDetails": lambda n : setattr(self, 'policy_status_details', n.get_collection_of_object_values(device_management_autopilot_policy_status_detail.DeviceManagementAutopilotPolicyStatusDetail)),
            "targetedAppCount": lambda n : setattr(self, 'targeted_app_count', n.get_int_value()),
            "targetedPolicyCount": lambda n : setattr(self, 'targeted_policy_count', n.get_int_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "windows10EnrollmentCompletionPageConfigurationDisplayName": lambda n : setattr(self, 'windows10_enrollment_completion_page_configuration_display_name', n.get_str_value()),
            "windows10EnrollmentCompletionPageConfigurationId": lambda n : setattr(self, 'windows10_enrollment_completion_page_configuration_id', n.get_str_value()),
            "windowsAutopilotDeploymentProfileDisplayName": lambda n : setattr(self, 'windows_autopilot_deployment_profile_display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. Managed device name.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. Managed device name.
        Args:
            value: Value to set for the managed_device_name property.
        """
        self._managed_device_name = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Device operating system version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Device operating system version.
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    @property
    def policy_status_details(self,) -> Optional[List[device_management_autopilot_policy_status_detail.DeviceManagementAutopilotPolicyStatusDetail]]:
        """
        Gets the policyStatusDetails property value. Policy and application status details for this device.
        Returns: Optional[List[device_management_autopilot_policy_status_detail.DeviceManagementAutopilotPolicyStatusDetail]]
        """
        return self._policy_status_details
    
    @policy_status_details.setter
    def policy_status_details(self,value: Optional[List[device_management_autopilot_policy_status_detail.DeviceManagementAutopilotPolicyStatusDetail]] = None) -> None:
        """
        Sets the policyStatusDetails property value. Policy and application status details for this device.
        Args:
            value: Value to set for the policy_status_details property.
        """
        self._policy_status_details = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_timedelta_value("accountSetupDuration", self.account_setup_duration)
        writer.write_enum_value("accountSetupStatus", self.account_setup_status)
        writer.write_timedelta_value("deploymentDuration", self.deployment_duration)
        writer.write_datetime_value("deploymentEndDateTime", self.deployment_end_date_time)
        writer.write_datetime_value("deploymentStartDateTime", self.deployment_start_date_time)
        writer.write_enum_value("deploymentState", self.deployment_state)
        writer.write_timedelta_value("deploymentTotalDuration", self.deployment_total_duration)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_timedelta_value("devicePreparationDuration", self.device_preparation_duration)
        writer.write_datetime_value("deviceRegisteredDateTime", self.device_registered_date_time)
        writer.write_str_value("deviceSerialNumber", self.device_serial_number)
        writer.write_timedelta_value("deviceSetupDuration", self.device_setup_duration)
        writer.write_enum_value("deviceSetupStatus", self.device_setup_status)
        writer.write_str_value("enrollmentFailureDetails", self.enrollment_failure_details)
        writer.write_datetime_value("enrollmentStartDateTime", self.enrollment_start_date_time)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_collection_of_object_values("policyStatusDetails", self.policy_status_details)
        writer.write_int_value("targetedAppCount", self.targeted_app_count)
        writer.write_int_value("targetedPolicyCount", self.targeted_policy_count)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("windows10EnrollmentCompletionPageConfigurationDisplayName", self.windows10_enrollment_completion_page_configuration_display_name)
        writer.write_str_value("windows10EnrollmentCompletionPageConfigurationId", self.windows10_enrollment_completion_page_configuration_id)
        writer.write_str_value("windowsAutopilotDeploymentProfileDisplayName", self.windows_autopilot_deployment_profile_display_name)
    
    @property
    def targeted_app_count(self,) -> Optional[int]:
        """
        Gets the targetedAppCount property value. Count of applications targeted.
        Returns: Optional[int]
        """
        return self._targeted_app_count
    
    @targeted_app_count.setter
    def targeted_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the targetedAppCount property value. Count of applications targeted.
        Args:
            value: Value to set for the targeted_app_count property.
        """
        self._targeted_app_count = value
    
    @property
    def targeted_policy_count(self,) -> Optional[int]:
        """
        Gets the targetedPolicyCount property value. Count of policies targeted.
        Returns: Optional[int]
        """
        return self._targeted_policy_count
    
    @targeted_policy_count.setter
    def targeted_policy_count(self,value: Optional[int] = None) -> None:
        """
        Sets the targetedPolicyCount property value. Count of policies targeted.
        Args:
            value: Value to set for the targeted_policy_count property.
        """
        self._targeted_policy_count = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name used to enroll the device.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name used to enroll the device.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def windows_autopilot_deployment_profile_display_name(self,) -> Optional[str]:
        """
        Gets the windowsAutopilotDeploymentProfileDisplayName property value. Autopilot profile name.
        Returns: Optional[str]
        """
        return self._windows_autopilot_deployment_profile_display_name
    
    @windows_autopilot_deployment_profile_display_name.setter
    def windows_autopilot_deployment_profile_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the windowsAutopilotDeploymentProfileDisplayName property value. Autopilot profile name.
        Args:
            value: Value to set for the windows_autopilot_deployment_profile_display_name property.
        """
        self._windows_autopilot_deployment_profile_display_name = value
    
    @property
    def windows10_enrollment_completion_page_configuration_display_name(self,) -> Optional[str]:
        """
        Gets the windows10EnrollmentCompletionPageConfigurationDisplayName property value. Enrollment Status Page profile name
        Returns: Optional[str]
        """
        return self._windows10_enrollment_completion_page_configuration_display_name
    
    @windows10_enrollment_completion_page_configuration_display_name.setter
    def windows10_enrollment_completion_page_configuration_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the windows10EnrollmentCompletionPageConfigurationDisplayName property value. Enrollment Status Page profile name
        Args:
            value: Value to set for the windows10_enrollment_completion_page_configuration_display_name property.
        """
        self._windows10_enrollment_completion_page_configuration_display_name = value
    
    @property
    def windows10_enrollment_completion_page_configuration_id(self,) -> Optional[str]:
        """
        Gets the windows10EnrollmentCompletionPageConfigurationId property value. Enrollment Status Page profile ID
        Returns: Optional[str]
        """
        return self._windows10_enrollment_completion_page_configuration_id
    
    @windows10_enrollment_completion_page_configuration_id.setter
    def windows10_enrollment_completion_page_configuration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the windows10EnrollmentCompletionPageConfigurationId property value. Enrollment Status Page profile ID
        Args:
            value: Value to set for the windows10_enrollment_completion_page_configuration_id property.
        """
        self._windows10_enrollment_completion_page_configuration_id = value
    

