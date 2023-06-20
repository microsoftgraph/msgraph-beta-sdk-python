from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import air_print_destination, device_configuration, ios_device_features_configuration, mac_o_s_device_features_configuration

from . import device_configuration

@dataclass
class AppleDeviceFeaturesConfigurationBase(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.appleDeviceFeaturesConfigurationBase"
    # An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
    air_print_destinations: Optional[List[air_print_destination.AirPrintDestination]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleDeviceFeaturesConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleDeviceFeaturesConfigurationBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from . import ios_device_features_configuration

            return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from . import mac_o_s_device_features_configuration

            return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
        return AppleDeviceFeaturesConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import air_print_destination, device_configuration, ios_device_features_configuration, mac_o_s_device_features_configuration

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("airPrintDestinations", self.air_print_destinations)
    

