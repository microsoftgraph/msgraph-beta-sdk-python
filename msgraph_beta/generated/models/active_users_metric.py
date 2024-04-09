from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ActiveUsersMetric(Entity):
    # The appId property
    app_id: Optional[str] = None
    # The appName property
    app_name: Optional[str] = None
    # The total number of users who made at least one authentication request within the specified time period.
    count: Optional[int] = None
    # The country property
    country: Optional[str] = None
    # Date of the insight.
    fact_date: Optional[datetime.date] = None
    # The language property
    language: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The os property
    os: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActiveUsersMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveUsersMetric
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ActiveUsersMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appName", self.app_name)
        writer.write_int_value("count", self.count)
        writer.write_str_value("country", self.country)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_str_value("language", self.language)
        writer.write_str_value("os", self.os)
    

