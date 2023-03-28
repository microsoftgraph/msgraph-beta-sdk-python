from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import encrypt_with, encrypt_with_template, encrypt_with_user_defined_rights, label_action_base

from . import label_action_base

class EncryptContent(label_action_base.LabelActionBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EncryptContent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.encryptContent"
        # The encryptWith property
        self._encrypt_with: Optional[encrypt_with.EncryptWith] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EncryptContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EncryptContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.encryptWithTemplate":
                from . import encrypt_with_template

                return encrypt_with_template.EncryptWithTemplate()
            if mapping_value == "#microsoft.graph.encryptWithUserDefinedRights":
                from . import encrypt_with_user_defined_rights

                return encrypt_with_user_defined_rights.EncryptWithUserDefinedRights()
        return EncryptContent()
    
    @property
    def encrypt_with(self,) -> Optional[encrypt_with.EncryptWith]:
        """
        Gets the encryptWith property value. The encryptWith property
        Returns: Optional[encrypt_with.EncryptWith]
        """
        return self._encrypt_with
    
    @encrypt_with.setter
    def encrypt_with(self,value: Optional[encrypt_with.EncryptWith] = None) -> None:
        """
        Sets the encryptWith property value. The encryptWith property
        Args:
            value: Value to set for the encrypt_with property.
        """
        self._encrypt_with = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import encrypt_with, encrypt_with_template, encrypt_with_user_defined_rights, label_action_base

        fields: Dict[str, Callable[[Any], None]] = {
            "encryptWith": lambda n : setattr(self, 'encrypt_with', n.get_enum_value(encrypt_with.EncryptWith)),
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
        writer.write_enum_value("encryptWith", self.encrypt_with)
    

