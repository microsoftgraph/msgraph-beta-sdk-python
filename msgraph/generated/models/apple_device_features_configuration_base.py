from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .air_print_destination import AirPrintDestination
    from .device_configuration import DeviceConfiguration
    from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
    from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AppleDeviceFeaturesConfigurationBase(DeviceConfiguration):
    """
    Apple device features configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appleDeviceFeaturesConfigurationBase"
    # An array of AirPrint printers that should always be shown. This collection can contain a maximum of 500 elements.
    air_print_destinations: Optional[List[AirPrintDestination]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleDeviceFeaturesConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleDeviceFeaturesConfigurationBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from .ios_device_features_configuration import IosDeviceFeaturesConfiguration

            return IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

            return MacOSDeviceFeaturesConfiguration()
        return AppleDeviceFeaturesConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .air_print_destination import AirPrintDestination
        from .device_configuration import DeviceConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

        from .air_print_destination import AirPrintDestination
        from .device_configuration import DeviceConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "airPrintDestinations": lambda n : setattr(self, 'air_print_destinations', n.get_collection_of_object_values(AirPrintDestination)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("airPrintDestinations", self.air_print_destinations)
    

