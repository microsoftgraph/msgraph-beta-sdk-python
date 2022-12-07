from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
exact_match_data_store = lazy_import('msgraph.generated.models.exact_match_data_store')
exact_match_upload_agent = lazy_import('msgraph.generated.models.exact_match_upload_agent')
job_response_base = lazy_import('msgraph.generated.models.job_response_base')
sensitive_type = lazy_import('msgraph.generated.models.sensitive_type')
sensitivity_label = lazy_import('msgraph.generated.models.sensitivity_label')

class DataClassificationService(entity.Entity):
    @property
    def classify_file_jobs(self,) -> Optional[List[job_response_base.JobResponseBase]]:
        """
        Gets the classifyFileJobs property value. The classifyFileJobs property
        Returns: Optional[List[job_response_base.JobResponseBase]]
        """
        return self._classify_file_jobs
    
    @classify_file_jobs.setter
    def classify_file_jobs(self,value: Optional[List[job_response_base.JobResponseBase]] = None) -> None:
        """
        Sets the classifyFileJobs property value. The classifyFileJobs property
        Args:
            value: Value to set for the classifyFileJobs property.
        """
        self._classify_file_jobs = value
    
    @property
    def classify_text_jobs(self,) -> Optional[List[job_response_base.JobResponseBase]]:
        """
        Gets the classifyTextJobs property value. The classifyTextJobs property
        Returns: Optional[List[job_response_base.JobResponseBase]]
        """
        return self._classify_text_jobs
    
    @classify_text_jobs.setter
    def classify_text_jobs(self,value: Optional[List[job_response_base.JobResponseBase]] = None) -> None:
        """
        Sets the classifyTextJobs property value. The classifyTextJobs property
        Args:
            value: Value to set for the classifyTextJobs property.
        """
        self._classify_text_jobs = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DataClassificationService and sets the default values.
        """
        super().__init__()
        # The classifyFileJobs property
        self._classify_file_jobs: Optional[List[job_response_base.JobResponseBase]] = None
        # The classifyTextJobs property
        self._classify_text_jobs: Optional[List[job_response_base.JobResponseBase]] = None
        # The evaluateDlpPoliciesJobs property
        self._evaluate_dlp_policies_jobs: Optional[List[job_response_base.JobResponseBase]] = None
        # The evaluateLabelJobs property
        self._evaluate_label_jobs: Optional[List[job_response_base.JobResponseBase]] = None
        # The exactMatchDataStores property
        self._exact_match_data_stores: Optional[List[exact_match_data_store.ExactMatchDataStore]] = None
        # The exactMatchUploadAgents property
        self._exact_match_upload_agents: Optional[List[exact_match_upload_agent.ExactMatchUploadAgent]] = None
        # The jobs property
        self._jobs: Optional[List[job_response_base.JobResponseBase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The sensitiveTypes property
        self._sensitive_types: Optional[List[sensitive_type.SensitiveType]] = None
        # The sensitivityLabels property
        self._sensitivity_labels: Optional[List[sensitivity_label.SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataClassificationService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataClassificationService
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataClassificationService()
    
    @property
    def evaluate_dlp_policies_jobs(self,) -> Optional[List[job_response_base.JobResponseBase]]:
        """
        Gets the evaluateDlpPoliciesJobs property value. The evaluateDlpPoliciesJobs property
        Returns: Optional[List[job_response_base.JobResponseBase]]
        """
        return self._evaluate_dlp_policies_jobs
    
    @evaluate_dlp_policies_jobs.setter
    def evaluate_dlp_policies_jobs(self,value: Optional[List[job_response_base.JobResponseBase]] = None) -> None:
        """
        Sets the evaluateDlpPoliciesJobs property value. The evaluateDlpPoliciesJobs property
        Args:
            value: Value to set for the evaluateDlpPoliciesJobs property.
        """
        self._evaluate_dlp_policies_jobs = value
    
    @property
    def evaluate_label_jobs(self,) -> Optional[List[job_response_base.JobResponseBase]]:
        """
        Gets the evaluateLabelJobs property value. The evaluateLabelJobs property
        Returns: Optional[List[job_response_base.JobResponseBase]]
        """
        return self._evaluate_label_jobs
    
    @evaluate_label_jobs.setter
    def evaluate_label_jobs(self,value: Optional[List[job_response_base.JobResponseBase]] = None) -> None:
        """
        Sets the evaluateLabelJobs property value. The evaluateLabelJobs property
        Args:
            value: Value to set for the evaluateLabelJobs property.
        """
        self._evaluate_label_jobs = value
    
    @property
    def exact_match_data_stores(self,) -> Optional[List[exact_match_data_store.ExactMatchDataStore]]:
        """
        Gets the exactMatchDataStores property value. The exactMatchDataStores property
        Returns: Optional[List[exact_match_data_store.ExactMatchDataStore]]
        """
        return self._exact_match_data_stores
    
    @exact_match_data_stores.setter
    def exact_match_data_stores(self,value: Optional[List[exact_match_data_store.ExactMatchDataStore]] = None) -> None:
        """
        Sets the exactMatchDataStores property value. The exactMatchDataStores property
        Args:
            value: Value to set for the exactMatchDataStores property.
        """
        self._exact_match_data_stores = value
    
    @property
    def exact_match_upload_agents(self,) -> Optional[List[exact_match_upload_agent.ExactMatchUploadAgent]]:
        """
        Gets the exactMatchUploadAgents property value. The exactMatchUploadAgents property
        Returns: Optional[List[exact_match_upload_agent.ExactMatchUploadAgent]]
        """
        return self._exact_match_upload_agents
    
    @exact_match_upload_agents.setter
    def exact_match_upload_agents(self,value: Optional[List[exact_match_upload_agent.ExactMatchUploadAgent]] = None) -> None:
        """
        Sets the exactMatchUploadAgents property value. The exactMatchUploadAgents property
        Args:
            value: Value to set for the exactMatchUploadAgents property.
        """
        self._exact_match_upload_agents = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classify_file_jobs": lambda n : setattr(self, 'classify_file_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "classify_text_jobs": lambda n : setattr(self, 'classify_text_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "evaluate_dlp_policies_jobs": lambda n : setattr(self, 'evaluate_dlp_policies_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "evaluate_label_jobs": lambda n : setattr(self, 'evaluate_label_jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "exact_match_data_stores": lambda n : setattr(self, 'exact_match_data_stores', n.get_collection_of_object_values(exact_match_data_store.ExactMatchDataStore)),
            "exact_match_upload_agents": lambda n : setattr(self, 'exact_match_upload_agents', n.get_collection_of_object_values(exact_match_upload_agent.ExactMatchUploadAgent)),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(job_response_base.JobResponseBase)),
            "sensitive_types": lambda n : setattr(self, 'sensitive_types', n.get_collection_of_object_values(sensitive_type.SensitiveType)),
            "sensitivity_labels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(sensitivity_label.SensitivityLabel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def jobs(self,) -> Optional[List[job_response_base.JobResponseBase]]:
        """
        Gets the jobs property value. The jobs property
        Returns: Optional[List[job_response_base.JobResponseBase]]
        """
        return self._jobs
    
    @jobs.setter
    def jobs(self,value: Optional[List[job_response_base.JobResponseBase]] = None) -> None:
        """
        Sets the jobs property value. The jobs property
        Args:
            value: Value to set for the jobs property.
        """
        self._jobs = value
    
    @property
    def sensitive_types(self,) -> Optional[List[sensitive_type.SensitiveType]]:
        """
        Gets the sensitiveTypes property value. The sensitiveTypes property
        Returns: Optional[List[sensitive_type.SensitiveType]]
        """
        return self._sensitive_types
    
    @sensitive_types.setter
    def sensitive_types(self,value: Optional[List[sensitive_type.SensitiveType]] = None) -> None:
        """
        Sets the sensitiveTypes property value. The sensitiveTypes property
        Args:
            value: Value to set for the sensitiveTypes property.
        """
        self._sensitive_types = value
    
    @property
    def sensitivity_labels(self,) -> Optional[List[sensitivity_label.SensitivityLabel]]:
        """
        Gets the sensitivityLabels property value. The sensitivityLabels property
        Returns: Optional[List[sensitivity_label.SensitivityLabel]]
        """
        return self._sensitivity_labels
    
    @sensitivity_labels.setter
    def sensitivity_labels(self,value: Optional[List[sensitivity_label.SensitivityLabel]] = None) -> None:
        """
        Sets the sensitivityLabels property value. The sensitivityLabels property
        Args:
            value: Value to set for the sensitivityLabels property.
        """
        self._sensitivity_labels = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

