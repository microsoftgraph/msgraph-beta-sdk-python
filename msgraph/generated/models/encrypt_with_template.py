from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .encrypt_content import EncryptContent

from .encrypt_content import EncryptContent

@dataclass
class EncryptWithTemplate(EncryptContent):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.encryptWithTemplate"
    # The availableForEncryption property
    available_for_encryption: Optional[bool] = None
    # The templateId property
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EncryptWithTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptWithTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EncryptWithTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .encrypt_content import EncryptContent

        from .encrypt_content import EncryptContent

        fields: Dict[str, Callable[[Any], None]] = {
            "availableForEncryption": lambda n : setattr(self, 'available_for_encryption', n.get_bool_value()),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("availableForEncryption", self.available_for_encryption)
        writer.write_str_value("templateId", self.template_id)
    

