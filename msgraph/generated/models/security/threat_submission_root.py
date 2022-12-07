from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
email_threat_submission = lazy_import('msgraph.generated.models.security.email_threat_submission')
email_threat_submission_policy = lazy_import('msgraph.generated.models.security.email_threat_submission_policy')
file_threat_submission = lazy_import('msgraph.generated.models.security.file_threat_submission')
url_threat_submission = lazy_import('msgraph.generated.models.security.url_threat_submission')

class ThreatSubmissionRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new threatSubmissionRoot and sets the default values.
        """
        super().__init__()
        # The emailThreats property
        self._email_threats: Optional[List[email_threat_submission.EmailThreatSubmission]] = None
        # The emailThreatSubmissionPolicies property
        self._email_threat_submission_policies: Optional[List[email_threat_submission_policy.EmailThreatSubmissionPolicy]] = None
        # The fileThreats property
        self._file_threats: Optional[List[file_threat_submission.FileThreatSubmission]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The urlThreats property
        self._url_threats: Optional[List[url_threat_submission.UrlThreatSubmission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatSubmissionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmissionRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatSubmissionRoot()
    
    @property
    def email_threats(self,) -> Optional[List[email_threat_submission.EmailThreatSubmission]]:
        """
        Gets the emailThreats property value. The emailThreats property
        Returns: Optional[List[email_threat_submission.EmailThreatSubmission]]
        """
        return self._email_threats
    
    @email_threats.setter
    def email_threats(self,value: Optional[List[email_threat_submission.EmailThreatSubmission]] = None) -> None:
        """
        Sets the emailThreats property value. The emailThreats property
        Args:
            value: Value to set for the emailThreats property.
        """
        self._email_threats = value
    
    @property
    def email_threat_submission_policies(self,) -> Optional[List[email_threat_submission_policy.EmailThreatSubmissionPolicy]]:
        """
        Gets the emailThreatSubmissionPolicies property value. The emailThreatSubmissionPolicies property
        Returns: Optional[List[email_threat_submission_policy.EmailThreatSubmissionPolicy]]
        """
        return self._email_threat_submission_policies
    
    @email_threat_submission_policies.setter
    def email_threat_submission_policies(self,value: Optional[List[email_threat_submission_policy.EmailThreatSubmissionPolicy]] = None) -> None:
        """
        Sets the emailThreatSubmissionPolicies property value. The emailThreatSubmissionPolicies property
        Args:
            value: Value to set for the emailThreatSubmissionPolicies property.
        """
        self._email_threat_submission_policies = value
    
    @property
    def file_threats(self,) -> Optional[List[file_threat_submission.FileThreatSubmission]]:
        """
        Gets the fileThreats property value. The fileThreats property
        Returns: Optional[List[file_threat_submission.FileThreatSubmission]]
        """
        return self._file_threats
    
    @file_threats.setter
    def file_threats(self,value: Optional[List[file_threat_submission.FileThreatSubmission]] = None) -> None:
        """
        Sets the fileThreats property value. The fileThreats property
        Args:
            value: Value to set for the fileThreats property.
        """
        self._file_threats = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email_threats": lambda n : setattr(self, 'email_threats', n.get_collection_of_object_values(email_threat_submission.EmailThreatSubmission)),
            "email_threat_submission_policies": lambda n : setattr(self, 'email_threat_submission_policies', n.get_collection_of_object_values(email_threat_submission_policy.EmailThreatSubmissionPolicy)),
            "file_threats": lambda n : setattr(self, 'file_threats', n.get_collection_of_object_values(file_threat_submission.FileThreatSubmission)),
            "url_threats": lambda n : setattr(self, 'url_threats', n.get_collection_of_object_values(url_threat_submission.UrlThreatSubmission)),
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
        writer.write_collection_of_object_values("emailThreats", self.email_threats)
        writer.write_collection_of_object_values("emailThreatSubmissionPolicies", self.email_threat_submission_policies)
        writer.write_collection_of_object_values("fileThreats", self.file_threats)
        writer.write_collection_of_object_values("urlThreats", self.url_threats)
    
    @property
    def url_threats(self,) -> Optional[List[url_threat_submission.UrlThreatSubmission]]:
        """
        Gets the urlThreats property value. The urlThreats property
        Returns: Optional[List[url_threat_submission.UrlThreatSubmission]]
        """
        return self._url_threats
    
    @url_threats.setter
    def url_threats(self,value: Optional[List[url_threat_submission.UrlThreatSubmission]] = None) -> None:
        """
        Sets the urlThreats property value. The urlThreats property
        Args:
            value: Value to set for the urlThreats property.
        """
        self._url_threats = value
    

