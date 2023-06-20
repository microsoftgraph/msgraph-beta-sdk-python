from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bandwidth_capacity_in_mbps, bgp_configuration, device_vendor, redundancy_configuration, tunnel_configuration
    from .. import entity

from .. import entity

@dataclass
class DeviceLink(entity.Entity):
    # The bandwidthCapacityInMbps property
    bandwidth_capacity_in_mbps: Optional[bandwidth_capacity_in_mbps.BandwidthCapacityInMbps] = None
    # The bgpConfiguration property
    bgp_configuration: Optional[bgp_configuration.BgpConfiguration] = None
    # The deviceVendor property
    device_vendor: Optional[device_vendor.DeviceVendor] = None
    # The ipAddress property
    ip_address: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The redundancyConfiguration property
    redundancy_configuration: Optional[redundancy_configuration.RedundancyConfiguration] = None
    # The tunnelConfiguration property
    tunnel_configuration: Optional[tunnel_configuration.TunnelConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLink
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bandwidth_capacity_in_mbps, bgp_configuration, device_vendor, redundancy_configuration, tunnel_configuration
        from .. import entity

        from . import bandwidth_capacity_in_mbps, bgp_configuration, device_vendor, redundancy_configuration, tunnel_configuration
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "bandwidthCapacityInMbps": lambda n : setattr(self, 'bandwidth_capacity_in_mbps', n.get_enum_value(bandwidth_capacity_in_mbps.BandwidthCapacityInMbps)),
            "bgpConfiguration": lambda n : setattr(self, 'bgp_configuration', n.get_object_value(bgp_configuration.BgpConfiguration)),
            "deviceVendor": lambda n : setattr(self, 'device_vendor', n.get_enum_value(device_vendor.DeviceVendor)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "redundancyConfiguration": lambda n : setattr(self, 'redundancy_configuration', n.get_object_value(redundancy_configuration.RedundancyConfiguration)),
            "tunnelConfiguration": lambda n : setattr(self, 'tunnel_configuration', n.get_object_value(tunnel_configuration.TunnelConfiguration)),
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
        writer.write_enum_value("bandwidthCapacityInMbps", self.bandwidth_capacity_in_mbps)
        writer.write_object_value("bgpConfiguration", self.bgp_configuration)
        writer.write_enum_value("deviceVendor", self.device_vendor)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("redundancyConfiguration", self.redundancy_configuration)
        writer.write_object_value("tunnelConfiguration", self.tunnel_configuration)
    

