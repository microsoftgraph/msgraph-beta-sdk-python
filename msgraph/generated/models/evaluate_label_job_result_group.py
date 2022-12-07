from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

evaluate_label_job_result = lazy_import('msgraph.generated.models.evaluate_label_job_result')

class EvaluateLabelJobResultGroup(AdditionalDataHolder, Parsable):
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
    def automatic(self,) -> Optional[evaluate_label_job_result.EvaluateLabelJobResult]:
        """
        Gets the automatic property value. The automatic property
        Returns: Optional[evaluate_label_job_result.EvaluateLabelJobResult]
        """
        return self._automatic
    
    @automatic.setter
    def automatic(self,value: Optional[evaluate_label_job_result.EvaluateLabelJobResult] = None) -> None:
        """
        Sets the automatic property value. The automatic property
        Args:
            value: Value to set for the automatic property.
        """
        self._automatic = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new evaluateLabelJobResultGroup and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The automatic property
        self._automatic: Optional[evaluate_label_job_result.EvaluateLabelJobResult] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recommended property
        self._recommended: Optional[evaluate_label_job_result.EvaluateLabelJobResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResultGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResultGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateLabelJobResultGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "automatic": lambda n : setattr(self, 'automatic', n.get_object_value(evaluate_label_job_result.EvaluateLabelJobResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommended": lambda n : setattr(self, 'recommended', n.get_object_value(evaluate_label_job_result.EvaluateLabelJobResult)),
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
    def recommended(self,) -> Optional[evaluate_label_job_result.EvaluateLabelJobResult]:
        """
        Gets the recommended property value. The recommended property
        Returns: Optional[evaluate_label_job_result.EvaluateLabelJobResult]
        """
        return self._recommended
    
    @recommended.setter
    def recommended(self,value: Optional[evaluate_label_job_result.EvaluateLabelJobResult] = None) -> None:
        """
        Sets the recommended property value. The recommended property
        Args:
            value: Value to set for the recommended property.
        """
        self._recommended = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("automatic", self.automatic)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recommended", self.recommended)
        writer.write_additional_data_value(self.additional_data)
    

