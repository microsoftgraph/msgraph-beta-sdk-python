from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import educational_activity_detail, institution_data, item_facet

from . import item_facet

@dataclass
class EducationalActivity(item_facet.ItemFacet):
    odata_type = "#microsoft.graph.educationalActivity"
    # The month and year the user graduated or completed the activity.
    completion_month_year: Optional[date] = None
    # The month and year the user completed the educational activity referenced.
    end_month_year: Optional[date] = None
    # The institution property
    institution: Optional[institution_data.InstitutionData] = None
    # The program property
    program: Optional[educational_activity_detail.EducationalActivityDetail] = None
    # The month and year the user commenced the activity referenced.
    start_month_year: Optional[date] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import educational_activity_detail, institution_data, item_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "completionMonthYear": lambda n : setattr(self, 'completion_month_year', n.get_date_value()),
            "endMonthYear": lambda n : setattr(self, 'end_month_year', n.get_date_value()),
            "institution": lambda n : setattr(self, 'institution', n.get_object_value(institution_data.InstitutionData)),
            "program": lambda n : setattr(self, 'program', n.get_object_value(educational_activity_detail.EducationalActivityDetail)),
            "startMonthYear": lambda n : setattr(self, 'start_month_year', n.get_date_value()),
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
        writer.write_date_value("completionMonthYear", self.completion_month_year)
        writer.write_date_value("endMonthYear", self.end_month_year)
        writer.write_object_value("institution", self.institution)
        writer.write_object_value("program", self.program)
        writer.write_date_value("startMonthYear", self.start_month_year)
    

