from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_content_footer_action import AddContentFooterAction
    from .add_content_header_action import AddContentHeaderAction
    from .add_watermark_action import AddWatermarkAction
    from .apply_label_action import ApplyLabelAction
    from .custom_action import CustomAction
    from .justify_action import JustifyAction
    from .metadata_action import MetadataAction
    from .protect_adhoc_action import ProtectAdhocAction
    from .protect_by_template_action import ProtectByTemplateAction
    from .protect_do_not_forward_action import ProtectDoNotForwardAction
    from .recommend_label_action import RecommendLabelAction
    from .remove_content_footer_action import RemoveContentFooterAction
    from .remove_content_header_action import RemoveContentHeaderAction
    from .remove_protection_action import RemoveProtectionAction
    from .remove_watermark_action import RemoveWatermarkAction

@dataclass
class InformationProtectionAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InformationProtectionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addContentFooterAction".casefold():
            from .add_content_footer_action import AddContentFooterAction

            return AddContentFooterAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addContentHeaderAction".casefold():
            from .add_content_header_action import AddContentHeaderAction

            return AddContentHeaderAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addWatermarkAction".casefold():
            from .add_watermark_action import AddWatermarkAction

            return AddWatermarkAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applyLabelAction".casefold():
            from .apply_label_action import ApplyLabelAction

            return ApplyLabelAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAction".casefold():
            from .custom_action import CustomAction

            return CustomAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.justifyAction".casefold():
            from .justify_action import JustifyAction

            return JustifyAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.metadataAction".casefold():
            from .metadata_action import MetadataAction

            return MetadataAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectAdhocAction".casefold():
            from .protect_adhoc_action import ProtectAdhocAction

            return ProtectAdhocAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectByTemplateAction".casefold():
            from .protect_by_template_action import ProtectByTemplateAction

            return ProtectByTemplateAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectDoNotForwardAction".casefold():
            from .protect_do_not_forward_action import ProtectDoNotForwardAction

            return ProtectDoNotForwardAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recommendLabelAction".casefold():
            from .recommend_label_action import RecommendLabelAction

            return RecommendLabelAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.removeContentFooterAction".casefold():
            from .remove_content_footer_action import RemoveContentFooterAction

            return RemoveContentFooterAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.removeContentHeaderAction".casefold():
            from .remove_content_header_action import RemoveContentHeaderAction

            return RemoveContentHeaderAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.removeProtectionAction".casefold():
            from .remove_protection_action import RemoveProtectionAction

            return RemoveProtectionAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.removeWatermarkAction".casefold():
            from .remove_watermark_action import RemoveWatermarkAction

            return RemoveWatermarkAction()
        return InformationProtectionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .add_content_footer_action import AddContentFooterAction
        from .add_content_header_action import AddContentHeaderAction
        from .add_watermark_action import AddWatermarkAction
        from .apply_label_action import ApplyLabelAction
        from .custom_action import CustomAction
        from .justify_action import JustifyAction
        from .metadata_action import MetadataAction
        from .protect_adhoc_action import ProtectAdhocAction
        from .protect_by_template_action import ProtectByTemplateAction
        from .protect_do_not_forward_action import ProtectDoNotForwardAction
        from .recommend_label_action import RecommendLabelAction
        from .remove_content_footer_action import RemoveContentFooterAction
        from .remove_content_header_action import RemoveContentHeaderAction
        from .remove_protection_action import RemoveProtectionAction
        from .remove_watermark_action import RemoveWatermarkAction

        from .add_content_footer_action import AddContentFooterAction
        from .add_content_header_action import AddContentHeaderAction
        from .add_watermark_action import AddWatermarkAction
        from .apply_label_action import ApplyLabelAction
        from .custom_action import CustomAction
        from .justify_action import JustifyAction
        from .metadata_action import MetadataAction
        from .protect_adhoc_action import ProtectAdhocAction
        from .protect_by_template_action import ProtectByTemplateAction
        from .protect_do_not_forward_action import ProtectDoNotForwardAction
        from .recommend_label_action import RecommendLabelAction
        from .remove_content_footer_action import RemoveContentFooterAction
        from .remove_content_header_action import RemoveContentHeaderAction
        from .remove_protection_action import RemoveProtectionAction
        from .remove_watermark_action import RemoveWatermarkAction

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

