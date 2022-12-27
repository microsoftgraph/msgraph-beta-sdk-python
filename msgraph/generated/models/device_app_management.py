from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_app_protection = lazy_import('msgraph.generated.models.android_managed_app_protection')
default_managed_app_protection = lazy_import('msgraph.generated.models.default_managed_app_protection')
device_app_management_task = lazy_import('msgraph.generated.models.device_app_management_task')
enterprise_code_signing_certificate = lazy_import('msgraph.generated.models.enterprise_code_signing_certificate')
entity = lazy_import('msgraph.generated.models.entity')
ios_lob_app_provisioning_configuration = lazy_import('msgraph.generated.models.ios_lob_app_provisioning_configuration')
ios_managed_app_protection = lazy_import('msgraph.generated.models.ios_managed_app_protection')
managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')
managed_app_registration = lazy_import('msgraph.generated.models.managed_app_registration')
managed_app_status = lazy_import('msgraph.generated.models.managed_app_status')
managed_device_mobile_app_configuration = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration')
managed_e_book = lazy_import('msgraph.generated.models.managed_e_book')
managed_e_book_category = lazy_import('msgraph.generated.models.managed_e_book_category')
mdm_windows_information_protection_policy = lazy_import('msgraph.generated.models.mdm_windows_information_protection_policy')
microsoft_store_for_business_portal_selection_options = lazy_import('msgraph.generated.models.microsoft_store_for_business_portal_selection_options')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
mobile_app_category = lazy_import('msgraph.generated.models.mobile_app_category')
policy_set = lazy_import('msgraph.generated.models.policy_set')
side_loading_key = lazy_import('msgraph.generated.models.side_loading_key')
symantec_code_signing_certificate = lazy_import('msgraph.generated.models.symantec_code_signing_certificate')
targeted_managed_app_configuration = lazy_import('msgraph.generated.models.targeted_managed_app_configuration')
vpp_token = lazy_import('msgraph.generated.models.vpp_token')
windows_defender_application_control_supplemental_policy = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy')
windows_information_protection_device_registration = lazy_import('msgraph.generated.models.windows_information_protection_device_registration')
windows_information_protection_policy = lazy_import('msgraph.generated.models.windows_information_protection_policy')
windows_information_protection_wipe_action = lazy_import('msgraph.generated.models.windows_information_protection_wipe_action')
windows_managed_app_protection = lazy_import('msgraph.generated.models.windows_managed_app_protection')
windows_management_app = lazy_import('msgraph.generated.models.windows_management_app')

