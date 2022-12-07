from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

derived_credential_provider_type = lazy_import('msgraph.generated.models.derived_credential_provider_type')

class DeviceManagementSettings(AdditionalDataHolder, Parsable):
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
    def android_device_administrator_enrollment_enabled(self,) -> Optional[bool]:
        """
        Gets the androidDeviceAdministratorEnrollmentEnabled property value. The property to determine if Android device administrator enrollment is enabled for this account.
        Returns: Optional[bool]
        """
        return self._android_device_administrator_enrollment_enabled
    
    @android_device_administrator_enrollment_enabled.setter
    def android_device_administrator_enrollment_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidDeviceAdministratorEnrollmentEnabled property value. The property to determine if Android device administrator enrollment is enabled for this account.
        Args:
            value: Value to set for the androidDeviceAdministratorEnrollmentEnabled property.
        """
        self._android_device_administrator_enrollment_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The property to determine if Android device administrator enrollment is enabled for this account.
        self._android_device_administrator_enrollment_enabled: Optional[bool] = None
        # Provider type for Derived Credentials.
        self._derived_credential_provider: Optional[derived_credential_provider_type.DerivedCredentialProviderType] = None
        # The Derived Credential Provider self-service URI.
        self._derived_credential_url: Optional[str] = None
        # The number of days a device is allowed to go without checking in to remain compliant.
        self._device_compliance_checkin_threshold_days: Optional[int] = None
        # When the device does not check in for specified number of days, the company data might be removed and the device will not be under management. Valid values 30 to 270
        self._device_inactivity_before_retirement_in_day: Optional[int] = None
        # Determines whether the autopilot diagnostic feature is enabled or not.
        self._enable_autopilot_diagnostics: Optional[bool] = None
        # Determines whether the device group membership report feature is enabled or not.
        self._enable_device_group_membership_report: Optional[bool] = None
        # Determines whether the enhanced troubleshooting UX is enabled or not.
        self._enable_enhanced_troubleshooting_experience: Optional[bool] = None
        # Determines whether the log collection feature should be available for use.
        self._enable_log_collection: Optional[bool] = None
        # Is feature enabled or not for enhanced jailbreak detection.
        self._enhanced_jail_break: Optional[bool] = None
        # The property to determine whether to ignore unsupported compliance settings on certian models of devices.
        self._ignore_devices_for_unsupported_settings_enabled: Optional[bool] = None
        # Is feature enabled or not for scheduled action for rule.
        self._is_scheduled_action_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Device should be noncompliant when there is no compliance policy targeted when this is true
        self._secure_by_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettings()
    
    @property
    def derived_credential_provider(self,) -> Optional[derived_credential_provider_type.DerivedCredentialProviderType]:
        """
        Gets the derivedCredentialProvider property value. Provider type for Derived Credentials.
        Returns: Optional[derived_credential_provider_type.DerivedCredentialProviderType]
        """
        return self._derived_credential_provider
    
    @derived_credential_provider.setter
    def derived_credential_provider(self,value: Optional[derived_credential_provider_type.DerivedCredentialProviderType] = None) -> None:
        """
        Sets the derivedCredentialProvider property value. Provider type for Derived Credentials.
        Args:
            value: Value to set for the derivedCredentialProvider property.
        """
        self._derived_credential_provider = value
    
    @property
    def derived_credential_url(self,) -> Optional[str]:
        """
        Gets the derivedCredentialUrl property value. The Derived Credential Provider self-service URI.
        Returns: Optional[str]
        """
        return self._derived_credential_url
    
    @derived_credential_url.setter
    def derived_credential_url(self,value: Optional[str] = None) -> None:
        """
        Sets the derivedCredentialUrl property value. The Derived Credential Provider self-service URI.
        Args:
            value: Value to set for the derivedCredentialUrl property.
        """
        self._derived_credential_url = value
    
    @property
    def device_compliance_checkin_threshold_days(self,) -> Optional[int]:
        """
        Gets the deviceComplianceCheckinThresholdDays property value. The number of days a device is allowed to go without checking in to remain compliant.
        Returns: Optional[int]
        """
        return self._device_compliance_checkin_threshold_days
    
    @device_compliance_checkin_threshold_days.setter
    def device_compliance_checkin_threshold_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceComplianceCheckinThresholdDays property value. The number of days a device is allowed to go without checking in to remain compliant.
        Args:
            value: Value to set for the deviceComplianceCheckinThresholdDays property.
        """
        self._device_compliance_checkin_threshold_days = value
    
    @property
    def device_inactivity_before_retirement_in_day(self,) -> Optional[int]:
        """
        Gets the deviceInactivityBeforeRetirementInDay property value. When the device does not check in for specified number of days, the company data might be removed and the device will not be under management. Valid values 30 to 270
        Returns: Optional[int]
        """
        return self._device_inactivity_before_retirement_in_day
    
    @device_inactivity_before_retirement_in_day.setter
    def device_inactivity_before_retirement_in_day(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceInactivityBeforeRetirementInDay property value. When the device does not check in for specified number of days, the company data might be removed and the device will not be under management. Valid values 30 to 270
        Args:
            value: Value to set for the deviceInactivityBeforeRetirementInDay property.
        """
        self._device_inactivity_before_retirement_in_day = value
    
    @property
    def enable_autopilot_diagnostics(self,) -> Optional[bool]:
        """
        Gets the enableAutopilotDiagnostics property value. Determines whether the autopilot diagnostic feature is enabled or not.
        Returns: Optional[bool]
        """
        return self._enable_autopilot_diagnostics
    
    @enable_autopilot_diagnostics.setter
    def enable_autopilot_diagnostics(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableAutopilotDiagnostics property value. Determines whether the autopilot diagnostic feature is enabled or not.
        Args:
            value: Value to set for the enableAutopilotDiagnostics property.
        """
        self._enable_autopilot_diagnostics = value
    
    @property
    def enable_device_group_membership_report(self,) -> Optional[bool]:
        """
        Gets the enableDeviceGroupMembershipReport property value. Determines whether the device group membership report feature is enabled or not.
        Returns: Optional[bool]
        """
        return self._enable_device_group_membership_report
    
    @enable_device_group_membership_report.setter
    def enable_device_group_membership_report(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableDeviceGroupMembershipReport property value. Determines whether the device group membership report feature is enabled or not.
        Args:
            value: Value to set for the enableDeviceGroupMembershipReport property.
        """
        self._enable_device_group_membership_report = value
    
    @property
    def enable_enhanced_troubleshooting_experience(self,) -> Optional[bool]:
        """
        Gets the enableEnhancedTroubleshootingExperience property value. Determines whether the enhanced troubleshooting UX is enabled or not.
        Returns: Optional[bool]
        """
        return self._enable_enhanced_troubleshooting_experience
    
    @enable_enhanced_troubleshooting_experience.setter
    def enable_enhanced_troubleshooting_experience(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableEnhancedTroubleshootingExperience property value. Determines whether the enhanced troubleshooting UX is enabled or not.
        Args:
            value: Value to set for the enableEnhancedTroubleshootingExperience property.
        """
        self._enable_enhanced_troubleshooting_experience = value
    
    @property
    def enable_log_collection(self,) -> Optional[bool]:
        """
        Gets the enableLogCollection property value. Determines whether the log collection feature should be available for use.
        Returns: Optional[bool]
        """
        return self._enable_log_collection
    
    @enable_log_collection.setter
    def enable_log_collection(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableLogCollection property value. Determines whether the log collection feature should be available for use.
        Args:
            value: Value to set for the enableLogCollection property.
        """
        self._enable_log_collection = value
    
    @property
    def enhanced_jail_break(self,) -> Optional[bool]:
        """
        Gets the enhancedJailBreak property value. Is feature enabled or not for enhanced jailbreak detection.
        Returns: Optional[bool]
        """
        return self._enhanced_jail_break
    
    @enhanced_jail_break.setter
    def enhanced_jail_break(self,value: Optional[bool] = None) -> None:
        """
        Sets the enhancedJailBreak property value. Is feature enabled or not for enhanced jailbreak detection.
        Args:
            value: Value to set for the enhancedJailBreak property.
        """
        self._enhanced_jail_break = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_device_administrator_enrollment_enabled": lambda n : setattr(self, 'android_device_administrator_enrollment_enabled', n.get_bool_value()),
            "derived_credential_provider": lambda n : setattr(self, 'derived_credential_provider', n.get_enum_value(derived_credential_provider_type.DerivedCredentialProviderType)),
            "derived_credential_url": lambda n : setattr(self, 'derived_credential_url', n.get_str_value()),
            "device_compliance_checkin_threshold_days": lambda n : setattr(self, 'device_compliance_checkin_threshold_days', n.get_int_value()),
            "device_inactivity_before_retirement_in_day": lambda n : setattr(self, 'device_inactivity_before_retirement_in_day', n.get_int_value()),
            "enable_autopilot_diagnostics": lambda n : setattr(self, 'enable_autopilot_diagnostics', n.get_bool_value()),
            "enable_device_group_membership_report": lambda n : setattr(self, 'enable_device_group_membership_report', n.get_bool_value()),
            "enable_enhanced_troubleshooting_experience": lambda n : setattr(self, 'enable_enhanced_troubleshooting_experience', n.get_bool_value()),
            "enable_log_collection": lambda n : setattr(self, 'enable_log_collection', n.get_bool_value()),
            "enhanced_jail_break": lambda n : setattr(self, 'enhanced_jail_break', n.get_bool_value()),
            "ignore_devices_for_unsupported_settings_enabled": lambda n : setattr(self, 'ignore_devices_for_unsupported_settings_enabled', n.get_bool_value()),
            "is_scheduled_action_enabled": lambda n : setattr(self, 'is_scheduled_action_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secure_by_default": lambda n : setattr(self, 'secure_by_default', n.get_bool_value()),
        }
        return fields
    
    @property
    def ignore_devices_for_unsupported_settings_enabled(self,) -> Optional[bool]:
        """
        Gets the ignoreDevicesForUnsupportedSettingsEnabled property value. The property to determine whether to ignore unsupported compliance settings on certian models of devices.
        Returns: Optional[bool]
        """
        return self._ignore_devices_for_unsupported_settings_enabled
    
    @ignore_devices_for_unsupported_settings_enabled.setter
    def ignore_devices_for_unsupported_settings_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the ignoreDevicesForUnsupportedSettingsEnabled property value. The property to determine whether to ignore unsupported compliance settings on certian models of devices.
        Args:
            value: Value to set for the ignoreDevicesForUnsupportedSettingsEnabled property.
        """
        self._ignore_devices_for_unsupported_settings_enabled = value
    
    @property
    def is_scheduled_action_enabled(self,) -> Optional[bool]:
        """
        Gets the isScheduledActionEnabled property value. Is feature enabled or not for scheduled action for rule.
        Returns: Optional[bool]
        """
        return self._is_scheduled_action_enabled
    
    @is_scheduled_action_enabled.setter
    def is_scheduled_action_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isScheduledActionEnabled property value. Is feature enabled or not for scheduled action for rule.
        Args:
            value: Value to set for the isScheduledActionEnabled property.
        """
        self._is_scheduled_action_enabled = value
    
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
    
    @property
    def secure_by_default(self,) -> Optional[bool]:
        """
        Gets the secureByDefault property value. Device should be noncompliant when there is no compliance policy targeted when this is true
        Returns: Optional[bool]
        """
        return self._secure_by_default
    
    @secure_by_default.setter
    def secure_by_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureByDefault property value. Device should be noncompliant when there is no compliance policy targeted when this is true
        Args:
            value: Value to set for the secureByDefault property.
        """
        self._secure_by_default = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("androidDeviceAdministratorEnrollmentEnabled", self.android_device_administrator_enrollment_enabled)
        writer.write_enum_value("derivedCredentialProvider", self.derived_credential_provider)
        writer.write_str_value("derivedCredentialUrl", self.derived_credential_url)
        writer.write_int_value("deviceComplianceCheckinThresholdDays", self.device_compliance_checkin_threshold_days)
        writer.write_int_value("deviceInactivityBeforeRetirementInDay", self.device_inactivity_before_retirement_in_day)
        writer.write_bool_value("enableAutopilotDiagnostics", self.enable_autopilot_diagnostics)
        writer.write_bool_value("enableDeviceGroupMembershipReport", self.enable_device_group_membership_report)
        writer.write_bool_value("enableEnhancedTroubleshootingExperience", self.enable_enhanced_troubleshooting_experience)
        writer.write_bool_value("enableLogCollection", self.enable_log_collection)
        writer.write_bool_value("enhancedJailBreak", self.enhanced_jail_break)
        writer.write_bool_value("ignoreDevicesForUnsupportedSettingsEnabled", self.ignore_devices_for_unsupported_settings_enabled)
        writer.write_bool_value("isScheduledActionEnabled", self.is_scheduled_action_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("secureByDefault", self.secure_by_default)
        writer.write_additional_data_value(self.additional_data)
    

