from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

sensitivity_label_assignment_method = lazy_import('msgraph.generated.models.sensitivity_label_assignment_method')

class SensitivityLabelAssignment(AdditionalDataHolder, Parsable):
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
    def assignment_method(self,) -> Optional[sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod]:
        """
        Gets the assignmentMethod property value. The assignmentMethod property
        Returns: Optional[sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod]
        """
        return self._assignment_method
    
    @assignment_method.setter
    def assignment_method(self,value: Optional[sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod] = None) -> None:
        """
        Sets the assignmentMethod property value. The assignmentMethod property
        Args:
            value: Value to set for the assignmentMethod property.
        """
        self._assignment_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sensitivityLabelAssignment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentMethod property
        self._assignment_method: Optional[sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier for the sensitivity label assigned to the file.
        self._sensitivity_label_id: Optional[str] = None
        # The unique identifier for the tenant that hosts the file when this label is applied.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityLabelAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabelAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitivityLabelAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_method": lambda n : setattr(self, 'assignment_method', n.get_enum_value(sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitivity_label_id": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        Gets the sensitivityLabelId property value. The unique identifier for the sensitivity label assigned to the file.
        Returns: Optional[str]
        """
        return self._sensitivity_label_id
    
    @sensitivity_label_id.setter
    def sensitivity_label_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sensitivityLabelId property value. The unique identifier for the sensitivity label assigned to the file.
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The unique identifier for the tenant that hosts the file when this label is applied.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The unique identifier for the tenant that hosts the file when this label is applied.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

