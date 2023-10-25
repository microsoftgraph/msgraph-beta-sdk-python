from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class InsightSummary(Entity):
    # The activeUsers property
    active_users: Optional[int] = None
    # The appId property
    app_id: Optional[str] = None
    # The authenticationCompletions property
    authentication_completions: Optional[int] = None
    # The authenticationRequests property
    authentication_requests: Optional[int] = None
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The securityTextCompletions property
    security_text_completions: Optional[int] = None
    # The securityTextRequests property
    security_text_requests: Optional[int] = None
    # The securityVoiceCompletions property
    security_voice_completions: Optional[int] = None
    # The securityVoiceRequests property
    security_voice_requests: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InsightSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsightSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InsightSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activeUsers": lambda n : setattr(self, 'active_users', n.get_int_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "authenticationCompletions": lambda n : setattr(self, 'authentication_completions', n.get_int_value()),
            "authenticationRequests": lambda n : setattr(self, 'authentication_requests', n.get_int_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "securityTextCompletions": lambda n : setattr(self, 'security_text_completions', n.get_int_value()),
            "securityTextRequests": lambda n : setattr(self, 'security_text_requests', n.get_int_value()),
            "securityVoiceCompletions": lambda n : setattr(self, 'security_voice_completions', n.get_int_value()),
            "securityVoiceRequests": lambda n : setattr(self, 'security_voice_requests', n.get_int_value()),
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
        writer.write_int_value("activeUsers", self.active_users)
        writer.write_str_value("appId", self.app_id)
        writer.write_int_value("authenticationCompletions", self.authentication_completions)
        writer.write_int_value("authenticationRequests", self.authentication_requests)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_str_value("os", self.os)
        writer.write_int_value("securityTextCompletions", self.security_text_completions)
        writer.write_int_value("securityTextRequests", self.security_text_requests)
        writer.write_int_value("securityVoiceCompletions", self.security_voice_completions)
        writer.write_int_value("securityVoiceRequests", self.security_voice_requests)
    

