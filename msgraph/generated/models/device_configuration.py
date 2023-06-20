from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_certificate_profile_base, android_custom_configuration, android_device_owner_certificate_profile_base, android_device_owner_derived_credential_authentication_configuration, android_device_owner_enterprise_wi_fi_configuration, android_device_owner_general_device_configuration, android_device_owner_imported_p_f_x_certificate_profile, android_device_owner_pkcs_certificate_profile, android_device_owner_scep_certificate_profile, android_device_owner_trusted_root_certificate, android_device_owner_vpn_configuration, android_device_owner_wi_fi_configuration, android_eas_email_profile_configuration, android_enterprise_wi_fi_configuration, android_for_work_certificate_profile_base, android_for_work_custom_configuration, android_for_work_eas_email_profile_base, android_for_work_enterprise_wi_fi_configuration, android_for_work_general_device_configuration, android_for_work_gmail_eas_configuration, android_for_work_imported_p_f_x_certificate_profile, android_for_work_nine_work_eas_configuration, android_for_work_pkcs_certificate_profile, android_for_work_scep_certificate_profile, android_for_work_trusted_root_certificate, android_for_work_vpn_configuration, android_for_work_wi_fi_configuration, android_general_device_configuration, android_imported_p_f_x_certificate_profile, android_oma_cp_configuration, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, android_vpn_configuration, android_wi_fi_configuration, android_work_profile_certificate_profile_base, android_work_profile_custom_configuration, android_work_profile_eas_email_profile_base, android_work_profile_enterprise_wi_fi_configuration, android_work_profile_general_device_configuration, android_work_profile_gmail_eas_configuration, android_work_profile_nine_work_eas_configuration, android_work_profile_pkcs_certificate_profile, android_work_profile_scep_certificate_profile, android_work_profile_trusted_root_certificate, android_work_profile_vpn_configuration, android_work_profile_wi_fi_configuration, aosp_device_owner_certificate_profile_base, aosp_device_owner_device_configuration, aosp_device_owner_enterprise_wi_fi_configuration, aosp_device_owner_pkcs_certificate_profile, aosp_device_owner_scep_certificate_profile, aosp_device_owner_trusted_root_certificate, aosp_device_owner_wi_fi_configuration, apple_device_features_configuration_base, apple_expedited_checkin_configuration_base, apple_vpn_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_group_assignment, device_configuration_user_overview, device_configuration_user_status, device_management_applicability_rule_device_mode, device_management_applicability_rule_os_edition, device_management_applicability_rule_os_version, eas_email_profile_configuration_base, edition_upgrade_configuration, entity, iosik_ev2_vpn_configuration, ios_certificate_profile, ios_certificate_profile_base, ios_custom_configuration, ios_derived_credential_authentication_configuration, ios_device_features_configuration, ios_eas_email_profile_configuration, ios_education_device_configuration, ios_edu_device_configuration, ios_enterprise_wi_fi_configuration, ios_expedited_checkin_configuration, ios_general_device_configuration, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, ios_trusted_root_certificate, ios_update_configuration, ios_vpn_configuration, ios_wi_fi_configuration, mac_o_s_certificate_profile_base, mac_o_s_custom_app_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_endpoint_protection_configuration, mac_o_s_enterprise_wi_fi_configuration, mac_o_s_extensions_configuration, mac_o_s_general_device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, mac_o_s_software_update_configuration, mac_o_s_trusted_root_certificate, mac_o_s_vpn_configuration, mac_o_s_wired_network_configuration, mac_o_s_wi_fi_configuration, setting_state_device_summary, shared_p_c_configuration, unsupported_device_configuration, vpn_configuration, windows10_certificate_profile_base, windows10_custom_configuration, windows10_device_firmware_configuration_interface, windows10_eas_email_profile_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_imported_p_f_x_certificate_profile, windows10_network_boundary_configuration, windows10_pkcs_certificate_profile, windows10_p_f_x_import_certificate_profile, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows10_vpn_configuration, windows81_certificate_profile_base, windows81_general_configuration, windows81_s_c_e_p_certificate_profile, windows81_trusted_root_certificate, windows81_vpn_configuration, windows81_wifi_import_configuration, windows_certificate_profile_base, windows_defender_advanced_threat_protection_configuration, windows_delivery_optimization_configuration, windows_domain_join_configuration, windows_health_monitoring_configuration, windows_identity_protection_configuration, windows_kiosk_configuration, windows_phone81_certificate_profile_base, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_phone81_imported_p_f_x_certificate_profile, windows_phone81_s_c_e_p_certificate_profile, windows_phone81_trusted_root_certificate, windows_phone81_vpn_configuration, windows_phone_e_a_s_email_profile_configuration, windows_update_for_business_configuration, windows_vpn_configuration, windows_wifi_configuration, windows_wifi_enterprise_e_a_p_configuration, windows_wired_network_configuration

