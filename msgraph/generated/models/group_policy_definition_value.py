from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_configuration_type, group_policy_definition, group_policy_presentation_value

from . import entity

@dataclass
class GroupPolicyDefinitionValue(entity.Entity):
    # Group Policy Configuration Type
    configuration_type: Optional[group_policy_configuration_type.GroupPolicyConfigurationType] = None
    # The date and time the object was created.
    created_date_time: Optional[datetime] = None
    # The associated group policy definition with the value.
    definition: Optional[group_policy_definition.GroupPolicyDefinition] = None
    # Enables or disables the associated group policy definition.
    enabled: Optional[bool] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The associated group policy presentation values with the definition value.
    presentation_values: Optional[List[group_policy_presentation_value.GroupPolicyPresentationValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyDefinitionValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinitionValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyDefinitionValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_configuration_type, group_policy_definition, group_policy_presentation_value

        from . import entity, group_policy_configuration_type, group_policy_definition, group_policy_presentation_value

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationType": lambda n : setattr(self, 'configuration_type', n.get_enum_value(group_policy_configuration_type.GroupPolicyConfigurationType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(group_policy_definition.GroupPolicyDefinition)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "presentationValues": lambda n : setattr(self, 'presentation_values', n.get_collection_of_object_values(group_policy_presentation_value.GroupPolicyPresentationValue)),
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
        writer.write_enum_value("configurationType", self.configuration_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definition", self.definition)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("presentationValues", self.presentation_values)
    

