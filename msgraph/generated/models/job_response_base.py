from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_error, classification_job_response, dlp_evaluate_policies_job_response, entity, evaluate_label_job_response

from . import entity

@dataclass
class JobResponseBase(entity.Entity):
    # The creationDateTime property
    creation_date_time: Optional[datetime] = None
    # The endDateTime property
    end_date_time: Optional[datetime] = None
    # The error property
    error: Optional[classification_error.ClassificationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime] = None
    # The status property
    status: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> JobResponseBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: JobResponseBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.classificationJobResponse":
                from . import classification_job_response

                return classification_job_response.ClassificationJobResponse()
            if mapping_value == "#microsoft.graph.dlpEvaluatePoliciesJobResponse":
                from . import dlp_evaluate_policies_job_response

                return dlp_evaluate_policies_job_response.DlpEvaluatePoliciesJobResponse()
            if mapping_value == "#microsoft.graph.evaluateLabelJobResponse":
                from . import evaluate_label_job_response

                return evaluate_label_job_response.EvaluateLabelJobResponse()
        return JobResponseBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_error, classification_job_response, dlp_evaluate_policies_job_response, entity, evaluate_label_job_response

        fields: Dict[str, Callable[[Any], None]] = {
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(classification_error.ClassificationError)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
    

