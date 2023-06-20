from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import evaluate_label_job_result_group, job_response_base

from . import job_response_base

@dataclass
class EvaluateLabelJobResponse(job_response_base.JobResponseBase):
    # The OdataType property
    odata_type: Optional[str] = None
    # The result property
    result: Optional[evaluate_label_job_result_group.EvaluateLabelJobResultGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateLabelJobResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import evaluate_label_job_result_group, job_response_base

        from . import evaluate_label_job_result_group, job_response_base

        fields: Dict[str, Callable[[Any], None]] = {
            "result": lambda n : setattr(self, 'result', n.get_object_value(evaluate_label_job_result_group.EvaluateLabelJobResultGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("result", self.result)
    

