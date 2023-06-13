from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, group_policy_migration_readiness, group_policy_setting_mapping, unsupported_group_policy_extension

from . import entity

@dataclass
class GroupPolicyMigrationReport(entity.Entity):
    """
    The Group Policy migration report.
    """
    # The date and time at which the GroupPolicyMigrationReport was created.
    created_date_time: Optional[datetime] = None
    # The name of Group Policy Object from the GPO Xml Content
    display_name: Optional[str] = None
    # The date and time at which the GroupPolicyMigrationReport was created.
    group_policy_created_date_time: Optional[datetime] = None
    # The date and time at which the GroupPolicyMigrationReport was last modified.
    group_policy_last_modified_date_time: Optional[datetime] = None
    # The Group Policy Object GUID from GPO Xml content
    group_policy_object_id: Optional[UUID] = None
    # A list of group policy settings to MDM/Intune mappings.
    group_policy_setting_mappings: Optional[List[group_policy_setting_mapping.GroupPolicySettingMapping]] = None
    # The date and time at which the GroupPolicyMigrationReport was last modified.
    last_modified_date_time: Optional[datetime] = None
    # Indicates if the Group Policy Object file is covered and ready for Intune migration.
    migration_readiness: Optional[group_policy_migration_readiness.GroupPolicyMigrationReadiness] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The distinguished name of the OU.
    ou_distinguished_name: Optional[str] = None
    # The list of scope tags for the configuration.
    role_scope_tag_ids: Optional[List[str]] = None
    # The number of Group Policy Settings supported by Intune.
    supported_settings_count: Optional[int] = None
    # The Percentage of Group Policy Settings supported by Intune.
    supported_settings_percent: Optional[int] = None
    # The Targeted in AD property from GPO Xml Content
    targeted_in_active_directory: Optional[bool] = None
    # The total number of Group Policy Settings from GPO file.
    total_settings_count: Optional[int] = None
    # A list of unsupported group policy extensions inside the Group Policy Object.
    unsupported_group_policy_extensions: Optional[List[unsupported_group_policy_extension.UnsupportedGroupPolicyExtension]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_migration_readiness, group_policy_setting_mapping, unsupported_group_policy_extension

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupPolicyCreatedDateTime": lambda n : setattr(self, 'group_policy_created_date_time', n.get_datetime_value()),
            "groupPolicyLastModifiedDateTime": lambda n : setattr(self, 'group_policy_last_modified_date_time', n.get_datetime_value()),
            "groupPolicyObjectId": lambda n : setattr(self, 'group_policy_object_id', n.get_uuid_value()),
            "groupPolicySettingMappings": lambda n : setattr(self, 'group_policy_setting_mappings', n.get_collection_of_object_values(group_policy_setting_mapping.GroupPolicySettingMapping)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "migrationReadiness": lambda n : setattr(self, 'migration_readiness', n.get_enum_value(group_policy_migration_readiness.GroupPolicyMigrationReadiness)),
            "ouDistinguishedName": lambda n : setattr(self, 'ou_distinguished_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supportedSettingsCount": lambda n : setattr(self, 'supported_settings_count', n.get_int_value()),
            "supportedSettingsPercent": lambda n : setattr(self, 'supported_settings_percent', n.get_int_value()),
            "targetedInActiveDirectory": lambda n : setattr(self, 'targeted_in_active_directory', n.get_bool_value()),
            "totalSettingsCount": lambda n : setattr(self, 'total_settings_count', n.get_int_value()),
            "unsupportedGroupPolicyExtensions": lambda n : setattr(self, 'unsupported_group_policy_extensions', n.get_collection_of_object_values(unsupported_group_policy_extension.UnsupportedGroupPolicyExtension)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("groupPolicyCreatedDateTime", self.group_policy_created_date_time)
        writer.write_datetime_value("groupPolicyLastModifiedDateTime", self.group_policy_last_modified_date_time)
        writer.write_uuid_value("groupPolicyObjectId", self.group_policy_object_id)
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
    

