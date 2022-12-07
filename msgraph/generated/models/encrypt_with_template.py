from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

encrypt_content = lazy_import('msgraph.generated.models.encrypt_content')

class EncryptWithTemplate(encrypt_content.EncryptContent):
    @property
    def available_for_encryption(self,) -> Optional[bool]:
        """
        Gets the availableForEncryption property value. The availableForEncryption property
        Returns: Optional[bool]
        """
        return self._available_for_encryption
    
    @available_for_encryption.setter
    def available_for_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the availableForEncryption property value. The availableForEncryption property
        Args:
            value: Value to set for the availableForEncryption property.
        """
        self._available_for_encryption = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EncryptWithTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.encryptWithTemplate"
        # The availableForEncryption property
        self._available_for_encryption: Optional[bool] = None
        # The templateId property
        self._template_id: Optional[str] = None
    
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
        fields = {
            "available_for_encryption": lambda n : setattr(self, 'available_for_encryption', n.get_bool_value()),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The templateId property
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The templateId property
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    

