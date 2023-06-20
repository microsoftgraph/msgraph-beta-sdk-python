from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, exact_match_data_store, exact_match_upload_agent, job_response_base, sensitive_type, sensitivity_label

from . import entity

@dataclass
class DataClassificationService(entity.Entity):
    # The classifyFileJobs property
    classify_file_jobs: Optional[List[job_response_base.JobResponseBase]] = None
    # The classifyTextJobs property
    classify_text_jobs: Optional[List[job_response_base.JobResponseBase]] = None
    # The evaluateDlpPoliciesJobs property
    evaluate_dlp_policies_jobs: Optional[List[job_response_base.JobResponseBase]] = None
    # The evaluateLabelJobs property
    evaluate_label_jobs: Optional[List[job_response_base.JobResponseBase]] = None
    # The exactMatchDataStores property
    exact_match_data_stores: Optional[List[exact_match_data_store.ExactMatchDataStore]] = None
    # The exactMatchUploadAgents property
    exact_match_upload_agents: Optional[List[exact_match_upload_agent.ExactMatchUploadAgent]] = None
    # The jobs property
    jobs: Optional[List[job_response_base.JobResponseBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitiveTypes property
    sensitive_types: Optional[List[sensitive_type.SensitiveType]] = None
    # The sensitivityLabels property
    sensitivity_labels: Optional[List[sensitivity_label.SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataClassificationService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataClassificationService
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataClassificationService()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, exact_match_data_store, exact_match_upload_agent, job_response_base, sensitive_type, sensitivity_label

        from . import entity, exact_match_data_store, exact_match_upload_agent, job_response_base, sensitive_type, sensitivity_label

        fields: Dict[str, Callable[[Any], None]] = {
            "classifyFileJobs": lambda n : setattr(self, 'classify_file_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "classifyTextJobs": lambda n : setattr(self, 'classify_text_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "evaluateDlpPoliciesJobs": lambda n : setattr(self, 'evaluate_dlp_policies_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "evaluateLabelJobs": lambda n : setattr(self, 'evaluate_label_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "exactMatchDataStores": lambda n : setattr(self, 'exact_match_data_stores', n.get_collection_of_object_values(exact_match_data_store.ExactMatchDataStore)),
            "exactMatchUploadAgents": lambda n : setattr(self, 'exact_match_upload_agents', n.get_collection_of_object_values(exact_match_upload_agent.ExactMatchUploadAgent)),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "sensitiveTypes": lambda n : setattr(self, 'sensitive_types', n.get_collection_of_object_values(sensitive_type.SensitiveType)),
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(sensitivity_label.SensitivityLabel)),
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
        writer.write_collection_of_object_values("classifyFileJobs", self.classify_file_jobs)
        writer.write_collection_of_object_values("classifyTextJobs", self.classify_text_jobs)
        writer.write_collection_of_object_values("evaluateDlpPoliciesJobs", self.evaluate_dlp_policies_jobs)
        writer.write_collection_of_object_values("evaluateLabelJobs", self.evaluate_label_jobs)
        writer.write_collection_of_object_values("exactMatchDataStores", self.exact_match_data_stores)
        writer.write_collection_of_object_values("exactMatchUploadAgents", self.exact_match_upload_agents)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("sensitiveTypes", self.sensitive_types)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
    

