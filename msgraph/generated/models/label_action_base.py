from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_footer, add_header, add_watermark, encrypt_content, encrypt_with_template, encrypt_with_user_defined_rights, mark_content, protect_group, protect_online_meeting_action, protect_site

class LabelActionBase(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new labelActionBase and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name property
        self._name: Optional[str] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LabelActionBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.addFooter":
                from . import add_footer

                return add_footer.AddFooter()
            if mapping_value == "#microsoft.graph.addHeader":
                from . import add_header

                return add_header.AddHeader()
            if mapping_value == "#microsoft.graph.addWatermark":
                from . import add_watermark

                return add_watermark.AddWatermark()
            if mapping_value == "#microsoft.graph.encryptContent":
                from . import encrypt_content

                return encrypt_content.EncryptContent()
            if mapping_value == "#microsoft.graph.encryptWithTemplate":
                from . import encrypt_with_template

                return encrypt_with_template.EncryptWithTemplate()
            if mapping_value == "#microsoft.graph.encryptWithUserDefinedRights":
                from . import encrypt_with_user_defined_rights

                return encrypt_with_user_defined_rights.EncryptWithUserDefinedRights()
            if mapping_value == "#microsoft.graph.markContent":
                from . import mark_content

                return mark_content.MarkContent()
            if mapping_value == "#microsoft.graph.protectGroup":
                from . import protect_group

                return protect_group.ProtectGroup()
            if mapping_value == "#microsoft.graph.protectOnlineMeetingAction":
                from . import protect_online_meeting_action

                return protect_online_meeting_action.ProtectOnlineMeetingAction()
            if mapping_value == "#microsoft.graph.protectSite":
                from . import protect_site

                return protect_site.ProtectSite()
        return LabelActionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_footer, add_header, add_watermark, encrypt_content, encrypt_with_template, encrypt_with_user_defined_rights, mark_content, protect_group, protect_online_meeting_action, protect_site

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

