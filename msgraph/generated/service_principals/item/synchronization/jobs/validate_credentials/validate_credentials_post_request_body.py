from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

@dataclass
class ValidateCredentialsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The applicationIdentifier property
    application_identifier: Optional[str] = None
    # The credentials property
    credentials: Optional[List[SynchronizationSecretKeyStringValuePair]] = None
    # The templateId property
    template_id: Optional[str] = None
    # The useSavedCredentials property
    use_saved_credentials: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateCredentialsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidateCredentialsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ValidateCredentialsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

        from ......models.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationIdentifier": lambda n : setattr(self, 'application_identifier', n.get_str_value()),
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(SynchronizationSecretKeyStringValuePair)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "useSavedCredentials": lambda n : setattr(self, 'use_saved_credentials', n.get_bool_value()),
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
        writer.write_str_value("applicationIdentifier", self.application_identifier)
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("templateId", self.template_id)
        writer.write_bool_value("useSavedCredentials", self.use_saved_credentials)
        writer.write_additional_data_value(self.additional_data)
    

