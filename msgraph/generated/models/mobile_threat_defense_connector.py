from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mobile_threat_partner_tenant_state = lazy_import('msgraph.generated.models.mobile_threat_partner_tenant_state')

class MobileThreatDefenseConnector(entity.Entity):
    """
    Entity which represents a connection to Mobile threat defense partner.
    """
    @property
    def allow_partner_to_collect_i_o_s_application_metadata(self,) -> Optional[bool]:
        """
        Gets the allowPartnerToCollectIOSApplicationMetadata property value. For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about installed applications from Intune
        Returns: Optional[bool]
        """
        return self._allow_partner_to_collect_i_o_s_application_metadata
    
    @allow_partner_to_collect_i_o_s_application_metadata.setter
    def allow_partner_to_collect_i_o_s_application_metadata(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPartnerToCollectIOSApplicationMetadata property value. For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about installed applications from Intune
        Args:
            value: Value to set for the allowPartnerToCollectIOSApplicationMetadata property.
        """
        self._allow_partner_to_collect_i_o_s_application_metadata = value
    
    @property
    def allow_partner_to_collect_i_o_s_personal_application_metadata(self,) -> Optional[bool]:
        """
        Gets the allowPartnerToCollectIOSPersonalApplicationMetadata property value. For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about personally installed applications from Intune
        Returns: Optional[bool]
        """
        return self._allow_partner_to_collect_i_o_s_personal_application_metadata
    
    @allow_partner_to_collect_i_o_s_personal_application_metadata.setter
    def allow_partner_to_collect_i_o_s_personal_application_metadata(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPartnerToCollectIOSPersonalApplicationMetadata property value. For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about personally installed applications from Intune
        Args:
            value: Value to set for the allowPartnerToCollectIOSPersonalApplicationMetadata property.
        """
        self._allow_partner_to_collect_i_o_s_personal_application_metadata = value
    
    @property
    def android_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the androidDeviceBlockedOnMissingPartnerData property value. For Android, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._android_device_blocked_on_missing_partner_data
    
    @android_device_blocked_on_missing_partner_data.setter
    def android_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidDeviceBlockedOnMissingPartnerData property value. For Android, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Args:
            value: Value to set for the androidDeviceBlockedOnMissingPartnerData property.
        """
        self._android_device_blocked_on_missing_partner_data = value
    
    @property
    def android_enabled(self,) -> Optional[bool]:
        """
        Gets the androidEnabled property value. For Android, set whether data from the data sync partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._android_enabled
    
    @android_enabled.setter
    def android_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidEnabled property value. For Android, set whether data from the data sync partner should be used during compliance evaluations
        Args:
            value: Value to set for the androidEnabled property.
        """
        self._android_enabled = value
    
    @property
    def android_mobile_application_management_enabled(self,) -> Optional[bool]:
        """
        Gets the androidMobileApplicationManagementEnabled property value. For Android, set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        Returns: Optional[bool]
        """
        return self._android_mobile_application_management_enabled
    
    @android_mobile_application_management_enabled.setter
    def android_mobile_application_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidMobileApplicationManagementEnabled property value. For Android, set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        Args:
            value: Value to set for the androidMobileApplicationManagementEnabled property.
        """
        self._android_mobile_application_management_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mobileThreatDefenseConnector and sets the default values.
        """
        super().__init__()
        # For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about installed applications from Intune
        self._allow_partner_to_collect_i_o_s_application_metadata: Optional[bool] = None
        # For IOS devices, allows the admin to configure whether the data sync partner may also collect metadata about personally installed applications from Intune
        self._allow_partner_to_collect_i_o_s_personal_application_metadata: Optional[bool] = None
        # For Android, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        self._android_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For Android, set whether data from the data sync partner should be used during compliance evaluations
        self._android_enabled: Optional[bool] = None
        # For Android, set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        self._android_mobile_application_management_enabled: Optional[bool] = None
        # For IOS, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        self._ios_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For IOS, get or set whether data from the data sync partner should be used during compliance evaluations
        self._ios_enabled: Optional[bool] = None
        # For IOS, get or set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        self._ios_mobile_application_management_enabled: Optional[bool] = None
        # DateTime of last Heartbeat recieved from the Data Sync Partner
        self._last_heartbeat_date_time: Optional[datetime] = None
        # For Mac, get or set whether Intune must receive data from the data sync partner prior to marking a device compliant
        self._mac_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For Mac, get or set whether data from the data sync partner should be used during compliance evaluations
        self._mac_enabled: Optional[bool] = None
        # When TRUE, configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, configuration profile management via Microsoft Defender for Endpoint is disabled.
        self._microsoft_defender_for_endpoint_attach_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Partner state of this tenant.
        self._partner_state: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState] = None
        # Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        self._partner_unresponsiveness_threshold_in_days: Optional[int] = None
        # Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Data Sync Partner
        self._partner_unsupported_os_version_blocked: Optional[bool] = None
        # For Windows, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        self._windows_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For Windows, get or set whether data from the data sync partner should be used during compliance evaluations
        self._windows_enabled: Optional[bool] = None
        # When TRUE, app protection policies using the Device Threat Level rule will evaluate devices including data from this connector for Windows. When FALSE, Intune will not use device risk details sent over this connector during app protection policies calculation for policies with a Device Threat Level configured. Existing devices that are not compliant due to risk levels obtained from this connector will also become compliant.
        self._windows_mobile_application_management_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileThreatDefenseConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileThreatDefenseConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileThreatDefenseConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_partner_to_collect_i_o_s_application_metadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_application_metadata', n.get_bool_value()),
            "allow_partner_to_collect_i_o_s_personal_application_metadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_personal_application_metadata', n.get_bool_value()),
            "android_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'android_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "android_enabled": lambda n : setattr(self, 'android_enabled', n.get_bool_value()),
            "android_mobile_application_management_enabled": lambda n : setattr(self, 'android_mobile_application_management_enabled', n.get_bool_value()),
            "ios_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'ios_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "ios_enabled": lambda n : setattr(self, 'ios_enabled', n.get_bool_value()),
            "ios_mobile_application_management_enabled": lambda n : setattr(self, 'ios_mobile_application_management_enabled', n.get_bool_value()),
            "last_heartbeat_date_time": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "mac_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'mac_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "mac_enabled": lambda n : setattr(self, 'mac_enabled', n.get_bool_value()),
            "microsoft_defender_for_endpoint_attach_enabled": lambda n : setattr(self, 'microsoft_defender_for_endpoint_attach_enabled', n.get_bool_value()),
            "partner_state": lambda n : setattr(self, 'partner_state', n.get_enum_value(mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState)),
            "partner_unresponsiveness_threshold_in_days": lambda n : setattr(self, 'partner_unresponsiveness_threshold_in_days', n.get_int_value()),
            "partner_unsupported_os_version_blocked": lambda n : setattr(self, 'partner_unsupported_os_version_blocked', n.get_bool_value()),
            "windows_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'windows_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "windows_enabled": lambda n : setattr(self, 'windows_enabled', n.get_bool_value()),
            "windows_mobile_application_management_enabled": lambda n : setattr(self, 'windows_mobile_application_management_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the iosDeviceBlockedOnMissingPartnerData property value. For IOS, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._ios_device_blocked_on_missing_partner_data
    
    @ios_device_blocked_on_missing_partner_data.setter
    def ios_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosDeviceBlockedOnMissingPartnerData property value. For IOS, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Args:
            value: Value to set for the iosDeviceBlockedOnMissingPartnerData property.
        """
        self._ios_device_blocked_on_missing_partner_data = value
    
    @property
    def ios_enabled(self,) -> Optional[bool]:
        """
        Gets the iosEnabled property value. For IOS, get or set whether data from the data sync partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._ios_enabled
    
    @ios_enabled.setter
    def ios_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosEnabled property value. For IOS, get or set whether data from the data sync partner should be used during compliance evaluations
        Args:
            value: Value to set for the iosEnabled property.
        """
        self._ios_enabled = value
    
    @property
    def ios_mobile_application_management_enabled(self,) -> Optional[bool]:
        """
        Gets the iosMobileApplicationManagementEnabled property value. For IOS, get or set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        Returns: Optional[bool]
        """
        return self._ios_mobile_application_management_enabled
    
    @ios_mobile_application_management_enabled.setter
    def ios_mobile_application_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosMobileApplicationManagementEnabled property value. For IOS, get or set whether data from the data sync partner should be used during Mobile Application Management (MAM) evaluations. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation.
        Args:
            value: Value to set for the iosMobileApplicationManagementEnabled property.
        """
        self._ios_mobile_application_management_enabled = value
    
    @property
    def last_heartbeat_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastHeartbeatDateTime property value. DateTime of last Heartbeat recieved from the Data Sync Partner
        Returns: Optional[datetime]
        """
        return self._last_heartbeat_date_time
    
    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastHeartbeatDateTime property value. DateTime of last Heartbeat recieved from the Data Sync Partner
        Args:
            value: Value to set for the lastHeartbeatDateTime property.
        """
        self._last_heartbeat_date_time = value
    
    @property
    def mac_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the macDeviceBlockedOnMissingPartnerData property value. For Mac, get or set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._mac_device_blocked_on_missing_partner_data
    
    @mac_device_blocked_on_missing_partner_data.setter
    def mac_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the macDeviceBlockedOnMissingPartnerData property value. For Mac, get or set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Args:
            value: Value to set for the macDeviceBlockedOnMissingPartnerData property.
        """
        self._mac_device_blocked_on_missing_partner_data = value
    
    @property
    def mac_enabled(self,) -> Optional[bool]:
        """
        Gets the macEnabled property value. For Mac, get or set whether data from the data sync partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._mac_enabled
    
    @mac_enabled.setter
    def mac_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the macEnabled property value. For Mac, get or set whether data from the data sync partner should be used during compliance evaluations
        Args:
            value: Value to set for the macEnabled property.
        """
        self._mac_enabled = value
    
    @property
    def microsoft_defender_for_endpoint_attach_enabled(self,) -> Optional[bool]:
        """
        Gets the microsoftDefenderForEndpointAttachEnabled property value. When TRUE, configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, configuration profile management via Microsoft Defender for Endpoint is disabled.
        Returns: Optional[bool]
        """
        return self._microsoft_defender_for_endpoint_attach_enabled
    
    @microsoft_defender_for_endpoint_attach_enabled.setter
    def microsoft_defender_for_endpoint_attach_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftDefenderForEndpointAttachEnabled property value. When TRUE, configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, configuration profile management via Microsoft Defender for Endpoint is disabled.
        Args:
            value: Value to set for the microsoftDefenderForEndpointAttachEnabled property.
        """
        self._microsoft_defender_for_endpoint_attach_enabled = value
    
    @property
    def partner_state(self,) -> Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState]:
        """
        Gets the partnerState property value. Partner state of this tenant.
        Returns: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState]
        """
        return self._partner_state
    
    @partner_state.setter
    def partner_state(self,value: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState] = None) -> None:
        """
        Sets the partnerState property value. Partner state of this tenant.
        Args:
            value: Value to set for the partnerState property.
        """
        self._partner_state = value
    
    @property
    def partner_unresponsiveness_threshold_in_days(self,) -> Optional[int]:
        """
        Gets the partnerUnresponsivenessThresholdInDays property value. Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        Returns: Optional[int]
        """
        return self._partner_unresponsiveness_threshold_in_days
    
    @partner_unresponsiveness_threshold_in_days.setter
    def partner_unresponsiveness_threshold_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the partnerUnresponsivenessThresholdInDays property value. Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        Args:
            value: Value to set for the partnerUnresponsivenessThresholdInDays property.
        """
        self._partner_unresponsiveness_threshold_in_days = value
    
    @property
    def partner_unsupported_os_version_blocked(self,) -> Optional[bool]:
        """
        Gets the partnerUnsupportedOsVersionBlocked property value. Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Data Sync Partner
        Returns: Optional[bool]
        """
        return self._partner_unsupported_os_version_blocked
    
    @partner_unsupported_os_version_blocked.setter
    def partner_unsupported_os_version_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the partnerUnsupportedOsVersionBlocked property value. Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Data Sync Partner
        Args:
            value: Value to set for the partnerUnsupportedOsVersionBlocked property.
        """
        self._partner_unsupported_os_version_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowPartnerToCollectIOSApplicationMetadata", self.allow_partner_to_collect_i_o_s_application_metadata)
        writer.write_bool_value("allowPartnerToCollectIOSPersonalApplicationMetadata", self.allow_partner_to_collect_i_o_s_personal_application_metadata)
        writer.write_bool_value("androidDeviceBlockedOnMissingPartnerData", self.android_device_blocked_on_missing_partner_data)
        writer.write_bool_value("androidEnabled", self.android_enabled)
        writer.write_bool_value("androidMobileApplicationManagementEnabled", self.android_mobile_application_management_enabled)
        writer.write_bool_value("iosDeviceBlockedOnMissingPartnerData", self.ios_device_blocked_on_missing_partner_data)
        writer.write_bool_value("iosEnabled", self.ios_enabled)
        writer.write_bool_value("iosMobileApplicationManagementEnabled", self.ios_mobile_application_management_enabled)
        writer.write_datetime_value("lastHeartbeatDateTime", self.last_heartbeat_date_time)
        writer.write_bool_value("macDeviceBlockedOnMissingPartnerData", self.mac_device_blocked_on_missing_partner_data)
        writer.write_bool_value("macEnabled", self.mac_enabled)
        writer.write_bool_value("microsoftDefenderForEndpointAttachEnabled", self.microsoft_defender_for_endpoint_attach_enabled)
        writer.write_enum_value("partnerState", self.partner_state)
        writer.write_int_value("partnerUnresponsivenessThresholdInDays", self.partner_unresponsiveness_threshold_in_days)
        writer.write_bool_value("partnerUnsupportedOsVersionBlocked", self.partner_unsupported_os_version_blocked)
        writer.write_bool_value("windowsDeviceBlockedOnMissingPartnerData", self.windows_device_blocked_on_missing_partner_data)
        writer.write_bool_value("windowsEnabled", self.windows_enabled)
        writer.write_bool_value("windowsMobileApplicationManagementEnabled", self.windows_mobile_application_management_enabled)
    
    @property
    def windows_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the windowsDeviceBlockedOnMissingPartnerData property value. For Windows, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._windows_device_blocked_on_missing_partner_data
    
    @windows_device_blocked_on_missing_partner_data.setter
    def windows_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsDeviceBlockedOnMissingPartnerData property value. For Windows, set whether Intune must receive data from the data sync partner prior to marking a device compliant
        Args:
            value: Value to set for the windowsDeviceBlockedOnMissingPartnerData property.
        """
        self._windows_device_blocked_on_missing_partner_data = value
    
    @property
    def windows_enabled(self,) -> Optional[bool]:
        """
        Gets the windowsEnabled property value. For Windows, get or set whether data from the data sync partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._windows_enabled
    
    @windows_enabled.setter
    def windows_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsEnabled property value. For Windows, get or set whether data from the data sync partner should be used during compliance evaluations
        Args:
            value: Value to set for the windowsEnabled property.
        """
        self._windows_enabled = value
    
    @property
    def windows_mobile_application_management_enabled(self,) -> Optional[bool]:
        """
        Gets the windowsMobileApplicationManagementEnabled property value. When TRUE, app protection policies using the Device Threat Level rule will evaluate devices including data from this connector for Windows. When FALSE, Intune will not use device risk details sent over this connector during app protection policies calculation for policies with a Device Threat Level configured. Existing devices that are not compliant due to risk levels obtained from this connector will also become compliant.
        Returns: Optional[bool]
        """
        return self._windows_mobile_application_management_enabled
    
    @windows_mobile_application_management_enabled.setter
    def windows_mobile_application_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsMobileApplicationManagementEnabled property value. When TRUE, app protection policies using the Device Threat Level rule will evaluate devices including data from this connector for Windows. When FALSE, Intune will not use device risk details sent over this connector during app protection policies calculation for policies with a Device Threat Level configured. Existing devices that are not compliant due to risk levels obtained from this connector will also become compliant.
        Args:
            value: Value to set for the windowsMobileApplicationManagementEnabled property.
        """
        self._windows_mobile_application_management_enabled = value
    

