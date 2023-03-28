from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group_policy_presentation, group_policy_presentation_check_box, group_policy_presentation_combo_box, group_policy_presentation_decimal_text_box, group_policy_presentation_dropdown_list, group_policy_presentation_list_box, group_policy_presentation_long_decimal_text_box, group_policy_presentation_multi_text_box, group_policy_presentation_text, group_policy_presentation_text_box

from . import group_policy_presentation

class GroupPolicyUploadedPresentation(group_policy_presentation.GroupPolicyPresentation):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyUploadedPresentation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyUploadedPresentation"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyUploadedPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedPresentation
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
        return GroupPolicyUploadedPresentation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

