from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

geo_coordinates = lazy_import('msgraph.generated.models.geo_coordinates')
item_facet = lazy_import('msgraph.generated.models.item_facet')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class ItemAddress(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemAddress and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemAddress"
        # The detail property
        self._detail: Optional[physical_address.PhysicalAddress] = None
        # Friendly name the user has assigned to this address.
        self._display_name: Optional[str] = None
        # The geocoordinates of the address.
        self._geo_coordinates: Optional[geo_coordinates.GeoCoordinates] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemAddress()
    
    @property
    def detail(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the detail property value. The detail property
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the detail property value. The detail property
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Friendly name the user has assigned to this address.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Friendly name the user has assigned to this address.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def geo_coordinates(self,) -> Optional[geo_coordinates.GeoCoordinates]:
        """
        Gets the geoCoordinates property value. The geocoordinates of the address.
        Returns: Optional[geo_coordinates.GeoCoordinates]
        """
        return self._geo_coordinates
    
    @geo_coordinates.setter
    def geo_coordinates(self,value: Optional[geo_coordinates.GeoCoordinates] = None) -> None:
        """
        Sets the geoCoordinates property value. The geocoordinates of the address.
        Args:
            value: Value to set for the geoCoordinates property.
        """
        self._geo_coordinates = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(physical_address.PhysicalAddress)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geo_coordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(geo_coordinates.GeoCoordinates)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
    

