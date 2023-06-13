from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import encrypt_content

from . import encrypt_content

@dataclass
class EncryptWithTemplate(encrypt_content.EncryptContent):
    odata_type = "#microsoft.graph.encryptWithTemplate"
    # The availableForEncryption property
    available_for_encryption: Optional[bool] = None
    # The templateId property
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EncryptWithTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EncryptWithTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EncryptWithTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import encrypt_content

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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("availableForEncryption", self.available_for_encryption)
        writer.write_str_value("templateId", self.template_id)
    

