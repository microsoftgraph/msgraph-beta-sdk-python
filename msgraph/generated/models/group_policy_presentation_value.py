from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_definition_value, group_policy_presentation, group_policy_presentation_value_boolean, group_policy_presentation_value_decimal, group_policy_presentation_value_list, group_policy_presentation_value_long_decimal, group_policy_presentation_value_multi_text, group_policy_presentation_value_text

from . import entity

@dataclass
class GroupPolicyPresentationValue(entity.Entity):
    """
    The base presentation value entity that stores the value for a single group policy presentation.
    """
    # The date and time the object was created.
    created_date_time: Optional[datetime] = None
    # The group policy definition value associated with the presentation value.
    definition_value: Optional[group_policy_definition_value.GroupPolicyDefinitionValue] = None
    # The date and time the object was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The group policy presentation associated with the presentation value.
    presentation: Optional[group_policy_presentation.GroupPolicyPresentation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueBoolean".casefold():
            from . import group_policy_presentation_value_boolean

            return group_policy_presentation_value_boolean.GroupPolicyPresentationValueBoolean()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueDecimal".casefold():
            from . import group_policy_presentation_value_decimal

            return group_policy_presentation_value_decimal.GroupPolicyPresentationValueDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueList".casefold():
            from . import group_policy_presentation_value_list

            return group_policy_presentation_value_list.GroupPolicyPresentationValueList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueLongDecimal".casefold():
            from . import group_policy_presentation_value_long_decimal

            return group_policy_presentation_value_long_decimal.GroupPolicyPresentationValueLongDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueMultiText".casefold():
            from . import group_policy_presentation_value_multi_text

            return group_policy_presentation_value_multi_text.GroupPolicyPresentationValueMultiText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueText".casefold():
            from . import group_policy_presentation_value_text

            return group_policy_presentation_value_text.GroupPolicyPresentationValueText()
        return GroupPolicyPresentationValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_definition_value, group_policy_presentation, group_policy_presentation_value_boolean, group_policy_presentation_value_decimal, group_policy_presentation_value_list, group_policy_presentation_value_long_decimal, group_policy_presentation_value_multi_text, group_policy_presentation_value_text

        from . import entity, group_policy_definition_value, group_policy_presentation, group_policy_presentation_value_boolean, group_policy_presentation_value_decimal, group_policy_presentation_value_list, group_policy_presentation_value_long_decimal, group_policy_presentation_value_multi_text, group_policy_presentation_value_text

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definitionValue": lambda n : setattr(self, 'definition_value', n.get_object_value(group_policy_definition_value.GroupPolicyDefinitionValue)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "presentation": lambda n : setattr(self, 'presentation', n.get_object_value(group_policy_presentation.GroupPolicyPresentation)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definitionValue", self.definition_value)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("presentation", self.presentation)
    

