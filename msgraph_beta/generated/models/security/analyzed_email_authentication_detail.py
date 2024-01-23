from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyzedEmailAuthenticationDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The compositeAuthentication property
    composite_authentication: Optional[str] = None
    # The dkim property
    dkim: Optional[str] = None
    # The dmarc property
    dmarc: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The senderPolicyFramework property
    sender_policy_framework: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnalyzedEmailAuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailAuthenticationDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailAuthenticationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "compositeAuthentication": lambda n : setattr(self, 'composite_authentication', n.get_str_value()),
            "dkim": lambda n : setattr(self, 'dkim', n.get_str_value()),
            "dmarc": lambda n : setattr(self, 'dmarc', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "senderPolicyFramework": lambda n : setattr(self, 'sender_policy_framework', n.get_str_value()),
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
        writer.write_str_value("compositeAuthentication", self.composite_authentication)
        writer.write_str_value("dkim", self.dkim)
        writer.write_str_value("dmarc", self.dmarc)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("senderPolicyFramework", self.sender_policy_framework)
        writer.write_additional_data_value(self.additional_data)
    

