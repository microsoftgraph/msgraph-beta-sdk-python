from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

inbound_domain = lazy_import('msgraph.generated.models.industry_data.inbound_domain')
industry_data_activity = lazy_import('msgraph.generated.models.industry_data.industry_data_activity')
industry_data_connector = lazy_import('msgraph.generated.models.industry_data.industry_data_connector')
year_time_period_definition = lazy_import('msgraph.generated.models.industry_data.year_time_period_definition')

class InboundFlow(industry_data_activity.IndustryDataActivity):
    def __init__(self,) -> None:
        """
        Instantiates a new InboundFlow and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.industryData.inboundFlow"
        # The dataConnector property
        self._data_connector: Optional[industry_data_connector.IndustryDataConnector] = None
        # The dataDomain property
        self._data_domain: Optional[inbound_domain.InboundDomain] = None
        # The start of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._effective_date_time: Optional[datetime] = None
        # The end of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._expiration_date_time: Optional[datetime] = None
        # The year property
        self._year: Optional[year_time_period_definition.YearTimePeriodDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InboundFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InboundFlow()
    
    @property
    def data_connector(self,) -> Optional[industry_data_connector.IndustryDataConnector]:
        """
        Gets the dataConnector property value. The dataConnector property
        Returns: Optional[industry_data_connector.IndustryDataConnector]
        """
        return self._data_connector
    
    @data_connector.setter
    def data_connector(self,value: Optional[industry_data_connector.IndustryDataConnector] = None) -> None:
        """
        Sets the dataConnector property value. The dataConnector property
        Args:
            value: Value to set for the data_connector property.
        """
        self._data_connector = value
    
    @property
    def data_domain(self,) -> Optional[inbound_domain.InboundDomain]:
        """
        Gets the dataDomain property value. The dataDomain property
        Returns: Optional[inbound_domain.InboundDomain]
        """
        return self._data_domain
    
    @data_domain.setter
    def data_domain(self,value: Optional[inbound_domain.InboundDomain] = None) -> None:
        """
        Sets the dataDomain property value. The dataDomain property
        Args:
            value: Value to set for the data_domain property.
        """
        self._data_domain = value
    
    @property
    def effective_date_time(self,) -> Optional[datetime]:
        """
        Gets the effectiveDateTime property value. The start of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._effective_date_time
    
    @effective_date_time.setter
    def effective_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the effectiveDateTime property value. The start of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the effective_date_time property.
        """
        self._effective_date_time = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The end of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The end of the time window when the flow is allowed to run. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("dataConnector", self.data_connector)
        writer.write_enum_value("dataDomain", self.data_domain)
        writer.write_datetime_value("effectiveDateTime", self.effective_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("year", self.year)
    
    @property
    def year(self,) -> Optional[year_time_period_definition.YearTimePeriodDefinition]:
        """
        Gets the year property value. The year property
        Returns: Optional[year_time_period_definition.YearTimePeriodDefinition]
        """
        return self._year
    
    @year.setter
    def year(self,value: Optional[year_time_period_definition.YearTimePeriodDefinition] = None) -> None:
        """
        Sets the year property value. The year property
        Args:
            value: Value to set for the year property.
        """
        self._year = value
    

