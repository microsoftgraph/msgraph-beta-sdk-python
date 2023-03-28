from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_definition_value, group_policy_presentation, group_policy_presentation_value_boolean, group_policy_presentation_value_decimal, group_policy_presentation_value_list, group_policy_presentation_value_long_decimal, group_policy_presentation_value_multi_text, group_policy_presentation_value_text

from . import entity

class GroupPolicyPresentationValue(entity.Entity):
    """
    The base presentation value entity that stores the value for a single group policy presentation.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyPresentationValue and sets the default values.
        """
        super().__init__()
        # The date and time the object was created.
        self._created_date_time: Optional[datetime] = None
        # The group policy definition value associated with the presentation value.
        self._definition_value: Optional[group_policy_definition_value.GroupPolicyDefinitionValue] = None
        # The date and time the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The group policy presentation associated with the presentation value.
        self._presentation: Optional[group_policy_presentation.GroupPolicyPresentation] = None
    
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
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueBoolean":
                from . import group_policy_presentation_value_boolean

                return group_policy_presentation_value_boolean.GroupPolicyPresentationValueBoolean()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueDecimal":
                from . import group_policy_presentation_value_decimal

                return group_policy_presentation_value_decimal.GroupPolicyPresentationValueDecimal()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueList":
                from . import group_policy_presentation_value_list

                return group_policy_presentation_value_list.GroupPolicyPresentationValueList()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueLongDecimal":
                from . import group_policy_presentation_value_long_decimal

                return group_policy_presentation_value_long_decimal.GroupPolicyPresentationValueLongDecimal()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueMultiText":
                from . import group_policy_presentation_value_multi_text

                return group_policy_presentation_value_multi_text.GroupPolicyPresentationValueMultiText()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationValueText":
                from . import group_policy_presentation_value_text

                return group_policy_presentation_value_text.GroupPolicyPresentationValueText()
        return GroupPolicyPresentationValue()
    
    @property
    def definition_value(self,) -> Optional[group_policy_definition_value.GroupPolicyDefinitionValue]:
        """
        Gets the definitionValue property value. The group policy definition value associated with the presentation value.
        Returns: Optional[group_policy_definition_value.GroupPolicyDefinitionValue]
        """
        return self._definition_value
    
    @definition_value.setter
    def definition_value(self,value: Optional[group_policy_definition_value.GroupPolicyDefinitionValue] = None) -> None:
        """
        Sets the definitionValue property value. The group policy definition value associated with the presentation value.
        Args:
            value: Value to set for the definition_value property.
        """
        self._definition_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the object was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def presentation(self,) -> Optional[group_policy_presentation.GroupPolicyPresentation]:
        """
        Gets the presentation property value. The group policy presentation associated with the presentation value.
        Returns: Optional[group_policy_presentation.GroupPolicyPresentation]
        """
        return self._presentation
    
    @presentation.setter
    def presentation(self,value: Optional[group_policy_presentation.GroupPolicyPresentation] = None) -> None:
        """
        Sets the presentation property value. The group policy presentation associated with the presentation value.
        Args:
            value: Value to set for the presentation property.
        """
        self._presentation = value
    
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
        writer.write_object_value("definitionValue", self.definition_value)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("presentation", self.presentation)
    

