from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_footer import AddFooter
    from .add_header import AddHeader
    from .add_watermark import AddWatermark
    from .encrypt_content import EncryptContent
    from .encrypt_with_template import EncryptWithTemplate
    from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
    from .mark_content import MarkContent
    from .protect_group import ProtectGroup
    from .protect_online_meeting_action import ProtectOnlineMeetingAction
    from .protect_site import ProtectSite

@dataclass
class LabelActionBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LabelActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LabelActionBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addFooter".casefold():
            from .add_footer import AddFooter

            return AddFooter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addHeader".casefold():
            from .add_header import AddHeader

            return AddHeader()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addWatermark".casefold():
            from .add_watermark import AddWatermark

            return AddWatermark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptContent".casefold():
            from .encrypt_content import EncryptContent

            return EncryptContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithTemplate".casefold():
            from .encrypt_with_template import EncryptWithTemplate

            return EncryptWithTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithUserDefinedRights".casefold():
            from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights

            return EncryptWithUserDefinedRights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.markContent".casefold():
            from .mark_content import MarkContent

            return MarkContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectGroup".casefold():
            from .protect_group import ProtectGroup

            return ProtectGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectOnlineMeetingAction".casefold():
            from .protect_online_meeting_action import ProtectOnlineMeetingAction

            return ProtectOnlineMeetingAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectSite".casefold():
            from .protect_site import ProtectSite

            return ProtectSite()
        return LabelActionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .encrypt_content import EncryptContent
        from .encrypt_with_template import EncryptWithTemplate
        from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
        from .mark_content import MarkContent
        from .protect_group import ProtectGroup
        from .protect_online_meeting_action import ProtectOnlineMeetingAction
        from .protect_site import ProtectSite

        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .encrypt_content import EncryptContent
        from .encrypt_with_template import EncryptWithTemplate
        from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
        from .mark_content import MarkContent
        from .protect_group import ProtectGroup
        from .protect_online_meeting_action import ProtectOnlineMeetingAction
        from .protect_site import ProtectSite

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