from . import entity

@dataclass
class DeviceConfiguration(entity.Entity):
    """
    Device Configuration.
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # The device mode applicability rule for this Policy.
    device_management_applicability_rule_device_mode: Optional[device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode] = None
    # The OS edition applicability for this Policy.
    device_management_applicability_rule_os_edition: Optional[device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition] = None
    # The OS version applicability rule for this Policy.
    device_management_applicability_rule_os_version: Optional[device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion] = None
    # Device Configuration Setting State Device Summary
    device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
    # Device Configuration devices status overview
    device_status_overview: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None
    # Device configuration installation status by device.
    device_statuses: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # The list of group assignments for the device configuration profile.
    group_assignments: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
    supports_scope_tags: Optional[bool] = None
    # Device Configuration users status overview
    user_status_overview: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None
    # Device configuration installation status by user.
    user_statuses: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCertificateProfileBase".casefold():
            from . import android_certificate_profile_base

            return android_certificate_profile_base.AndroidCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from . import android_custom_configuration

            return android_custom_configuration.AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerCertificateProfileBase".casefold():
            from . import android_device_owner_certificate_profile_base

            return android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration".casefold():
            from . import android_device_owner_derived_credential_authentication_configuration

            return android_device_owner_derived_credential_authentication_configuration.AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from . import android_device_owner_enterprise_wi_fi_configuration

            return android_device_owner_enterprise_wi_fi_configuration.AndroidDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration".casefold():
            from . import android_device_owner_general_device_configuration

            return android_device_owner_general_device_configuration.AndroidDeviceOwnerGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile".casefold():
            from . import android_device_owner_imported_p_f_x_certificate_profile

            return android_device_owner_imported_p_f_x_certificate_profile.AndroidDeviceOwnerImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile".casefold():
            from . import android_device_owner_pkcs_certificate_profile

            return android_device_owner_pkcs_certificate_profile.AndroidDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile".casefold():
            from . import android_device_owner_scep_certificate_profile

            return android_device_owner_scep_certificate_profile.AndroidDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate".casefold():
            from . import android_device_owner_trusted_root_certificate

            return android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerVpnConfiguration".casefold():
            from . import android_device_owner_vpn_configuration

            return android_device_owner_vpn_configuration.AndroidDeviceOwnerVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerWiFiConfiguration".casefold():
            from . import android_device_owner_wi_fi_configuration

            return android_device_owner_wi_fi_configuration.AndroidDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEasEmailProfileConfiguration".casefold():
            from . import android_eas_email_profile_configuration

            return android_eas_email_profile_configuration.AndroidEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEnterpriseWiFiConfiguration".casefold():
            from . import android_enterprise_wi_fi_configuration

            return android_enterprise_wi_fi_configuration.AndroidEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCertificateProfileBase".casefold():
            from . import android_for_work_certificate_profile_base

            return android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCustomConfiguration".casefold():
            from . import android_for_work_custom_configuration

            return android_for_work_custom_configuration.AndroidForWorkCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEasEmailProfileBase".casefold():
            from . import android_for_work_eas_email_profile_base

            return android_for_work_eas_email_profile_base.AndroidForWorkEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration".casefold():
            from . import android_for_work_enterprise_wi_fi_configuration

            return android_for_work_enterprise_wi_fi_configuration.AndroidForWorkEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration".casefold():
            from . import android_for_work_general_device_configuration

            return android_for_work_general_device_configuration.AndroidForWorkGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGmailEasConfiguration".casefold():
            from . import android_for_work_gmail_eas_configuration

            return android_for_work_gmail_eas_configuration.AndroidForWorkGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile".casefold():
            from . import android_for_work_imported_p_f_x_certificate_profile

            return android_for_work_imported_p_f_x_certificate_profile.AndroidForWorkImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkNineWorkEasConfiguration".casefold():
            from . import android_for_work_nine_work_eas_configuration

            return android_for_work_nine_work_eas_configuration.AndroidForWorkNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkPkcsCertificateProfile".casefold():
            from . import android_for_work_pkcs_certificate_profile

            return android_for_work_pkcs_certificate_profile.AndroidForWorkPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkScepCertificateProfile".casefold():
            from . import android_for_work_scep_certificate_profile

            return android_for_work_scep_certificate_profile.AndroidForWorkScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkTrustedRootCertificate".casefold():
            from . import android_for_work_trusted_root_certificate

            return android_for_work_trusted_root_certificate.AndroidForWorkTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkVpnConfiguration".casefold():
            from . import android_for_work_vpn_configuration

            return android_for_work_vpn_configuration.AndroidForWorkVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkWiFiConfiguration".casefold():
            from . import android_for_work_wi_fi_configuration

            return android_for_work_wi_fi_configuration.AndroidForWorkWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from . import android_general_device_configuration

            return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidImportedPFXCertificateProfile".casefold():
            from . import android_imported_p_f_x_certificate_profile

            return android_imported_p_f_x_certificate_profile.AndroidImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidOmaCpConfiguration".casefold():
            from . import android_oma_cp_configuration

            return android_oma_cp_configuration.AndroidOmaCpConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidPkcsCertificateProfile".casefold():
            from . import android_pkcs_certificate_profile

            return android_pkcs_certificate_profile.AndroidPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidScepCertificateProfile".casefold():
            from . import android_scep_certificate_profile

            return android_scep_certificate_profile.AndroidScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidTrustedRootCertificate".casefold():
            from . import android_trusted_root_certificate

            return android_trusted_root_certificate.AndroidTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidVpnConfiguration".casefold():
            from . import android_vpn_configuration

            return android_vpn_configuration.AndroidVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWiFiConfiguration".casefold():
            from . import android_wi_fi_configuration

            return android_wi_fi_configuration.AndroidWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCertificateProfileBase".casefold():
            from . import android_work_profile_certificate_profile_base

            return android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from . import android_work_profile_custom_configuration

            return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEasEmailProfileBase".casefold():
            from . import android_work_profile_eas_email_profile_base

            return android_work_profile_eas_email_profile_base.AndroidWorkProfileEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration".casefold():
            from . import android_work_profile_enterprise_wi_fi_configuration

            return android_work_profile_enterprise_wi_fi_configuration.AndroidWorkProfileEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from . import android_work_profile_general_device_configuration

            return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGmailEasConfiguration".casefold():
            from . import android_work_profile_gmail_eas_configuration

            return android_work_profile_gmail_eas_configuration.AndroidWorkProfileGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration".casefold():
            from . import android_work_profile_nine_work_eas_configuration

            return android_work_profile_nine_work_eas_configuration.AndroidWorkProfileNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile".casefold():
            from . import android_work_profile_pkcs_certificate_profile

            return android_work_profile_pkcs_certificate_profile.AndroidWorkProfilePkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileScepCertificateProfile".casefold():
            from . import android_work_profile_scep_certificate_profile

            return android_work_profile_scep_certificate_profile.AndroidWorkProfileScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileTrustedRootCertificate".casefold():
            from . import android_work_profile_trusted_root_certificate

            return android_work_profile_trusted_root_certificate.AndroidWorkProfileTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileVpnConfiguration".casefold():
            from . import android_work_profile_vpn_configuration

            return android_work_profile_vpn_configuration.AndroidWorkProfileVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileWiFiConfiguration".casefold():
            from . import android_work_profile_wi_fi_configuration

            return android_work_profile_wi_fi_configuration.AndroidWorkProfileWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerCertificateProfileBase".casefold():
            from . import aosp_device_owner_certificate_profile_base

            return aosp_device_owner_certificate_profile_base.AospDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration".casefold():
            from . import aosp_device_owner_device_configuration

            return aosp_device_owner_device_configuration.AospDeviceOwnerDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from . import aosp_device_owner_enterprise_wi_fi_configuration

            return aosp_device_owner_enterprise_wi_fi_configuration.AospDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile".casefold():
            from . import aosp_device_owner_pkcs_certificate_profile

            return aosp_device_owner_pkcs_certificate_profile.AospDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile".casefold():
            from . import aosp_device_owner_scep_certificate_profile

            return aosp_device_owner_scep_certificate_profile.AospDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate".casefold():
            from . import aosp_device_owner_trusted_root_certificate

            return aosp_device_owner_trusted_root_certificate.AospDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerWiFiConfiguration".casefold():
            from . import aosp_device_owner_wi_fi_configuration

            return aosp_device_owner_wi_fi_configuration.AospDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from . import apple_device_features_configuration_base

            return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleExpeditedCheckinConfigurationBase".casefold():
            from . import apple_expedited_checkin_configuration_base

            return apple_expedited_checkin_configuration_base.AppleExpeditedCheckinConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVpnConfiguration".casefold():
            from . import apple_vpn_configuration

            return apple_vpn_configuration.AppleVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.easEmailProfileConfigurationBase".casefold():
            from . import eas_email_profile_configuration_base

            return eas_email_profile_configuration_base.EasEmailProfileConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from . import edition_upgrade_configuration

            return edition_upgrade_configuration.EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from . import ios_certificate_profile

            return ios_certificate_profile.IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfileBase".casefold():
            from . import ios_certificate_profile_base

            return ios_certificate_profile_base.IosCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from . import ios_custom_configuration

            return ios_custom_configuration.IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration".casefold():
            from . import ios_derived_credential_authentication_configuration

            return ios_derived_credential_authentication_configuration.IosDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from . import ios_device_features_configuration

            return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEasEmailProfileConfiguration".casefold():
            from . import ios_eas_email_profile_configuration

            return ios_eas_email_profile_configuration.IosEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEducationDeviceConfiguration".casefold():
            from . import ios_education_device_configuration

            return ios_education_device_configuration.IosEducationDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEduDeviceConfiguration".casefold():
            from . import ios_edu_device_configuration

            return ios_edu_device_configuration.IosEduDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEnterpriseWiFiConfiguration".casefold():
            from . import ios_enterprise_wi_fi_configuration

            return ios_enterprise_wi_fi_configuration.IosEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosExpeditedCheckinConfiguration".casefold():
            from . import ios_expedited_checkin_configuration

            return ios_expedited_checkin_configuration.IosExpeditedCheckinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from . import ios_general_device_configuration

            return ios_general_device_configuration.IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosikEv2VpnConfiguration".casefold():
            from . import iosik_ev2_vpn_configuration

            return iosik_ev2_vpn_configuration.IosikEv2VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosImportedPFXCertificateProfile".casefold():
            from . import ios_imported_p_f_x_certificate_profile

            return ios_imported_p_f_x_certificate_profile.IosImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from . import ios_pkcs_certificate_profile

            return ios_pkcs_certificate_profile.IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from . import ios_scep_certificate_profile

            return ios_scep_certificate_profile.IosScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosTrustedRootCertificate".casefold():
            from . import ios_trusted_root_certificate

            return ios_trusted_root_certificate.IosTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from . import ios_update_configuration

            return ios_update_configuration.IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVpnConfiguration".casefold():
            from . import ios_vpn_configuration

            return ios_vpn_configuration.IosVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosWiFiConfiguration".casefold():
            from . import ios_wi_fi_configuration

            return ios_wi_fi_configuration.IosWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCertificateProfileBase".casefold():
            from . import mac_o_s_certificate_profile_base

            return mac_o_s_certificate_profile_base.MacOSCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomAppConfiguration".casefold():
            from . import mac_o_s_custom_app_configuration

            return mac_o_s_custom_app_configuration.MacOSCustomAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from . import mac_o_s_custom_configuration

            return mac_o_s_custom_configuration.MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from . import mac_o_s_device_features_configuration

            return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEndpointProtectionConfiguration".casefold():
            from . import mac_o_s_endpoint_protection_configuration

            return mac_o_s_endpoint_protection_configuration.MacOSEndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEnterpriseWiFiConfiguration".casefold():
            from . import mac_o_s_enterprise_wi_fi_configuration

            return mac_o_s_enterprise_wi_fi_configuration.MacOSEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSExtensionsConfiguration".casefold():
            from . import mac_o_s_extensions_configuration

            return mac_o_s_extensions_configuration.MacOSExtensionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from . import mac_o_s_general_device_configuration

            return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSImportedPFXCertificateProfile".casefold():
            from . import mac_o_s_imported_p_f_x_certificate_profile

            return mac_o_s_imported_p_f_x_certificate_profile.MacOSImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkcsCertificateProfile".casefold():
            from . import mac_o_s_pkcs_certificate_profile

            return mac_o_s_pkcs_certificate_profile.MacOSPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSScepCertificateProfile".casefold():
            from . import mac_o_s_scep_certificate_profile

            return mac_o_s_scep_certificate_profile.MacOSScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateConfiguration".casefold():
            from . import mac_o_s_software_update_configuration

            return mac_o_s_software_update_configuration.MacOSSoftwareUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSTrustedRootCertificate".casefold():
            from . import mac_o_s_trusted_root_certificate

            return mac_o_s_trusted_root_certificate.MacOSTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSVpnConfiguration".casefold():
            from . import mac_o_s_vpn_configuration

            return mac_o_s_vpn_configuration.MacOSVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiFiConfiguration".casefold():
            from . import mac_o_s_wi_fi_configuration

            return mac_o_s_wi_fi_configuration.MacOSWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiredNetworkConfiguration".casefold():
            from . import mac_o_s_wired_network_configuration

            return mac_o_s_wired_network_configuration.MacOSWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from . import shared_p_c_configuration

            return shared_p_c_configuration.SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unsupportedDeviceConfiguration".casefold():
            from . import unsupported_device_configuration

            return unsupported_device_configuration.UnsupportedDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vpnConfiguration".casefold():
            from . import vpn_configuration

            return vpn_configuration.VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CertificateProfileBase".casefold():
            from . import windows10_certificate_profile_base

            return windows10_certificate_profile_base.Windows10CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from . import windows10_custom_configuration

            return windows10_custom_configuration.Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface".casefold():
            from . import windows10_device_firmware_configuration_interface

            return windows10_device_firmware_configuration_interface.Windows10DeviceFirmwareConfigurationInterface()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EasEmailProfileConfiguration".casefold():
            from . import windows10_eas_email_profile_configuration

            return windows10_eas_email_profile_configuration.Windows10EasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from . import windows10_endpoint_protection_configuration

            return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from . import windows10_enterprise_modern_app_management_configuration

            return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from . import windows10_general_configuration

            return windows10_general_configuration.Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10ImportedPFXCertificateProfile".casefold():
            from . import windows10_imported_p_f_x_certificate_profile

            return windows10_imported_p_f_x_certificate_profile.Windows10ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10NetworkBoundaryConfiguration".casefold():
            from . import windows10_network_boundary_configuration

            return windows10_network_boundary_configuration.Windows10NetworkBoundaryConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PFXImportCertificateProfile".casefold():
            from . import windows10_p_f_x_import_certificate_profile

            return windows10_p_f_x_import_certificate_profile.Windows10PFXImportCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from . import windows10_pkcs_certificate_profile

            return windows10_pkcs_certificate_profile.Windows10PkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from . import windows10_secure_assessment_configuration

            return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from . import windows10_team_general_configuration

            return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10VpnConfiguration".casefold():
            from . import windows10_vpn_configuration

            return windows10_vpn_configuration.Windows10VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CertificateProfileBase".casefold():
            from . import windows81_certificate_profile_base

            return windows81_certificate_profile_base.Windows81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from . import windows81_general_configuration

            return windows81_general_configuration.Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from . import windows81_s_c_e_p_certificate_profile

            return windows81_s_c_e_p_certificate_profile.Windows81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81TrustedRootCertificate".casefold():
            from . import windows81_trusted_root_certificate

            return windows81_trusted_root_certificate.Windows81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81VpnConfiguration".casefold():
            from . import windows81_vpn_configuration

            return windows81_vpn_configuration.Windows81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81WifiImportConfiguration".casefold():
            from . import windows81_wifi_import_configuration

            return windows81_wifi_import_configuration.Windows81WifiImportConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsCertificateProfileBase".casefold():
            from . import windows_certificate_profile_base

            return windows_certificate_profile_base.WindowsCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from . import windows_defender_advanced_threat_protection_configuration

            return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDeliveryOptimizationConfiguration".casefold():
            from . import windows_delivery_optimization_configuration

            return windows_delivery_optimization_configuration.WindowsDeliveryOptimizationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDomainJoinConfiguration".casefold():
            from . import windows_domain_join_configuration

            return windows_domain_join_configuration.WindowsDomainJoinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHealthMonitoringConfiguration".casefold():
            from . import windows_health_monitoring_configuration

            return windows_health_monitoring_configuration.WindowsHealthMonitoringConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsIdentityProtectionConfiguration".casefold():
            from . import windows_identity_protection_configuration

            return windows_identity_protection_configuration.WindowsIdentityProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskConfiguration".casefold():
            from . import windows_kiosk_configuration

            return windows_kiosk_configuration.WindowsKioskConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CertificateProfileBase".casefold():
            from . import windows_phone81_certificate_profile_base

            return windows_phone81_certificate_profile_base.WindowsPhone81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from . import windows_phone81_custom_configuration

            return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from . import windows_phone81_general_configuration

            return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile".casefold():
            from . import windows_phone81_imported_p_f_x_certificate_profile

            return windows_phone81_imported_p_f_x_certificate_profile.WindowsPhone81ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81SCEPCertificateProfile".casefold():
            from . import windows_phone81_s_c_e_p_certificate_profile

            return windows_phone81_s_c_e_p_certificate_profile.WindowsPhone81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81TrustedRootCertificate".casefold():
            from . import windows_phone81_trusted_root_certificate

            return windows_phone81_trusted_root_certificate.WindowsPhone81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81VpnConfiguration".casefold():
            from . import windows_phone81_vpn_configuration

            return windows_phone81_vpn_configuration.WindowsPhone81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration".casefold():
            from . import windows_phone_e_a_s_email_profile_configuration

            return windows_phone_e_a_s_email_profile_configuration.WindowsPhoneEASEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from . import windows_update_for_business_configuration

            return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsVpnConfiguration".casefold():
            from . import windows_vpn_configuration

            return windows_vpn_configuration.WindowsVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiConfiguration".casefold():
            from . import windows_wifi_configuration

            return windows_wifi_configuration.WindowsWifiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration".casefold():
            from . import windows_wifi_enterprise_e_a_p_configuration

            return windows_wifi_enterprise_e_a_p_configuration.WindowsWifiEnterpriseEAPConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWiredNetworkConfiguration".casefold():
            from . import windows_wired_network_configuration

            return windows_wired_network_configuration.WindowsWiredNetworkConfiguration()
        return DeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_certificate_profile_base, android_custom_configuration, android_device_owner_certificate_profile_base, android_device_owner_derived_credential_authentication_configuration, android_device_owner_enterprise_wi_fi_configuration, android_device_owner_general_device_configuration, android_device_owner_imported_p_f_x_certificate_profile, android_device_owner_pkcs_certificate_profile, android_device_owner_scep_certificate_profile, android_device_owner_trusted_root_certificate, android_device_owner_vpn_configuration, android_device_owner_wi_fi_configuration, android_eas_email_profile_configuration, android_enterprise_wi_fi_configuration, android_for_work_certificate_profile_base, android_for_work_custom_configuration, android_for_work_eas_email_profile_base, android_for_work_enterprise_wi_fi_configuration, android_for_work_general_device_configuration, android_for_work_gmail_eas_configuration, android_for_work_imported_p_f_x_certificate_profile, android_for_work_nine_work_eas_configuration, android_for_work_pkcs_certificate_profile, android_for_work_scep_certificate_profile, android_for_work_trusted_root_certificate, android_for_work_vpn_configuration, android_for_work_wi_fi_configuration, android_general_device_configuration, android_imported_p_f_x_certificate_profile, android_oma_cp_configuration, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, android_vpn_configuration, android_wi_fi_configuration, android_work_profile_certificate_profile_base, android_work_profile_custom_configuration, android_work_profile_eas_email_profile_base, android_work_profile_enterprise_wi_fi_configuration, android_work_profile_general_device_configuration, android_work_profile_gmail_eas_configuration, android_work_profile_nine_work_eas_configuration, android_work_profile_pkcs_certificate_profile, android_work_profile_scep_certificate_profile, android_work_profile_trusted_root_certificate, android_work_profile_vpn_configuration, android_work_profile_wi_fi_configuration, aosp_device_owner_certificate_profile_base, aosp_device_owner_device_configuration, aosp_device_owner_enterprise_wi_fi_configuration, aosp_device_owner_pkcs_certificate_profile, aosp_device_owner_scep_certificate_profile, aosp_device_owner_trusted_root_certificate, aosp_device_owner_wi_fi_configuration, apple_device_features_configuration_base, apple_expedited_checkin_configuration_base, apple_vpn_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_group_assignment, device_configuration_user_overview, device_configuration_user_status, device_management_applicability_rule_device_mode, device_management_applicability_rule_os_edition, device_management_applicability_rule_os_version, eas_email_profile_configuration_base, edition_upgrade_configuration, entity, iosik_ev2_vpn_configuration, ios_certificate_profile, ios_certificate_profile_base, ios_custom_configuration, ios_derived_credential_authentication_configuration, ios_device_features_configuration, ios_eas_email_profile_configuration, ios_education_device_configuration, ios_edu_device_configuration, ios_enterprise_wi_fi_configuration, ios_expedited_checkin_configuration, ios_general_device_configuration, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, ios_trusted_root_certificate, ios_update_configuration, ios_vpn_configuration, ios_wi_fi_configuration, mac_o_s_certificate_profile_base, mac_o_s_custom_app_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_endpoint_protection_configuration, mac_o_s_enterprise_wi_fi_configuration, mac_o_s_extensions_configuration, mac_o_s_general_device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, mac_o_s_software_update_configuration, mac_o_s_trusted_root_certificate, mac_o_s_vpn_configuration, mac_o_s_wired_network_configuration, mac_o_s_wi_fi_configuration, setting_state_device_summary, shared_p_c_configuration, unsupported_device_configuration, vpn_configuration, windows10_certificate_profile_base, windows10_custom_configuration, windows10_device_firmware_configuration_interface, windows10_eas_email_profile_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_imported_p_f_x_certificate_profile, windows10_network_boundary_configuration, windows10_pkcs_certificate_profile, windows10_p_f_x_import_certificate_profile, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows10_vpn_configuration, windows81_certificate_profile_base, windows81_general_configuration, windows81_s_c_e_p_certificate_profile, windows81_trusted_root_certificate, windows81_vpn_configuration, windows81_wifi_import_configuration, windows_certificate_profile_base, windows_defender_advanced_threat_protection_configuration, windows_delivery_optimization_configuration, windows_domain_join_configuration, windows_health_monitoring_configuration, windows_identity_protection_configuration, windows_kiosk_configuration, windows_phone81_certificate_profile_base, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_phone81_imported_p_f_x_certificate_profile, windows_phone81_s_c_e_p_certificate_profile, windows_phone81_trusted_root_certificate, windows_phone81_vpn_configuration, windows_phone_e_a_s_email_profile_configuration, windows_update_for_business_configuration, windows_vpn_configuration, windows_wifi_configuration, windows_wifi_enterprise_e_a_p_configuration, windows_wired_network_configuration

        from . import android_certificate_profile_base, android_custom_configuration, android_device_owner_certificate_profile_base, android_device_owner_derived_credential_authentication_configuration, android_device_owner_enterprise_wi_fi_configuration, android_device_owner_general_device_configuration, android_device_owner_imported_p_f_x_certificate_profile, android_device_owner_pkcs_certificate_profile, android_device_owner_scep_certificate_profile, android_device_owner_trusted_root_certificate, android_device_owner_vpn_configuration, android_device_owner_wi_fi_configuration, android_eas_email_profile_configuration, android_enterprise_wi_fi_configuration, android_for_work_certificate_profile_base, android_for_work_custom_configuration, android_for_work_eas_email_profile_base, android_for_work_enterprise_wi_fi_configuration, android_for_work_general_device_configuration, android_for_work_gmail_eas_configuration, android_for_work_imported_p_f_x_certificate_profile, android_for_work_nine_work_eas_configuration, android_for_work_pkcs_certificate_profile, android_for_work_scep_certificate_profile, android_for_work_trusted_root_certificate, android_for_work_vpn_configuration, android_for_work_wi_fi_configuration, android_general_device_configuration, android_imported_p_f_x_certificate_profile, android_oma_cp_configuration, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, android_vpn_configuration, android_wi_fi_configuration, android_work_profile_certificate_profile_base, android_work_profile_custom_configuration, android_work_profile_eas_email_profile_base, android_work_profile_enterprise_wi_fi_configuration, android_work_profile_general_device_configuration, android_work_profile_gmail_eas_configuration, android_work_profile_nine_work_eas_configuration, android_work_profile_pkcs_certificate_profile, android_work_profile_scep_certificate_profile, android_work_profile_trusted_root_certificate, android_work_profile_vpn_configuration, android_work_profile_wi_fi_configuration, aosp_device_owner_certificate_profile_base, aosp_device_owner_device_configuration, aosp_device_owner_enterprise_wi_fi_configuration, aosp_device_owner_pkcs_certificate_profile, aosp_device_owner_scep_certificate_profile, aosp_device_owner_trusted_root_certificate, aosp_device_owner_wi_fi_configuration, apple_device_features_configuration_base, apple_expedited_checkin_configuration_base, apple_vpn_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_group_assignment, device_configuration_user_overview, device_configuration_user_status, device_management_applicability_rule_device_mode, device_management_applicability_rule_os_edition, device_management_applicability_rule_os_version, eas_email_profile_configuration_base, edition_upgrade_configuration, entity, iosik_ev2_vpn_configuration, ios_certificate_profile, ios_certificate_profile_base, ios_custom_configuration, ios_derived_credential_authentication_configuration, ios_device_features_configuration, ios_eas_email_profile_configuration, ios_education_device_configuration, ios_edu_device_configuration, ios_enterprise_wi_fi_configuration, ios_expedited_checkin_configuration, ios_general_device_configuration, ios_imported_p_f_x_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, ios_trusted_root_certificate, ios_update_configuration, ios_vpn_configuration, ios_wi_fi_configuration, mac_o_s_certificate_profile_base, mac_o_s_custom_app_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_endpoint_protection_configuration, mac_o_s_enterprise_wi_fi_configuration, mac_o_s_extensions_configuration, mac_o_s_general_device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, mac_o_s_software_update_configuration, mac_o_s_trusted_root_certificate, mac_o_s_vpn_configuration, mac_o_s_wired_network_configuration, mac_o_s_wi_fi_configuration, setting_state_device_summary, shared_p_c_configuration, unsupported_device_configuration, vpn_configuration, windows10_certificate_profile_base, windows10_custom_configuration, windows10_device_firmware_configuration_interface, windows10_eas_email_profile_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_imported_p_f_x_certificate_profile, windows10_network_boundary_configuration, windows10_pkcs_certificate_profile, windows10_p_f_x_import_certificate_profile, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows10_vpn_configuration, windows81_certificate_profile_base, windows81_general_configuration, windows81_s_c_e_p_certificate_profile, windows81_trusted_root_certificate, windows81_vpn_configuration, windows81_wifi_import_configuration, windows_certificate_profile_base, windows_defender_advanced_threat_protection_configuration, windows_delivery_optimization_configuration, windows_domain_join_configuration, windows_health_monitoring_configuration, windows_identity_protection_configuration, windows_kiosk_configuration, windows_phone81_certificate_profile_base, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_phone81_imported_p_f_x_certificate_profile, windows_phone81_s_c_e_p_certificate_profile, windows_phone81_trusted_root_certificate, windows_phone81_vpn_configuration, windows_phone_e_a_s_email_profile_configuration, windows_update_for_business_configuration, windows_vpn_configuration, windows_wifi_configuration, windows_wifi_enterprise_e_a_p_configuration, windows_wired_network_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceManagementApplicabilityRuleDeviceMode": lambda n : setattr(self, 'device_management_applicability_rule_device_mode', n.get_object_value(device_management_applicability_rule_device_mode.DeviceManagementApplicabilityRuleDeviceMode)),
            "deviceManagementApplicabilityRuleOsEdition": lambda n : setattr(self, 'device_management_applicability_rule_os_edition', n.get_object_value(device_management_applicability_rule_os_edition.DeviceManagementApplicabilityRuleOsEdition)),
            "deviceManagementApplicabilityRuleOsVersion": lambda n : setattr(self, 'device_management_applicability_rule_os_version', n.get_object_value(device_management_applicability_rule_os_version.DeviceManagementApplicabilityRuleOsVersion)),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_configuration_device_overview.DeviceConfigurationDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_configuration_device_status.DeviceConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(device_configuration_group_assignment.DeviceConfigurationGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supportsScopeTags": lambda n : setattr(self, 'supports_scope_tags', n.get_bool_value()),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_configuration_user_overview.DeviceConfigurationUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_configuration_user_status.DeviceConfigurationUserStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("deviceManagementApplicabilityRuleDeviceMode", self.device_management_applicability_rule_device_mode)
        writer.write_object_value("deviceManagementApplicabilityRuleOsEdition", self.device_management_applicability_rule_os_edition)
        writer.write_object_value("deviceManagementApplicabilityRuleOsVersion", self.device_management_applicability_rule_os_version)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

