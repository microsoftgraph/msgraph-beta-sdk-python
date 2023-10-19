from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair

@dataclass
class AndroidDeviceOwnerUserFacingMessage(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a user-facing message with locale information as well as a default message to be used if the user's locale doesn't match with any of the localized messages
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The default message displayed if the user's locale doesn't match with any of the localized messages
    default_message: Optional[str] = None
    # The list of <locale, message> pairs. This collection can contain a maximum of 500 elements.
    localized_messages: Optional[List[KeyValuePair]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerUserFacingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerUserFacingMessage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerUserFacingMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair

        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultMessage": lambda n : setattr(self, 'default_message', n.get_str_value()),
            "localizedMessages": lambda n : setattr(self, 'localized_messages', n.get_collection_of_object_values(KeyValuePair)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("defaultMessage", self.default_message)
        writer.write_collection_of_object_values("localizedMessages", self.localized_messages)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

