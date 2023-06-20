from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_footer, add_header, add_watermark, encrypt_content, encrypt_with_template, encrypt_with_user_defined_rights, mark_content, protect_group, protect_online_meeting_action, protect_site

@dataclass
class LabelActionBase(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LabelActionBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addFooter".casefold():
            from . import add_footer

            return add_footer.AddFooter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addHeader".casefold():
            from . import add_header

            return add_header.AddHeader()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addWatermark".casefold():
            from . import add_watermark

            return add_watermark.AddWatermark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptContent".casefold():
            from . import encrypt_content

            return encrypt_content.EncryptContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithTemplate".casefold():
            from . import encrypt_with_template

            return encrypt_with_template.EncryptWithTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithUserDefinedRights".casefold():
            from . import encrypt_with_user_defined_rights

            return encrypt_with_user_defined_rights.EncryptWithUserDefinedRights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.markContent".casefold():
            from . import mark_content

            return mark_content.MarkContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectGroup".casefold():
            from . import protect_group

            return protect_group.ProtectGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectOnlineMeetingAction".casefold():
            from . import protect_online_meeting_action

            return protect_online_meeting_action.ProtectOnlineMeetingAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectSite".casefold():
            from . import protect_site

            return protect_site.ProtectSite()
        return LabelActionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_footer, add_header, add_watermark, encrypt_content, encrypt_with_template, encrypt_with_user_defined_rights, mark_content, protect_group, protect_online_meeting_action, protect_site

        from . import add_footer, add_header, add_watermark, encrypt_content, encrypt_with_template, encrypt_with_user_defined_rights, mark_content, protect_group, protect_online_meeting_action, protect_site

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

