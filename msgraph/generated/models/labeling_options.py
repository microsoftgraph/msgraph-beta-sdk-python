from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_method = lazy_import('msgraph.generated.models.assignment_method')
downgrade_justification = lazy_import('msgraph.generated.models.downgrade_justification')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class LabelingOptions(AdditionalDataHolder, Parsable):
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
        Instantiates a new labelingOptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentMethod property
        self._assignment_method: Optional[assignment_method.AssignmentMethod] = None
        # The downgrade justification object that indicates if downgrade was justified and, if so, the reason.
        self._downgrade_justification: Optional[downgrade_justification.DowngradeJustification] = None
        # Extended properties will be parsed and returned in the standard MIP labeled metadata format as part of the label information.
        self._extended_properties: Optional[List[key_value_pair.KeyValuePair]] = None
        # The GUID of the label that should be applied to the information.
        self._label_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LabelingOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LabelingOptions()
    
    @property
    def downgrade_justification(self,) -> Optional[downgrade_justification.DowngradeJustification]:
        """
        Gets the downgradeJustification property value. The downgrade justification object that indicates if downgrade was justified and, if so, the reason.
        Returns: Optional[downgrade_justification.DowngradeJustification]
        """
        return self._downgrade_justification
    
    @downgrade_justification.setter
    def downgrade_justification(self,value: Optional[downgrade_justification.DowngradeJustification] = None) -> None:
        """
        Sets the downgradeJustification property value. The downgrade justification object that indicates if downgrade was justified and, if so, the reason.
        Args:
            value: Value to set for the downgradeJustification property.
        """
        self._downgrade_justification = value
    
    @property
    def extended_properties(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the extendedProperties property value. Extended properties will be parsed and returned in the standard MIP labeled metadata format as part of the label information.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._extended_properties
    
    @extended_properties.setter
    def extended_properties(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the extendedProperties property value. Extended properties will be parsed and returned in the standard MIP labeled metadata format as part of the label information.
        Args:
            value: Value to set for the extendedProperties property.
        """
        self._extended_properties = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_method": lambda n : setattr(self, 'assignment_method', n.get_enum_value(assignment_method.AssignmentMethod)),
            "downgrade_justification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(downgrade_justification.DowngradeJustification)),
            "extended_properties": lambda n : setattr(self, 'extended_properties', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "label_id": lambda n : setattr(self, 'label_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def label_id(self,) -> Optional[str]:
        """
        Gets the labelId property value. The GUID of the label that should be applied to the information.
        Returns: Optional[str]
        """
        return self._label_id
    
    @label_id.setter
    def label_id(self,value: Optional[str] = None) -> None:
        """
        Sets the labelId property value. The GUID of the label that should be applied to the information.
        Args:
            value: Value to set for the labelId property.
        """
        self._label_id = value
    
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
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_collection_of_object_values("extendedProperties", self.extended_properties)
        writer.write_str_value("labelId", self.label_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

