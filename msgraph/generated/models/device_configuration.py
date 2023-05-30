from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_certificate_profile_base, android_custom_configuration, android_device_owner_certificate_profile_base, android_device_owner_derived_credential_authentication_configuration, android_device_owner_enterprise_wi_fi_configuration, android_device_owner_general_device_configuration, android_device_owner_imported_p_f_x_certificate_profile, android_device_owner_pkcs_certificate_profile, android_device_owner_scep_certificate_profile, android_device_owner_trusted_root_certificate, android_device_owner_vpn_configuration, android_device_owner_wi_fi_configuration, android_eas_email_profile_configuration, android_enterprise_wi_fi_configuration, android_for_work_certificate_profile_base, android_for_work_custom_configuration, android_for_work_eas_email_profile_base, android_for_work_enterprise_wi_fi_configuration, android_for_work_general_device_configuration, android_for_work_gmail_eas_configuration, android_for_work_imported_p_f_x_certificate_profile, android_for_work_nine_work_eas_configuration, android_for_work_pkcs_certificate_profile, android_for_work_scep_certificate_profile, android_for_work_trusted_root_certificate, android_for_work_vpn_configuration, android_for_work_wi_fi_configuration, android_general_device_configuration, android_imported_p_f_x_certificate_profile, android_oma_cp_configuration, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, android_vpn_configuration, android_wi_fi_configuration, android_work_profile_certificate_profile_base, android_work_profile_custom_configuration, android_work_profile_eas_email_profile_base, android_work_profile_enterprise_wi_fi_configuration, android_work_profile_general_device_configuration, android_work_profile_gmail_eas_configuration, android_work_profile_nine_work_eas_configuration, android_work_profile_pkcs_certificate_profile, android_work_profile_scep_certificate_profile, android_work_profile_trusted_root_certificate, android_work_profile_vpn_configuration, android_work_profile_wi_fi_configuration, aosp_device_owner_certificate_profile_base, aosp_device_owner_device_configuration, aosp_device_owner_enterprise_wi_fi_configuration, aosp_device_owner_pkcs_certificate_profile, aosp_device_owner_scep_certificate_profile, aosp_device_owner_trusted_root_certificate, aosp_device_owner_wi_fi_configuration, apple_device_features_configuration_base, apple_expedited_checkin_configuration_base, apple_vpn_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_group_assignment, device_configuration_user_overview, device_configuration_user_status, device_management_applicability_rule_device_mode, device_management_applicability_rule_os_edition, device_management_applicability_rule_os_version, eas_email_profile_configuration_base, edition_upgrade_configuration, entity, iosik_ev2_vpn_configuration, ios_certificate_profile, ios_certificate_profile_base, ios_custom_configuration, ios_derived_credential_authentication_configuration, ios_device_features_configuration, ios_eas_email_profile_configuration, ios_education_device_configuration, ios_edu_device_configuration, ios_enterprise_wi_fi_configuration, ios_expedited_checkin_configuration, ios_general_device_configuration, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, ios_trusted_root_certificate, ios_update_configuration, ios_vpn_configuration, ios_wi_fi_configuration, mac_o_s_certificate_profile_base, mac_o_s_custom_app_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_endpoint_protection_configuration, mac_o_s_enterprise_wi_fi_configuration, mac_o_s_extensions_configuration, mac_o_s_general_device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, mac_o_s_software_update_configuration, mac_o_s_trusted_root_certificate, mac_o_s_vpn_configuration, mac_o_s_wired_network_configuration, mac_o_s_wi_fi_configuration, setting_state_device_summary, shared_p_c_configuration, unsupported_device_configuration, vpn_configuration, windows10_certificate_profile_base, windows10_custom_configuration, windows10_device_firmware_configuration_interface, windows10_eas_email_profile_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_imported_p_f_x_certificate_profile, windows10_network_boundary_configuration, windows10_pkcs_certificate_profile, windows10_p_f_x_import_certificate_profile, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows10_vpn_configuration, windows81_certificate_profile_base, windows81_general_configuration, windows81_s_c_e_p_certificate_profile, windows81_trusted_root_certificate, windows81_vpn_configuration, windows81_wifi_import_configuration, windows_certificate_profile_base, windows_defender_advanced_threat_protection_configuration, windows_delivery_optimization_configuration, windows_domain_join_configuration, windows_health_monitoring_configuration, windows_identity_protection_configuration, windows_kiosk_configuration, windows_phone81_certificate_profile_base, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_phone81_imported_p_f_x_certificate_profile, windows_phone81_s_c_e_p_certificate_profile, windows_phone81_trusted_root_certificate, windows_phone81_vpn_configuration, windows_phone_e_a_s_email_profile_configuration, windows_update_for_business_configuration, windows_vpn_configuration, windows_wifi_configuration, windows_wifi_enterprise_e_a_p_configuration, windows_wired_network_configuration

from . import entity

