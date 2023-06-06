from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_gender

@dataclass
class EducationStudent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Birth date of the student.
    birth_date: Optional[date] = None
    # ID of the student in the source system.
    external_id: Optional[str] = None
    # Possible values are: female, male, other.
    gender: Optional[education_gender.EducationGender] = None
    # Current grade level of the student.
    grade: Optional[str] = None
    # Year the student is graduating from the school.
    graduation_year: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Student Number.
    student_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationStudent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationStudent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationStudent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_gender

        fields: Dict[str, Callable[[Any], None]] = {
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_enum_value(education_gender.EducationGender)),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "graduationYear": lambda n : setattr(self, 'graduation_year', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "studentNumber": lambda n : setattr(self, 'student_number', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("gender", self.gender)
        writer.write_str_value("grade", self.grade)
        writer.write_str_value("graduationYear", self.graduation_year)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("studentNumber", self.student_number)
        writer.write_additional_data_value(self.additional_data)
    

