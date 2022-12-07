from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alternative_security_id = lazy_import('msgraph.generated.models.alternative_security_id')
command = lazy_import('msgraph.generated.models.command')
directory_object = lazy_import('msgraph.generated.models.directory_object')
extension = lazy_import('msgraph.generated.models.extension')
on_premises_extension_attributes = lazy_import('msgraph.generated.models.on_premises_extension_attributes')
usage_right = lazy_import('msgraph.generated.models.usage_right')

class Device(directory_object.DirectoryObject):
    """
    Casts the previous resource to device.
    """
    @property
    def account_enabled(self,) -> Optional[bool]:
        """
        Gets the accountEnabled property value. true if the account is enabled; otherwise, false. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        Returns: Optional[bool]
        """
        return self._account_enabled
    
    @account_enabled.setter
    def account_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountEnabled property value. true if the account is enabled; otherwise, false. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        Args:
            value: Value to set for the accountEnabled property.
        """
        self._account_enabled = value
    
    @property
    def alternative_security_ids(self,) -> Optional[List[alternative_security_id.AlternativeSecurityId]]:
        """
        Gets the alternativeSecurityIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[alternative_security_id.AlternativeSecurityId]]
        """
        return self._alternative_security_ids
    
    @alternative_security_ids.setter
    def alternative_security_ids(self,value: Optional[List[alternative_security_id.AlternativeSecurityId]] = None) -> None:
        """
        Sets the alternativeSecurityIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the alternativeSecurityIds property.
        """
        self._alternative_security_ids = value
    
    @property
    def approximate_last_sign_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the approximateLastSignInDateTime property value. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        Returns: Optional[datetime]
        """
        return self._approximate_last_sign_in_date_time
    
    @approximate_last_sign_in_date_time.setter
    def approximate_last_sign_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the approximateLastSignInDateTime property value. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        Args:
            value: Value to set for the approximateLastSignInDateTime property.
        """
        self._approximate_last_sign_in_date_time = value
    
    @property
    def commands(self,) -> Optional[List[command.Command]]:
        """
        Gets the commands property value. Set of commands sent to this device.
        Returns: Optional[List[command.Command]]
        """
        return self._commands
    
    @commands.setter
    def commands(self,value: Optional[List[command.Command]] = None) -> None:
        """
        Sets the commands property value. Set of commands sent to this device.
        Args:
            value: Value to set for the commands property.
        """
        self._commands = value
    
    @property
    def compliance_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceExpirationDateTime property value. The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._compliance_expiration_date_time
    
    @compliance_expiration_date_time.setter
    def compliance_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceExpirationDateTime property value. The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the complianceExpirationDateTime property.
        """
        self._compliance_expiration_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new device and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.device"
        # true if the account is enabled; otherwise, false. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        self._account_enabled: Optional[bool] = None
        # For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        self._alternative_security_ids: Optional[List[alternative_security_id.AlternativeSecurityId]] = None
        # The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        self._approximate_last_sign_in_date_time: Optional[datetime] = None
        # Set of commands sent to this device.
        self._commands: Optional[List[command.Command]] = None
        # The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._compliance_expiration_date_time: Optional[datetime] = None
        # User-defined property set by Intune to automatically add devices to groups and simplify managing devices.
        self._device_category: Optional[str] = None
        # Unique Identifier set by Azure Device Registration Service at the time of registration. This is an alternate key that can be used to reference the device object. Also Supports $filter (eq, ne, not, startsWith).
        self._device_id: Optional[str] = None
        # For internal use only. Set to null.
        self._device_metadata: Optional[str] = None
        # Ownership of the device. This property is set by Intune. Possible values are: unknown, company, personal.
        self._device_ownership: Optional[str] = None
        # For internal use only.
        self._device_version: Optional[int] = None
        # The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # The on-premises domain name of Hybrid Azure AD joined devices. This property is set by Intune.
        self._domain_name: Optional[str] = None
        # Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.
        self._enrollment_profile_name: Optional[str] = None
        # Enrollment type of the device. This property is set by Intune. Possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement.
        self._enrollment_type: Optional[str] = None
        # Contains extension attributes 1-15 for the device. The individual extension attributes are not selectable. These properties are mastered in cloud and can be set during creation or update of a device object in Azure AD. Supports $filter (eq, not, startsWith, and eq on null values).
        self._extension_attributes: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes] = None
        # The collection of open extensions defined for the device. Read-only. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # List of hostNames for the device.
        self._hostnames: Optional[List[str]] = None
        # true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        self._is_compliant: Optional[bool] = None
        # true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        self._is_managed: Optional[bool] = None
        # The isManagementRestricted property
        self._is_management_restricted: Optional[bool] = None
        # true if device is rooted; false if device is jail-broken. This can only be updated by Intune.
        self._is_rooted: Optional[bool] = None
        # Form factor of device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        self._kind: Optional[str] = None
        # Management channel of the device.  This property is set by Intune. Possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.
        self._management_type: Optional[str] = None
        # Manufacturer of the device. Read-only.
        self._manufacturer: Optional[str] = None
        # Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        self._mdm_app_id: Optional[str] = None
        # Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Model of the device. Read-only.
        self._model: Optional[str] = None
        # Friendly name of a device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        self._name: Optional[str] = None
        # The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        self._on_premises_sync_enabled: Optional[bool] = None
        # The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        self._operating_system: Optional[str] = None
        # Operating system version of the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        self._operating_system_version: Optional[str] = None
        # For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, /$count eq 0, /$count ne 0.
        self._physical_ids: Optional[List[str]] = None
        # Platform of device. Only returned if user signs in with a Microsoft account as part of Project Rome. Only returned if user signs in with a Microsoft account as part of Project Rome.
        self._platform: Optional[str] = None
        # The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        self._profile_type: Optional[str] = None
        # The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        self._registered_owners: Optional[List[directory_object.DirectoryObject]] = None
        # Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        self._registered_users: Optional[List[directory_object.DirectoryObject]] = None
        # Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._registration_date_time: Optional[datetime] = None
        # Device is online or offline. Only returned if user signs in with a Microsoft account as part of Project Rome.
        self._status: Optional[str] = None
        # List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        self._system_labels: Optional[List[str]] = None
        # Groups and administrative units that this device is a member of. This operation is transitive. Supports $expand.
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Type of trust for the joined device. Read-only. Possible values: Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        self._trust_type: Optional[str] = None
        # Represents the usage rights a device has been granted.
        self._usage_rights: Optional[List[usage_right.UsageRight]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Device:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Device
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Device()
    
    @property
    def device_category(self,) -> Optional[str]:
        """
        Gets the deviceCategory property value. User-defined property set by Intune to automatically add devices to groups and simplify managing devices.
        Returns: Optional[str]
        """
        return self._device_category
    
    @device_category.setter
    def device_category(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceCategory property value. User-defined property set by Intune to automatically add devices to groups and simplify managing devices.
        Args:
            value: Value to set for the deviceCategory property.
        """
        self._device_category = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Unique Identifier set by Azure Device Registration Service at the time of registration. This is an alternate key that can be used to reference the device object. Also Supports $filter (eq, ne, not, startsWith).
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Unique Identifier set by Azure Device Registration Service at the time of registration. This is an alternate key that can be used to reference the device object. Also Supports $filter (eq, ne, not, startsWith).
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_metadata(self,) -> Optional[str]:
        """
        Gets the deviceMetadata property value. For internal use only. Set to null.
        Returns: Optional[str]
        """
        return self._device_metadata
    
    @device_metadata.setter
    def device_metadata(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceMetadata property value. For internal use only. Set to null.
        Args:
            value: Value to set for the deviceMetadata property.
        """
        self._device_metadata = value
    
    @property
    def device_ownership(self,) -> Optional[str]:
        """
        Gets the deviceOwnership property value. Ownership of the device. This property is set by Intune. Possible values are: unknown, company, personal.
        Returns: Optional[str]
        """
        return self._device_ownership
    
    @device_ownership.setter
    def device_ownership(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceOwnership property value. Ownership of the device. This property is set by Intune. Possible values are: unknown, company, personal.
        Args:
            value: Value to set for the deviceOwnership property.
        """
        self._device_ownership = value
    
    @property
    def device_version(self,) -> Optional[int]:
        """
        Gets the deviceVersion property value. For internal use only.
        Returns: Optional[int]
        """
        return self._device_version
    
    @device_version.setter
    def device_version(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceVersion property value. For internal use only.
        Args:
            value: Value to set for the deviceVersion property.
        """
        self._device_version = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. The on-premises domain name of Hybrid Azure AD joined devices. This property is set by Intune.
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. The on-premises domain name of Hybrid Azure AD joined devices. This property is set by Intune.
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    @property
    def enrollment_profile_name(self,) -> Optional[str]:
        """
        Gets the enrollmentProfileName property value. Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.
        Returns: Optional[str]
        """
        return self._enrollment_profile_name
    
    @enrollment_profile_name.setter
    def enrollment_profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentProfileName property value. Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.
        Args:
            value: Value to set for the enrollmentProfileName property.
        """
        self._enrollment_profile_name = value
    
    @property
    def enrollment_type(self,) -> Optional[str]:
        """
        Gets the enrollmentType property value. Enrollment type of the device. This property is set by Intune. Possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement.
        Returns: Optional[str]
        """
        return self._enrollment_type
    
    @enrollment_type.setter
    def enrollment_type(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentType property value. Enrollment type of the device. This property is set by Intune. Possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement.
        Args:
            value: Value to set for the enrollmentType property.
        """
        self._enrollment_type = value
    
    @property
    def extension_attributes(self,) -> Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes]:
        """
        Gets the extensionAttributes property value. Contains extension attributes 1-15 for the device. The individual extension attributes are not selectable. These properties are mastered in cloud and can be set during creation or update of a device object in Azure AD. Supports $filter (eq, not, startsWith, and eq on null values).
        Returns: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes]
        """
        return self._extension_attributes
    
    @extension_attributes.setter
    def extension_attributes(self,value: Optional[on_premises_extension_attributes.OnPremisesExtensionAttributes] = None) -> None:
        """
        Sets the extensionAttributes property value. Contains extension attributes 1-15 for the device. The individual extension attributes are not selectable. These properties are mastered in cloud and can be set during creation or update of a device object in Azure AD. Supports $filter (eq, not, startsWith, and eq on null values).
        Args:
            value: Value to set for the extensionAttributes property.
        """
        self._extension_attributes = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the device. Read-only. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the device. Read-only. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_enabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "alternative_security_ids": lambda n : setattr(self, 'alternative_security_ids', n.get_collection_of_object_values(alternative_security_id.AlternativeSecurityId)),
            "approximate_last_sign_in_date_time": lambda n : setattr(self, 'approximate_last_sign_in_date_time', n.get_datetime_value()),
            "commands": lambda n : setattr(self, 'commands', n.get_collection_of_object_values(command.Command)),
            "compliance_expiration_date_time": lambda n : setattr(self, 'compliance_expiration_date_time', n.get_datetime_value()),
            "device_category": lambda n : setattr(self, 'device_category', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_metadata": lambda n : setattr(self, 'device_metadata', n.get_str_value()),
            "device_ownership": lambda n : setattr(self, 'device_ownership', n.get_str_value()),
            "device_version": lambda n : setattr(self, 'device_version', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "enrollment_profile_name": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "enrollment_type": lambda n : setattr(self, 'enrollment_type', n.get_str_value()),
            "extension_attributes": lambda n : setattr(self, 'extension_attributes', n.get_object_value(on_premises_extension_attributes.OnPremisesExtensionAttributes)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "hostnames": lambda n : setattr(self, 'hostnames', n.get_collection_of_primitive_values(str)),
            "is_compliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "is_managed": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "is_management_restricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "is_rooted": lambda n : setattr(self, 'is_rooted', n.get_bool_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "management_type": lambda n : setattr(self, 'management_type', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdm_app_id": lambda n : setattr(self, 'mdm_app_id', n.get_str_value()),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "on_premises_last_sync_date_time": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "on_premises_sync_enabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "operating_system_version": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "physical_ids": lambda n : setattr(self, 'physical_ids', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "profile_type": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "registered_owners": lambda n : setattr(self, 'registered_owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "registered_users": lambda n : setattr(self, 'registered_users', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "registration_date_time": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "system_labels": lambda n : setattr(self, 'system_labels', n.get_collection_of_primitive_values(str)),
            "transitive_member_of": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "trust_type": lambda n : setattr(self, 'trust_type', n.get_str_value()),
            "usage_rights": lambda n : setattr(self, 'usage_rights', n.get_collection_of_object_values(usage_right.UsageRight)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hostnames(self,) -> Optional[List[str]]:
        """
        Gets the hostnames property value. List of hostNames for the device.
        Returns: Optional[List[str]]
        """
        return self._hostnames
    
    @hostnames.setter
    def hostnames(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the hostnames property value. List of hostNames for the device.
        Args:
            value: Value to set for the hostnames property.
        """
        self._hostnames = value
    
    @property
    def is_compliant(self,) -> Optional[bool]:
        """
        Gets the isCompliant property value. true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Returns: Optional[bool]
        """
        return self._is_compliant
    
    @is_compliant.setter
    def is_compliant(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompliant property value. true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the isCompliant property.
        """
        self._is_compliant = value
    
    @property
    def is_managed(self,) -> Optional[bool]:
        """
        Gets the isManaged property value. true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Returns: Optional[bool]
        """
        return self._is_managed
    
    @is_managed.setter
    def is_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManaged property value. true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the isManaged property.
        """
        self._is_managed = value
    
    @property
    def is_management_restricted(self,) -> Optional[bool]:
        """
        Gets the isManagementRestricted property value. The isManagementRestricted property
        Returns: Optional[bool]
        """
        return self._is_management_restricted
    
    @is_management_restricted.setter
    def is_management_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManagementRestricted property value. The isManagementRestricted property
        Args:
            value: Value to set for the isManagementRestricted property.
        """
        self._is_management_restricted = value
    
    @property
    def is_rooted(self,) -> Optional[bool]:
        """
        Gets the isRooted property value. true if device is rooted; false if device is jail-broken. This can only be updated by Intune.
        Returns: Optional[bool]
        """
        return self._is_rooted
    
    @is_rooted.setter
    def is_rooted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRooted property value. true if device is rooted; false if device is jail-broken. This can only be updated by Intune.
        Args:
            value: Value to set for the isRooted property.
        """
        self._is_rooted = value
    
    @property
    def kind(self,) -> Optional[str]:
        """
        Gets the kind property value. Form factor of device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Returns: Optional[str]
        """
        return self._kind
    
    @kind.setter
    def kind(self,value: Optional[str] = None) -> None:
        """
        Sets the kind property value. Form factor of device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Args:
            value: Value to set for the kind property.
        """
        self._kind = value
    
    @property
    def management_type(self,) -> Optional[str]:
        """
        Gets the managementType property value. Management channel of the device.  This property is set by Intune. Possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.
        Returns: Optional[str]
        """
        return self._management_type
    
    @management_type.setter
    def management_type(self,value: Optional[str] = None) -> None:
        """
        Sets the managementType property value. Management channel of the device.  This property is set by Intune. Possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.
        Args:
            value: Value to set for the managementType property.
        """
        self._management_type = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer of the device. Read-only.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer of the device. Read-only.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def mdm_app_id(self,) -> Optional[str]:
        """
        Gets the mdmAppId property value. Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        Returns: Optional[str]
        """
        return self._mdm_app_id
    
    @mdm_app_id.setter
    def mdm_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmAppId property value. Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        Args:
            value: Value to set for the mdmAppId property.
        """
        self._mdm_app_id = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the memberOf property.
        """
        self._member_of = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model of the device. Read-only.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model of the device. Read-only.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Friendly name of a device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Friendly name of a device. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Args:
            value: Value to set for the onPremisesLastSyncDateTime property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Args:
            value: Value to set for the onPremisesSyncEnabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    @property
    def operating_system_version(self,) -> Optional[str]:
        """
        Gets the operatingSystemVersion property value. Operating system version of the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._operating_system_version
    
    @operating_system_version.setter
    def operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemVersion property value. Operating system version of the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Args:
            value: Value to set for the operatingSystemVersion property.
        """
        self._operating_system_version = value
    
    @property
    def physical_ids(self,) -> Optional[List[str]]:
        """
        Gets the physicalIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, /$count eq 0, /$count ne 0.
        Returns: Optional[List[str]]
        """
        return self._physical_ids
    
    @physical_ids.setter
    def physical_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the physicalIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, /$count eq 0, /$count ne 0.
        Args:
            value: Value to set for the physicalIds property.
        """
        self._physical_ids = value
    
    @property
    def platform(self,) -> Optional[str]:
        """
        Gets the platform property value. Platform of device. Only returned if user signs in with a Microsoft account as part of Project Rome. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Returns: Optional[str]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[str] = None) -> None:
        """
        Sets the platform property value. Platform of device. Only returned if user signs in with a Microsoft account as part of Project Rome. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def profile_type(self,) -> Optional[str]:
        """
        Gets the profileType property value. The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        Returns: Optional[str]
        """
        return self._profile_type
    
    @profile_type.setter
    def profile_type(self,value: Optional[str] = None) -> None:
        """
        Sets the profileType property value. The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        Args:
            value: Value to set for the profileType property.
        """
        self._profile_type = value
    
    @property
    def registered_owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the registeredOwners property value. The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._registered_owners
    
    @registered_owners.setter
    def registered_owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the registeredOwners property value. The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the registeredOwners property.
        """
        self._registered_owners = value
    
    @property
    def registered_users(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the registeredUsers property value. Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._registered_users
    
    @registered_users.setter
    def registered_users(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the registeredUsers property value. Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the registeredUsers property.
        """
        self._registered_users = value
    
    @property
    def registration_date_time(self,) -> Optional[datetime]:
        """
        Gets the registrationDateTime property value. Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._registration_date_time
    
    @registration_date_time.setter
    def registration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registrationDateTime property value. Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the registrationDateTime property.
        """
        self._registration_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("alternativeSecurityIds", self.alternative_security_ids)
        writer.write_datetime_value("approximateLastSignInDateTime", self.approximate_last_sign_in_date_time)
        writer.write_collection_of_object_values("commands", self.commands)
        writer.write_datetime_value("complianceExpirationDateTime", self.compliance_expiration_date_time)
        writer.write_str_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceMetadata", self.device_metadata)
        writer.write_str_value("deviceOwnership", self.device_ownership)
        writer.write_int_value("deviceVersion", self.device_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("enrollmentProfileName", self.enrollment_profile_name)
        writer.write_str_value("enrollmentType", self.enrollment_type)
        writer.write_object_value("extensionAttributes", self.extension_attributes)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_primitive_values("hostnames", self.hostnames)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isRooted", self.is_rooted)
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("managementType", self.management_type)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmAppId", self.mdm_app_id)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_str_value("model", self.model)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_collection_of_primitive_values("physicalIds", self.physical_ids)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_collection_of_object_values("registeredOwners", self.registered_owners)
        writer.write_collection_of_object_values("registeredUsers", self.registered_users)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_str_value("status", self.status)
        writer.write_collection_of_primitive_values("systemLabels", self.system_labels)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_collection_of_object_values("usageRights", self.usage_rights)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. Device is online or offline. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. Device is online or offline. Only returned if user signs in with a Microsoft account as part of Project Rome.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def system_labels(self,) -> Optional[List[str]]:
        """
        Gets the systemLabels property value. List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._system_labels
    
    @system_labels.setter
    def system_labels(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the systemLabels property value. List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the systemLabels property.
        """
        self._system_labels = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. Groups and administrative units that this device is a member of. This operation is transitive. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. Groups and administrative units that this device is a member of. This operation is transitive. Supports $expand.
        Args:
            value: Value to set for the transitiveMemberOf property.
        """
        self._transitive_member_of = value
    
    @property
    def trust_type(self,) -> Optional[str]:
        """
        Gets the trustType property value. Type of trust for the joined device. Read-only. Possible values: Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        Returns: Optional[str]
        """
        return self._trust_type
    
    @trust_type.setter
    def trust_type(self,value: Optional[str] = None) -> None:
        """
        Sets the trustType property value. Type of trust for the joined device. Read-only. Possible values: Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        Args:
            value: Value to set for the trustType property.
        """
        self._trust_type = value
    
    @property
    def usage_rights(self,) -> Optional[List[usage_right.UsageRight]]:
        """
        Gets the usageRights property value. Represents the usage rights a device has been granted.
        Returns: Optional[List[usage_right.UsageRight]]
        """
        return self._usage_rights
    
    @usage_rights.setter
    def usage_rights(self,value: Optional[List[usage_right.UsageRight]] = None) -> None:
        """
        Sets the usageRights property value. Represents the usage rights a device has been granted.
        Args:
            value: Value to set for the usageRights property.
        """
        self._usage_rights = value
    

