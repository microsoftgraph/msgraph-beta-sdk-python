from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .device_app_management_task import DeviceAppManagementTask
    from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
    from .entity import Entity
    from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_policy import ManagedAppPolicy
    from .managed_app_registration import ManagedAppRegistration
    from .managed_app_status import ManagedAppStatus
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
    from .managed_e_book import ManagedEBook
    from .managed_e_book_category import ManagedEBookCategory
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .microsoft_store_for_business_portal_selection_options import MicrosoftStoreForBusinessPortalSelectionOptions
    from .mobile_app import MobileApp
    from .mobile_app_catalog_package import MobileAppCatalogPackage
    from .mobile_app_category import MobileAppCategory
    from .mobile_app_relationship import MobileAppRelationship
    from .policy_set import PolicySet
    from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .vpp_token import VppToken
    from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
    from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy
    from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
    from .windows_managed_app_protection import WindowsManagedAppProtection
    from .windows_management_app import WindowsManagementApp

from .entity import Entity

@dataclass
class DeviceAppManagement(Entity):
    """
    Singleton entity that acts as a container for all device app management functionality.
    """
    # Android managed app policies.
    android_managed_app_protections: Optional[List[AndroidManagedAppProtection]] = None
    # Default managed app policies.
    default_managed_app_protections: Optional[List[DefaultManagedAppProtection]] = None
    # Device app management tasks.
    device_app_management_tasks: Optional[List[DeviceAppManagementTask]] = None
    # The Windows Enterprise Code Signing Certificate.
    enterprise_code_signing_certificates: Optional[List[EnterpriseCodeSigningCertificate]] = None
    # The IOS Lob App Provisioning Configurations.
    ios_lob_app_provisioning_configurations: Optional[List[IosLobAppProvisioningConfiguration]] = None
    # iOS managed app policies.
    ios_managed_app_protections: Optional[List[IosManagedAppProtection]] = None
    # Whether the account is enabled for syncing applications from the Microsoft Store for Business.
    is_enabled_for_microsoft_store_for_business: Optional[bool] = None
    # Managed app policies.
    managed_app_policies: Optional[List[ManagedAppPolicy]] = None
    # The managed app registrations.
    managed_app_registrations: Optional[List[ManagedAppRegistration]] = None
    # The managed app statuses.
    managed_app_statuses: Optional[List[ManagedAppStatus]] = None
    # The mobile eBook categories.
    managed_e_book_categories: Optional[List[ManagedEBookCategory]] = None
    # The Managed eBook.
    managed_e_books: Optional[List[ManagedEBook]] = None
    # Windows information protection for apps running on devices which are MDM enrolled.
    mdm_windows_information_protection_policies: Optional[List[MdmWindowsInformationProtectionPolicy]] = None
    # The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
    microsoft_store_for_business_language: Optional[str] = None
    # The last time an application sync from the Microsoft Store for Business was completed.
    microsoft_store_for_business_last_completed_application_sync_time: Optional[datetime.datetime] = None
    # The last time the apps from the Microsoft Store for Business were synced successfully for the account.
    microsoft_store_for_business_last_successful_sync_date_time: Optional[datetime.datetime] = None
    # Portal to which admin syncs available Microsoft Store for Business apps. This is available in the Intune Admin Console.
    microsoft_store_for_business_portal_selection: Optional[MicrosoftStoreForBusinessPortalSelectionOptions] = None
    # MobileAppCatalogPackage entities.
    mobile_app_catalog_packages: Optional[List[MobileAppCatalogPackage]] = None
    # The mobile app categories.
    mobile_app_categories: Optional[List[MobileAppCategory]] = None
    # The Managed Device Mobile Application Configurations.
    mobile_app_configurations: Optional[List[ManagedDeviceMobileAppConfiguration]] = None
    # List mobileAppRelationship objects for mobile applications.
    mobile_app_relationships: Optional[List[MobileAppRelationship]] = None
    # The mobile apps.
    mobile_apps: Optional[List[MobileApp]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The PolicySet of Policies and Applications
    policy_sets: Optional[List[PolicySet]] = None
    # The WinPhone Symantec Code Signing Certificate.
    symantec_code_signing_certificate: Optional[SymantecCodeSigningCertificate] = None
    # Targeted managed app configurations.
    targeted_managed_app_configurations: Optional[List[TargetedManagedAppConfiguration]] = None
    # List of Vpp tokens for this organization.
    vpp_tokens: Optional[List[VppToken]] = None
    # The collection of Windows Defender Application Control Supplemental Policies.
    wdac_supplemental_policies: Optional[List[WindowsDefenderApplicationControlSupplementalPolicy]] = None
    # Windows information protection device registrations that are not MDM enrolled.
    windows_information_protection_device_registrations: Optional[List[WindowsInformationProtectionDeviceRegistration]] = None
    # Windows information protection for apps running on devices which are not MDM enrolled.
    windows_information_protection_policies: Optional[List[WindowsInformationProtectionPolicy]] = None
    # Windows information protection wipe actions.
    windows_information_protection_wipe_actions: Optional[List[WindowsInformationProtectionWipeAction]] = None
    # Windows managed app policies.
    windows_managed_app_protections: Optional[List[WindowsManagedAppProtection]] = None
    # Windows management app.
    windows_management_app: Optional[WindowsManagementApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAppManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceAppManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .device_app_management_task import DeviceAppManagementTask
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entity import Entity
        from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_e_book import ManagedEBook
        from .managed_e_book_category import ManagedEBookCategory
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .microsoft_store_for_business_portal_selection_options import MicrosoftStoreForBusinessPortalSelectionOptions
        from .mobile_app import MobileApp
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_relationship import MobileAppRelationship
        from .policy_set import PolicySet
        from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .vpp_token import VppToken
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
        from .windows_managed_app_protection import WindowsManagedAppProtection
        from .windows_management_app import WindowsManagementApp

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .device_app_management_task import DeviceAppManagementTask
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entity import Entity
        from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_e_book import ManagedEBook
        from .managed_e_book_category import ManagedEBookCategory
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .microsoft_store_for_business_portal_selection_options import MicrosoftStoreForBusinessPortalSelectionOptions
        from .mobile_app import MobileApp
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_relationship import MobileAppRelationship
        from .policy_set import PolicySet
        from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .vpp_token import VppToken
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
        from .windows_managed_app_protection import WindowsManagedAppProtection
        from .windows_management_app import WindowsManagementApp

        fields: Dict[str, Callable[[Any], None]] = {
            "androidManagedAppProtections": lambda n : setattr(self, 'android_managed_app_protections', n.get_collection_of_object_values(AndroidManagedAppProtection)),
            "defaultManagedAppProtections": lambda n : setattr(self, 'default_managed_app_protections', n.get_collection_of_object_values(DefaultManagedAppProtection)),
            "deviceAppManagementTasks": lambda n : setattr(self, 'device_app_management_tasks', n.get_collection_of_object_values(DeviceAppManagementTask)),
            "enterpriseCodeSigningCertificates": lambda n : setattr(self, 'enterprise_code_signing_certificates', n.get_collection_of_object_values(EnterpriseCodeSigningCertificate)),
            "iosLobAppProvisioningConfigurations": lambda n : setattr(self, 'ios_lob_app_provisioning_configurations', n.get_collection_of_object_values(IosLobAppProvisioningConfiguration)),
            "iosManagedAppProtections": lambda n : setattr(self, 'ios_managed_app_protections', n.get_collection_of_object_values(IosManagedAppProtection)),
            "isEnabledForMicrosoftStoreForBusiness": lambda n : setattr(self, 'is_enabled_for_microsoft_store_for_business', n.get_bool_value()),
            "managedAppPolicies": lambda n : setattr(self, 'managed_app_policies', n.get_collection_of_object_values(ManagedAppPolicy)),
            "managedAppRegistrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(ManagedAppRegistration)),
            "managedAppStatuses": lambda n : setattr(self, 'managed_app_statuses', n.get_collection_of_object_values(ManagedAppStatus)),
            "managedEBookCategories": lambda n : setattr(self, 'managed_e_book_categories', n.get_collection_of_object_values(ManagedEBookCategory)),
            "managedEBooks": lambda n : setattr(self, 'managed_e_books', n.get_collection_of_object_values(ManagedEBook)),
            "mdmWindowsInformationProtectionPolicies": lambda n : setattr(self, 'mdm_windows_information_protection_policies', n.get_collection_of_object_values(MdmWindowsInformationProtectionPolicy)),
            "microsoftStoreForBusinessLanguage": lambda n : setattr(self, 'microsoft_store_for_business_language', n.get_str_value()),
            "microsoftStoreForBusinessLastCompletedApplicationSyncTime": lambda n : setattr(self, 'microsoft_store_for_business_last_completed_application_sync_time', n.get_datetime_value()),
            "microsoftStoreForBusinessLastSuccessfulSyncDateTime": lambda n : setattr(self, 'microsoft_store_for_business_last_successful_sync_date_time', n.get_datetime_value()),
            "microsoftStoreForBusinessPortalSelection": lambda n : setattr(self, 'microsoft_store_for_business_portal_selection', n.get_collection_of_enum_values(MicrosoftStoreForBusinessPortalSelectionOptions)),
            "mobileAppCatalogPackages": lambda n : setattr(self, 'mobile_app_catalog_packages', n.get_collection_of_object_values(MobileAppCatalogPackage)),
            "mobileAppCategories": lambda n : setattr(self, 'mobile_app_categories', n.get_collection_of_object_values(MobileAppCategory)),
            "mobileAppConfigurations": lambda n : setattr(self, 'mobile_app_configurations', n.get_collection_of_object_values(ManagedDeviceMobileAppConfiguration)),
            "mobileAppRelationships": lambda n : setattr(self, 'mobile_app_relationships', n.get_collection_of_object_values(MobileAppRelationship)),
            "mobileApps": lambda n : setattr(self, 'mobile_apps', n.get_collection_of_object_values(MobileApp)),
            "policySets": lambda n : setattr(self, 'policy_sets', n.get_collection_of_object_values(PolicySet)),
            "symantecCodeSigningCertificate": lambda n : setattr(self, 'symantec_code_signing_certificate', n.get_object_value(SymantecCodeSigningCertificate)),
            "targetedManagedAppConfigurations": lambda n : setattr(self, 'targeted_managed_app_configurations', n.get_collection_of_object_values(TargetedManagedAppConfiguration)),
            "vppTokens": lambda n : setattr(self, 'vpp_tokens', n.get_collection_of_object_values(VppToken)),
            "wdacSupplementalPolicies": lambda n : setattr(self, 'wdac_supplemental_policies', n.get_collection_of_object_values(WindowsDefenderApplicationControlSupplementalPolicy)),
            "windowsInformationProtectionDeviceRegistrations": lambda n : setattr(self, 'windows_information_protection_device_registrations', n.get_collection_of_object_values(WindowsInformationProtectionDeviceRegistration)),
            "windowsInformationProtectionPolicies": lambda n : setattr(self, 'windows_information_protection_policies', n.get_collection_of_object_values(WindowsInformationProtectionPolicy)),
            "windowsInformationProtectionWipeActions": lambda n : setattr(self, 'windows_information_protection_wipe_actions', n.get_collection_of_object_values(WindowsInformationProtectionWipeAction)),
            "windowsManagedAppProtections": lambda n : setattr(self, 'windows_managed_app_protections', n.get_collection_of_object_values(WindowsManagedAppProtection)),
            "windowsManagementApp": lambda n : setattr(self, 'windows_management_app', n.get_object_value(WindowsManagementApp)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
        writer.write_collection_of_object_values("mobileAppCatalogPackages", self.mobile_app_catalog_packages)
        writer.write_collection_of_object_values("mobileAppCategories", self.mobile_app_categories)
        writer.write_collection_of_object_values("mobileAppConfigurations", self.mobile_app_configurations)
        writer.write_collection_of_object_values("mobileAppRelationships", self.mobile_app_relationships)
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
    

