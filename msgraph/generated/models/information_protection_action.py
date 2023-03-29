from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_content_footer_action, add_content_header_action, add_watermark_action, apply_label_action, custom_action, justify_action, metadata_action, protect_adhoc_action, protect_by_template_action, protect_do_not_forward_action, recommend_label_action, remove_content_footer_action, remove_content_header_action, remove_protection_action, remove_watermark_action

class InformationProtectionAction(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new informationProtectionAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.addContentFooterAction":
                from . import add_content_footer_action

                return add_content_footer_action.AddContentFooterAction()
            if mapping_value == "#microsoft.graph.addContentHeaderAction":
                from . import add_content_header_action

                return add_content_header_action.AddContentHeaderAction()
            if mapping_value == "#microsoft.graph.addWatermarkAction":
                from . import add_watermark_action

                return add_watermark_action.AddWatermarkAction()
            if mapping_value == "#microsoft.graph.applyLabelAction":
                from . import apply_label_action

                return apply_label_action.ApplyLabelAction()
            if mapping_value == "#microsoft.graph.customAction":
                from . import custom_action

                return custom_action.CustomAction()
            if mapping_value == "#microsoft.graph.justifyAction":
                from . import justify_action

                return justify_action.JustifyAction()
            if mapping_value == "#microsoft.graph.metadataAction":
                from . import metadata_action

                return metadata_action.MetadataAction()
            if mapping_value == "#microsoft.graph.protectAdhocAction":
                from . import protect_adhoc_action

                return protect_adhoc_action.ProtectAdhocAction()
            if mapping_value == "#microsoft.graph.protectByTemplateAction":
                from . import protect_by_template_action

                return protect_by_template_action.ProtectByTemplateAction()
            if mapping_value == "#microsoft.graph.protectDoNotForwardAction":
                from . import protect_do_not_forward_action

                return protect_do_not_forward_action.ProtectDoNotForwardAction()
            if mapping_value == "#microsoft.graph.recommendLabelAction":
                from . import recommend_label_action

                return recommend_label_action.RecommendLabelAction()
            if mapping_value == "#microsoft.graph.removeContentFooterAction":
                from . import remove_content_footer_action

                return remove_content_footer_action.RemoveContentFooterAction()
            if mapping_value == "#microsoft.graph.removeContentHeaderAction":
                from . import remove_content_header_action

                return remove_content_header_action.RemoveContentHeaderAction()
            if mapping_value == "#microsoft.graph.removeProtectionAction":
                from . import remove_protection_action

                return remove_protection_action.RemoveProtectionAction()
            if mapping_value == "#microsoft.graph.removeWatermarkAction":
                from . import remove_watermark_action

                return remove_watermark_action.RemoveWatermarkAction()
        return InformationProtectionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_content_footer_action, add_content_header_action, add_watermark_action, apply_label_action, custom_action, justify_action, metadata_action, protect_adhoc_action, protect_by_template_action, protect_do_not_forward_action, recommend_label_action, remove_content_footer_action, remove_content_header_action, remove_protection_action, remove_watermark_action

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

