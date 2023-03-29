from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import artifact, host

from . import artifact

class HostComponent(artifact.Artifact):
    def __init__(self,) -> None:
        """
        Instantiates a new hostComponent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.hostComponent"
        # The type of component that was detected (for example, Operating System, Framework, Remote Access, or Server).
        self._category: Optional[str] = None
        # The first date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._first_seen_date_time: Optional[datetime] = None
        # The host property
        self._host: Optional[host.Host] = None
        # The most recent date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_seen_date_time: Optional[datetime] = None
        # A name running on the artifact, for example, Microsoft IIS.
        self._name: Optional[str] = None
        # The component version running on the artifact, for example, v8.5. This should not be assumed to be strictly numerical.
        self._version: Optional[str] = None
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. The type of component that was detected (for example, Operating System, Framework, Remote Access, or Server).
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. The type of component that was detected (for example, Operating System, Framework, Remote Access, or Server).
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostComponent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostComponent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostComponent()
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The first date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The first date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
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
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(host.Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        Gets the lastSeenDateTime property value. The most recent date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The most recent date and time when this web component was observed by Microsoft Defender Threat Intelligence. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. A name running on the artifact, for example, Microsoft IIS.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. A name running on the artifact, for example, Microsoft IIS.
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
        writer.write_str_value("category", self.category)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The component version running on the artifact, for example, v8.5. This should not be assumed to be strictly numerical.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The component version running on the artifact, for example, v8.5. This should not be assumed to be strictly numerical.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

