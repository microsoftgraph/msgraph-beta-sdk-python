from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

educational_activity_detail = lazy_import('msgraph.generated.models.educational_activity_detail')
institution_data = lazy_import('msgraph.generated.models.institution_data')
item_facet = lazy_import('msgraph.generated.models.item_facet')

class EducationalActivity(item_facet.ItemFacet):
    @property
    def completion_month_year(self,) -> Optional[Date]:
        """
        Gets the completionMonthYear property value. The month and year the user graduated or completed the activity.
        Returns: Optional[Date]
        """
        return self._completion_month_year
    
    @completion_month_year.setter
    def completion_month_year(self,value: Optional[Date] = None) -> None:
        """
        Sets the completionMonthYear property value. The month and year the user graduated or completed the activity.
        Args:
            value: Value to set for the completionMonthYear property.
        """
        self._completion_month_year = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EducationalActivity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationalActivity"
        # The month and year the user graduated or completed the activity.
        self._completion_month_year: Optional[Date] = None
        # The month and year the user completed the educational activity referenced.
        self._end_month_year: Optional[Date] = None
        # The institution property
        self._institution: Optional[institution_data.InstitutionData] = None
        # The program property
        self._program: Optional[educational_activity_detail.EducationalActivityDetail] = None
        # The month and year the user commenced the activity referenced.
        self._start_month_year: Optional[Date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationalActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationalActivity()
    
    @property
    def end_month_year(self,) -> Optional[Date]:
        """
        Gets the endMonthYear property value. The month and year the user completed the educational activity referenced.
        Returns: Optional[Date]
        """
        return self._end_month_year
    
    @end_month_year.setter
    def end_month_year(self,value: Optional[Date] = None) -> None:
        """
        Sets the endMonthYear property value. The month and year the user completed the educational activity referenced.
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
            "completion_month_year": lambda n : setattr(self, 'completion_month_year', n.get_object_value(Date)),
            "end_month_year": lambda n : setattr(self, 'end_month_year', n.get_object_value(Date)),
            "institution": lambda n : setattr(self, 'institution', n.get_object_value(institution_data.InstitutionData)),
            "program": lambda n : setattr(self, 'program', n.get_object_value(educational_activity_detail.EducationalActivityDetail)),
            "start_month_year": lambda n : setattr(self, 'start_month_year', n.get_object_value(Date)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def institution(self,) -> Optional[institution_data.InstitutionData]:
        """
        Gets the institution property value. The institution property
        Returns: Optional[institution_data.InstitutionData]
        """
        return self._institution
    
    @institution.setter
    def institution(self,value: Optional[institution_data.InstitutionData] = None) -> None:
        """
        Sets the institution property value. The institution property
        Args:
            value: Value to set for the institution property.
        """
        self._institution = value
    
    @property
    def program(self,) -> Optional[educational_activity_detail.EducationalActivityDetail]:
        """
        Gets the program property value. The program property
        Returns: Optional[educational_activity_detail.EducationalActivityDetail]
        """
        return self._program
    
    @program.setter
    def program(self,value: Optional[educational_activity_detail.EducationalActivityDetail] = None) -> None:
        """
        Sets the program property value. The program property
        Args:
            value: Value to set for the program property.
        """
        self._program = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("completionMonthYear", self.completion_month_year)
        writer.write_object_value("endMonthYear", self.end_month_year)
        writer.write_object_value("institution", self.institution)
        writer.write_object_value("program", self.program)
        writer.write_object_value("startMonthYear", self.start_month_year)
    
    @property
    def start_month_year(self,) -> Optional[Date]:
        """
        Gets the startMonthYear property value. The month and year the user commenced the activity referenced.
        Returns: Optional[Date]
        """
        return self._start_month_year
    
    @start_month_year.setter
    def start_month_year(self,value: Optional[Date] = None) -> None:
        """
        Sets the startMonthYear property value. The month and year the user commenced the activity referenced.
        Args:
            value: Value to set for the startMonthYear property.
        """
        self._start_month_year = value
    

