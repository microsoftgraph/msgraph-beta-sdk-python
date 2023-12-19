from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .get_mail_tips_post_request_body_mail_tips_options import GetMailTipsPostRequestBody_MailTipsOptions

@dataclass
class GetMailTipsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The EmailAddresses property
    email_addresses: Optional[List[str]] = None
    # The MailTipsOptions property
    mail_tips_options: Optional[GetMailTipsPostRequestBody_MailTipsOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetMailTipsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetMailTipsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GetMailTipsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .get_mail_tips_post_request_body_mail_tips_options import GetMailTipsPostRequestBody_MailTipsOptions

        from .get_mail_tips_post_request_body_mail_tips_options import GetMailTipsPostRequestBody_MailTipsOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "EmailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_primitive_values(str)),
            "MailTipsOptions": lambda n : setattr(self, 'mail_tips_options', n.get_enum_value(GetMailTipsPostRequestBody_MailTipsOptions)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("EmailAddresses", self.email_addresses)
        writer.write_enum_value("MailTipsOptions", self.mail_tips_options)
        writer.write_additional_data_value(self.additional_data)
    

