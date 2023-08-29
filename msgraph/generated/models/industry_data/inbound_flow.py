from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inbound_domain import InboundDomain
    from .inbound_file_flow import InboundFileFlow
    from .industry_data_activity import IndustryDataActivity
    from .industry_data_connector import IndustryDataConnector
    from .year_time_period_definition import YearTimePeriodDefinition

from .industry_data_activity import IndustryDataActivity

@dataclass
class InboundFlow(IndustryDataActivity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.inboundFlow"
    # The dataConnector property
    data_connector: Optional[IndustryDataConnector] = None
    # The dataDomain property
    data_domain: Optional[InboundDomain] = None
    # The start of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    effective_date_time: Optional[datetime.datetime] = None
    # The end of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration_date_time: Optional[datetime.datetime] = None
    # The year property
    year: Optional[YearTimePeriodDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InboundFlow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFileFlow".casefold():
            from .inbound_file_flow import InboundFileFlow

            return InboundFileFlow()
        return InboundFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .inbound_domain import InboundDomain
        from .inbound_file_flow import InboundFileFlow
        from .industry_data_activity import IndustryDataActivity
        from .industry_data_connector import IndustryDataConnector
        from .year_time_period_definition import YearTimePeriodDefinition

        from .inbound_domain import InboundDomain
        from .inbound_file_flow import InboundFileFlow
        from .industry_data_activity import IndustryDataActivity
        from .industry_data_connector import IndustryDataConnector
        from .year_time_period_definition import YearTimePeriodDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "dataConnector": lambda n : setattr(self, 'data_connector', n.get_object_value(IndustryDataConnector)),
            "dataDomain": lambda n : setattr(self, 'data_domain', n.get_enum_value(InboundDomain)),
            "effectiveDateTime": lambda n : setattr(self, 'effective_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "year": lambda n : setattr(self, 'year', n.get_object_value(YearTimePeriodDefinition)),
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
        writer.write_object_value("dataConnector", self.data_connector)
        writer.write_enum_value("dataDomain", self.data_domain)
        writer.write_datetime_value("effectiveDateTime", self.effective_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("year", self.year)
    

