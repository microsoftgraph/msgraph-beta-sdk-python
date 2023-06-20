from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import artifact, hostname, host_component, host_cookie, host_reputation, host_tracker, ip_address, passive_dns_record

from . import artifact

@dataclass
class Host(artifact.Artifact):
    odata_type = "#microsoft.graph.security.host"
    # The hostComponents that are associated with this host.
    components: Optional[List[host_component.HostComponent]] = None
    # The hostCookies that are associated with this host.
    cookies: Optional[List[host_cookie.HostCookie]] = None
    # The first date and time when this host was observed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime] = None
    # The most recent date and time when this host was observed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime] = None
    # Passive DNS retrieval about this host.
    passive_dns: Optional[List[passive_dns_record.PassiveDnsRecord]] = None
    # Reverse passive DNS retrieval about this host.
    passive_dns_reverse: Optional[List[passive_dns_record.PassiveDnsRecord]] = None
    # Represents a calculated reputation of this host.
    reputation: Optional[host_reputation.HostReputation] = None
    # The hostTrackers that are associated with this host.
    trackers: Optional[List[host_tracker.HostTracker]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Host:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Host
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from . import hostname

            return hostname.Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from . import ip_address

            return ip_address.IpAddress()
        return Host()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import artifact, hostname, host_component, host_cookie, host_reputation, host_tracker, ip_address, passive_dns_record

        from . import artifact, hostname, host_component, host_cookie, host_reputation, host_tracker, ip_address, passive_dns_record

        fields: Dict[str, Callable[[Any], None]] = {
            "components": lambda n : setattr(self, 'components', n.get_collection_of_object_values(host_component.HostComponent)),
            "cookies": lambda n : setattr(self, 'cookies', n.get_collection_of_object_values(host_cookie.HostCookie)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "passiveDns": lambda n : setattr(self, 'passive_dns', n.get_collection_of_object_values(passive_dns_record.PassiveDnsRecord)),
            "passiveDnsReverse": lambda n : setattr(self, 'passive_dns_reverse', n.get_collection_of_object_values(passive_dns_record.PassiveDnsRecord)),
            "reputation": lambda n : setattr(self, 'reputation', n.get_object_value(host_reputation.HostReputation)),
            "trackers": lambda n : setattr(self, 'trackers', n.get_collection_of_object_values(host_tracker.HostTracker)),
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
        writer.write_collection_of_object_values("components", self.components)
        writer.write_collection_of_object_values("cookies", self.cookies)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("passiveDns", self.passive_dns)
        writer.write_collection_of_object_values("passiveDnsReverse", self.passive_dns_reverse)
        writer.write_object_value("reputation", self.reputation)
        writer.write_collection_of_object_values("trackers", self.trackers)
    

