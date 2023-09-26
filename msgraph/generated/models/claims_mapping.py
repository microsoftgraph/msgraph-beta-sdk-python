from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ClaimsMapping(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The claim that provides the display name or full name for the user. It's a required property.
    display_name: Optional[str] = None
    # The claim that provides the email address of the user.
    email: Optional[str] = None
    # The claim that provides the first name of the user.
    given_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The claim that provides the last name of the user.
    surname: Optional[str] = None
    # The claim that provides the unique identifier for the signed-in user. It is a required property.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClaimsMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClaimsMapping
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ClaimsMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

