from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_configuration_assignment = lazy_import('msgraph.generated.models.group_policy_configuration_assignment')
group_policy_configuration_ingestion_type = lazy_import('msgraph.generated.models.group_policy_configuration_ingestion_type')
group_policy_definition_value = lazy_import('msgraph.generated.models.group_policy_definition_value')

class GroupPolicyConfiguration(entity.Entity):
    """
    The group policy configuration entity contains the configured values for one or more group policy definitions.
    """
    @property
    def assignments(self,) -> Optional[List[group_policy_configuration_assignment.GroupPolicyConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the configuration.
        Returns: Optional[List[group_policy_configuration_assignment.GroupPolicyConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[group_policy_configuration_assignment.GroupPolicyConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the configuration.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyConfiguration and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the configuration.
        self._assignments: Optional[List[group_policy_configuration_assignment.GroupPolicyConfigurationAssignment]] = None
        # The date and time the object was created.
        self._created_date_time: Optional[datetime] = None
        # The list of enabled or disabled group policy definition values for the configuration.
        self._definition_values: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None
        # User provided description for the resource object.
        self._description: Optional[str] = None
        # User provided name for the resource object.
        self._display_name: Optional[str] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Group Policy Configuration Ingestion Type
        self._policy_configuration_ingestion_type: Optional[group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType] = None
        # The list of scope tags for the configuration.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the object was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyConfiguration()
    
    @property
    def definition_values(self,) -> Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]:
        """
        Gets the definitionValues property value. The list of enabled or disabled group policy definition values for the configuration.
        Returns: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]]
        """
        return self._definition_values
    
    @definition_values.setter
    def definition_values(self,value: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None) -> None:
        """
        Sets the definitionValues property value. The list of enabled or disabled group policy definition values for the configuration.
        Args:
            value: Value to set for the definitionValues property.
        """
        self._definition_values = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. User provided description for the resource object.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. User provided description for the resource object.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. User provided name for the resource object.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. User provided name for the resource object.
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(group_policy_configuration_assignment.GroupPolicyConfigurationAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definition_values": lambda n : setattr(self, 'definition_values', n.get_collection_of_object_values(group_policy_definition_value.GroupPolicyDefinitionValue)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policy_configuration_ingestion_type": lambda n : setattr(self, 'policy_configuration_ingestion_type', n.get_enum_value(group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def policy_configuration_ingestion_type(self,) -> Optional[group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType]:
        """
        Gets the policyConfigurationIngestionType property value. Group Policy Configuration Ingestion Type
        Returns: Optional[group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType]
        """
        return self._policy_configuration_ingestion_type
    
    @policy_configuration_ingestion_type.setter
    def policy_configuration_ingestion_type(self,value: Optional[group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType] = None) -> None:
        """
        Sets the policyConfigurationIngestionType property value. Group Policy Configuration Ingestion Type
        Args:
            value: Value to set for the policyConfigurationIngestionType property.
        """
        self._policy_configuration_ingestion_type = value
    
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("definitionValues", self.definition_values)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("policyConfigurationIngestionType", self.policy_configuration_ingestion_type)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

