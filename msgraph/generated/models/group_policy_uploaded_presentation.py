from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group_policy_presentation, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box

from . import group_policy_presentation

@dataclass
class GroupPolicyUploadedPresentation(group_policy_presentation.GroupPolicyPresentation):
    odata_type = "#microsoft.graph.groupPolicyUploadedPresentation"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyUploadedPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedPresentation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationCheckBox".casefold():
            from . import group_policy_presentation_check_box

            return group_policy_presentation_check_box.GroupPolicyPresentationCheckBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationComboBox".casefold():
            from . import group_policy_presentation_combo_box

            return group_policy_presentation_combo_box.GroupPolicyPresentationComboBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDecimalTextBox".casefold():
            from . import group_policy_presentation_decimal_text_box

            return group_policy_presentation_decimal_text_box.GroupPolicyPresentationDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDropdownList".casefold():
            from . import group_policy_presentation_dropdown_list

            return group_policy_presentation_dropdown_list.GroupPolicyPresentationDropdownList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationListBox".casefold():
            from . import group_policy_presentation_list_box

            return group_policy_presentation_list_box.GroupPolicyPresentationListBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox".casefold():
            from . import group_policy_presentation_long_decimal_text_box

            return group_policy_presentation_long_decimal_text_box.GroupPolicyPresentationLongDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationMultiTextBox".casefold():
            from . import group_policy_presentation_multi_text_box

            return group_policy_presentation_multi_text_box.GroupPolicyPresentationMultiTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationText".casefold():
            from . import group_policy_presentation_text

            return group_policy_presentation_text.GroupPolicyPresentationText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationTextBox".casefold():
            from . import group_policy_presentation_text_box

            return group_policy_presentation_text_box.GroupPolicyPresentationTextBox()
        return GroupPolicyUploadedPresentation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group_policy_presentation, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box

        from . import group_policy_presentation, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box

        fields: Dict[str, Callable[[Any], None]] = {
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
    

