from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .geo_coordinates import GeoCoordinates

@dataclass
class SignInLocation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
    city: Optional[str] = None
    # Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.
    country_or_region: Optional[str] = None
    # Provides the latitude, longitude and altitude where the sign-in originated.
    geo_coordinates: Optional[GeoCoordinates] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInLocation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SignInLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .geo_coordinates import GeoCoordinates

        from .geo_coordinates import GeoCoordinates

        fields: Dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(GeoCoordinates)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

