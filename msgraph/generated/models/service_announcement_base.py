from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, key_value_pair, service_health_issue, service_update_message

from . import entity

class ServiceAnnouncementBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new serviceAnnouncementBase and sets the default values.
        """
        super().__init__()
        # Additional details about service event. This property doesn't support filters.
        self._details: Optional[List[key_value_pair.KeyValuePair]] = None
        # The end time of the service event.
        self._end_date_time: Optional[datetime] = None
        # The last modified time of the service event.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The start time of the service event.
        self._start_date_time: Optional[datetime] = None
        # The title of the service event.
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceAnnouncementBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncementBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.serviceHealthIssue":
                from . import service_health_issue

                return service_health_issue.ServiceHealthIssue()
            if mapping_value == "#microsoft.graph.serviceUpdateMessage":
                from . import service_update_message

                return service_update_message.ServiceUpdateMessage()
        return ServiceAnnouncementBase()
    
    @property
    def details(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the details property value. Additional details about service event. This property doesn't support filters.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the details property value. Additional details about service event. This property doesn't support filters.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The end time of the service event.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The end time of the service event.
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, key_value_pair, service_health_issue, service_update_message

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The last modified time of the service event.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The last modified time of the service event.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The start time of the service event.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The start time of the service event.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the service event.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the service event.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

