from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_resource = lazy_import('msgraph.generated.models.governance_resource')
governance_role_definition = lazy_import('msgraph.generated.models.governance_role_definition')
governance_rule_setting = lazy_import('msgraph.generated.models.governance_rule_setting')

class GovernanceRoleSetting(entity.Entity):
    @property
    def admin_eligible_settings(self,) -> Optional[List[governance_rule_setting.GovernanceRuleSetting]]:
        """
        Gets the adminEligibleSettings property value. The rule settings that are evaluated when an administrator tries to add an eligible role assignment.
        Returns: Optional[List[governance_rule_setting.GovernanceRuleSetting]]
        """
        return self._admin_eligible_settings
    
    @admin_eligible_settings.setter
    def admin_eligible_settings(self,value: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None) -> None:
        """
        Sets the adminEligibleSettings property value. The rule settings that are evaluated when an administrator tries to add an eligible role assignment.
        Args:
            value: Value to set for the adminEligibleSettings property.
        """
        self._admin_eligible_settings = value
    
    @property
    def admin_member_settings(self,) -> Optional[List[governance_rule_setting.GovernanceRuleSetting]]:
        """
        Gets the adminMemberSettings property value. The rule settings that are evaluated when an administrator tries to add a direct member role assignment.
        Returns: Optional[List[governance_rule_setting.GovernanceRuleSetting]]
        """
        return self._admin_member_settings
    
    @admin_member_settings.setter
    def admin_member_settings(self,value: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None) -> None:
        """
        Sets the adminMemberSettings property value. The rule settings that are evaluated when an administrator tries to add a direct member role assignment.
        Args:
            value: Value to set for the adminMemberSettings property.
        """
        self._admin_member_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new governanceRoleSetting and sets the default values.
        """
        super().__init__()
        # The rule settings that are evaluated when an administrator tries to add an eligible role assignment.
        self._admin_eligible_settings: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None
        # The rule settings that are evaluated when an administrator tries to add a direct member role assignment.
        self._admin_member_settings: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None
        # Read-only. Indicate if the roleSetting is a default roleSetting
        self._is_default: Optional[bool] = None
        # Read-only. The display name of the administrator who last updated the roleSetting.
        self._last_updated_by: Optional[str] = None
        # Read-only. The time when the role setting was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. The associated resource for this role setting.
        self._resource: Optional[governance_resource.GovernanceResource] = None
        # Required. The id of the resource that the role setting is associated with.
        self._resource_id: Optional[str] = None
        # Read-only. The role definition that is enforced with this role setting.
        self._role_definition: Optional[governance_role_definition.GovernanceRoleDefinition] = None
        # Required. The id of the role definition that the role setting is associated with.
        self._role_definition_id: Optional[str] = None
        # The rule settings that are evaluated when a user tries to add an eligible role assignment. The setting is not supported for now.
        self._user_eligible_settings: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None
        # The rule settings that are evaluated when a user tries to activate his role assignment.
        self._user_member_settings: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRoleSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceRoleSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_eligible_settings": lambda n : setattr(self, 'admin_eligible_settings', n.get_collection_of_object_values(governance_rule_setting.GovernanceRuleSetting)),
            "admin_member_settings": lambda n : setattr(self, 'admin_member_settings', n.get_collection_of_object_values(governance_rule_setting.GovernanceRuleSetting)),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "last_updated_by": lambda n : setattr(self, 'last_updated_by', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(governance_resource.GovernanceResource)),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(governance_role_definition.GovernanceRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "user_eligible_settings": lambda n : setattr(self, 'user_eligible_settings', n.get_collection_of_object_values(governance_rule_setting.GovernanceRuleSetting)),
            "user_member_settings": lambda n : setattr(self, 'user_member_settings', n.get_collection_of_object_values(governance_rule_setting.GovernanceRuleSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Read-only. Indicate if the roleSetting is a default roleSetting
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Read-only. Indicate if the roleSetting is a default roleSetting
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def last_updated_by(self,) -> Optional[str]:
        """
        Gets the lastUpdatedBy property value. Read-only. The display name of the administrator who last updated the roleSetting.
        Returns: Optional[str]
        """
        return self._last_updated_by
    
    @last_updated_by.setter
    def last_updated_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastUpdatedBy property value. Read-only. The display name of the administrator who last updated the roleSetting.
        Args:
            value: Value to set for the lastUpdatedBy property.
        """
        self._last_updated_by = value
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Read-only. The time when the role setting was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Read-only. The time when the role setting was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def resource(self,) -> Optional[governance_resource.GovernanceResource]:
        """
        Gets the resource property value. Read-only. The associated resource for this role setting.
        Returns: Optional[governance_resource.GovernanceResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[governance_resource.GovernanceResource] = None) -> None:
        """
        Sets the resource property value. Read-only. The associated resource for this role setting.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. Required. The id of the resource that the role setting is associated with.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Required. The id of the resource that the role setting is associated with.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def role_definition(self,) -> Optional[governance_role_definition.GovernanceRoleDefinition]:
        """
        Gets the roleDefinition property value. Read-only. The role definition that is enforced with this role setting.
        Returns: Optional[governance_role_definition.GovernanceRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[governance_role_definition.GovernanceRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Read-only. The role definition that is enforced with this role setting.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Required. The id of the role definition that the role setting is associated with.
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Required. The id of the role definition that the role setting is associated with.
        Args:
            value: Value to set for the roleDefinitionId property.
        """
        self._role_definition_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("adminEligibleSettings", self.admin_eligible_settings)
        writer.write_collection_of_object_values("adminMemberSettings", self.admin_member_settings)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("lastUpdatedBy", self.last_updated_by)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_collection_of_object_values("userEligibleSettings", self.user_eligible_settings)
        writer.write_collection_of_object_values("userMemberSettings", self.user_member_settings)
    
    @property
    def user_eligible_settings(self,) -> Optional[List[governance_rule_setting.GovernanceRuleSetting]]:
        """
        Gets the userEligibleSettings property value. The rule settings that are evaluated when a user tries to add an eligible role assignment. The setting is not supported for now.
        Returns: Optional[List[governance_rule_setting.GovernanceRuleSetting]]
        """
        return self._user_eligible_settings
    
    @user_eligible_settings.setter
    def user_eligible_settings(self,value: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None) -> None:
        """
        Sets the userEligibleSettings property value. The rule settings that are evaluated when a user tries to add an eligible role assignment. The setting is not supported for now.
        Args:
            value: Value to set for the userEligibleSettings property.
        """
        self._user_eligible_settings = value
    
    @property
    def user_member_settings(self,) -> Optional[List[governance_rule_setting.GovernanceRuleSetting]]:
        """
        Gets the userMemberSettings property value. The rule settings that are evaluated when a user tries to activate his role assignment.
        Returns: Optional[List[governance_rule_setting.GovernanceRuleSetting]]
        """
        return self._user_member_settings
    
    @user_member_settings.setter
    def user_member_settings(self,value: Optional[List[governance_rule_setting.GovernanceRuleSetting]] = None) -> None:
        """
        Sets the userMemberSettings property value. The rule settings that are evaluated when a user tries to activate his role assignment.
        Args:
            value: Value to set for the userMemberSettings property.
        """
        self._user_member_settings = value
    