class DeviceConfiguration(entity.Entity):
    """
    Device Configuration.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfiguration and sets the default values.
        """
        super().__init__()
        # The list of assignments for the device configuration profile.
        self._assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # The device mode applicability rule for this Policy.
        self._device_management_applicability_rule_device_mode: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode] = None
        # The OS edition applicability for this Policy.
        self._device_management_applicability_rule_os_edition: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition] = None
        # The OS version applicability rule for this Policy.
        self._device_management_applicability_rule_os_version: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion] = None
        # Device Configuration Setting State Device Summary
        self._device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
        # Device Configuration devices status overview
        self._device_status_overview: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None
        # Device configuration installation status by device.
        self._device_statuses: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # The list of group assignments for the device configuration profile.
        self._group_assignments: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        self._supports_scope_tags: Optional[bool] = None
        # Device Configuration users status overview
        self._user_status_overview: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None
        # Device configuration installation status by user.
        self._user_statuses: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None
        # Version of the device configuration.
        self._version: Optional[int] = None
    
    @property
    def assignments(self,) -> Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of assignments for the device configuration profile.
        Returns: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for the device configuration profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidCertificateProfileBase":
                from . import android_certificate_profile_base

                return android_certificate_profile_base.AndroidCertificateProfileBase()
            if mapping_value == "#microsoft.graph.androidCustomConfiguration":
                from . import android_custom_configuration

                return android_custom_configuration.AndroidCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerCertificateProfileBase":
                from . import android_device_owner_certificate_profile_base

                return android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration":
                from . import android_device_owner_derived_credential_authentication_configuration

                return android_device_owner_derived_credential_authentication_configuration.AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration":
                from . import android_device_owner_enterprise_wi_fi_configuration

                return android_device_owner_enterprise_wi_fi_configuration.AndroidDeviceOwnerEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration":
                from . import android_device_owner_general_device_configuration

                return android_device_owner_general_device_configuration.AndroidDeviceOwnerGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile":
                from . import android_device_owner_imported_p_f_x_certificate_profile

                return android_device_owner_imported_p_f_x_certificate_profile.AndroidDeviceOwnerImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile":
                from . import android_device_owner_pkcs_certificate_profile

                return android_device_owner_pkcs_certificate_profile.AndroidDeviceOwnerPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile":
                from . import android_device_owner_scep_certificate_profile

                return android_device_owner_scep_certificate_profile.AndroidDeviceOwnerScepCertificateProfile()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate":
                from . import android_device_owner_trusted_root_certificate

                return android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerVpnConfiguration":
                from . import android_device_owner_vpn_configuration

                return android_device_owner_vpn_configuration.AndroidDeviceOwnerVpnConfiguration()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerWiFiConfiguration":
                from . import android_device_owner_wi_fi_configuration

                return android_device_owner_wi_fi_configuration.AndroidDeviceOwnerWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidEasEmailProfileConfiguration":
                from . import android_eas_email_profile_configuration

                return android_eas_email_profile_configuration.AndroidEasEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.androidEnterpriseWiFiConfiguration":
                from . import android_enterprise_wi_fi_configuration

                return android_enterprise_wi_fi_configuration.AndroidEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkCertificateProfileBase":
                from . import android_for_work_certificate_profile_base

                return android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase()
            if mapping_value == "#microsoft.graph.androidForWorkCustomConfiguration":
                from . import android_for_work_custom_configuration

                return android_for_work_custom_configuration.AndroidForWorkCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkEasEmailProfileBase":
                from . import android_for_work_eas_email_profile_base

                return android_for_work_eas_email_profile_base.AndroidForWorkEasEmailProfileBase()
            if mapping_value == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration":
                from . import android_for_work_enterprise_wi_fi_configuration

                return android_for_work_enterprise_wi_fi_configuration.AndroidForWorkEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration":
                from . import android_for_work_general_device_configuration

                return android_for_work_general_device_configuration.AndroidForWorkGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkGmailEasConfiguration":
                from . import android_for_work_gmail_eas_configuration

                return android_for_work_gmail_eas_configuration.AndroidForWorkGmailEasConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile":
                from . import android_for_work_imported_p_f_x_certificate_profile

                return android_for_work_imported_p_f_x_certificate_profile.AndroidForWorkImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.androidForWorkNineWorkEasConfiguration":
                from . import android_for_work_nine_work_eas_configuration

                return android_for_work_nine_work_eas_configuration.AndroidForWorkNineWorkEasConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkPkcsCertificateProfile":
                from . import android_for_work_pkcs_certificate_profile

                return android_for_work_pkcs_certificate_profile.AndroidForWorkPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.androidForWorkScepCertificateProfile":
                from . import android_for_work_scep_certificate_profile

                return android_for_work_scep_certificate_profile.AndroidForWorkScepCertificateProfile()
            if mapping_value == "#microsoft.graph.androidForWorkTrustedRootCertificate":
                from . import android_for_work_trusted_root_certificate

                return android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.androidForWorkVpnConfiguration":
                from . import android_for_work_vpn_configuration

                return android_for_work_vpn_configuration.AndroidForWorkVpnConfiguration()
            if mapping_value == "#microsoft.graph.androidForWorkWiFiConfiguration":
                from . import android_for_work_wi_fi_configuration

                return android_for_work_wi_fi_configuration.AndroidForWorkWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidGeneralDeviceConfiguration":
                from . import android_general_device_configuration

                return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidImportedPFXCertificateProfile":
                from . import android_imported_p_f_x_certificate_profile

                return android_imported_p_f_x_certificate_profile.AndroidImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.androidOmaCpConfiguration":
                from . import android_oma_cp_configuration

                return android_oma_cp_configuration.AndroidOmaCpConfiguration()
            if mapping_value == "#microsoft.graph.androidPkcsCertificateProfile":
                from . import android_pkcs_certificate_profile

                return android_pkcs_certificate_profile.AndroidPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.androidScepCertificateProfile":
                from . import android_scep_certificate_profile

                return android_scep_certificate_profile.AndroidScepCertificateProfile()
            if mapping_value == "#microsoft.graph.androidTrustedRootCertificate":
                from . import android_trusted_root_certificate

                return android_trusted_root_certificate.AndroidTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.androidVpnConfiguration":
                from . import android_vpn_configuration

                return android_vpn_configuration.AndroidVpnConfiguration()
            if mapping_value == "#microsoft.graph.androidWiFiConfiguration":
                from . import android_wi_fi_configuration

                return android_wi_fi_configuration.AndroidWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileCertificateProfileBase":
                from . import android_work_profile_certificate_profile_base

                return android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase()
            if mapping_value == "#microsoft.graph.androidWorkProfileCustomConfiguration":
                from . import android_work_profile_custom_configuration

                return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileEasEmailProfileBase":
                from . import android_work_profile_eas_email_profile_base

                return android_work_profile_eas_email_profile_base.AndroidWorkProfileEasEmailProfileBase()
            if mapping_value == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration":
                from . import android_work_profile_enterprise_wi_fi_configuration

                return android_work_profile_enterprise_wi_fi_configuration.AndroidWorkProfileEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
                from . import android_work_profile_general_device_configuration

                return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileGmailEasConfiguration":
                from . import android_work_profile_gmail_eas_configuration

                return android_work_profile_gmail_eas_configuration.AndroidWorkProfileGmailEasConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration":
                from . import android_work_profile_nine_work_eas_configuration

                return android_work_profile_nine_work_eas_configuration.AndroidWorkProfileNineWorkEasConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile":
                from . import android_work_profile_pkcs_certificate_profile

                return android_work_profile_pkcs_certificate_profile.AndroidWorkProfilePkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.androidWorkProfileScepCertificateProfile":
                from . import android_work_profile_scep_certificate_profile

                return android_work_profile_scep_certificate_profile.AndroidWorkProfileScepCertificateProfile()
            if mapping_value == "#microsoft.graph.androidWorkProfileTrustedRootCertificate":
                from . import android_work_profile_trusted_root_certificate

                return android_work_profile_trusted_root_certificate.AndroidWorkProfileTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.androidWorkProfileVpnConfiguration":
                from . import android_work_profile_vpn_configuration

                return android_work_profile_vpn_configuration.AndroidWorkProfileVpnConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileWiFiConfiguration":
                from . import android_work_profile_wi_fi_configuration

                return android_work_profile_wi_fi_configuration.AndroidWorkProfileWiFiConfiguration()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerCertificateProfileBase":
                from . import aosp_device_owner_certificate_profile_base

                return aosp_device_owner_certificate_profile_base.AospDeviceOwnerCertificateProfileBase()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration":
                from . import aosp_device_owner_device_configuration

                return aosp_device_owner_device_configuration.AospDeviceOwnerDeviceConfiguration()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration":
                from . import aosp_device_owner_enterprise_wi_fi_configuration

                return aosp_device_owner_enterprise_wi_fi_configuration.AospDeviceOwnerEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile":
                from . import aosp_device_owner_pkcs_certificate_profile

                return aosp_device_owner_pkcs_certificate_profile.AospDeviceOwnerPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile":
                from . import aosp_device_owner_scep_certificate_profile

                return aosp_device_owner_scep_certificate_profile.AospDeviceOwnerScepCertificateProfile()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate":
                from . import aosp_device_owner_trusted_root_certificate

                return aosp_device_owner_trusted_root_certificate.AospDeviceOwnerTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.aospDeviceOwnerWiFiConfiguration":
                from . import aosp_device_owner_wi_fi_configuration

                return aosp_device_owner_wi_fi_configuration.AospDeviceOwnerWiFiConfiguration()
            if mapping_value == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
                from . import apple_device_features_configuration_base

                return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
            if mapping_value == "#microsoft.graph.appleExpeditedCheckinConfigurationBase":
                from . import apple_expedited_checkin_configuration_base

                return apple_expedited_checkin_configuration_base.AppleExpeditedCheckinConfigurationBase()
            if mapping_value == "#microsoft.graph.appleVpnConfiguration":
                from . import apple_vpn_configuration

                return apple_vpn_configuration.AppleVpnConfiguration()
            if mapping_value == "#microsoft.graph.easEmailProfileConfigurationBase":
                from . import eas_email_profile_configuration_base

                return eas_email_profile_configuration_base.EasEmailProfileConfigurationBase()
            if mapping_value == "#microsoft.graph.editionUpgradeConfiguration":
                from . import edition_upgrade_configuration

                return edition_upgrade_configuration.EditionUpgradeConfiguration()
            if mapping_value == "#microsoft.graph.iosCertificateProfile":
                from . import ios_certificate_profile

                return ios_certificate_profile.IosCertificateProfile()
            if mapping_value == "#microsoft.graph.iosCertificateProfileBase":
                from . import ios_certificate_profile_base

                return ios_certificate_profile_base.IosCertificateProfileBase()
            if mapping_value == "#microsoft.graph.iosCustomConfiguration":
                from . import ios_custom_configuration

                return ios_custom_configuration.IosCustomConfiguration()
            if mapping_value == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration":
                from . import ios_derived_credential_authentication_configuration

                return ios_derived_credential_authentication_configuration.IosDerivedCredentialAuthenticationConfiguration()
            if mapping_value == "#microsoft.graph.iosDeviceFeaturesConfiguration":
                from . import ios_device_features_configuration

                return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.iosEasEmailProfileConfiguration":
                from . import ios_eas_email_profile_configuration

                return ios_eas_email_profile_configuration.IosEasEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.iosEducationDeviceConfiguration":
                from . import ios_education_device_configuration

                return ios_education_device_configuration.IosEducationDeviceConfiguration()
            if mapping_value == "#microsoft.graph.iosEduDeviceConfiguration":
                from . import ios_edu_device_configuration

                return ios_edu_device_configuration.IosEduDeviceConfiguration()
            if mapping_value == "#microsoft.graph.iosEnterpriseWiFiConfiguration":
                from . import ios_enterprise_wi_fi_configuration

                return ios_enterprise_wi_fi_configuration.IosEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.iosExpeditedCheckinConfiguration":
                from . import ios_expedited_checkin_configuration

                return ios_expedited_checkin_configuration.IosExpeditedCheckinConfiguration()
            if mapping_value == "#microsoft.graph.iosGeneralDeviceConfiguration":
                from . import ios_general_device_configuration

                return ios_general_device_configuration.IosGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.iosikEv2VpnConfiguration":
                from . import iosik_ev2_vpn_configuration

                return iosik_ev2_vpn_configuration.IosikEv2VpnConfiguration()
            if mapping_value == "#microsoft.graph.iosImportedPFXCertificateProfile":
                from . import ios_imported_p_f_x_certificate_profile

                return ios_imported_p_f_x_certificate_profile.IosImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.iosPkcsCertificateProfile":
                from . import ios_pkcs_certificate_profile

                return ios_pkcs_certificate_profile.IosPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.iosScepCertificateProfile":
                from . import ios_scep_certificate_profile

                return ios_scep_certificate_profile.IosScepCertificateProfile()
            if mapping_value == "#microsoft.graph.iosTrustedRootCertificate":
                from . import ios_trusted_root_certificate

                return ios_trusted_root_certificate.IosTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.iosUpdateConfiguration":
                from . import ios_update_configuration

                return ios_update_configuration.IosUpdateConfiguration()
            if mapping_value == "#microsoft.graph.iosVpnConfiguration":
                from . import ios_vpn_configuration

                return ios_vpn_configuration.IosVpnConfiguration()
            if mapping_value == "#microsoft.graph.iosWiFiConfiguration":
                from . import ios_wi_fi_configuration

                return ios_wi_fi_configuration.IosWiFiConfiguration()
            if mapping_value == "#microsoft.graph.macOSCertificateProfileBase":
                from . import mac_o_s_certificate_profile_base

                return mac_o_s_certificate_profile_base.MacOSCertificateProfileBase()
            if mapping_value == "#microsoft.graph.macOSCustomAppConfiguration":
                from . import mac_o_s_custom_app_configuration

                return mac_o_s_custom_app_configuration.MacOSCustomAppConfiguration()
            if mapping_value == "#microsoft.graph.macOSCustomConfiguration":
                from . import mac_o_s_custom_configuration

                return mac_o_s_custom_configuration.MacOSCustomConfiguration()
            if mapping_value == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
                from . import mac_o_s_device_features_configuration

                return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.macOSEndpointProtectionConfiguration":
                from . import mac_o_s_endpoint_protection_configuration

                return mac_o_s_endpoint_protection_configuration.MacOSEndpointProtectionConfiguration()
            if mapping_value == "#microsoft.graph.macOSEnterpriseWiFiConfiguration":
                from . import mac_o_s_enterprise_wi_fi_configuration

                return mac_o_s_enterprise_wi_fi_configuration.MacOSEnterpriseWiFiConfiguration()
            if mapping_value == "#microsoft.graph.macOSExtensionsConfiguration":
                from . import mac_o_s_extensions_configuration

                return mac_o_s_extensions_configuration.MacOSExtensionsConfiguration()
            if mapping_value == "#microsoft.graph.macOSGeneralDeviceConfiguration":
                from . import mac_o_s_general_device_configuration

                return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.macOSImportedPFXCertificateProfile":
                from . import mac_o_s_imported_p_f_x_certificate_profile

                return mac_o_s_imported_p_f_x_certificate_profile.MacOSImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.macOSPkcsCertificateProfile":
                from . import mac_o_s_pkcs_certificate_profile

                return mac_o_s_pkcs_certificate_profile.MacOSPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.macOSScepCertificateProfile":
                from . import mac_o_s_scep_certificate_profile

                return mac_o_s_scep_certificate_profile.MacOSScepCertificateProfile()
            if mapping_value == "#microsoft.graph.macOSSoftwareUpdateConfiguration":
                from . import mac_o_s_software_update_configuration

                return mac_o_s_software_update_configuration.MacOSSoftwareUpdateConfiguration()
            if mapping_value == "#microsoft.graph.macOSTrustedRootCertificate":
                from . import mac_o_s_trusted_root_certificate

                return mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.macOSVpnConfiguration":
                from . import mac_o_s_vpn_configuration

                return mac_o_s_vpn_configuration.MacOSVpnConfiguration()
            if mapping_value == "#microsoft.graph.macOSWiFiConfiguration":
                from . import mac_o_s_wi_fi_configuration

                return mac_o_s_wi_fi_configuration.MacOSWiFiConfiguration()
            if mapping_value == "#microsoft.graph.macOSWiredNetworkConfiguration":
                from . import mac_o_s_wired_network_configuration

                return mac_o_s_wired_network_configuration.MacOSWiredNetworkConfiguration()
            if mapping_value == "#microsoft.graph.sharedPCConfiguration":
                from . import shared_p_c_configuration

                return shared_p_c_configuration.SharedPCConfiguration()
            if mapping_value == "#microsoft.graph.unsupportedDeviceConfiguration":
                from . import unsupported_device_configuration

                return unsupported_device_configuration.UnsupportedDeviceConfiguration()
            if mapping_value == "#microsoft.graph.vpnConfiguration":
                from . import vpn_configuration

                return vpn_configuration.VpnConfiguration()
            if mapping_value == "#microsoft.graph.windows10CertificateProfileBase":
                from . import windows10_certificate_profile_base

                return windows10_certificate_profile_base.Windows10CertificateProfileBase()
            if mapping_value == "#microsoft.graph.windows10CustomConfiguration":
                from . import windows10_custom_configuration

                return windows10_custom_configuration.Windows10CustomConfiguration()
            if mapping_value == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface":
                from . import windows10_device_firmware_configuration_interface

                return windows10_device_firmware_configuration_interface.Windows10DeviceFirmwareConfigurationInterface()
            if mapping_value == "#microsoft.graph.windows10EasEmailProfileConfiguration":
                from . import windows10_eas_email_profile_configuration

                return windows10_eas_email_profile_configuration.Windows10EasEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.windows10EndpointProtectionConfiguration":
                from . import windows10_endpoint_protection_configuration

                return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
                from . import windows10_enterprise_modern_app_management_configuration

                return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
            if mapping_value == "#microsoft.graph.windows10GeneralConfiguration":
                from . import windows10_general_configuration

                return windows10_general_configuration.Windows10GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows10ImportedPFXCertificateProfile":
                from . import windows10_imported_p_f_x_certificate_profile

                return windows10_imported_p_f_x_certificate_profile.Windows10ImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10NetworkBoundaryConfiguration":
                from . import windows10_network_boundary_configuration

                return windows10_network_boundary_configuration.Windows10NetworkBoundaryConfiguration()
            if mapping_value == "#microsoft.graph.windows10PFXImportCertificateProfile":
                from . import windows10_p_f_x_import_certificate_profile

                return windows10_p_f_x_import_certificate_profile.Windows10PFXImportCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10PkcsCertificateProfile":
                from . import windows10_pkcs_certificate_profile

                return windows10_pkcs_certificate_profile.Windows10PkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10SecureAssessmentConfiguration":
                from . import windows10_secure_assessment_configuration

                return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
            if mapping_value == "#microsoft.graph.windows10TeamGeneralConfiguration":
                from . import windows10_team_general_configuration

                return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows10VpnConfiguration":
                from . import windows10_vpn_configuration

                return windows10_vpn_configuration.Windows10VpnConfiguration()
            if mapping_value == "#microsoft.graph.windows81CertificateProfileBase":
                from . import windows81_certificate_profile_base

                return windows81_certificate_profile_base.Windows81CertificateProfileBase()
            if mapping_value == "#microsoft.graph.windows81GeneralConfiguration":
                from . import windows81_general_configuration

                return windows81_general_configuration.Windows81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows81SCEPCertificateProfile":
                from . import windows81_s_c_e_p_certificate_profile

                return windows81_s_c_e_p_certificate_profile.Windows81SCEPCertificateProfile()
            if mapping_value == "#microsoft.graph.windows81TrustedRootCertificate":
                from . import windows81_trusted_root_certificate

                return windows81_trusted_root_certificate.Windows81TrustedRootCertificate()
            if mapping_value == "#microsoft.graph.windows81VpnConfiguration":
                from . import windows81_vpn_configuration

                return windows81_vpn_configuration.Windows81VpnConfiguration()
            if mapping_value == "#microsoft.graph.windows81WifiImportConfiguration":
                from . import windows81_wifi_import_configuration

                return windows81_wifi_import_configuration.Windows81WifiImportConfiguration()
            if mapping_value == "#microsoft.graph.windowsCertificateProfileBase":
                from . import windows_certificate_profile_base

                return windows_certificate_profile_base.WindowsCertificateProfileBase()
            if mapping_value == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
                from . import windows_defender_advanced_threat_protection_configuration

                return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windowsDeliveryOptimizationConfiguration":
                from . import windows_delivery_optimization_configuration

                return windows_delivery_optimization_configuration.WindowsDeliveryOptimizationConfiguration()
            if mapping_value == "#microsoft.graph.windowsDomainJoinConfiguration":
                from . import windows_domain_join_configuration

                return windows_domain_join_configuration.WindowsDomainJoinConfiguration()
            if mapping_value == "#microsoft.graph.windowsHealthMonitoringConfiguration":
                from . import windows_health_monitoring_configuration

                return windows_health_monitoring_configuration.WindowsHealthMonitoringConfiguration()
            if mapping_value == "#microsoft.graph.windowsIdentityProtectionConfiguration":
                from . import windows_identity_protection_configuration

                return windows_identity_protection_configuration.WindowsIdentityProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windowsKioskConfiguration":
                from . import windows_kiosk_configuration

                return windows_kiosk_configuration.WindowsKioskConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81CertificateProfileBase":
                from . import windows_phone81_certificate_profile_base

                return windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase()
            if mapping_value == "#microsoft.graph.windowsPhone81CustomConfiguration":
                from . import windows_phone81_custom_configuration

                return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81GeneralConfiguration":
                from . import windows_phone81_general_configuration

                return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile":
                from . import windows_phone81_imported_p_f_x_certificate_profile

                return windows_phone81_imported_p_f_x_certificate_profile.WindowsPhone81ImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.windowsPhone81SCEPCertificateProfile":
                from . import windows_phone81_s_c_e_p_certificate_profile

                return windows_phone81_s_c_e_p_certificate_profile.WindowsPhone81SCEPCertificateProfile()
            if mapping_value == "#microsoft.graph.windowsPhone81TrustedRootCertificate":
                from . import windows_phone81_trusted_root_certificate

                return windows_phone81_trusted_root_certificate.WindowsPhone81TrustedRootCertificate()
            if mapping_value == "#microsoft.graph.windowsPhone81VpnConfiguration":
                from . import windows_phone81_vpn_configuration

                return windows_phone81_vpn_configuration.WindowsPhone81VpnConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration":
                from . import windows_phone_e_a_s_email_profile_configuration

                return windows_phone_e_a_s_email_profile_configuration.WindowsPhoneEASEmailProfileConfiguration()
            if mapping_value == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
                from . import windows_update_for_business_configuration

                return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
            if mapping_value == "#microsoft.graph.windowsVpnConfiguration":
                from . import windows_vpn_configuration

                return windows_vpn_configuration.WindowsVpnConfiguration()
            if mapping_value == "#microsoft.graph.windowsWifiConfiguration":
                from . import windows_wifi_configuration

                return windows_wifi_configuration.WindowsWifiConfiguration()
            if mapping_value == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration":
                from . import windows_wifi_enterprise_e_a_p_configuration

                return windows_wifi_enterprise_e_a_p_configuration.WindowsWifiEnterpriseEAPConfiguration()
            if mapping_value == "#microsoft.graph.windowsWiredNetworkConfiguration":
                from . import windows_wired_network_configuration

                return windows_wired_network_configuration.WindowsWiredNetworkConfiguration()
        return DeviceConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the Device Configuration.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the Device Configuration.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_management_applicability_rule_device_mode(self,) -> Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode]:
        """
        Gets the deviceManagementApplicabilityRuleDeviceMode property value. The device mode applicability rule for this Policy.
        Returns: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode]
        """
        return self._device_management_applicability_rule_device_mode
    
    @device_management_applicability_rule_device_mode.setter
    def device_management_applicability_rule_device_mode(self,value: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleDeviceMode property value. The device mode applicability rule for this Policy.
        Args:
            value: Value to set for the device_management_applicability_rule_device_mode property.
        """
        self._device_management_applicability_rule_device_mode = value
    
    @property
    def device_management_applicability_rule_os_edition(self,) -> Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition]:
        """
        Gets the deviceManagementApplicabilityRuleOsEdition property value. The OS edition applicability for this Policy.
        Returns: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition]
        """
        return self._device_management_applicability_rule_os_edition
    
    @device_management_applicability_rule_os_edition.setter
    def device_management_applicability_rule_os_edition(self,value: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleOsEdition property value. The OS edition applicability for this Policy.
        Args:
            value: Value to set for the device_management_applicability_rule_os_edition property.
        """
        self._device_management_applicability_rule_os_edition = value
    
    @property
    def device_management_applicability_rule_os_version(self,) -> Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion]:
        """
        Gets the deviceManagementApplicabilityRuleOsVersion property value. The OS version applicability rule for this Policy.
        Returns: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion]
        """
        return self._device_management_applicability_rule_os_version
    
    @device_management_applicability_rule_os_version.setter
    def device_management_applicability_rule_os_version(self,value: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion] = None) -> None:
        """
        Sets the deviceManagementApplicabilityRuleOsVersion property value. The OS version applicability rule for this Policy.
        Args:
            value: Value to set for the device_management_applicability_rule_os_version property.
        """
        self._device_management_applicability_rule_os_version = value
    
    @property
    def device_setting_state_summaries(self,) -> Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]:
        """
        Gets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Returns: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]
        """
        return self._device_setting_state_summaries
    
    @device_setting_state_summaries.setter
    def device_setting_state_summaries(self,value: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None) -> None:
        """
        Sets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Args:
            value: Value to set for the device_setting_state_summaries property.
        """
        self._device_setting_state_summaries = value
    
    @property
    def device_status_overview(self,) -> Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]:
        """
        Gets the deviceStatusOverview property value. Device Configuration devices status overview
        Returns: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]
        """
        return self._device_status_overview
    
    @device_status_overview.setter
    def device_status_overview(self,value: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None) -> None:
        """
        Sets the deviceStatusOverview property value. Device Configuration devices status overview
        Args:
            value: Value to set for the device_status_overview property.
        """
        self._device_status_overview = value
    
    @property
    def device_statuses(self,) -> Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]:
        """
        Gets the deviceStatuses property value. Device configuration installation status by device.
        Returns: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. Device configuration installation status by device.
        Args:
            value: Value to set for the device_statuses property.
        """
        self._device_statuses = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_certificate_profile_base, android_custom_configuration, android_device_owner_certificate_profile_base, android_device_owner_derived_credential_authentication_configuration, android_device_owner_enterprise_wi_fi_configuration, android_device_owner_general_device_configuration, android_device_owner_imported_p_f_x_certificate_profile, android_device_owner_pkcs_certificate_profile, android_device_owner_scep_certificate_profile, android_device_owner_trusted_root_certificate, android_device_owner_vpn_configuration, android_device_owner_wi_fi_configuration, android_eas_email_profile_configuration, android_enterprise_wi_fi_configuration, android_for_work_certificate_profile_base, android_for_work_custom_configuration, android_for_work_eas_email_profile_base, android_for_work_enterprise_wi_fi_configuration, android_for_work_general_device_configuration, android_for_work_gmail_eas_configuration, android_for_work_imported_p_f_x_certificate_profile, android_for_work_nine_work_eas_configuration, android_for_work_pkcs_certificate_profile, android_for_work_scep_certificate_profile, android_for_work_trusted_root_certificate, android_for_work_vpn_configuration, android_for_work_wi_fi_configuration, android_general_device_configuration, android_imported_p_f_x_certificate_profile, android_oma_cp_configuration, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, android_vpn_configuration, android_wi_fi_configuration, android_work_profile_certificate_profile_base, android_work_profile_custom_configuration, android_work_profile_eas_email_profile_base, android_work_profile_enterprise_wi_fi_configuration, android_work_profile_general_device_configuration, android_work_profile_gmail_eas_configuration, android_work_profile_nine_work_eas_configuration, android_work_profile_pkcs_certificate_profile, android_work_profile_scep_certificate_profile, android_work_profile_trusted_root_certificate, android_work_profile_vpn_configuration, android_work_profile_wi_fi_configuration, aosp_device_owner_certificate_profile_base, aosp_device_owner_device_configuration, aosp_device_owner_enterprise_wi_fi_configuration, aosp_device_owner_pkcs_certificate_profile, aosp_device_owner_scep_certificate_profile, aosp_device_owner_trusted_root_certificate, aosp_device_owner_wi_fi_configuration, apple_device_features_configuration_base, apple_expedited_checkin_configuration_base, apple_vpn_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_group_assignment, device_configuration_user_overview, device_configuration_user_status, device_management_applicability_rule_device_mode, device_management_applicability_rule_os_edition, device_management_applicability_rule_os_version, eas_email_profile_configuration_base, edition_upgrade_configuration, entity, iosik_ev2_vpn_configuration, ios_certificate_profile, ios_certificate_profile_base, ios_custom_configuration, ios_derived_credential_authentication_configuration, ios_device_features_configuration, ios_eas_email_profile_configuration, ios_education_device_configuration, ios_edu_device_configuration, ios_enterprise_wi_fi_configuration, ios_expedited_checkin_configuration, ios_general_device_configuration, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, ios_trusted_root_certificate, ios_update_configuration, ios_vpn_configuration, ios_wi_fi_configuration, mac_o_s_certificate_profile_base, mac_o_s_custom_app_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_endpoint_protection_configuration, mac_o_s_enterprise_wi_fi_configuration, mac_o_s_extensions_configuration, mac_o_s_general_device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, mac_o_s_software_update_configuration, mac_o_s_trusted_root_certificate, mac_o_s_vpn_configuration, mac_o_s_wired_network_configuration, mac_o_s_wi_fi_configuration, setting_state_device_summary, shared_p_c_configuration, unsupported_device_configuration, vpn_configuration, windows10_certificate_profile_base, windows10_custom_configuration, windows10_device_firmware_configuration_interface, windows10_eas_email_profile_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_imported_p_f_x_certificate_profile, windows10_network_boundary_configuration, windows10_pkcs_certificate_profile, windows10_p_f_x_import_certificate_profile, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows10_vpn_configuration, windows81_certificate_profile_base, windows81_general_configuration, windows81_s_c_e_p_certificate_profile, windows81_trusted_root_certificate, windows81_vpn_configuration, windows81_wifi_import_configuration, windows_certificate_profile_base, windows_defender_advanced_threat_protection_configuration, windows_delivery_optimization_configuration, windows_domain_join_configuration, windows_health_monitoring_configuration, windows_identity_protection_configuration, windows_kiosk_configuration, windows_phone81_certificate_profile_base, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_phone81_imported_p_f_x_certificate_profile, windows_phone81_s_c_e_p_certificate_profile, windows_phone81_trusted_root_certificate, windows_phone81_vpn_configuration, windows_phone_e_a_s_email_profile_configuration, windows_update_for_business_configuration, windows_vpn_configuration, windows_wifi_configuration, windows_wifi_enterprise_e_a_p_configuration, windows_wired_network_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceManagementApplicabilityRuleDeviceMode": lambda n : setattr(self, 'device_management_applicability_rule_device_mode', n.get_object_value(device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode)),
            "deviceManagementApplicabilityRuleOsEdition": lambda n : setattr(self, 'device_management_applicability_rule_os_edition', n.get_object_value(device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition)),
            "deviceManagementApplicabilityRuleOsVersion": lambda n : setattr(self, 'device_management_applicability_rule_os_version', n.get_object_value(device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion)),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_configuration_device_status.DeviceConfigurationDeviceStatus)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_configuration_device_overview.DeviceConfigurationDeviceOverview)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(device_configuration_group_assignment.DeviceConfigurationGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supportsScopeTags": lambda n : setattr(self, 'supports_scope_tags', n.get_bool_value()),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_configuration_user_status.DeviceConfigurationUserStatus)),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_configuration_user_overview.DeviceConfigurationUserOverview)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_assignments(self,) -> Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]:
        """
        Gets the groupAssignments property value. The list of group assignments for the device configuration profile.
        Returns: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]
        """
        return self._group_assignments
    
    @group_assignments.setter
    def group_assignments(self,value: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None) -> None:
        """
        Sets the groupAssignments property value. The list of group assignments for the device configuration profile.
        Args:
            value: Value to set for the group_assignments property.
        """
        self._group_assignments = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the role_scope_tag_ids property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("deviceManagementApplicabilityRuleDeviceMode", self.device_management_applicability_rule_device_mode)
        writer.write_object_value("deviceManagementApplicabilityRuleOsEdition", self.device_management_applicability_rule_os_edition)
        writer.write_object_value("deviceManagementApplicabilityRuleOsVersion", self.device_management_applicability_rule_os_version)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_int_value("version", self.version)
    
    @property
    def supports_scope_tags(self,) -> Optional[bool]:
        """
        Gets the supportsScopeTags property value. Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        Returns: Optional[bool]
        """
        return self._supports_scope_tags
    
    @supports_scope_tags.setter
    def supports_scope_tags(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsScopeTags property value. Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
        Args:
            value: Value to set for the supports_scope_tags property.
        """
        self._supports_scope_tags = value
    
    @property
    def user_status_overview(self,) -> Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]:
        """
        Gets the userStatusOverview property value. Device Configuration users status overview
        Returns: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]
        """
        return self._user_status_overview
    
    @user_status_overview.setter
    def user_status_overview(self,value: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None) -> None:
        """
        Sets the userStatusOverview property value. Device Configuration users status overview
        Args:
            value: Value to set for the user_status_overview property.
        """
        self._user_status_overview = value
    
    @property
    def user_statuses(self,) -> Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]:
        """
        Gets the userStatuses property value. Device configuration installation status by user.
        Returns: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. Device configuration installation status by user.
        Args:
            value: Value to set for the user_statuses property.
        """
        self._user_statuses = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the device configuration.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the device configuration.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

