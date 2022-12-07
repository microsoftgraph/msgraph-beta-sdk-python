from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_method = lazy_import('msgraph.generated.models.security.assignment_method')

class ContentLabel(AdditionalDataHolder, Parsable):
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
    def assignment_method(self,) -> Optional[assignment_method.AssignmentMethod]:
        """
        Gets the assignmentMethod property value. The assignmentMethod property
        Returns: Optional[assignment_method.AssignmentMethod]
        """
        return self._assignment_method
    
    @assignment_method.setter
    def assignment_method(self,value: Optional[assignment_method.AssignmentMethod] = None) -> None:
        """
        Sets the assignmentMethod property value. The assignmentMethod property
        Args:
            value: Value to set for the assignmentMethod property.
        """
        self._assignment_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new contentLabel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentMethod property
        self._assignment_method: Optional[assignment_method.AssignmentMethod] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The sensitivityLabelId property
        self._sensitivity_label_id: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_method": lambda n : setattr(self, 'assignment_method', n.get_enum_value(assignment_method.AssignmentMethod)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitivity_label_id": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
        }
        return fields
    
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
    def sensitivity_label_id(self,) -> Optional[str]:
        """
        Gets the sensitivityLabelId property value. The sensitivityLabelId property
        Returns: Optional[str]
        """
        return self._sensitivity_label_id
    
    @sensitivity_label_id.setter
    def sensitivity_label_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sensitivityLabelId property value. The sensitivityLabelId property
        Args:
            value: Value to set for the sensitivityLabelId property.
        """
        self._sensitivity_label_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
        writer.write_additional_data_value(self.additional_data)
    

