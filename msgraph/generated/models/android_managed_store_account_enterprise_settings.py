from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_enrollment_company_code = lazy_import('msgraph.generated.models.android_enrollment_company_code')
android_managed_store_account_app_sync_status = lazy_import('msgraph.generated.models.android_managed_store_account_app_sync_status')
android_managed_store_account_bind_status = lazy_import('msgraph.generated.models.android_managed_store_account_bind_status')
android_managed_store_account_enrollment_target = lazy_import('msgraph.generated.models.android_managed_store_account_enrollment_target')
entity = lazy_import('msgraph.generated.models.entity')

class AndroidManagedStoreAccountEnterpriseSettings(entity.Entity):
    @property
    def android_device_owner_fully_managed_enrollment_enabled(self,) -> Optional[bool]:
        """
        Gets the androidDeviceOwnerFullyManagedEnrollmentEnabled property value. Company codes for AndroidManagedStoreAccountEnterpriseSettings
        Returns: Optional[bool]
        """
        return self._android_device_owner_fully_managed_enrollment_enabled
    
    @android_device_owner_fully_managed_enrollment_enabled.setter
    def android_device_owner_fully_managed_enrollment_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidDeviceOwnerFullyManagedEnrollmentEnabled property value. Company codes for AndroidManagedStoreAccountEnterpriseSettings
        Args:
            value: Value to set for the androidDeviceOwnerFullyManagedEnrollmentEnabled property.
        """
        self._android_device_owner_fully_managed_enrollment_enabled = value
    
    @property
    def bind_status(self,) -> Optional[android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus]:
        """
        Gets the bindStatus property value. Bind status of the tenant with the Google EMM API
        Returns: Optional[android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus]
        """
        return self._bind_status
    
    @bind_status.setter
    def bind_status(self,value: Optional[android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus] = None) -> None:
        """
        Sets the bindStatus property value. Bind status of the tenant with the Google EMM API
        Args:
            value: Value to set for the bindStatus property.
        """
        self._bind_status = value
    
    @property
    def company_codes(self,) -> Optional[List[android_enrollment_company_code.AndroidEnrollmentCompanyCode]]:
        """
        Gets the companyCodes property value. Company codes for AndroidManagedStoreAccountEnterpriseSettings
        Returns: Optional[List[android_enrollment_company_code.AndroidEnrollmentCompanyCode]]
        """
        return self._company_codes
    
    @company_codes.setter
    def company_codes(self,value: Optional[List[android_enrollment_company_code.AndroidEnrollmentCompanyCode]] = None) -> None:
        """
        Sets the companyCodes property value. Company codes for AndroidManagedStoreAccountEnterpriseSettings
        Args:
            value: Value to set for the companyCodes property.
        """
        self._company_codes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidManagedStoreAccountEnterpriseSettings and sets the default values.
        """
        super().__init__()
        # Company codes for AndroidManagedStoreAccountEnterpriseSettings
        self._android_device_owner_fully_managed_enrollment_enabled: Optional[bool] = None
        # Bind status of the tenant with the Google EMM API
        self._bind_status: Optional[android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus] = None
        # Company codes for AndroidManagedStoreAccountEnterpriseSettings
        self._company_codes: Optional[List[android_enrollment_company_code.AndroidEnrollmentCompanyCode]] = None
        # Indicates if this account is flighting for Android Device Owner Management with CloudDPC.
        self._device_owner_management_enabled: Optional[bool] = None
        # Android for Work device management targeting type for the account
        self._enrollment_target: Optional[android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget] = None
        # Last completion time for app sync
        self._last_app_sync_date_time: Optional[datetime] = None
        # Sync status of the tenant with the Google EMM API
        self._last_app_sync_status: Optional[android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus] = None
        # Last modification time for Android enterprise settings
        self._last_modified_date_time: Optional[datetime] = None
        # Initial scope tags for MGP apps
        self._managed_google_play_initial_scope_tag_ids: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Organization name used when onboarding Android Enterprise
        self._owner_organization_name: Optional[str] = None
        # Owner UPN that created the enterprise
        self._owner_user_principal_name: Optional[str] = None
        # Specifies which AAD groups can enroll devices in Android for Work device management if enrollmentTarget is set to 'Targeted'
        self._target_group_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAccountEnterpriseSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAccountEnterpriseSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAccountEnterpriseSettings()
    
    @property
    def device_owner_management_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceOwnerManagementEnabled property value. Indicates if this account is flighting for Android Device Owner Management with CloudDPC.
        Returns: Optional[bool]
        """
        return self._device_owner_management_enabled
    
    @device_owner_management_enabled.setter
    def device_owner_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceOwnerManagementEnabled property value. Indicates if this account is flighting for Android Device Owner Management with CloudDPC.
        Args:
            value: Value to set for the deviceOwnerManagementEnabled property.
        """
        self._device_owner_management_enabled = value
    
    @property
    def enrollment_target(self,) -> Optional[android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget]:
        """
        Gets the enrollmentTarget property value. Android for Work device management targeting type for the account
        Returns: Optional[android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget]
        """
        return self._enrollment_target
    
    @enrollment_target.setter
    def enrollment_target(self,value: Optional[android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget] = None) -> None:
        """
        Sets the enrollmentTarget property value. Android for Work device management targeting type for the account
        Args:
            value: Value to set for the enrollmentTarget property.
        """
        self._enrollment_target = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_device_owner_fully_managed_enrollment_enabled": lambda n : setattr(self, 'android_device_owner_fully_managed_enrollment_enabled', n.get_bool_value()),
            "bind_status": lambda n : setattr(self, 'bind_status', n.get_enum_value(android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus)),
            "company_codes": lambda n : setattr(self, 'company_codes', n.get_collection_of_object_values(android_enrollment_company_code.AndroidEnrollmentCompanyCode)),
            "device_owner_management_enabled": lambda n : setattr(self, 'device_owner_management_enabled', n.get_bool_value()),
            "enrollment_target": lambda n : setattr(self, 'enrollment_target', n.get_enum_value(android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget)),
            "last_app_sync_date_time": lambda n : setattr(self, 'last_app_sync_date_time', n.get_datetime_value()),
            "last_app_sync_status": lambda n : setattr(self, 'last_app_sync_status', n.get_enum_value(android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managed_google_play_initial_scope_tag_ids": lambda n : setattr(self, 'managed_google_play_initial_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "owner_organization_name": lambda n : setattr(self, 'owner_organization_name', n.get_str_value()),
            "owner_user_principal_name": lambda n : setattr(self, 'owner_user_principal_name', n.get_str_value()),
            "target_group_ids": lambda n : setattr(self, 'target_group_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_app_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastAppSyncDateTime property value. Last completion time for app sync
        Returns: Optional[datetime]
        """
        return self._last_app_sync_date_time
    
    @last_app_sync_date_time.setter
    def last_app_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastAppSyncDateTime property value. Last completion time for app sync
        Args:
            value: Value to set for the lastAppSyncDateTime property.
        """
        self._last_app_sync_date_time = value
    
    @property
    def last_app_sync_status(self,) -> Optional[android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus]:
        """
        Gets the lastAppSyncStatus property value. Sync status of the tenant with the Google EMM API
        Returns: Optional[android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus]
        """
        return self._last_app_sync_status
    
    @last_app_sync_status.setter
    def last_app_sync_status(self,value: Optional[android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus] = None) -> None:
        """
        Sets the lastAppSyncStatus property value. Sync status of the tenant with the Google EMM API
        Args:
            value: Value to set for the lastAppSyncStatus property.
        """
        self._last_app_sync_status = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modification time for Android enterprise settings
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modification time for Android enterprise settings
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def managed_google_play_initial_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the managedGooglePlayInitialScopeTagIds property value. Initial scope tags for MGP apps
        Returns: Optional[List[str]]
        """
        return self._managed_google_play_initial_scope_tag_ids
    
    @managed_google_play_initial_scope_tag_ids.setter
    def managed_google_play_initial_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the managedGooglePlayInitialScopeTagIds property value. Initial scope tags for MGP apps
        Args:
            value: Value to set for the managedGooglePlayInitialScopeTagIds property.
        """
        self._managed_google_play_initial_scope_tag_ids = value
    
    @property
    def owner_organization_name(self,) -> Optional[str]:
        """
        Gets the ownerOrganizationName property value. Organization name used when onboarding Android Enterprise
        Returns: Optional[str]
        """
        return self._owner_organization_name
    
    @owner_organization_name.setter
    def owner_organization_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerOrganizationName property value. Organization name used when onboarding Android Enterprise
        Args:
            value: Value to set for the ownerOrganizationName property.
        """
        self._owner_organization_name = value
    
    @property
    def owner_user_principal_name(self,) -> Optional[str]:
        """
        Gets the ownerUserPrincipalName property value. Owner UPN that created the enterprise
        Returns: Optional[str]
        """
        return self._owner_user_principal_name
    
    @owner_user_principal_name.setter
    def owner_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerUserPrincipalName property value. Owner UPN that created the enterprise
        Args:
            value: Value to set for the ownerUserPrincipalName property.
        """
        self._owner_user_principal_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("androidDeviceOwnerFullyManagedEnrollmentEnabled", self.android_device_owner_fully_managed_enrollment_enabled)
        writer.write_enum_value("bindStatus", self.bind_status)
        writer.write_collection_of_object_values("companyCodes", self.company_codes)
        writer.write_bool_value("deviceOwnerManagementEnabled", self.device_owner_management_enabled)
        writer.write_enum_value("enrollmentTarget", self.enrollment_target)
        writer.write_datetime_value("lastAppSyncDateTime", self.last_app_sync_date_time)
        writer.write_enum_value("lastAppSyncStatus", self.last_app_sync_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("managedGooglePlayInitialScopeTagIds", self.managed_google_play_initial_scope_tag_ids)
        writer.write_str_value("ownerOrganizationName", self.owner_organization_name)
        writer.write_str_value("ownerUserPrincipalName", self.owner_user_principal_name)
        writer.write_collection_of_primitive_values("targetGroupIds", self.target_group_ids)
    
    @property
    def target_group_ids(self,) -> Optional[List[str]]:
        """
        Gets the targetGroupIds property value. Specifies which AAD groups can enroll devices in Android for Work device management if enrollmentTarget is set to 'Targeted'
        Returns: Optional[List[str]]
        """
        return self._target_group_ids
    
    @target_group_ids.setter
    def target_group_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetGroupIds property value. Specifies which AAD groups can enroll devices in Android for Work device management if enrollmentTarget is set to 'Targeted'
        Args:
            value: Value to set for the targetGroupIds property.
        """
        self._target_group_ids = value
    

