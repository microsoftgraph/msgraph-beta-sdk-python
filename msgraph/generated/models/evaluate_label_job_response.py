from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

evaluate_label_job_result_group = lazy_import('msgraph.generated.models.evaluate_label_job_result_group')
job_response_base = lazy_import('msgraph.generated.models.job_response_base')

class EvaluateLabelJobResponse(job_response_base.JobResponseBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EvaluateLabelJobResponse and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The result property
        self._result: Optional[evaluate_label_job_result_group.EvaluateLabelJobResultGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateLabelJobResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "result": lambda n : setattr(self, 'result', n.get_object_value(evaluate_label_job_result_group.EvaluateLabelJobResultGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def result(self,) -> Optional[evaluate_label_job_result_group.EvaluateLabelJobResultGroup]:
        """
        Gets the result property value. The result property
        Returns: Optional[evaluate_label_job_result_group.EvaluateLabelJobResultGroup]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[evaluate_label_job_result_group.EvaluateLabelJobResultGroup] = None) -> None:
        """
        Sets the result property value. The result property
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("result", self.result)
    

