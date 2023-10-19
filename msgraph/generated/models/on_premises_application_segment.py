from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cors_configuration import CorsConfiguration

@dataclass
class OnPremisesApplicationSegment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If you're configuring a traffic manager in front of multiple App Proxy application segments, contains the user-friendly URL that will point to the traffic manager.
    alternate_url: Optional[str] = None
    # CORS Rule definition for a particular application segment.
    cors_configurations: Optional[List[CorsConfiguration]] = None
    # The published external URL for the application segment; for example, https://intranet.contoso.com./
    external_url: Optional[str] = None
    # The internal URL of the application segment; for example, https://intranet/.
    internal_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesApplicationSegment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesApplicationSegment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cors_configuration import CorsConfiguration

        from .cors_configuration import CorsConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateUrl": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "corsConfigurations": lambda n : setattr(self, 'cors_configurations', n.get_collection_of_object_values(CorsConfiguration)),
            "externalUrl": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internalUrl": lambda n : setattr(self, 'internal_url', n.get_str_value()),
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
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_collection_of_object_values("corsConfigurations", self.cors_configurations)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

