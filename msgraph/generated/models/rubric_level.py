from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_assignment_grade_type, education_item_body

class RubricLevel(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new rubricLevel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description of this rubric level.
        self._description: Optional[education_item_body.EducationItemBody] = None
        # The name of this rubric level.
        self._display_name: Optional[str] = None
        # Null if this is a no-points rubric; educationAssignmentPointsGradeType if it is a points rubric.
        self._grading: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None
        # The ID of this resource.
        self._level_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricLevel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RubricLevel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RubricLevel()
    
    @property
    def description(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the description property value. The description of this rubric level.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the description property value. The description of this rubric level.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of this rubric level.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of this rubric level.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_assignment_grade_type, education_item_body

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_object_value(education_item_body.EducationItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(education_assignment_grade_type.EducationAssignmentGradeType)),
            "levelId": lambda n : setattr(self, 'level_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def grading(self,) -> Optional[education_assignment_grade_type.EducationAssignmentGradeType]:
        """
        Gets the grading property value. Null if this is a no-points rubric; educationAssignmentPointsGradeType if it is a points rubric.
        Returns: Optional[education_assignment_grade_type.EducationAssignmentGradeType]
        """
        return self._grading
    
    @grading.setter
    def grading(self,value: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None) -> None:
        """
        Sets the grading property value. Null if this is a no-points rubric; educationAssignmentPointsGradeType if it is a points rubric.
        Args:
            value: Value to set for the grading property.
        """
        self._grading = value
    
    @property
    def level_id(self,) -> Optional[str]:
        """
        Gets the levelId property value. The ID of this resource.
        Returns: Optional[str]
        """
        return self._level_id
    
    @level_id.setter
    def level_id(self,value: Optional[str] = None) -> None:
        """
        Sets the levelId property value. The ID of this resource.
        Args:
            value: Value to set for the level_id property.
        """
        self._level_id = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("grading", self.grading)
        writer.write_str_value("levelId", self.level_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

