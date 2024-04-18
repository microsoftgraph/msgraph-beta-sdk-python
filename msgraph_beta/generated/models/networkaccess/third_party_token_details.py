from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ThirdPartyTokenDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The issuedAtDateTime property
    issued_at_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The uniqueTokenIdentifier property
    unique_token_identifier: Optional[str] = None
    # The validFromDateTime property
    valid_from_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThirdPartyTokenDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThirdPartyTokenDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ThirdPartyTokenDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "issuedAtDateTime": lambda n : setattr(self, 'issued_at_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uniqueTokenIdentifier": lambda n : setattr(self, 'unique_token_identifier', n.get_str_value()),
            "validFromDateTime": lambda n : setattr(self, 'valid_from_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("issuedAtDateTime", self.issued_at_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uniqueTokenIdentifier", self.unique_token_identifier)
        writer.write_datetime_value("validFromDateTime", self.valid_from_date_time)
        writer.write_additional_data_value(self.additional_data)
    

