from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_method = lazy_import('msgraph.generated.models.assignment_method')
label_details = lazy_import('msgraph.generated.models.label_details')

class InformationProtectionContentLabel(AdditionalDataHolder, Parsable):
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
        Instantiates a new informationProtectionContentLabel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentMethod property
        self._assignment_method: Optional[assignment_method.AssignmentMethod] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._creation_date_time: Optional[datetime] = None
        # Details on the label that is currently applied to the file.
        self._label: Optional[label_details.LabelDetails] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionContentLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionContentLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtectionContentLabel()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_method": lambda n : setattr(self, 'assignment_method', n.get_enum_value(assignment_method.AssignmentMethod)),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_object_value(label_details.LabelDetails)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def label(self,) -> Optional[label_details.LabelDetails]:
        """
        Gets the label property value. Details on the label that is currently applied to the file.
        Returns: Optional[label_details.LabelDetails]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[label_details.LabelDetails] = None) -> None:
        """
        Sets the label property value. Details on the label that is currently applied to the file.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
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
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

