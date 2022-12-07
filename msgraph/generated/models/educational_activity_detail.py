from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EducationalActivityDetail(AdditionalDataHolder, Parsable):
    @property
    def abbreviation(self,) -> Optional[str]:
        """
        Gets the abbreviation property value. Shortened name of the degree or program (example: PhD, MBA)
        Returns: Optional[str]
        """
        return self._abbreviation
    
    @abbreviation.setter
    def abbreviation(self,value: Optional[str] = None) -> None:
        """
        Sets the abbreviation property value. Shortened name of the degree or program (example: PhD, MBA)
        Args:
            value: Value to set for the abbreviation property.
        """
        self._abbreviation = value
    
    @property
    def activities(self,) -> Optional[List[str]]:
        """
        Gets the activities property value. Extracurricular activities undertaken alongside the program.
        Returns: Optional[List[str]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the activities property value. Extracurricular activities undertaken alongside the program.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
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
    def awards(self,) -> Optional[List[str]]:
        """
        Gets the awards property value. Any awards or honors associated with the program.
        Returns: Optional[List[str]]
        """
        return self._awards
    
    @awards.setter
    def awards(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the awards property value. Any awards or honors associated with the program.
        Args:
            value: Value to set for the awards property.
        """
        self._awards = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationalActivityDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Shortened name of the degree or program (example: PhD, MBA)
        self._abbreviation: Optional[str] = None
        # Extracurricular activities undertaken alongside the program.
        self._activities: Optional[List[str]] = None
        # Any awards or honors associated with the program.
        self._awards: Optional[List[str]] = None
        # Short description of the program provided by the user.
        self._description: Optional[str] = None
        # Long-form name of the program that the user has provided.
        self._display_name: Optional[str] = None
        # Majors and minors associated with the program. (if applicable)
        self._fields_of_study: Optional[List[str]] = None
        # The final grade, class, GPA or score.
        self._grade: Optional[str] = None
        # Additional notes the user has provided.
        self._notes: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Link to the degree or program page.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationalActivityDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationalActivityDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationalActivityDetail()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Short description of the program provided by the user.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Short description of the program provided by the user.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Long-form name of the program that the user has provided.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Long-form name of the program that the user has provided.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def fields_of_study(self,) -> Optional[List[str]]:
        """
        Gets the fieldsOfStudy property value. Majors and minors associated with the program. (if applicable)
        Returns: Optional[List[str]]
        """
        return self._fields_of_study
    
    @fields_of_study.setter
    def fields_of_study(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fieldsOfStudy property value. Majors and minors associated with the program. (if applicable)
        Args:
            value: Value to set for the fieldsOfStudy property.
        """
        self._fields_of_study = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "abbreviation": lambda n : setattr(self, 'abbreviation', n.get_str_value()),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_primitive_values(str)),
            "awards": lambda n : setattr(self, 'awards', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fields_of_study": lambda n : setattr(self, 'fields_of_study', n.get_collection_of_primitive_values(str)),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    @property
    def grade(self,) -> Optional[str]:
        """
        Gets the grade property value. The final grade, class, GPA or score.
        Returns: Optional[str]
        """
        return self._grade
    
    @grade.setter
    def grade(self,value: Optional[str] = None) -> None:
        """
        Sets the grade property value. The final grade, class, GPA or score.
        Args:
            value: Value to set for the grade property.
        """
        self._grade = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Additional notes the user has provided.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Additional notes the user has provided.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("abbreviation", self.abbreviation)
        writer.write_collection_of_primitive_values("activities", self.activities)
        writer.write_collection_of_primitive_values("awards", self.awards)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("fieldsOfStudy", self.fields_of_study)
        writer.write_str_value("grade", self.grade)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Link to the degree or program page.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Link to the degree or program page.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

