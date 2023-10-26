from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_detail import CompanyDetail

@dataclass
class PositionDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Detail about the company or employer.
    company: Optional[CompanyDetail] = None
    # Description of the position in question.
    description: Optional[str] = None
    # When the position ended.
    end_month_year: Optional[datetime.date] = None
    # The title held when in that position.
    job_title: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role the position entailed.
    role: Optional[str] = None
    # The start month and year of the position.
    start_month_year: Optional[datetime.date] = None
    # Short summary of the position.
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PositionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PositionDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PositionDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .company_detail import CompanyDetail

        from .company_detail import CompanyDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "company": lambda n : setattr(self, 'company', n.get_object_value(CompanyDetail)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "endMonthYear": lambda n : setattr(self, 'end_month_year', n.get_date_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "startMonthYear": lambda n : setattr(self, 'start_month_year', n.get_date_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("company", self.company)
        writer.write_str_value("description", self.description)
        writer.write_date_value("endMonthYear", self.end_month_year)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("role", self.role)
        writer.write_date_value("startMonthYear", self.start_month_year)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

