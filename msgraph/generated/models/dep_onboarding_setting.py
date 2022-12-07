from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dep_i_o_s_enrollment_profile = lazy_import('msgraph.generated.models.dep_i_o_s_enrollment_profile')
dep_mac_o_s_enrollment_profile = lazy_import('msgraph.generated.models.dep_mac_o_s_enrollment_profile')
dep_token_type = lazy_import('msgraph.generated.models.dep_token_type')
enrollment_profile = lazy_import('msgraph.generated.models.enrollment_profile')
entity = lazy_import('msgraph.generated.models.entity')
imported_apple_device_identity = lazy_import('msgraph.generated.models.imported_apple_device_identity')

class DepOnboardingSetting(entity.Entity):
    """
    The depOnboardingSetting represents an instance of the Apple DEP service being onboarded to Intune. The onboarded service instance manages an Apple Token used to synchronize data between Apple and Intune.
    """
    @property
    def apple_identifier(self,) -> Optional[str]:
        """
        Gets the appleIdentifier property value. The Apple ID used to obtain the current token.
        Returns: Optional[str]
        """
        return self._apple_identifier
    
    @apple_identifier.setter
    def apple_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the appleIdentifier property value. The Apple ID used to obtain the current token.
        Args:
            value: Value to set for the appleIdentifier property.
        """
        self._apple_identifier = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new depOnboardingSetting and sets the default values.
        """
        super().__init__()
        # The Apple ID used to obtain the current token.
        self._apple_identifier: Optional[str] = None
        # Consent granted for data sharing with Apple Dep Service
        self._data_sharing_consent_granted: Optional[bool] = None
        # Default iOS Enrollment Profile
        self._default_ios_enrollment_profile: Optional[dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile] = None
        # Default MacOs Enrollment Profile
        self._default_mac_os_enrollment_profile: Optional[dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile] = None
        # The enrollment profiles.
        self._enrollment_profiles: Optional[List[enrollment_profile.EnrollmentProfile]] = None
        # The imported Apple device identities.
        self._imported_apple_device_identities: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]] = None
        # When the service was onboarded.
        self._last_modified_date_time: Optional[datetime] = None
        # When the service last syned with Intune
        self._last_successful_sync_date_time: Optional[datetime] = None
        # Error code reported by Apple during last dep sync.
        self._last_sync_error_code: Optional[int] = None
        # When Intune last requested a sync.
        self._last_sync_triggered_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Whether or not the Dep token sharing is enabled with the School Data Sync service.
        self._share_token_with_school_data_sync_service: Optional[bool] = None
        # Gets synced device count
        self._synced_device_count: Optional[int] = None
        # When the token will expire.
        self._token_expiration_date_time: Optional[datetime] = None
        # Friendly Name for Dep Token
        self._token_name: Optional[str] = None
        # The tokenType property
        self._token_type: Optional[dep_token_type.DepTokenType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DepOnboardingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DepOnboardingSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DepOnboardingSetting()
    
    @property
    def data_sharing_consent_granted(self,) -> Optional[bool]:
        """
        Gets the dataSharingConsentGranted property value. Consent granted for data sharing with Apple Dep Service
        Returns: Optional[bool]
        """
        return self._data_sharing_consent_granted
    
    @data_sharing_consent_granted.setter
    def data_sharing_consent_granted(self,value: Optional[bool] = None) -> None:
        """
        Sets the dataSharingConsentGranted property value. Consent granted for data sharing with Apple Dep Service
        Args:
            value: Value to set for the dataSharingConsentGranted property.
        """
        self._data_sharing_consent_granted = value
    
    @property
    def default_ios_enrollment_profile(self,) -> Optional[dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile]:
        """
        Gets the defaultIosEnrollmentProfile property value. Default iOS Enrollment Profile
        Returns: Optional[dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile]
        """
        return self._default_ios_enrollment_profile
    
    @default_ios_enrollment_profile.setter
    def default_ios_enrollment_profile(self,value: Optional[dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile] = None) -> None:
        """
        Sets the defaultIosEnrollmentProfile property value. Default iOS Enrollment Profile
        Args:
            value: Value to set for the defaultIosEnrollmentProfile property.
        """
        self._default_ios_enrollment_profile = value
    
    @property
    def default_mac_os_enrollment_profile(self,) -> Optional[dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile]:
        """
        Gets the defaultMacOsEnrollmentProfile property value. Default MacOs Enrollment Profile
        Returns: Optional[dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile]
        """
        return self._default_mac_os_enrollment_profile
    
    @default_mac_os_enrollment_profile.setter
    def default_mac_os_enrollment_profile(self,value: Optional[dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile] = None) -> None:
        """
        Sets the defaultMacOsEnrollmentProfile property value. Default MacOs Enrollment Profile
        Args:
            value: Value to set for the defaultMacOsEnrollmentProfile property.
        """
        self._default_mac_os_enrollment_profile = value
    
    @property
    def enrollment_profiles(self,) -> Optional[List[enrollment_profile.EnrollmentProfile]]:
        """
        Gets the enrollmentProfiles property value. The enrollment profiles.
        Returns: Optional[List[enrollment_profile.EnrollmentProfile]]
        """
        return self._enrollment_profiles
    
    @enrollment_profiles.setter
    def enrollment_profiles(self,value: Optional[List[enrollment_profile.EnrollmentProfile]] = None) -> None:
        """
        Sets the enrollmentProfiles property value. The enrollment profiles.
        Args:
            value: Value to set for the enrollmentProfiles property.
        """
        self._enrollment_profiles = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_identifier": lambda n : setattr(self, 'apple_identifier', n.get_str_value()),
            "data_sharing_consent_granted": lambda n : setattr(self, 'data_sharing_consent_granted', n.get_bool_value()),
            "default_ios_enrollment_profile": lambda n : setattr(self, 'default_ios_enrollment_profile', n.get_object_value(dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile)),
            "default_mac_os_enrollment_profile": lambda n : setattr(self, 'default_mac_os_enrollment_profile', n.get_object_value(dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile)),
            "enrollment_profiles": lambda n : setattr(self, 'enrollment_profiles', n.get_collection_of_object_values(enrollment_profile.EnrollmentProfile)),
            "imported_apple_device_identities": lambda n : setattr(self, 'imported_apple_device_identities', n.get_collection_of_object_values(imported_apple_device_identity.ImportedAppleDeviceIdentity)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "last_successful_sync_date_time": lambda n : setattr(self, 'last_successful_sync_date_time', n.get_datetime_value()),
            "last_sync_error_code": lambda n : setattr(self, 'last_sync_error_code', n.get_int_value()),
            "last_sync_triggered_date_time": lambda n : setattr(self, 'last_sync_triggered_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "share_token_with_school_data_sync_service": lambda n : setattr(self, 'share_token_with_school_data_sync_service', n.get_bool_value()),
            "synced_device_count": lambda n : setattr(self, 'synced_device_count', n.get_int_value()),
            "token_expiration_date_time": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "token_name": lambda n : setattr(self, 'token_name', n.get_str_value()),
            "token_type": lambda n : setattr(self, 'token_type', n.get_enum_value(dep_token_type.DepTokenType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def imported_apple_device_identities(self,) -> Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]]:
        """
        Gets the importedAppleDeviceIdentities property value. The imported Apple device identities.
        Returns: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]]
        """
        return self._imported_apple_device_identities
    
    @imported_apple_device_identities.setter
    def imported_apple_device_identities(self,value: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]] = None) -> None:
        """
        Sets the importedAppleDeviceIdentities property value. The imported Apple device identities.
        Args:
            value: Value to set for the importedAppleDeviceIdentities property.
        """
        self._imported_apple_device_identities = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. When the service was onboarded.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. When the service was onboarded.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_successful_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSuccessfulSyncDateTime property value. When the service last syned with Intune
        Returns: Optional[datetime]
        """
        return self._last_successful_sync_date_time
    
    @last_successful_sync_date_time.setter
    def last_successful_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSuccessfulSyncDateTime property value. When the service last syned with Intune
        Args:
            value: Value to set for the lastSuccessfulSyncDateTime property.
        """
        self._last_successful_sync_date_time = value
    
    @property
    def last_sync_error_code(self,) -> Optional[int]:
        """
        Gets the lastSyncErrorCode property value. Error code reported by Apple during last dep sync.
        Returns: Optional[int]
        """
        return self._last_sync_error_code
    
    @last_sync_error_code.setter
    def last_sync_error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the lastSyncErrorCode property value. Error code reported by Apple during last dep sync.
        Args:
            value: Value to set for the lastSyncErrorCode property.
        """
        self._last_sync_error_code = value
    
    @property
    def last_sync_triggered_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncTriggeredDateTime property value. When Intune last requested a sync.
        Returns: Optional[datetime]
        """
        return self._last_sync_triggered_date_time
    
    @last_sync_triggered_date_time.setter
    def last_sync_triggered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncTriggeredDateTime property value. When Intune last requested a sync.
        Args:
            value: Value to set for the lastSyncTriggeredDateTime property.
        """
        self._last_sync_triggered_date_time = value
    
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
            value: Value to set for the roleScopeTagIds property.
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
        writer.write_str_value("appleIdentifier", self.apple_identifier)
        writer.write_bool_value("dataSharingConsentGranted", self.data_sharing_consent_granted)
        writer.write_object_value("defaultIosEnrollmentProfile", self.default_ios_enrollment_profile)
        writer.write_object_value("defaultMacOsEnrollmentProfile", self.default_mac_os_enrollment_profile)
        writer.write_collection_of_object_values("enrollmentProfiles", self.enrollment_profiles)
        writer.write_collection_of_object_values("importedAppleDeviceIdentities", self.imported_apple_device_identities)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastSuccessfulSyncDateTime", self.last_successful_sync_date_time)
        writer.write_int_value("lastSyncErrorCode", self.last_sync_error_code)
        writer.write_datetime_value("lastSyncTriggeredDateTime", self.last_sync_triggered_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("shareTokenWithSchoolDataSyncService", self.share_token_with_school_data_sync_service)
        writer.write_int_value("syncedDeviceCount", self.synced_device_count)
        writer.write_datetime_value("tokenExpirationDateTime", self.token_expiration_date_time)
        writer.write_str_value("tokenName", self.token_name)
        writer.write_enum_value("tokenType", self.token_type)
    
    @property
    def share_token_with_school_data_sync_service(self,) -> Optional[bool]:
        """
        Gets the shareTokenWithSchoolDataSyncService property value. Whether or not the Dep token sharing is enabled with the School Data Sync service.
        Returns: Optional[bool]
        """
        return self._share_token_with_school_data_sync_service
    
    @share_token_with_school_data_sync_service.setter
    def share_token_with_school_data_sync_service(self,value: Optional[bool] = None) -> None:
        """
        Sets the shareTokenWithSchoolDataSyncService property value. Whether or not the Dep token sharing is enabled with the School Data Sync service.
        Args:
            value: Value to set for the shareTokenWithSchoolDataSyncService property.
        """
        self._share_token_with_school_data_sync_service = value
    
    @property
    def synced_device_count(self,) -> Optional[int]:
        """
        Gets the syncedDeviceCount property value. Gets synced device count
        Returns: Optional[int]
        """
        return self._synced_device_count
    
    @synced_device_count.setter
    def synced_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the syncedDeviceCount property value. Gets synced device count
        Args:
            value: Value to set for the syncedDeviceCount property.
        """
        self._synced_device_count = value
    
    @property
    def token_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the tokenExpirationDateTime property value. When the token will expire.
        Returns: Optional[datetime]
        """
        return self._token_expiration_date_time
    
    @token_expiration_date_time.setter
    def token_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the tokenExpirationDateTime property value. When the token will expire.
        Args:
            value: Value to set for the tokenExpirationDateTime property.
        """
        self._token_expiration_date_time = value
    
    @property
    def token_name(self,) -> Optional[str]:
        """
        Gets the tokenName property value. Friendly Name for Dep Token
        Returns: Optional[str]
        """
        return self._token_name
    
    @token_name.setter
    def token_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenName property value. Friendly Name for Dep Token
        Args:
            value: Value to set for the tokenName property.
        """
        self._token_name = value
    
    @property
    def token_type(self,) -> Optional[dep_token_type.DepTokenType]:
        """
        Gets the tokenType property value. The tokenType property
        Returns: Optional[dep_token_type.DepTokenType]
        """
        return self._token_type
    
    @token_type.setter
    def token_type(self,value: Optional[dep_token_type.DepTokenType] = None) -> None:
        """
        Sets the tokenType property value. The tokenType property
        Args:
            value: Value to set for the tokenType property.
        """
        self._token_type = value
    

