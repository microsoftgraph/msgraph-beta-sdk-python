from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import sensitivity_label_assignment

class ExtractSensitivityLabelsResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new extractSensitivityLabelsResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of sensitivity labels assigned to a file.
        self._labels: Optional[List[sensitivity_label_assignment.SensitivityLabelAssignment]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExtractSensitivityLabelsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExtractSensitivityLabelsResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExtractSensitivityLabelsResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import sensitivity_label_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(sensitivity_label_assignment.SensitivityLabelAssignment)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def labels(self,) -> Optional[List[sensitivity_label_assignment.SensitivityLabelAssignment]]:
        """
        Gets the labels property value. List of sensitivity labels assigned to a file.
        Returns: Optional[List[sensitivity_label_assignment.SensitivityLabelAssignment]]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[List[sensitivity_label_assignment.SensitivityLabelAssignment]] = None) -> None:
        """
        Sets the labels property value. List of sensitivity labels assigned to a file.
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
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
        writer.write_collection_of_object_values("labels", self.labels)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

