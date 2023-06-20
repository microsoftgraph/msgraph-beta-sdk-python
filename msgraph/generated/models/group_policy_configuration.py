from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_configuration_assignment, group_policy_configuration_ingestion_type, group_policy_definition_value

from . import entity

@dataclass
class GroupPolicyConfiguration(entity.Entity):
    """
    The group policy configuration entity contains the configured values for one or more group policy definitions.
    """
    # The list of group assignments for the configuration.
    assignments: Optional[List[group_policy_configuration_assignment.GroupPolicyConfigurationAssignment]] = None
    # The date and time the object was created.
    created_date_time: Optional[datetime] = None
    # The list of enabled or disabled group policy definition values for the configuration.
    definition_values: Optional[List[group_policy_definition_value.GroupPolicyDefinitionValue]] = None
    # User provided description for the resource object.
    description: Optional[str] = None
    # User provided name for the resource object.
    display_name: Optional[str] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Group Policy Configuration Ingestion Type
    policy_configuration_ingestion_type: Optional[group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType] = None
    # The list of scope tags for the configuration.
    role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_configuration_assignment, group_policy_configuration_ingestion_type, group_policy_definition_value

        from . import entity, group_policy_configuration_assignment, group_policy_configuration_ingestion_type, group_policy_definition_value

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(group_policy_configuration_assignment.GroupPolicyConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definitionValues": lambda n : setattr(self, 'definition_values', n.get_collection_of_object_values(group_policy_definition_value.GroupPolicyDefinitionValue)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policyConfigurationIngestionType": lambda n : setattr(self, 'policy_configuration_ingestion_type', n.get_enum_value(group_policy_configuration_ingestion_type.GroupPolicyConfigurationIngestionType)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("definitionValues", self.definition_values)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("policyConfigurationIngestionType", self.policy_configuration_ingestion_type)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

