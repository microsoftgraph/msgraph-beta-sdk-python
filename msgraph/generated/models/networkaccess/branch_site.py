from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .connectivity_state import ConnectivityState
    from .device_link import DeviceLink
    from .forwarding_profile import ForwardingProfile
    from .region import Region

from ..entity import Entity

@dataclass
class BranchSite(Entity):
    # The bandwidthCapacity property
    bandwidth_capacity: Optional[int] = None
    # The connectivityState property
    connectivity_state: Optional[ConnectivityState] = None
    # The country property
    country: Optional[str] = None
    # The deviceLinks property
    device_links: Optional[List[DeviceLink]] = None
    # The forwardingProfiles property
    forwarding_profiles: Optional[List[ForwardingProfile]] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region property
    region: Optional[Region] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BranchSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BranchSite
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BranchSite()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .connectivity_state import ConnectivityState
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region

        from ..entity import Entity
        from .connectivity_state import ConnectivityState
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region

        fields: Dict[str, Callable[[Any], None]] = {
            "bandwidthCapacity": lambda n : setattr(self, 'bandwidth_capacity', n.get_int_value()),
            "connectivityState": lambda n : setattr(self, 'connectivity_state', n.get_enum_value(ConnectivityState)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "deviceLinks": lambda n : setattr(self, 'device_links', n.get_collection_of_object_values(DeviceLink)),
            "forwardingProfiles": lambda n : setattr(self, 'forwarding_profiles', n.get_collection_of_object_values(ForwardingProfile)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(Region)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_int_value("bandwidthCapacity", self.bandwidth_capacity)
        writer.write_enum_value("connectivityState", self.connectivity_state)
        writer.write_str_value("country", self.country)
        writer.write_collection_of_object_values("deviceLinks", self.device_links)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_datetime_value()("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
        writer.write_str_value("version", self.version)
    

