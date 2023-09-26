from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host
    from .host_port_banner import HostPortBanner
    from .host_port_component import HostPortComponent
    from .host_port_protocol import HostPortProtocol
    from .host_port_status import HostPortStatus
    from .ssl_certificate import SslCertificate

from ..entity import Entity

@dataclass
class HostPort(Entity):
    # The banners property
    banners: Optional[List[HostPortBanner]] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host property
    host: Optional[Host] = None
    # The lastScanDateTime property
    last_scan_date_time: Optional[datetime.datetime] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The mostRecentSslCertificate property
    most_recent_ssl_certificate: Optional[SslCertificate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The protocol property
    protocol: Optional[HostPortProtocol] = None
    # The services property
    services: Optional[List[HostPortComponent]] = None
    # The status property
    status: Optional[HostPortStatus] = None
    # The timesObserved property
    times_observed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostPort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostPort
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HostPort()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host
        from .host_port_banner import HostPortBanner
        from .host_port_component import HostPortComponent
        from .host_port_protocol import HostPortProtocol
        from .host_port_status import HostPortStatus
        from .ssl_certificate import SslCertificate

        from ..entity import Entity
        from .host import Host
        from .host_port_banner import HostPortBanner
        from .host_port_component import HostPortComponent
        from .host_port_protocol import HostPortProtocol
        from .host_port_status import HostPortStatus
        from .ssl_certificate import SslCertificate

        fields: Dict[str, Callable[[Any], None]] = {
            "banners": lambda n : setattr(self, 'banners', n.get_collection_of_object_values(HostPortBanner)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastScanDateTime": lambda n : setattr(self, 'last_scan_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "mostRecentSslCertificate": lambda n : setattr(self, 'most_recent_ssl_certificate', n.get_object_value(SslCertificate)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(HostPortProtocol)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(HostPortComponent)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HostPortStatus)),
            "timesObserved": lambda n : setattr(self, 'times_observed', n.get_int_value()),
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
        writer.write_collection_of_object_values("banners", self.banners)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastScanDateTime", self.last_scan_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_object_value("mostRecentSslCertificate", self.most_recent_ssl_certificate)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("timesObserved", self.times_observed)
    

