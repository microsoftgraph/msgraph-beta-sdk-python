from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_customization import EducationSynchronizationCustomization
    from .education_synchronization_customizations_base import EducationSynchronizationCustomizationsBase

from .education_synchronization_customizations_base import EducationSynchronizationCustomizationsBase

@dataclass
class EducationSynchronizationCustomizations(EducationSynchronizationCustomizationsBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationSynchronizationCustomizations"
    # Customizations for School entities.
    school: Optional[EducationSynchronizationCustomization] = None
    # Customizations for Section entities.
    section: Optional[EducationSynchronizationCustomization] = None
    # Customizations for Student entities.
    student: Optional[EducationSynchronizationCustomization] = None
    # Customizations for Student Enrollments.
    student_enrollment: Optional[EducationSynchronizationCustomization] = None
    # Customizations for Teacher entities.
    teacher: Optional[EducationSynchronizationCustomization] = None
    # Customizations for Teacher Rosters.
    teacher_roster: Optional[EducationSynchronizationCustomization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationCustomizations:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationCustomizations
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationCustomizations()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_customization import EducationSynchronizationCustomization
        from .education_synchronization_customizations_base import EducationSynchronizationCustomizationsBase

        from .education_synchronization_customization import EducationSynchronizationCustomization
        from .education_synchronization_customizations_base import EducationSynchronizationCustomizationsBase

        fields: Dict[str, Callable[[Any], None]] = {
            "school": lambda n : setattr(self, 'school', n.get_object_value(EducationSynchronizationCustomization)),
            "section": lambda n : setattr(self, 'section', n.get_object_value(EducationSynchronizationCustomization)),
            "student": lambda n : setattr(self, 'student', n.get_object_value(EducationSynchronizationCustomization)),
            "studentEnrollment": lambda n : setattr(self, 'student_enrollment', n.get_object_value(EducationSynchronizationCustomization)),
            "teacher": lambda n : setattr(self, 'teacher', n.get_object_value(EducationSynchronizationCustomization)),
            "teacherRoster": lambda n : setattr(self, 'teacher_roster', n.get_object_value(EducationSynchronizationCustomization)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("school", self.school)
        writer.write_object_value("section", self.section)
        writer.write_object_value("student", self.student)
        writer.write_object_value("studentEnrollment", self.student_enrollment)
        writer.write_object_value("teacher", self.teacher)
        writer.write_object_value("teacherRoster", self.teacher_roster)
    

