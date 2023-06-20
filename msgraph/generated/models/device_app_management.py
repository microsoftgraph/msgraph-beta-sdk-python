from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_app_protection, default_managed_app_protection, device_app_management_task, enterprise_code_signing_certificate, entity, ios_lob_app_provisioning_configuration, ios_managed_app_protection, managed_app_policy, managed_app_registration, managed_app_status, managed_device_mobile_app_configuration, managed_e_book, managed_e_book_category, mdm_windows_information_protection_policy, microsoft_store_for_business_portal_selection_options, mobile_app, mobile_app_category, policy_set, symantec_code_signing_certificate, targeted_managed_app_configuration, vpp_token, windows_defender_application_control_supplemental_policy, windows_information_protection_device_registration, windows_information_protection_policy, windows_information_protection_wipe_action, windows_managed_app_protection, windows_management_app

from . import entity

@dataclass
class DeviceAppManagement(entity.Entity):
    # Android managed app policies.
    android_managed_app_protections: Optional[List[android_managed_app_protection.AndroidManagedAppProtection]] = None
    # Default managed app policies.
    default_managed_app_protections: Optional[List[default_managed_app_protection.DefaultManagedAppProtection]] = None
    # Device app management tasks.
    device_app_management_tasks: Optional[List[device_app_management_task.DeviceAppManagementTask]] = None
    # The Windows Enterprise Code Signing Certificate.
    enterprise_code_signing_certificates: Optional[List[enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate]] = None
    # The IOS Lob App Provisioning Configurations.
    ios_lob_app_provisioning_configurations: Optional[List[ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration]] = None
    # iOS managed app policies.
    ios_managed_app_protections: Optional[List[ios_managed_app_protection.IosManagedAppProtection]] = None
    # Whether the account is enabled for syncing applications from the Microsoft Store for Business.
    is_enabled_for_microsoft_store_for_business: Optional[bool] = None
    # Managed app policies.
    managed_app_policies: Optional[List[managed_app_policy.ManagedAppPolicy]] = None
    # The managed app registrations.
    managed_app_registrations: Optional[List[managed_app_registration.ManagedAppRegistration]] = None
    # The managed app statuses.
    managed_app_statuses: Optional[List[managed_app_status.ManagedAppStatus]] = None
    # The mobile eBook categories.
    managed_e_book_categories: Optional[List[managed_e_book_category.ManagedEBookCategory]] = None
    # The Managed eBook.
    managed_e_books: Optional[List[managed_e_book.ManagedEBook]] = None
    # Windows information protection for apps running on devices which are MDM enrolled.
    mdm_windows_information_protection_policies: Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]] = None
    # The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
    microsoft_store_for_business_language: Optional[str] = None
    # The last time an application sync from the Microsoft Store for Business was completed.
    microsoft_store_for_business_last_completed_application_sync_time: Optional[datetime] = None
    # The last time the apps from the Microsoft Store for Business were synced successfully for the account.
    microsoft_store_for_business_last_successful_sync_date_time: Optional[datetime] = None
    # Portal to which admin syncs available Microsoft Store for Business apps. This is available in the Intune Admin Console.
    microsoft_store_for_business_portal_selection: Optional[microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions] = None
    # The mobile app categories.
    mobile_app_categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
    # The Managed Device Mobile Application Configurations.
    mobile_app_configurations: Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]] = None
    # The mobile apps.
    mobile_apps: Optional[List[mobile_app.MobileApp]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The PolicySet of Policies and Applications
    policy_sets: Optional[List[policy_set.PolicySet]] = None
    # The WinPhone Symantec Code Signing Certificate.
    symantec_code_signing_certificate: Optional[symantec_code_signing_certificate.SymantecCodeSigningCertificate] = None
    # Targeted managed app configurations.
    targeted_managed_app_configurations: Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]] = None
    # List of Vpp tokens for this organization.
    vpp_tokens: Optional[List[vpp_token.VppToken]] = None
    # The collection of Windows Defender Application Control Supplemental Policies.
    wdac_supplemental_policies: Optional[List[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]] = None
    # Windows information protection device registrations that are not MDM enrolled.
    windows_information_protection_device_registrations: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]] = None
    # Windows information protection for apps running on devices which are not MDM enrolled.
    windows_information_protection_policies: Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]] = None
    # Windows information protection wipe actions.
    windows_information_protection_wipe_actions: Optional[List[windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction]] = None
    # Windows managed app policies.
    windows_managed_app_protections: Optional[List[windows_managed_app_protection.WindowsManagedAppProtection]] = None
    # Windows management app.
    windows_management_app: Optional[windows_management_app.WindowsManagementApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAppManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceAppManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_managed_app_protection, default_managed_app_protection, device_app_management_task, enterprise_code_signing_certificate, entity, ios_lob_app_provisioning_configuration, ios_managed_app_protection, managed_app_policy, managed_app_registration, managed_app_status, managed_device_mobile_app_configuration, managed_e_book, managed_e_book_category, mdm_windows_information_protection_policy, microsoft_store_for_business_portal_selection_options, mobile_app, mobile_app_category, policy_set, symantec_code_signing_certificate, targeted_managed_app_configuration, vpp_token, windows_defender_application_control_supplemental_policy, windows_information_protection_device_registration, windows_information_protection_policy, windows_information_protection_wipe_action, windows_managed_app_protection, windows_management_app

        from . import android_managed_app_protection, default_managed_app_protection, device_app_management_task, enterprise_code_signing_certificate, entity, ios_lob_app_provisioning_configuration, ios_managed_app_protection, managed_app_policy, managed_app_registration, managed_app_status, managed_device_mobile_app_configuration, managed_e_book, managed_e_book_category, mdm_windows_information_protection_policy, microsoft_store_for_business_portal_selection_options, mobile_app, mobile_app_category, policy_set, symantec_code_signing_certificate, targeted_managed_app_configuration, vpp_token, windows_defender_application_control_supplemental_policy, windows_information_protection_device_registration, windows_information_protection_policy, windows_information_protection_wipe_action, windows_managed_app_protection, windows_management_app

        fields: Dict[str, Callable[[Any], None]] = {
            "androidManagedAppProtections": lambda n : setattr(self, 'android_managed_app_protections', n.get_collection_of_object_values(android_managed_app_protection.AndroidManagedAppProtection)),
            "defaultManagedAppProtections": lambda n : setattr(self, 'default_managed_app_protections', n.get_collection_of_object_values(default_managed_app_protection.DefaultManagedAppProtection)),
            "deviceAppManagementTasks": lambda n : setattr(self, 'device_app_management_tasks', n.get_collection_of_object_values(device_app_management_task.DeviceAppManagementTask)),
            "enterpriseCodeSigningCertificates": lambda n : setattr(self, 'enterprise_code_signing_certificates', n.get_collection_of_object_values(enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate)),
            "iosLobAppProvisioningConfigurations": lambda n : setattr(self, 'ios_lob_app_provisioning_configurations', n.get_collection_of_object_values(ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration)),
            "iosManagedAppProtections": lambda n : setattr(self, 'ios_managed_app_protections', n.get_collection_of_object_values(ios_managed_app_protection.IosManagedAppProtection)),
            "isEnabledForMicrosoftStoreForBusiness": lambda n : setattr(self, 'is_enabled_for_microsoft_store_for_business', n.get_bool_value()),
            "managedAppPolicies": lambda n : setattr(self, 'managed_app_policies', n.get_collection_of_object_values(managed_app_policy.ManagedAppPolicy)),
            "managedAppRegistrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(managed_app_registration.ManagedAppRegistration)),
            "managedAppStatuses": lambda n : setattr(self, 'managed_app_statuses', n.get_collection_of_object_values(managed_app_status.ManagedAppStatus)),
            "managedEBookCategories": lambda n : setattr(self, 'managed_e_book_categories', n.get_collection_of_object_values(managed_e_book_category.ManagedEBookCategory)),
            "managedEBooks": lambda n : setattr(self, 'managed_e_books', n.get_collection_of_object_values(managed_e_book.ManagedEBook)),
            "mdmWindowsInformationProtectionPolicies": lambda n : setattr(self, 'mdm_windows_information_protection_policies', n.get_collection_of_object_values(mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy)),
            "microsoftStoreForBusinessLanguage": lambda n : setattr(self, 'microsoft_store_for_business_language', n.get_str_value()),
            "microsoftStoreForBusinessLastCompletedApplicationSyncTime": lambda n : setattr(self, 'microsoft_store_for_business_last_completed_application_sync_time', n.get_datetime_value()),
            "microsoftStoreForBusinessLastSuccessfulSyncDateTime": lambda n : setattr(self, 'microsoft_store_for_business_last_successful_sync_date_time', n.get_datetime_value()),
            "microsoftStoreForBusinessPortalSelection": lambda n : setattr(self, 'microsoft_store_for_business_portal_selection', n.get_enum_value(microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions)),
            "mobileAppCategories": lambda n : setattr(self, 'mobile_app_categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "mobileAppConfigurations": lambda n : setattr(self, 'mobile_app_configurations', n.get_collection_of_object_values(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration)),
            "mobileApps": lambda n : setattr(self, 'mobile_apps', n.get_collection_of_object_values(mobile_app.MobileApp)),
            "policySets": lambda n : setattr(self, 'policy_sets', n.get_collection_of_object_values(policy_set.PolicySet)),
            "symantecCodeSigningCertificate": lambda n : setattr(self, 'symantec_code_signing_certificate', n.get_object_value(symantec_code_signing_certificate.SymantecCodeSigningCertificate)),
            "targetedManagedAppConfigurations": lambda n : setattr(self, 'targeted_managed_app_configurations', n.get_collection_of_object_values(targeted_managed_app_configuration.TargetedManagedAppConfiguration)),
            "vppTokens": lambda n : setattr(self, 'vpp_tokens', n.get_collection_of_object_values(vpp_token.VppToken)),
            "wdacSupplementalPolicies": lambda n : setattr(self, 'wdac_supplemental_policies', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy)),
            "windowsInformationProtectionDeviceRegistrations": lambda n : setattr(self, 'windows_information_protection_device_registrations', n.get_collection_of_object_values(windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration)),
            "windowsInformationProtectionPolicies": lambda n : setattr(self, 'windows_information_protection_policies', n.get_collection_of_object_values(windows_information_protection_policy.WindowsInformationProtectionPolicy)),
            "windowsInformationProtectionWipeActions": lambda n : setattr(self, 'windows_information_protection_wipe_actions', n.get_collection_of_object_values(windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction)),
            "windowsManagedAppProtections": lambda n : setattr(self, 'windows_managed_app_protections', n.get_collection_of_object_values(windows_managed_app_protection.WindowsManagedAppProtection)),
            "windowsManagementApp": lambda n : setattr(self, 'windows_management_app', n.get_object_value(windows_management_app.WindowsManagementApp)),
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
        writer.write_collection_of_object_values("androidManagedAppProtections", self.android_managed_app_protections)
        writer.write_collection_of_object_values("defaultManagedAppProtections", self.default_managed_app_protections)
        writer.write_collection_of_object_values("deviceAppManagementTasks", self.device_app_management_tasks)
        writer.write_collection_of_object_values("enterpriseCodeSigningCertificates", self.enterprise_code_signing_certificates)
        writer.write_collection_of_object_values("iosLobAppProvisioningConfigurations", self.ios_lob_app_provisioning_configurations)
        writer.write_collection_of_object_values("iosManagedAppProtections", self.ios_managed_app_protections)
        writer.write_bool_value("isEnabledForMicrosoftStoreForBusiness", self.is_enabled_for_microsoft_store_for_business)
        writer.write_collection_of_object_values("managedAppPolicies", self.managed_app_policies)
        writer.write_collection_of_object_values("managedAppRegistrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managedAppStatuses", self.managed_app_statuses)
        writer.write_collection_of_object_values("managedEBookCategories", self.managed_e_book_categories)
        writer.write_collection_of_object_values("managedEBooks", self.managed_e_books)
        writer.write_collection_of_object_values("mdmWindowsInformationProtectionPolicies", self.mdm_windows_information_protection_policies)
        writer.write_str_value("microsoftStoreForBusinessLanguage", self.microsoft_store_for_business_language)
        writer.write_datetime_value("microsoftStoreForBusinessLastCompletedApplicationSyncTime", self.microsoft_store_for_business_last_completed_application_sync_time)
        writer.write_datetime_value("microsoftStoreForBusinessLastSuccessfulSyncDateTime", self.microsoft_store_for_business_last_successful_sync_date_time)
        writer.write_enum_value("microsoftStoreForBusinessPortalSelection", self.microsoft_store_for_business_portal_selection)
        writer.write_collection_of_object_values("mobileAppCategories", self.mobile_app_categories)
        writer.write_collection_of_object_values("mobileAppConfigurations", self.mobile_app_configurations)
        writer.write_collection_of_object_values("mobileApps", self.mobile_apps)
        writer.write_collection_of_object_values("policySets", self.policy_sets)
        writer.write_object_value("symantecCodeSigningCertificate", self.symantec_code_signing_certificate)
        writer.write_collection_of_object_values("targetedManagedAppConfigurations", self.targeted_managed_app_configurations)
        writer.write_collection_of_object_values("vppTokens", self.vpp_tokens)
        writer.write_collection_of_object_values("wdacSupplementalPolicies", self.wdac_supplemental_policies)
        writer.write_collection_of_object_values("windowsInformationProtectionDeviceRegistrations", self.windows_information_protection_device_registrations)
        writer.write_collection_of_object_values("windowsInformationProtectionPolicies", self.windows_information_protection_policies)
        writer.write_collection_of_object_values("windowsInformationProtectionWipeActions", self.windows_information_protection_wipe_actions)
        writer.write_collection_of_object_values("windowsManagedAppProtections", self.windows_managed_app_protections)
        writer.write_object_value("windowsManagementApp", self.windows_management_app)
    

