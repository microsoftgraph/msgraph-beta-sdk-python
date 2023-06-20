from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_content_footer_action, add_content_header_action, add_watermark_action, apply_label_action, custom_action, justify_action, metadata_action, protect_adhoc_action, protect_by_template_action, protect_do_not_forward_action, recommend_label_action, remove_content_footer_action, remove_content_header_action, remove_protection_action, remove_watermark_action

@dataclass
class InformationProtectionAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.addContentFooterAction".casefold():
            from . import add_content_footer_action

            return add_content_footer_action.AddContentFooterAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.addContentHeaderAction".casefold():
            from . import add_content_header_action

            return add_content_header_action.AddContentHeaderAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.addWatermarkAction".casefold():
            from . import add_watermark_action

            return add_watermark_action.AddWatermarkAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.applyLabelAction".casefold():
            from . import apply_label_action

            return apply_label_action.ApplyLabelAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.customAction".casefold():
            from . import custom_action

            return custom_action.CustomAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.justifyAction".casefold():
            from . import justify_action

            return justify_action.JustifyAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.metadataAction".casefold():
            from . import metadata_action

            return metadata_action.MetadataAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.protectAdhocAction".casefold():
            from . import protect_adhoc_action

            return protect_adhoc_action.ProtectAdhocAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.protectByTemplateAction".casefold():
            from . import protect_by_template_action

            return protect_by_template_action.ProtectByTemplateAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.protectDoNotForwardAction".casefold():
            from . import protect_do_not_forward_action

            return protect_do_not_forward_action.ProtectDoNotForwardAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.recommendLabelAction".casefold():
            from . import recommend_label_action

            return recommend_label_action.RecommendLabelAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.removeContentFooterAction".casefold():
            from . import remove_content_footer_action

            return remove_content_footer_action.RemoveContentFooterAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.removeContentHeaderAction".casefold():
            from . import remove_content_header_action

            return remove_content_header_action.RemoveContentHeaderAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.removeProtectionAction".casefold():
            from . import remove_protection_action

            return remove_protection_action.RemoveProtectionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.removeWatermarkAction".casefold():
            from . import remove_watermark_action

            return remove_watermark_action.RemoveWatermarkAction()
        return InformationProtectionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_content_footer_action, add_content_header_action, add_watermark_action, apply_label_action, custom_action, justify_action, metadata_action, protect_adhoc_action, protect_by_template_action, protect_do_not_forward_action, recommend_label_action, remove_content_footer_action, remove_content_header_action, remove_protection_action, remove_watermark_action

        from . import add_content_footer_action, add_content_header_action, add_watermark_action, apply_label_action, custom_action, justify_action, metadata_action, protect_adhoc_action, protect_by_template_action, protect_do_not_forward_action, recommend_label_action, remove_content_footer_action, remove_content_header_action, remove_protection_action, remove_watermark_action

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

