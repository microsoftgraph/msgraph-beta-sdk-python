from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_threat_submission, email_threat_submission_policy, file_threat_submission, url_threat_submission
    from .. import entity

from .. import entity

@dataclass
class ThreatSubmissionRoot(entity.Entity):
    # The emailThreatSubmissionPolicies property
    email_threat_submission_policies: Optional[List[email_threat_submission_policy.EmailThreatSubmissionPolicy]] = None
    # The emailThreats property
    email_threats: Optional[List[email_threat_submission.EmailThreatSubmission]] = None
    # The fileThreats property
    file_threats: Optional[List[file_threat_submission.FileThreatSubmission]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The urlThreats property
    url_threats: Optional[List[url_threat_submission.UrlThreatSubmission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatSubmissionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmissionRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ThreatSubmissionRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_threat_submission, email_threat_submission_policy, file_threat_submission, url_threat_submission
        from .. import entity

        from . import email_threat_submission, email_threat_submission_policy, file_threat_submission, url_threat_submission
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "emailThreatSubmissionPolicies": lambda n : setattr(self, 'email_threat_submission_policies', n.get_collection_of_object_values(email_threat_submission_policy.EmailThreatSubmissionPolicy)),
            "emailThreats": lambda n : setattr(self, 'email_threats', n.get_collection_of_object_values(email_threat_submission.EmailThreatSubmission)),
            "fileThreats": lambda n : setattr(self, 'file_threats', n.get_collection_of_object_values(file_threat_submission.FileThreatSubmission)),
            "urlThreats": lambda n : setattr(self, 'url_threats', n.get_collection_of_object_values(url_threat_submission.UrlThreatSubmission)),
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
        writer.write_collection_of_object_values("emailThreatSubmissionPolicies", self.email_threat_submission_policies)
        writer.write_collection_of_object_values("emailThreats", self.email_threats)
        writer.write_collection_of_object_values("fileThreats", self.file_threats)
        writer.write_collection_of_object_values("urlThreats", self.url_threats)
    

