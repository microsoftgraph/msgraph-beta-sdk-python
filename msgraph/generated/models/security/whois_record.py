from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host
    from .whois_contact import WhoisContact
    from .whois_nameserver import WhoisNameserver

from ..entity import Entity

@dataclass
class WhoisRecord(Entity):
    # The abuse property
    abuse: Optional[WhoisContact] = None
    # The admin property
    admin: Optional[WhoisContact] = None
    # The billing property
    billing: Optional[WhoisContact] = None
    # The domainStatus property
    domain_status: Optional[str] = None
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host property
    host: Optional[Host] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The lastUpdateDateTime property
    last_update_date_time: Optional[datetime.datetime] = None
    # The nameservers property
    nameservers: Optional[List[WhoisNameserver]] = None
    # The noc property
    noc: Optional[WhoisContact] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rawWhoisText property
    raw_whois_text: Optional[str] = None
    # The registrant property
    registrant: Optional[WhoisContact] = None
    # The registrar property
    registrar: Optional[WhoisContact] = None
    # The registrationDateTime property
    registration_date_time: Optional[datetime.datetime] = None
    # The technical property
    technical: Optional[WhoisContact] = None
    # The whoisServer property
    whois_server: Optional[str] = None
    # The zone property
    zone: Optional[WhoisContact] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WhoisRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhoisRecord
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WhoisRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host
        from .whois_contact import WhoisContact
        from .whois_nameserver import WhoisNameserver

        from ..entity import Entity
        from .host import Host
        from .whois_contact import WhoisContact
        from .whois_nameserver import WhoisNameserver

        fields: Dict[str, Callable[[Any], None]] = {
            "abuse": lambda n : setattr(self, 'abuse', n.get_object_value(WhoisContact)),
            "admin": lambda n : setattr(self, 'admin', n.get_object_value(WhoisContact)),
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(WhoisContact)),
            "domainStatus": lambda n : setattr(self, 'domain_status', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "nameservers": lambda n : setattr(self, 'nameservers', n.get_collection_of_object_values(WhoisNameserver)),
            "noc": lambda n : setattr(self, 'noc', n.get_object_value(WhoisContact)),
            "rawWhoisText": lambda n : setattr(self, 'raw_whois_text', n.get_str_value()),
            "registrant": lambda n : setattr(self, 'registrant', n.get_object_value(WhoisContact)),
            "registrar": lambda n : setattr(self, 'registrar', n.get_object_value(WhoisContact)),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "technical": lambda n : setattr(self, 'technical', n.get_object_value(WhoisContact)),
            "whoisServer": lambda n : setattr(self, 'whois_server', n.get_str_value()),
            "zone": lambda n : setattr(self, 'zone', n.get_object_value(WhoisContact)),
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
        writer.write_object_value("abuse", self.abuse)
        writer.write_object_value("admin", self.admin)
        writer.write_object_value("billing", self.billing)
        writer.write_str_value("domainStatus", self.domain_status)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_collection_of_object_values("nameservers", self.nameservers)
        writer.write_object_value("noc", self.noc)
        writer.write_str_value("rawWhoisText", self.raw_whois_text)
        writer.write_object_value("registrant", self.registrant)
        writer.write_object_value("registrar", self.registrar)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_object_value("technical", self.technical)
        writer.write_str_value("whoisServer", self.whois_server)
        writer.write_object_value("zone", self.zone)
    

