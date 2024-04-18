from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .device_link import DeviceLink
    from .forwarding_profile import ForwardingProfile
    from .region import Region
    from .remote_network_connectivity_configuration import RemoteNetworkConnectivityConfiguration

from ..entity import Entity

@dataclass
class RemoteNetwork(Entity):
    # Specifies the connectivity details of all device links associated with a remote network.
    connectivity_configuration: Optional[RemoteNetworkConnectivityConfiguration] = None
    # Each unique CPE device associated with a remote network is specified. Supports $expand.
    device_links: Optional[List[DeviceLink]] = None
    # Each forwarding profile associated with a remote network is specified. Supports $expand and $select.
    forwarding_profiles: Optional[List[ForwardingProfile]] = None
    # last modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region property
    region: Optional[Region] = None
    # Remote network version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteNetwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteNetwork
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RemoteNetwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region
        from .remote_network_connectivity_configuration import RemoteNetworkConnectivityConfiguration

        from ..entity import Entity
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region
        from .remote_network_connectivity_configuration import RemoteNetworkConnectivityConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "connectivityConfiguration": lambda n : setattr(self, 'connectivity_configuration', n.get_object_value(RemoteNetworkConnectivityConfiguration)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("connectivityConfiguration", self.connectivity_configuration)
        writer.write_collection_of_object_values("deviceLinks", self.device_links)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
        writer.write_str_value("version", self.version)
    

