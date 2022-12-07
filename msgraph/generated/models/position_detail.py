from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

company_detail = lazy_import('msgraph.generated.models.company_detail')

class PositionDetail(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def company(self,) -> Optional[company_detail.CompanyDetail]:
        """
        Gets the company property value. Detail about the company or employer.
        Returns: Optional[company_detail.CompanyDetail]
        """
        return self._company
    
    @company.setter
    def company(self,value: Optional[company_detail.CompanyDetail] = None) -> None:
        """
        Sets the company property value. Detail about the company or employer.
        Args:
            value: Value to set for the company property.
        """
        self._company = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new positionDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Detail about the company or employer.
        self._company: Optional[company_detail.CompanyDetail] = None
        # Description of the position in question.
        self._description: Optional[str] = None
        # When the position ended.
        self._end_month_year: Optional[Date] = None
        # The title held when in that position.
        self._job_title: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The role the position entailed.
        self._role: Optional[str] = None
        # The start month and year of the position.
        self._start_month_year: Optional[Date] = None
        # Short summary of the position.
        self._summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PositionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PositionDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PositionDetail()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the position in question.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the position in question.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def end_month_year(self,) -> Optional[Date]:
        """
        Gets the endMonthYear property value. When the position ended.
        Returns: Optional[Date]
        """
        return self._end_month_year
    
    @end_month_year.setter
    def end_month_year(self,value: Optional[Date] = None) -> None:
        """
        Sets the endMonthYear property value. When the position ended.
        Args:
            value: Value to set for the endMonthYear property.
        """
        self._end_month_year = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "company": lambda n : setattr(self, 'company', n.get_object_value(company_detail.CompanyDetail)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "end_month_year": lambda n : setattr(self, 'end_month_year', n.get_object_value(Date)),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "start_month_year": lambda n : setattr(self, 'start_month_year', n.get_object_value(Date)),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
        }
        return fields
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The title held when in that position.
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The title held when in that position.
        Args:
            value: Value to set for the jobTitle property.
        """
        self._job_title = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def role(self,) -> Optional[str]:
        """
        Gets the role property value. The role the position entailed.
        Returns: Optional[str]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[str] = None) -> None:
        """
        Sets the role property value. The role the position entailed.
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("company", self.company)
        writer.write_str_value("description", self.description)
        writer.write_object_value("endMonthYear", self.end_month_year)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("role", self.role)
        writer.write_object_value("startMonthYear", self.start_month_year)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_month_year(self,) -> Optional[Date]:
        """
        Gets the startMonthYear property value. The start month and year of the position.
        Returns: Optional[Date]
        """
        return self._start_month_year
    
    @start_month_year.setter
    def start_month_year(self,value: Optional[Date] = None) -> None:
        """
        Sets the startMonthYear property value. The start month and year of the position.
        Args:
            value: Value to set for the startMonthYear property.
        """
        self._start_month_year = value
    
    @property
    def summary(self,) -> Optional[str]:
        """
        Gets the summary property value. Short summary of the position.
        Returns: Optional[str]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[str] = None) -> None:
        """
        Sets the summary property value. Short summary of the position.
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    

