from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.key_credential import KeyCredential
    from ....models.password_credential import PasswordCredential

@dataclass
class AddKeyPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The keyCredential property
    key_credential: Optional[KeyCredential] = None
    # The passwordCredential property
    password_credential: Optional[PasswordCredential] = None
    # The proof property
    proof: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddKeyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddKeyPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddKeyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.key_credential import KeyCredential
        from ....models.password_credential import PasswordCredential

        from ....models.key_credential import KeyCredential
        from ....models.password_credential import PasswordCredential

        fields: Dict[str, Callable[[Any], None]] = {
            "keyCredential": lambda n : setattr(self, 'key_credential', n.get_object_value(KeyCredential)),
            "passwordCredential": lambda n : setattr(self, 'password_credential', n.get_object_value(PasswordCredential)),
            "proof": lambda n : setattr(self, 'proof', n.get_str_value()),
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
        writer.write_object_value("keyCredential", self.key_credential)
        writer.write_object_value("passwordCredential", self.password_credential)
        writer.write_str_value("proof", self.proof)
        writer.write_additional_data_value(self.additional_data)
    

