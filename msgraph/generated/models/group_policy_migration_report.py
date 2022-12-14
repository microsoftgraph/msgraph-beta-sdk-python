from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_migration_readiness = lazy_import('msgraph.generated.models.group_policy_migration_readiness')
group_policy_setting_mapping = lazy_import('msgraph.generated.models.group_policy_setting_mapping')
unsupported_group_policy_extension = lazy_import('msgraph.generated.models.unsupported_group_policy_extension')

class GroupPolicyMigrationReport(entity.Entity):
    """
    The Group Policy migration report.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyMigrationReport and sets the default values.
        """
        super().__init__()
        # The date and time at which the GroupPolicyMigrationReport was created.
        self._created_date_time: Optional[datetime] = None
        # The name of Group Policy Object from the GPO Xml Content
        self._display_name: Optional[str] = None
        # The date and time at which the GroupPolicyMigrationReport was created.
        self._group_policy_created_date_time: Optional[datetime] = None
        # The date and time at which the GroupPolicyMigrationReport was last modified.
        self._group_policy_last_modified_date_time: Optional[datetime] = None
        # The Group Policy Object GUID from GPO Xml content
        self._group_policy_object_id: Optional[Guid] = None
        # A list of group policy settings to MDM/Intune mappings.
        self._group_policy_setting_mappings: Optional[List[group_policy_setting_mapping.GroupPolicySettingMapping]] = None
        # The date and time at which the GroupPolicyMigrationReport was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Indicates if the Group Policy Object file is covered and ready for Intune migration.
        self._migration_readiness: Optional[group_policy_migration_readiness.GroupPolicyMigrationReadiness] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The distinguished name of the OU.
        self._ou_distinguished_name: Optional[str] = None
        # The list of scope tags for the configuration.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The number of Group Policy Settings supported by Intune.
        self._supported_settings_count: Optional[int] = None
        # The Percentage of Group Policy Settings supported by Intune.
        self._supported_settings_percent: Optional[int] = None
        # The Targeted in AD property from GPO Xml Content
        self._targeted_in_active_directory: Optional[bool] = None
        # The total number of Group Policy Settings from GPO file.
        self._total_settings_count: Optional[int] = None
        # A list of unsupported group policy extensions inside the Group Policy Object.
        self._unsupported_group_policy_extensions: Optional[List[unsupported_group_policy_extension.UnsupportedGroupPolicyExtension]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time at which the GroupPolicyMigrationReport was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time at which the GroupPolicyMigrationReport was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyMigrationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyMigrationReport
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyMigrationReport()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of Group Policy Object from the GPO Xml Content
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of Group Policy Object from the GPO Xml Content
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group_policy_created_date_time": lambda n : setattr(self, 'group_policy_created_date_time', n.get_datetime_value()),
            "group_policy_last_modified_date_time": lambda n : setattr(self, 'group_policy_last_modified_date_time', n.get_datetime_value()),
            "group_policy_object_id": lambda n : setattr(self, 'group_policy_object_id', n.get_object_value(Guid)),
            "group_policy_setting_mappings": lambda n : setattr(self, 'group_policy_setting_mappings', n.get_collection_of_object_values(group_policy_setting_mapping.GroupPolicySettingMapping)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "migration_readiness": lambda n : setattr(self, 'migration_readiness', n.get_enum_value(group_policy_migration_readiness.GroupPolicyMigrationReadiness)),
            "ou_distinguished_name": lambda n : setattr(self, 'ou_distinguished_name', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supported_settings_count": lambda n : setattr(self, 'supported_settings_count', n.get_int_value()),
            "supported_settings_percent": lambda n : setattr(self, 'supported_settings_percent', n.get_int_value()),
            "targeted_in_active_directory": lambda n : setattr(self, 'targeted_in_active_directory', n.get_bool_value()),
            "total_settings_count": lambda n : setattr(self, 'total_settings_count', n.get_int_value()),
            "unsupported_group_policy_extensions": lambda n : setattr(self, 'unsupported_group_policy_extensions', n.get_collection_of_object_values(unsupported_group_policy_extension.UnsupportedGroupPolicyExtension)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the groupPolicyCreatedDateTime property value. The date and time at which the GroupPolicyMigrationReport was created.
        Returns: Optional[datetime]
        """
        return self._group_policy_created_date_time
    
    @group_policy_created_date_time.setter
    def group_policy_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the groupPolicyCreatedDateTime property value. The date and time at which the GroupPolicyMigrationReport was created.
        Args:
            value: Value to set for the groupPolicyCreatedDateTime property.
        """
        self._group_policy_created_date_time = value
    
    @property
    def group_policy_last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the groupPolicyLastModifiedDateTime property value. The date and time at which the GroupPolicyMigrationReport was last modified.
        Returns: Optional[datetime]
        """
        return self._group_policy_last_modified_date_time
    
    @group_policy_last_modified_date_time.setter
    def group_policy_last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the groupPolicyLastModifiedDateTime property value. The date and time at which the GroupPolicyMigrationReport was last modified.
        Args:
            value: Value to set for the groupPolicyLastModifiedDateTime property.
        """
        self._group_policy_last_modified_date_time = value
    
    @property
    def group_policy_object_id(self,) -> Optional[Guid]:
        """
        Gets the groupPolicyObjectId property value. The Group Policy Object GUID from GPO Xml content
        Returns: Optional[Guid]
        """
        return self._group_policy_object_id
    
    @group_policy_object_id.setter
    def group_policy_object_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the groupPolicyObjectId property value. The Group Policy Object GUID from GPO Xml content
        Args:
            value: Value to set for the groupPolicyObjectId property.
        """
        self._group_policy_object_id = value
    
    @property
    def group_policy_setting_mappings(self,) -> Optional[List[group_policy_setting_mapping.GroupPolicySettingMapping]]:
        """
        Gets the groupPolicySettingMappings property value. A list of group policy settings to MDM/Intune mappings.
        Returns: Optional[List[group_policy_setting_mapping.GroupPolicySettingMapping]]
        """
        return self._group_policy_setting_mappings
    
    @group_policy_setting_mappings.setter
    def group_policy_setting_mappings(self,value: Optional[List[group_policy_setting_mapping.GroupPolicySettingMapping]] = None) -> None:
        """
        Sets the groupPolicySettingMappings property value. A list of group policy settings to MDM/Intune mappings.
        Args:
            value: Value to set for the groupPolicySettingMappings property.
        """
        self._group_policy_setting_mappings = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time at which the GroupPolicyMigrationReport was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time at which the GroupPolicyMigrationReport was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def migration_readiness(self,) -> Optional[group_policy_migration_readiness.GroupPolicyMigrationReadiness]:
        """
        Gets the migrationReadiness property value. Indicates if the Group Policy Object file is covered and ready for Intune migration.
        Returns: Optional[group_policy_migration_readiness.GroupPolicyMigrationReadiness]
        """
        return self._migration_readiness
    
    @migration_readiness.setter
    def migration_readiness(self,value: Optional[group_policy_migration_readiness.GroupPolicyMigrationReadiness] = None) -> None:
        """
        Sets the migrationReadiness property value. Indicates if the Group Policy Object file is covered and ready for Intune migration.
        Args:
            value: Value to set for the migrationReadiness property.
        """
        self._migration_readiness = value
    
    @property
    def ou_distinguished_name(self,) -> Optional[str]:
        """
        Gets the ouDistinguishedName property value. The distinguished name of the OU.
        Returns: Optional[str]
        """
        return self._ou_distinguished_name
    
    @ou_distinguished_name.setter
    def ou_distinguished_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ouDistinguishedName property value. The distinguished name of the OU.
        Args:
            value: Value to set for the ouDistinguishedName property.
        """
        self._ou_distinguished_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. The list of scope tags for the configuration.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. The list of scope tags for the configuration.
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("groupPolicyCreatedDateTime", self.group_policy_created_date_time)
        writer.write_datetime_value("groupPolicyLastModifiedDateTime", self.group_policy_last_modified_date_time)
        writer.write_object_value("groupPolicyObjectId", self.group_policy_object_id)
        writer.write_collection_of_object_values("groupPolicySettingMappings", self.group_policy_setting_mappings)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("migrationReadiness", self.migration_readiness)
        writer.write_str_value("ouDistinguishedName", self.ou_distinguished_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("supportedSettingsCount", self.supported_settings_count)
        writer.write_int_value("supportedSettingsPercent", self.supported_settings_percent)
        writer.write_bool_value("targetedInActiveDirectory", self.targeted_in_active_directory)
        writer.write_int_value("totalSettingsCount", self.total_settings_count)
        writer.write_collection_of_object_values("unsupportedGroupPolicyExtensions", self.unsupported_group_policy_extensions)
    
    @property
    def supported_settings_count(self,) -> Optional[int]:
        """
        Gets the supportedSettingsCount property value. The number of Group Policy Settings supported by Intune.
        Returns: Optional[int]
        """
        return self._supported_settings_count
    
    @supported_settings_count.setter
    def supported_settings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the supportedSettingsCount property value. The number of Group Policy Settings supported by Intune.
        Args:
            value: Value to set for the supportedSettingsCount property.
        """
        self._supported_settings_count = value
    
    @property
    def supported_settings_percent(self,) -> Optional[int]:
        """
        Gets the supportedSettingsPercent property value. The Percentage of Group Policy Settings supported by Intune.
        Returns: Optional[int]
        """
        return self._supported_settings_percent
    
    @supported_settings_percent.setter
    def supported_settings_percent(self,value: Optional[int] = None) -> None:
        """
        Sets the supportedSettingsPercent property value. The Percentage of Group Policy Settings supported by Intune.
        Args:
            value: Value to set for the supportedSettingsPercent property.
        """
        self._supported_settings_percent = value
    
    @property
    def targeted_in_active_directory(self,) -> Optional[bool]:
        """
        Gets the targetedInActiveDirectory property value. The Targeted in AD property from GPO Xml Content
        Returns: Optional[bool]
        """
        return self._targeted_in_active_directory
    
    @targeted_in_active_directory.setter
    def targeted_in_active_directory(self,value: Optional[bool] = None) -> None:
        """
        Sets the targetedInActiveDirectory property value. The Targeted in AD property from GPO Xml Content
        Args:
            value: Value to set for the targetedInActiveDirectory property.
        """
        self._targeted_in_active_directory = value
    
    @property
    def total_settings_count(self,) -> Optional[int]:
        """
        Gets the totalSettingsCount property value. The total number of Group Policy Settings from GPO file.
        Returns: Optional[int]
        """
        return self._total_settings_count
    
    @total_settings_count.setter
    def total_settings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalSettingsCount property value. The total number of Group Policy Settings from GPO file.
        Args:
            value: Value to set for the totalSettingsCount property.
        """
        self._total_settings_count = value
    
    @property
    def unsupported_group_policy_extensions(self,) -> Optional[List[unsupported_group_policy_extension.UnsupportedGroupPolicyExtension]]:
        """
        Gets the unsupportedGroupPolicyExtensions property value. A list of unsupported group policy extensions inside the Group Policy Object.
        Returns: Optional[List[unsupported_group_policy_extension.UnsupportedGroupPolicyExtension]]
        """
        return self._unsupported_group_policy_extensions
    
    @unsupported_group_policy_extensions.setter
    def unsupported_group_policy_extensions(self,value: Optional[List[unsupported_group_policy_extension.UnsupportedGroupPolicyExtension]] = None) -> None:
        """
        Sets the unsupportedGroupPolicyExtensions property value. A list of unsupported group policy extensions inside the Group Policy Object.
        Args:
            value: Value to set for the unsupportedGroupPolicyExtensions property.
        """
        self._unsupported_group_policy_extensions = value
    

