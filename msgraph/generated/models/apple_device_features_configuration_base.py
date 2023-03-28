from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import air_print_destination, device_configuration, ios_device_features_configuration, mac_o_s_device_features_configuration

from . import device_configuration

class AppleDeviceFeaturesConfigurationBase(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AppleDeviceFeaturesConfigurationBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appleDeviceFeaturesConfigurationBase"
        # An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
        self._air_print_destinations: Optional[List[air_print_destination.AirPrintDestination]] = None
    
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
            value: Value to set for the air_print_destinations property.
        """
        self._air_print_destinations = value
    
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosDeviceFeaturesConfiguration":
                from . import ios_device_features_configuration

                return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
                from . import mac_o_s_device_features_configuration

                return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
        return AppleDeviceFeaturesConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import air_print_destination, device_configuration, ios_device_features_configuration, mac_o_s_device_features_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "airPrintDestinations": lambda n : setattr(self, 'air_print_destinations', n.get_collection_of_object_values(air_print_destination.AirPrintDestination)),
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
    

