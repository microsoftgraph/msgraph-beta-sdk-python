from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AppleExpeditedCheckinConfigurationBase(DeviceConfiguration):
    """
    Experimental profile to increase the rate of device check-ins per day of iOS/macOS devices. This profile type is deprecated.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appleExpeditedCheckinConfigurationBase"
    # Gets or sets whether to enable expedited device check-ins.
    enable_expedited_checkin: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleExpeditedCheckinConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleExpeditedCheckinConfigurationBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosExpeditedCheckinConfiguration".casefold():
            from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

            return IosExpeditedCheckinConfiguration()
        return AppleExpeditedCheckinConfigurationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

        from .device_configuration import DeviceConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "enableExpeditedCheckin": lambda n : setattr(self, 'enable_expedited_checkin', n.get_bool_value()),
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
        writer.write_bool_value("enableExpeditedCheckin", self.enable_expedited_checkin)
    

