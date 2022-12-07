from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

air_print_destination = lazy_import('msgraph.generated.models.air_print_destination')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class AppleDeviceFeaturesConfigurationBase(device_configuration.DeviceConfiguration):
    @property
    def air_print_destinations(self,) -> Optional[List[air_print_destination.AirPrintDestination]]:
        """
        Gets the airPrintDestinations property value. An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[air_print_destination.AirPrintDestination]]
        """
        return self._air_print_destinations
    
    @air_print_destinations.setter
    def air_print_destinations(self,value: Optional[List[air_print_destination.AirPrintDestination]] = None) -> None:
        """
        Sets the airPrintDestinations property value. An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the airPrintDestinations property.
        """
        self._air_print_destinations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AppleDeviceFeaturesConfigurationBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appleDeviceFeaturesConfigurationBase"
        # An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
        self._air_print_destinations: Optional[List[air_print_destination.AirPrintDestination]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleDeviceFeaturesConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleDeviceFeaturesConfigurationBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleDeviceFeaturesConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "air_print_destinations": lambda n : setattr(self, 'air_print_destinations', n.get_collection_of_object_values(air_print_destination.AirPrintDestination)),
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
        writer.write_collection_of_object_values("airPrintDestinations", self.air_print_destinations)
    

