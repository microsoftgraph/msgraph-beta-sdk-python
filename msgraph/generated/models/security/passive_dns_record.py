from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import artifact, host

from . import artifact

class PassiveDnsRecord(artifact.Artifact):
    def __init__(self,) -> None:
        """
        Instantiates a new passiveDnsRecord and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.passiveDnsRecord"
        # The artifact property
        self._artifact: Optional[artifact.Artifact] = None
        # The date and time that this passiveDnsRecord entry was collected by Microsoft. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._collected_date_time: Optional[datetime] = None
        # The date and time when this passiveDnsRecord entry was first seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._first_seen_date_time: Optional[datetime] = None
        # The date and time when this passiveDnsRecord entry was most recently seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_seen_date_time: Optional[datetime] = None
        # The parentHost property
        self._parent_host: Optional[host.Host] = None
        # The DNS record type for this passiveDnsRecord entry.
        self._record_type: Optional[str] = None
    
    @property
    def artifact(self,) -> Optional[artifact.Artifact]:
        """
        Gets the artifact property value. The artifact property
        Returns: Optional[artifact.Artifact]
        """
        return self._artifact
    
    @artifact.setter
    def artifact(self,value: Optional[artifact.Artifact] = None) -> None:
        """
        Sets the artifact property value. The artifact property
        Args:
            value: Value to set for the artifact property.
        """
        self._artifact = value
    
    @property
    def collected_date_time(self,) -> Optional[datetime]:
        """
        Gets the collectedDateTime property value. The date and time that this passiveDnsRecord entry was collected by Microsoft. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._collected_date_time
    
    @collected_date_time.setter
    def collected_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the collectedDateTime property value. The date and time that this passiveDnsRecord entry was collected by Microsoft. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the collected_date_time property.
        """
        self._collected_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PassiveDnsRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PassiveDnsRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PassiveDnsRecord()
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The date and time when this passiveDnsRecord entry was first seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The date and time when this passiveDnsRecord entry was first seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
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
            "artifact": lambda n : setattr(self, 'artifact', n.get_object_value(artifact.Artifact)),
            "collectedDateTime": lambda n : setattr(self, 'collected_date_time', n.get_datetime_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "parentHost": lambda n : setattr(self, 'parent_host', n.get_object_value(host.Host)),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The date and time when this passiveDnsRecord entry was most recently seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The date and time when this passiveDnsRecord entry was most recently seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def parent_host(self,) -> Optional[host.Host]:
        """
        Gets the parentHost property value. The parentHost property
        Returns: Optional[host.Host]
        """
        return self._parent_host
    
    @parent_host.setter
    def parent_host(self,value: Optional[host.Host] = None) -> None:
        """
        Sets the parentHost property value. The parentHost property
        Args:
            value: Value to set for the parent_host property.
        """
        self._parent_host = value
    
    @property
    def record_type(self,) -> Optional[str]:
        """
        Gets the recordType property value. The DNS record type for this passiveDnsRecord entry.
        Returns: Optional[str]
        """
        return self._record_type
    
    @record_type.setter
    def record_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recordType property value. The DNS record type for this passiveDnsRecord entry.
        Args:
            value: Value to set for the record_type property.
        """
        self._record_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("artifact", self.artifact)
        writer.write_datetime_value("collectedDateTime", self.collected_date_time)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_object_value("parentHost", self.parent_host)
        writer.write_str_value("recordType", self.record_type)
    

