from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class IpReferenceData(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The asn property
    asn: Optional[int] = None
    # The city property
    city: Optional[str] = None
    # The countryOrRegionCode property
    country_or_region_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization property
    organization: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The vendor property
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpReferenceData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpReferenceData
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IpReferenceData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "asn": lambda n : setattr(self, 'asn', n.get_int_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegionCode": lambda n : setattr(self, 'country_or_region_code', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
        writer.write_int_value("asn", self.asn)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegionCode", self.country_or_region_code)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("state", self.state)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    

