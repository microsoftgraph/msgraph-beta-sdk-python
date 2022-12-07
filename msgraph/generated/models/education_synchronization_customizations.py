from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_synchronization_customization = lazy_import('msgraph.generated.models.education_synchronization_customization')
education_synchronization_customizations_base = lazy_import('msgraph.generated.models.education_synchronization_customizations_base')

class EducationSynchronizationCustomizations(education_synchronization_customizations_base.EducationSynchronizationCustomizationsBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationSynchronizationCustomizations and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationSynchronizationCustomizations"
        # Customizations for School entities.
        self._school: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
        # Customizations for Section entities.
        self._section: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
        # Customizations for Student entities.
        self._student: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
        # Customizations for Student Enrollments.
        self._student_enrollment: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
        # Customizations for Teacher entities.
        self._teacher: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
        # Customizations for Teacher Rosters.
        self._teacher_roster: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationCustomizations:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationCustomizations
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationCustomizations()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "school": lambda n : setattr(self, 'school', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
            "section": lambda n : setattr(self, 'section', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
            "student": lambda n : setattr(self, 'student', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
            "student_enrollment": lambda n : setattr(self, 'student_enrollment', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
            "teacher": lambda n : setattr(self, 'teacher', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
            "teacher_roster": lambda n : setattr(self, 'teacher_roster', n.get_object_value(education_synchronization_customization.EducationSynchronizationCustomization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def school(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the school property value. Customizations for School entities.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._school
    
    @school.setter
    def school(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the school property value. Customizations for School entities.
        Args:
            value: Value to set for the school property.
        """
        self._school = value
    
    @property
    def section(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the section property value. Customizations for Section entities.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._section
    
    @section.setter
    def section(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the section property value. Customizations for Section entities.
        Args:
            value: Value to set for the section property.
        """
        self._section = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("school", self.school)
        writer.write_object_value("section", self.section)
        writer.write_object_value("student", self.student)
        writer.write_object_value("studentEnrollment", self.student_enrollment)
        writer.write_object_value("teacher", self.teacher)
        writer.write_object_value("teacherRoster", self.teacher_roster)
    
    @property
    def student(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the student property value. Customizations for Student entities.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._student
    
    @student.setter
    def student(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the student property value. Customizations for Student entities.
        Args:
            value: Value to set for the student property.
        """
        self._student = value
    
    @property
    def student_enrollment(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the studentEnrollment property value. Customizations for Student Enrollments.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._student_enrollment
    
    @student_enrollment.setter
    def student_enrollment(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the studentEnrollment property value. Customizations for Student Enrollments.
        Args:
            value: Value to set for the studentEnrollment property.
        """
        self._student_enrollment = value
    
    @property
    def teacher(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the teacher property value. Customizations for Teacher entities.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._teacher
    
    @teacher.setter
    def teacher(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the teacher property value. Customizations for Teacher entities.
        Args:
            value: Value to set for the teacher property.
        """
        self._teacher = value
    
    @property
    def teacher_roster(self,) -> Optional[education_synchronization_customization.EducationSynchronizationCustomization]:
        """
        Gets the teacherRoster property value. Customizations for Teacher Rosters.
        Returns: Optional[education_synchronization_customization.EducationSynchronizationCustomization]
        """
        return self._teacher_roster
    
    @teacher_roster.setter
    def teacher_roster(self,value: Optional[education_synchronization_customization.EducationSynchronizationCustomization] = None) -> None:
        """
        Sets the teacherRoster property value. Customizations for Teacher Rosters.
        Args:
            value: Value to set for the teacherRoster property.
        """
        self._teacher_roster = value
    

