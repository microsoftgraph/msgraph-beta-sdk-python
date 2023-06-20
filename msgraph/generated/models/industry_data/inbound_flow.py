from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_domain, inbound_file_flow, industry_data_activity, industry_data_connector, year_time_period_definition

from . import industry_data_activity

@dataclass
class InboundFlow(industry_data_activity.IndustryDataActivity):
    odata_type = "#microsoft.graph.industryData.inboundFlow"
    # The dataConnector property
    data_connector: Optional[industry_data_connector.IndustryDataConnector] = None
    # The dataDomain property
    data_domain: Optional[inbound_domain.InboundDomain] = None
    # The start of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    effective_date_time: Optional[datetime] = None
    # The end of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration_date_time: Optional[datetime] = None
    # The year property
    year: Optional[year_time_period_definition.YearTimePeriodDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InboundFlow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFileFlow".casefold():
            from . import inbound_file_flow

            return inbound_file_flow.InboundFileFlow()
        return InboundFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_domain, inbound_file_flow, industry_data_activity, industry_data_connector, year_time_period_definition

        from . import inbound_domain, inbound_file_flow, industry_data_activity, industry_data_connector, year_time_period_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "dataConnector": lambda n : setattr(self, 'data_connector', n.get_object_value(industry_data_connector.IndustryDataConnector)),
            "dataDomain": lambda n : setattr(self, 'data_domain', n.get_enum_value(inbound_domain.InboundDomain)),
            "effectiveDateTime": lambda n : setattr(self, 'effective_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "year": lambda n : setattr(self, 'year', n.get_object_value(year_time_period_definition.YearTimePeriodDefinition)),
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
        writer.write_object_value("dataConnector", self.data_connector)
        writer.write_enum_value("dataDomain", self.data_domain)
        writer.write_datetime_value("effectiveDateTime", self.effective_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("year", self.year)
    

