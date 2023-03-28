from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import artifact, host

from . import artifact

class HostCookie(artifact.Artifact):
    def __init__(self,) -> None:
        """
        Instantiates a new hostCookie and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.hostCookie"
        # The URI for which the cookie is valid.
        self._domain: Optional[str] = None
        # The first date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._first_seen_date_time: Optional[datetime] = None
        # The host property
        self._host: Optional[host.Host] = None
        # The most recent date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_seen_date_time: Optional[datetime] = None
        # The name of the cookie, for example, JSESSIONID or SEARCH_NAMESITE.
        self._name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostCookie:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostCookie
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostCookie()
    
    @property
    def domain(self,) -> Optional[str]:
        """
        Gets the domain property value. The URI for which the cookie is valid.
        Returns: Optional[str]
        """
        return self._domain
    
    @domain.setter
    def domain(self,value: Optional[str] = None) -> None:
        """
        Sets the domain property value. The URI for which the cookie is valid.
        Args:
            value: Value to set for the domain property.
        """
        self._domain = value
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The first date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The first date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the first_seen_date_time property.
        """
        self._first_seen_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import artifact, host

        fields: Dict[str, Callable[[Any], None]] = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(host.Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host(self,) -> Optional[host.Host]:
        """
        Gets the host property value. The host property
        Returns: Optional[host.Host]
        """
        return self._host
    
    @host.setter
    def host(self,value: Optional[host.Host] = None) -> None:
        """
        Sets the host property value. The host property
        Args:
            value: Value to set for the host property.
        """
        self._host = value
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The most recent date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The most recent date and time when this hostCookie was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the cookie, for example, JSESSIONID or SEARCH_NAMESITE.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the cookie, for example, JSESSIONID or SEARCH_NAMESITE.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("domain", self.domain)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("name", self.name)
    

