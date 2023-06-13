from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, group_policy_definition, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box, group_policy_uploaded_presentation

from . import entity

@dataclass
class GroupPolicyPresentation(entity.Entity):
    """
    The base entity for the display presentation of any of the additional options in a group policy definition.
    """
    # The group policy definition associated with the presentation.
    definition: Optional[group_policy_definition.GroupPolicyDefinition] = None
    # Localized text label for any presentation entity. The default value is empty.
    label: Optional[str] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationCheckBox":
                from . import group_policy_presentation_check_box

                return group_policy_presentation_check_box.GroupPolicyPresentationCheckBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationComboBox":
                from . import group_policy_presentation_combo_box

                return group_policy_presentation_combo_box.GroupPolicyPresentationComboBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationDecimalTextBox":
                from . import group_policy_presentation_decimal_text_box

                return group_policy_presentation_decimal_text_box.GroupPolicyPresentationDecimalTextBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationDropdownList":
                from . import group_policy_presentation_dropdown_list

                return group_policy_presentation_dropdown_list.GroupPolicyPresentationDropdownList()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationListBox":
                from . import group_policy_presentation_list_box

                return group_policy_presentation_list_box.GroupPolicyPresentationListBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox":
                from . import group_policy_presentation_long_decimal_text_box

                return group_policy_presentation_long_decimal_text_box.GroupPolicyPresentationLongDecimalTextBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationMultiTextBox":
                from . import group_policy_presentation_multi_text_box

                return group_policy_presentation_multi_text_box.GroupPolicyPresentationMultiTextBox()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationText":
                from . import group_policy_presentation_text

                return group_policy_presentation_text.GroupPolicyPresentationText()
            if mapping_value == "#microsoft.graph.groupPolicyPresentationTextBox":
                from . import group_policy_presentation_text_box

                return group_policy_presentation_text_box.GroupPolicyPresentationTextBox()
            if mapping_value == "#microsoft.graph.groupPolicyUploadedPresentation":
                from . import group_policy_uploaded_presentation

                return group_policy_uploaded_presentation.GroupPolicyUploadedPresentation()
        return GroupPolicyPresentation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, group_policy_definition, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box, group_policy_uploaded_presentation

        fields: Dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(group_policy_definition.GroupPolicyDefinition)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("label", self.label)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