class DeviceAppManagement(entity.Entity):
    @property
    def android_managed_app_protections(self,) -> Optional[List[android_managed_app_protection.AndroidManagedAppProtection]]:
        """
        Gets the androidManagedAppProtections property value. Android managed app policies.
        Returns: Optional[List[android_managed_app_protection.AndroidManagedAppProtection]]
        """
        return self._android_managed_app_protections
    
    @android_managed_app_protections.setter
    def android_managed_app_protections(self,value: Optional[List[android_managed_app_protection.AndroidManagedAppProtection]] = None) -> None:
        """
        Sets the androidManagedAppProtections property value. Android managed app policies.
        Args:
            value: Value to set for the androidManagedAppProtections property.
        """
        self._android_managed_app_protections = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceAppManagement and sets the default values.
        """
        super().__init__()
        # Android managed app policies.
        self._android_managed_app_protections: Optional[List[android_managed_app_protection.AndroidManagedAppProtection]] = None
        # Default managed app policies.
        self._default_managed_app_protections: Optional[List[default_managed_app_protection.DefaultManagedAppProtection]] = None
        # Device app management tasks.
        self._device_app_management_tasks: Optional[List[device_app_management_task.DeviceAppManagementTask]] = None
        # The Windows Enterprise Code Signing Certificate.
        self._enterprise_code_signing_certificates: Optional[List[enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate]] = None
        # The IOS Lob App Provisioning Configurations.
        self._ios_lob_app_provisioning_configurations: Optional[List[ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration]] = None
        # iOS managed app policies.
        self._ios_managed_app_protections: Optional[List[ios_managed_app_protection.IosManagedAppProtection]] = None
        # Whether the account is enabled for syncing applications from the Microsoft Store for Business.
        self._is_enabled_for_microsoft_store_for_business: Optional[bool] = None
        # Managed app policies.
        self._managed_app_policies: Optional[List[managed_app_policy.ManagedAppPolicy]] = None
        # The managed app registrations.
        self._managed_app_registrations: Optional[List[managed_app_registration.ManagedAppRegistration]] = None
        # The managed app statuses.
        self._managed_app_statuses: Optional[List[managed_app_status.ManagedAppStatus]] = None
        # The mobile eBook categories.
        self._managed_e_book_categories: Optional[List[managed_e_book_category.ManagedEBookCategory]] = None
        # The Managed eBook.
        self._managed_e_books: Optional[List[managed_e_book.ManagedEBook]] = None
        # Windows information protection for apps running on devices which are MDM enrolled.
        self._mdm_windows_information_protection_policies: Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]] = None
        # The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
        self._microsoft_store_for_business_language: Optional[str] = None
        # The last time an application sync from the Microsoft Store for Business was completed.
        self._microsoft_store_for_business_last_completed_application_sync_time: Optional[datetime] = None
        # The last time the apps from the Microsoft Store for Business were synced successfully for the account.
        self._microsoft_store_for_business_last_successful_sync_date_time: Optional[datetime] = None
        # Portal to which admin syncs available Microsoft Store for Business apps. This is available in the Intune Admin Console.
        self._microsoft_store_for_business_portal_selection: Optional[microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions] = None
        # The mobile app categories.
        self._mobile_app_categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
        # The Managed Device Mobile Application Configurations.
        self._mobile_app_configurations: Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]] = None
        # The mobile apps.
        self._mobile_apps: Optional[List[mobile_app.MobileApp]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The PolicySet of Policies and Applications
        self._policy_sets: Optional[List[policy_set.PolicySet]] = None
        # Side Loading Keys that are required for the Windows 8 and 8.1 Apps installation.
        self._side_loading_keys: Optional[List[side_loading_key.SideLoadingKey]] = None
        # The WinPhone Symantec Code Signing Certificate.
        self._symantec_code_signing_certificate: Optional[symantec_code_signing_certificate.SymantecCodeSigningCertificate] = None
        # Targeted managed app configurations.
        self._targeted_managed_app_configurations: Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]] = None
        # List of Vpp tokens for this organization.
        self._vpp_tokens: Optional[List[vpp_token.VppToken]] = None
        # The collection of Windows Defender Application Control Supplemental Policies.
        self._wdac_supplemental_policies: Optional[List[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]] = None
        # Windows information protection device registrations that are not MDM enrolled.
        self._windows_information_protection_device_registrations: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]] = None
        # Windows information protection for apps running on devices which are not MDM enrolled.
        self._windows_information_protection_policies: Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]] = None
        # Windows information protection wipe actions.
        self._windows_information_protection_wipe_actions: Optional[List[windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction]] = None
        # Windows managed app policies.
        self._windows_managed_app_protections: Optional[List[windows_managed_app_protection.WindowsManagedAppProtection]] = None
        # Windows management app.
        self._windows_management_app: Optional[windows_management_app.WindowsManagementApp] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAppManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAppManagement()
    
    @property
    def default_managed_app_protections(self,) -> Optional[List[default_managed_app_protection.DefaultManagedAppProtection]]:
        """
        Gets the defaultManagedAppProtections property value. Default managed app policies.
        Returns: Optional[List[default_managed_app_protection.DefaultManagedAppProtection]]
        """
        return self._default_managed_app_protections
    
    @default_managed_app_protections.setter
    def default_managed_app_protections(self,value: Optional[List[default_managed_app_protection.DefaultManagedAppProtection]] = None) -> None:
        """
        Sets the defaultManagedAppProtections property value. Default managed app policies.
        Args:
            value: Value to set for the defaultManagedAppProtections property.
        """
        self._default_managed_app_protections = value
    
    @property
    def device_app_management_tasks(self,) -> Optional[List[device_app_management_task.DeviceAppManagementTask]]:
        """
        Gets the deviceAppManagementTasks property value. Device app management tasks.
        Returns: Optional[List[device_app_management_task.DeviceAppManagementTask]]
        """
        return self._device_app_management_tasks
    
    @device_app_management_tasks.setter
    def device_app_management_tasks(self,value: Optional[List[device_app_management_task.DeviceAppManagementTask]] = None) -> None:
        """
        Sets the deviceAppManagementTasks property value. Device app management tasks.
        Args:
            value: Value to set for the deviceAppManagementTasks property.
        """
        self._device_app_management_tasks = value
    
    @property
    def enterprise_code_signing_certificates(self,) -> Optional[List[enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate]]:
        """
        Gets the enterpriseCodeSigningCertificates property value. The Windows Enterprise Code Signing Certificate.
        Returns: Optional[List[enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate]]
        """
        return self._enterprise_code_signing_certificates
    
    @enterprise_code_signing_certificates.setter
    def enterprise_code_signing_certificates(self,value: Optional[List[enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate]] = None) -> None:
        """
        Sets the enterpriseCodeSigningCertificates property value. The Windows Enterprise Code Signing Certificate.
        Args:
            value: Value to set for the enterpriseCodeSigningCertificates property.
        """
        self._enterprise_code_signing_certificates = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_managed_app_protections": lambda n : setattr(self, 'android_managed_app_protections', n.get_collection_of_object_values(android_managed_app_protection.AndroidManagedAppProtection)),
            "default_managed_app_protections": lambda n : setattr(self, 'default_managed_app_protections', n.get_collection_of_object_values(default_managed_app_protection.DefaultManagedAppProtection)),
            "device_app_management_tasks": lambda n : setattr(self, 'device_app_management_tasks', n.get_collection_of_object_values(device_app_management_task.DeviceAppManagementTask)),
            "enterprise_code_signing_certificates": lambda n : setattr(self, 'enterprise_code_signing_certificates', n.get_collection_of_object_values(enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate)),
            "ios_lob_app_provisioning_configurations": lambda n : setattr(self, 'ios_lob_app_provisioning_configurations', n.get_collection_of_object_values(ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration)),
            "ios_managed_app_protections": lambda n : setattr(self, 'ios_managed_app_protections', n.get_collection_of_object_values(ios_managed_app_protection.IosManagedAppProtection)),
            "is_enabled_for_microsoft_store_for_business": lambda n : setattr(self, 'is_enabled_for_microsoft_store_for_business', n.get_bool_value()),
            "managed_app_policies": lambda n : setattr(self, 'managed_app_policies', n.get_collection_of_object_values(managed_app_policy.ManagedAppPolicy)),
            "managed_app_registrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(managed_app_registration.ManagedAppRegistration)),
            "managed_app_statuses": lambda n : setattr(self, 'managed_app_statuses', n.get_collection_of_object_values(managed_app_status.ManagedAppStatus)),
            "managed_e_book_categories": lambda n : setattr(self, 'managed_e_book_categories', n.get_collection_of_object_values(managed_e_book_category.ManagedEBookCategory)),
            "managed_e_books": lambda n : setattr(self, 'managed_e_books', n.get_collection_of_object_values(managed_e_book.ManagedEBook)),
            "mdm_windows_information_protection_policies": lambda n : setattr(self, 'mdm_windows_information_protection_policies', n.get_collection_of_object_values(mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy)),
            "microsoft_store_for_business_language": lambda n : setattr(self, 'microsoft_store_for_business_language', n.get_str_value()),
            "microsoft_store_for_business_last_completed_application_sync_time": lambda n : setattr(self, 'microsoft_store_for_business_last_completed_application_sync_time', n.get_datetime_value()),
            "microsoft_store_for_business_last_successful_sync_date_time": lambda n : setattr(self, 'microsoft_store_for_business_last_successful_sync_date_time', n.get_datetime_value()),
            "microsoft_store_for_business_portal_selection": lambda n : setattr(self, 'microsoft_store_for_business_portal_selection', n.get_enum_value(microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions)),
            "mobile_app_categories": lambda n : setattr(self, 'mobile_app_categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "mobile_app_configurations": lambda n : setattr(self, 'mobile_app_configurations', n.get_collection_of_object_values(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration)),
            "mobile_apps": lambda n : setattr(self, 'mobile_apps', n.get_collection_of_object_values(mobile_app.MobileApp)),
            "policy_sets": lambda n : setattr(self, 'policy_sets', n.get_collection_of_object_values(policy_set.PolicySet)),
            "side_loading_keys": lambda n : setattr(self, 'side_loading_keys', n.get_collection_of_object_values(side_loading_key.SideLoadingKey)),
            "symantec_code_signing_certificate": lambda n : setattr(self, 'symantec_code_signing_certificate', n.get_object_value(symantec_code_signing_certificate.SymantecCodeSigningCertificate)),
            "targeted_managed_app_configurations": lambda n : setattr(self, 'targeted_managed_app_configurations', n.get_collection_of_object_values(targeted_managed_app_configuration.TargetedManagedAppConfiguration)),
            "vpp_tokens": lambda n : setattr(self, 'vpp_tokens', n.get_collection_of_object_values(vpp_token.VppToken)),
            "wdac_supplemental_policies": lambda n : setattr(self, 'wdac_supplemental_policies', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy)),
            "windows_information_protection_device_registrations": lambda n : setattr(self, 'windows_information_protection_device_registrations', n.get_collection_of_object_values(windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration)),
            "windows_information_protection_policies": lambda n : setattr(self, 'windows_information_protection_policies', n.get_collection_of_object_values(windows_information_protection_policy.WindowsInformationProtectionPolicy)),
            "windows_information_protection_wipe_actions": lambda n : setattr(self, 'windows_information_protection_wipe_actions', n.get_collection_of_object_values(windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction)),
            "windows_managed_app_protections": lambda n : setattr(self, 'windows_managed_app_protections', n.get_collection_of_object_values(windows_managed_app_protection.WindowsManagedAppProtection)),
            "windows_management_app": lambda n : setattr(self, 'windows_management_app', n.get_object_value(windows_management_app.WindowsManagementApp)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_lob_app_provisioning_configurations(self,) -> Optional[List[ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration]]:
        """
        Gets the iosLobAppProvisioningConfigurations property value. The IOS Lob App Provisioning Configurations.
        Returns: Optional[List[ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration]]
        """
        return self._ios_lob_app_provisioning_configurations
    
    @ios_lob_app_provisioning_configurations.setter
    def ios_lob_app_provisioning_configurations(self,value: Optional[List[ios_lob_app_provisioning_configuration.IosLobAppProvisioningConfiguration]] = None) -> None:
        """
        Sets the iosLobAppProvisioningConfigurations property value. The IOS Lob App Provisioning Configurations.
        Args:
            value: Value to set for the iosLobAppProvisioningConfigurations property.
        """
        self._ios_lob_app_provisioning_configurations = value
    
    @property
    def ios_managed_app_protections(self,) -> Optional[List[ios_managed_app_protection.IosManagedAppProtection]]:
        """
        Gets the iosManagedAppProtections property value. iOS managed app policies.
        Returns: Optional[List[ios_managed_app_protection.IosManagedAppProtection]]
        """
        return self._ios_managed_app_protections
    
    @ios_managed_app_protections.setter
    def ios_managed_app_protections(self,value: Optional[List[ios_managed_app_protection.IosManagedAppProtection]] = None) -> None:
        """
        Sets the iosManagedAppProtections property value. iOS managed app policies.
        Args:
            value: Value to set for the iosManagedAppProtections property.
        """
        self._ios_managed_app_protections = value
    
    @property
    def is_enabled_for_microsoft_store_for_business(self,) -> Optional[bool]:
        """
        Gets the isEnabledForMicrosoftStoreForBusiness property value. Whether the account is enabled for syncing applications from the Microsoft Store for Business.
        Returns: Optional[bool]
        """
        return self._is_enabled_for_microsoft_store_for_business
    
    @is_enabled_for_microsoft_store_for_business.setter
    def is_enabled_for_microsoft_store_for_business(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledForMicrosoftStoreForBusiness property value. Whether the account is enabled for syncing applications from the Microsoft Store for Business.
        Args:
            value: Value to set for the isEnabledForMicrosoftStoreForBusiness property.
        """
        self._is_enabled_for_microsoft_store_for_business = value
    
    @property
    def managed_app_policies(self,) -> Optional[List[managed_app_policy.ManagedAppPolicy]]:
        """
        Gets the managedAppPolicies property value. Managed app policies.
        Returns: Optional[List[managed_app_policy.ManagedAppPolicy]]
        """
        return self._managed_app_policies
    
    @managed_app_policies.setter
    def managed_app_policies(self,value: Optional[List[managed_app_policy.ManagedAppPolicy]] = None) -> None:
        """
        Sets the managedAppPolicies property value. Managed app policies.
        Args:
            value: Value to set for the managedAppPolicies property.
        """
        self._managed_app_policies = value
    
    @property
    def managed_app_registrations(self,) -> Optional[List[managed_app_registration.ManagedAppRegistration]]:
        """
        Gets the managedAppRegistrations property value. The managed app registrations.
        Returns: Optional[List[managed_app_registration.ManagedAppRegistration]]
        """
        return self._managed_app_registrations
    
    @managed_app_registrations.setter
    def managed_app_registrations(self,value: Optional[List[managed_app_registration.ManagedAppRegistration]] = None) -> None:
        """
        Sets the managedAppRegistrations property value. The managed app registrations.
        Args:
            value: Value to set for the managedAppRegistrations property.
        """
        self._managed_app_registrations = value
    
    @property
    def managed_app_statuses(self,) -> Optional[List[managed_app_status.ManagedAppStatus]]:
        """
        Gets the managedAppStatuses property value. The managed app statuses.
        Returns: Optional[List[managed_app_status.ManagedAppStatus]]
        """
        return self._managed_app_statuses
    
    @managed_app_statuses.setter
    def managed_app_statuses(self,value: Optional[List[managed_app_status.ManagedAppStatus]] = None) -> None:
        """
        Sets the managedAppStatuses property value. The managed app statuses.
        Args:
            value: Value to set for the managedAppStatuses property.
        """
        self._managed_app_statuses = value
    
    @property
    def managed_e_book_categories(self,) -> Optional[List[managed_e_book_category.ManagedEBookCategory]]:
        """
        Gets the managedEBookCategories property value. The mobile eBook categories.
        Returns: Optional[List[managed_e_book_category.ManagedEBookCategory]]
        """
        return self._managed_e_book_categories
    
    @managed_e_book_categories.setter
    def managed_e_book_categories(self,value: Optional[List[managed_e_book_category.ManagedEBookCategory]] = None) -> None:
        """
        Sets the managedEBookCategories property value. The mobile eBook categories.
        Args:
            value: Value to set for the managedEBookCategories property.
        """
        self._managed_e_book_categories = value
    
    @property
    def managed_e_books(self,) -> Optional[List[managed_e_book.ManagedEBook]]:
        """
        Gets the managedEBooks property value. The Managed eBook.
        Returns: Optional[List[managed_e_book.ManagedEBook]]
        """
        return self._managed_e_books
    
    @managed_e_books.setter
    def managed_e_books(self,value: Optional[List[managed_e_book.ManagedEBook]] = None) -> None:
        """
        Sets the managedEBooks property value. The Managed eBook.
        Args:
            value: Value to set for the managedEBooks property.
        """
        self._managed_e_books = value
    
    @property
    def mdm_windows_information_protection_policies(self,) -> Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]]:
        """
        Gets the mdmWindowsInformationProtectionPolicies property value. Windows information protection for apps running on devices which are MDM enrolled.
        Returns: Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]]
        """
        return self._mdm_windows_information_protection_policies
    
    @mdm_windows_information_protection_policies.setter
    def mdm_windows_information_protection_policies(self,value: Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]] = None) -> None:
        """
        Sets the mdmWindowsInformationProtectionPolicies property value. Windows information protection for apps running on devices which are MDM enrolled.
        Args:
            value: Value to set for the mdmWindowsInformationProtectionPolicies property.
        """
        self._mdm_windows_information_protection_policies = value
    
    @property
    def microsoft_store_for_business_language(self,) -> Optional[str]:
        """
        Gets the microsoftStoreForBusinessLanguage property value. The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
        Returns: Optional[str]
        """
        return self._microsoft_store_for_business_language
    
    @microsoft_store_for_business_language.setter
    def microsoft_store_for_business_language(self,value: Optional[str] = None) -> None:
        """
        Sets the microsoftStoreForBusinessLanguage property value. The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
        Args:
            value: Value to set for the microsoftStoreForBusinessLanguage property.
        """
        self._microsoft_store_for_business_language = value
    
    @property
    def microsoft_store_for_business_last_completed_application_sync_time(self,) -> Optional[datetime]:
        """
        Gets the microsoftStoreForBusinessLastCompletedApplicationSyncTime property value. The last time an application sync from the Microsoft Store for Business was completed.
        Returns: Optional[datetime]
        """
        return self._microsoft_store_for_business_last_completed_application_sync_time
    
    @microsoft_store_for_business_last_completed_application_sync_time.setter
    def microsoft_store_for_business_last_completed_application_sync_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the microsoftStoreForBusinessLastCompletedApplicationSyncTime property value. The last time an application sync from the Microsoft Store for Business was completed.
        Args:
            value: Value to set for the microsoftStoreForBusinessLastCompletedApplicationSyncTime property.
        """
        self._microsoft_store_for_business_last_completed_application_sync_time = value
    
    @property
    def microsoft_store_for_business_last_successful_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the microsoftStoreForBusinessLastSuccessfulSyncDateTime property value. The last time the apps from the Microsoft Store for Business were synced successfully for the account.
        Returns: Optional[datetime]
        """
        return self._microsoft_store_for_business_last_successful_sync_date_time
    
    @microsoft_store_for_business_last_successful_sync_date_time.setter
    def microsoft_store_for_business_last_successful_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the microsoftStoreForBusinessLastSuccessfulSyncDateTime property value. The last time the apps from the Microsoft Store for Business were synced successfully for the account.
        Args:
            value: Value to set for the microsoftStoreForBusinessLastSuccessfulSyncDateTime property.
        """
        self._microsoft_store_for_business_last_successful_sync_date_time = value
    
    @property
    def microsoft_store_for_business_portal_selection(self,) -> Optional[microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions]:
        """
        Gets the microsoftStoreForBusinessPortalSelection property value. Portal to which admin syncs available Microsoft Store for Business apps. This is available in the Intune Admin Console.
        Returns: Optional[microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions]
        """
        return self._microsoft_store_for_business_portal_selection
    
    @microsoft_store_for_business_portal_selection.setter
    def microsoft_store_for_business_portal_selection(self,value: Optional[microsoft_store_for_business_portal_selection_options.MicrosoftStoreForBusinessPortalSelectionOptions] = None) -> None:
        """
        Sets the microsoftStoreForBusinessPortalSelection property value. Portal to which admin syncs available Microsoft Store for Business apps. This is available in the Intune Admin Console.
        Args:
            value: Value to set for the microsoftStoreForBusinessPortalSelection property.
        """
        self._microsoft_store_for_business_portal_selection = value
    
    @property
    def mobile_app_categories(self,) -> Optional[List[mobile_app_category.MobileAppCategory]]:
        """
        Gets the mobileAppCategories property value. The mobile app categories.
        Returns: Optional[List[mobile_app_category.MobileAppCategory]]
        """
        return self._mobile_app_categories
    
    @mobile_app_categories.setter
    def mobile_app_categories(self,value: Optional[List[mobile_app_category.MobileAppCategory]] = None) -> None:
        """
        Sets the mobileAppCategories property value. The mobile app categories.
        Args:
            value: Value to set for the mobileAppCategories property.
        """
        self._mobile_app_categories = value
    
    @property
    def mobile_app_configurations(self,) -> Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]]:
        """
        Gets the mobileAppConfigurations property value. The Managed Device Mobile Application Configurations.
        Returns: Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]]
        """
        return self._mobile_app_configurations
    
    @mobile_app_configurations.setter
    def mobile_app_configurations(self,value: Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]] = None) -> None:
        """
        Sets the mobileAppConfigurations property value. The Managed Device Mobile Application Configurations.
        Args:
            value: Value to set for the mobileAppConfigurations property.
        """
        self._mobile_app_configurations = value
    
    @property
    def mobile_apps(self,) -> Optional[List[mobile_app.MobileApp]]:
        """
        Gets the mobileApps property value. The mobile apps.
        Returns: Optional[List[mobile_app.MobileApp]]
        """
        return self._mobile_apps
    
    @mobile_apps.setter
    def mobile_apps(self,value: Optional[List[mobile_app.MobileApp]] = None) -> None:
        """
        Sets the mobileApps property value. The mobile apps.
        Args:
            value: Value to set for the mobileApps property.
        """
        self._mobile_apps = value
    
    @property
    def policy_sets(self,) -> Optional[List[policy_set.PolicySet]]:
        """
        Gets the policySets property value. The PolicySet of Policies and Applications
        Returns: Optional[List[policy_set.PolicySet]]
        """
        return self._policy_sets
    
    @policy_sets.setter
    def policy_sets(self,value: Optional[List[policy_set.PolicySet]] = None) -> None:
        """
        Sets the policySets property value. The PolicySet of Policies and Applications
        Args:
            value: Value to set for the policySets property.
        """
        self._policy_sets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_collection_of_object_values("sideLoadingKeys", self.side_loading_keys)
        writer.write_object_value("symantecCodeSigningCertificate", self.symantec_code_signing_certificate)
        writer.write_collection_of_object_values("targetedManagedAppConfigurations", self.targeted_managed_app_configurations)
        writer.write_collection_of_object_values("vppTokens", self.vpp_tokens)
        writer.write_collection_of_object_values("wdacSupplementalPolicies", self.wdac_supplemental_policies)
        writer.write_collection_of_object_values("windowsInformationProtectionDeviceRegistrations", self.windows_information_protection_device_registrations)
        writer.write_collection_of_object_values("windowsInformationProtectionPolicies", self.windows_information_protection_policies)
        writer.write_collection_of_object_values("windowsInformationProtectionWipeActions", self.windows_information_protection_wipe_actions)
        writer.write_collection_of_object_values("windowsManagedAppProtections", self.windows_managed_app_protections)
        writer.write_object_value("windowsManagementApp", self.windows_management_app)
    
    @property
    def side_loading_keys(self,) -> Optional[List[side_loading_key.SideLoadingKey]]:
        """
        Gets the sideLoadingKeys property value. Side Loading Keys that are required for the Windows 8 and 8.1 Apps installation.
        Returns: Optional[List[side_loading_key.SideLoadingKey]]
        """
        return self._side_loading_keys
    
    @side_loading_keys.setter
    def side_loading_keys(self,value: Optional[List[side_loading_key.SideLoadingKey]] = None) -> None:
        """
        Sets the sideLoadingKeys property value. Side Loading Keys that are required for the Windows 8 and 8.1 Apps installation.
        Args:
            value: Value to set for the sideLoadingKeys property.
        """
        self._side_loading_keys = value
    
    @property
    def symantec_code_signing_certificate(self,) -> Optional[symantec_code_signing_certificate.SymantecCodeSigningCertificate]:
        """
        Gets the symantecCodeSigningCertificate property value. The WinPhone Symantec Code Signing Certificate.
        Returns: Optional[symantec_code_signing_certificate.SymantecCodeSigningCertificate]
        """
        return self._symantec_code_signing_certificate
    
    @symantec_code_signing_certificate.setter
    def symantec_code_signing_certificate(self,value: Optional[symantec_code_signing_certificate.SymantecCodeSigningCertificate] = None) -> None:
        """
        Sets the symantecCodeSigningCertificate property value. The WinPhone Symantec Code Signing Certificate.
        Args:
            value: Value to set for the symantecCodeSigningCertificate property.
        """
        self._symantec_code_signing_certificate = value
    
    @property
    def targeted_managed_app_configurations(self,) -> Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]]:
        """
        Gets the targetedManagedAppConfigurations property value. Targeted managed app configurations.
        Returns: Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]]
        """
        return self._targeted_managed_app_configurations
    
    @targeted_managed_app_configurations.setter
    def targeted_managed_app_configurations(self,value: Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]] = None) -> None:
        """
        Sets the targetedManagedAppConfigurations property value. Targeted managed app configurations.
        Args:
            value: Value to set for the targetedManagedAppConfigurations property.
        """
        self._targeted_managed_app_configurations = value
    
    @property
    def vpp_tokens(self,) -> Optional[List[vpp_token.VppToken]]:
        """
        Gets the vppTokens property value. List of Vpp tokens for this organization.
        Returns: Optional[List[vpp_token.VppToken]]
        """
        return self._vpp_tokens
    
    @vpp_tokens.setter
    def vpp_tokens(self,value: Optional[List[vpp_token.VppToken]] = None) -> None:
        """
        Sets the vppTokens property value. List of Vpp tokens for this organization.
        Args:
            value: Value to set for the vppTokens property.
        """
        self._vpp_tokens = value
    
    @property
    def wdac_supplemental_policies(self,) -> Optional[List[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]]:
        """
        Gets the wdacSupplementalPolicies property value. The collection of Windows Defender Application Control Supplemental Policies.
        Returns: Optional[List[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]]
        """
        return self._wdac_supplemental_policies
    
    @wdac_supplemental_policies.setter
    def wdac_supplemental_policies(self,value: Optional[List[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]] = None) -> None:
        """
        Sets the wdacSupplementalPolicies property value. The collection of Windows Defender Application Control Supplemental Policies.
        Args:
            value: Value to set for the wdacSupplementalPolicies property.
        """
        self._wdac_supplemental_policies = value
    
    @property
    def windows_information_protection_device_registrations(self,) -> Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]]:
        """
        Gets the windowsInformationProtectionDeviceRegistrations property value. Windows information protection device registrations that are not MDM enrolled.
        Returns: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]]
        """
        return self._windows_information_protection_device_registrations
    
    @windows_information_protection_device_registrations.setter
    def windows_information_protection_device_registrations(self,value: Optional[List[windows_information_protection_device_registration.WindowsInformationProtectionDeviceRegistration]] = None) -> None:
        """
        Sets the windowsInformationProtectionDeviceRegistrations property value. Windows information protection device registrations that are not MDM enrolled.
        Args:
            value: Value to set for the windowsInformationProtectionDeviceRegistrations property.
        """
        self._windows_information_protection_device_registrations = value
    
    @property
    def windows_information_protection_policies(self,) -> Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]]:
        """
        Gets the windowsInformationProtectionPolicies property value. Windows information protection for apps running on devices which are not MDM enrolled.
        Returns: Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]]
        """
        return self._windows_information_protection_policies
    
    @windows_information_protection_policies.setter
    def windows_information_protection_policies(self,value: Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]] = None) -> None:
        """
        Sets the windowsInformationProtectionPolicies property value. Windows information protection for apps running on devices which are not MDM enrolled.
        Args:
            value: Value to set for the windowsInformationProtectionPolicies property.
        """
        self._windows_information_protection_policies = value
    
    @property
    def windows_information_protection_wipe_actions(self,) -> Optional[List[windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction]]:
        """
        Gets the windowsInformationProtectionWipeActions property value. Windows information protection wipe actions.
        Returns: Optional[List[windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction]]
        """
        return self._windows_information_protection_wipe_actions
    
    @windows_information_protection_wipe_actions.setter
    def windows_information_protection_wipe_actions(self,value: Optional[List[windows_information_protection_wipe_action.WindowsInformationProtectionWipeAction]] = None) -> None:
        """
        Sets the windowsInformationProtectionWipeActions property value. Windows information protection wipe actions.
        Args:
            value: Value to set for the windowsInformationProtectionWipeActions property.
        """
        self._windows_information_protection_wipe_actions = value
    
    @property
    def windows_managed_app_protections(self,) -> Optional[List[windows_managed_app_protection.WindowsManagedAppProtection]]:
        """
        Gets the windowsManagedAppProtections property value. Windows managed app policies.
        Returns: Optional[List[windows_managed_app_protection.WindowsManagedAppProtection]]
        """
        return self._windows_managed_app_protections
    
    @windows_managed_app_protections.setter
    def windows_managed_app_protections(self,value: Optional[List[windows_managed_app_protection.WindowsManagedAppProtection]] = None) -> None:
        """
        Sets the windowsManagedAppProtections property value. Windows managed app policies.
        Args:
            value: Value to set for the windowsManagedAppProtections property.
        """
        self._windows_managed_app_protections = value
    
    @property
    def windows_management_app(self,) -> Optional[windows_management_app.WindowsManagementApp]:
        """
        Gets the windowsManagementApp property value. Windows management app.
        Returns: Optional[windows_management_app.WindowsManagementApp]
        """
        return self._windows_management_app
    
    @windows_management_app.setter
    def windows_management_app(self,value: Optional[windows_management_app.WindowsManagementApp] = None) -> None:
        """
        Sets the windowsManagementApp property value. Windows management app.
        Args:
            value: Value to set for the windowsManagementApp property.
        """
        self._windows_management_app = value
    

