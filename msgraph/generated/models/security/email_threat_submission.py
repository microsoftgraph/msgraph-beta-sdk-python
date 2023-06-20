from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attack_simulation_info, email_content_threat_submission, email_url_threat_submission, submission_category, tenant_allow_or_block_list_action, threat_submission

from . import threat_submission

@dataclass
class EmailThreatSubmission(threat_submission.ThreatSubmission):
    odata_type = "#microsoft.graph.security.emailThreatSubmission"
    # If the email is phishing simulation, this field will not be null.
    attack_simulation_info: Optional[attack_simulation_info.AttackSimulationInfo] = None
    # Specifies the internet message id of the email being submitted. This information is present in the email header.
    internet_message_id: Optional[str] = None
    # The original category of the submission. The possible values are: notJunk, spam, phishing, malware and unkownFutureValue.
    original_category: Optional[submission_category.SubmissionCategory] = None
    # Specifies the date and time stamp when the email was received.
    received_date_time: Optional[datetime] = None
    # Specifies the email address (in smtp format) of the recipient who received the email.
    recipient_email_address: Optional[str] = None
    # Specifies the email address of the sender.
    sender: Optional[str] = None
    # Specifies the IP address of the sender.
    sender_i_p: Optional[str] = None
    # Specifies the subject of the email .
    subject: Optional[str] = None
    # It is used to automatically add allows for the components such as URL, file, sender; which are deemed bad by Microsoft so that similar messages in the future can be allowed.
    tenant_allow_or_block_list_action: Optional[tenant_allow_or_block_list_action.TenantAllowOrBlockListAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailThreatSubmission
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailContentThreatSubmission".casefold():
            from . import email_content_threat_submission

            return email_content_threat_submission.EmailContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailUrlThreatSubmission".casefold():
            from . import email_url_threat_submission

            return email_url_threat_submission.EmailUrlThreatSubmission()
        return EmailThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attack_simulation_info, email_content_threat_submission, email_url_threat_submission, submission_category, tenant_allow_or_block_list_action, threat_submission

        from . import attack_simulation_info, email_content_threat_submission, email_url_threat_submission, submission_category, tenant_allow_or_block_list_action, threat_submission

        fields: Dict[str, Callable[[Any], None]] = {
            "attackSimulationInfo": lambda n : setattr(self, 'attack_simulation_info', n.get_object_value(attack_simulation_info.AttackSimulationInfo)),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "originalCategory": lambda n : setattr(self, 'original_category', n.get_enum_value(submission_category.SubmissionCategory)),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipientEmailAddress": lambda n : setattr(self, 'recipient_email_address', n.get_str_value()),
            "sender": lambda n : setattr(self, 'sender', n.get_str_value()),
            "senderIP": lambda n : setattr(self, 'sender_i_p', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "tenantAllowOrBlockListAction": lambda n : setattr(self, 'tenant_allow_or_block_list_action', n.get_object_value(tenant_allow_or_block_list_action.TenantAllowOrBlockListAction)),
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
        writer.write_object_value("attackSimulationInfo", self.attack_simulation_info)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_enum_value("originalCategory", self.original_category)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_str_value("recipientEmailAddress", self.recipient_email_address)
        writer.write_str_value("sender", self.sender)
        writer.write_str_value("senderIP", self.sender_i_p)
        writer.write_str_value("subject", self.subject)
        writer.write_object_value("tenantAllowOrBlockListAction", self.tenant_allow_or_block_list_action)
    

