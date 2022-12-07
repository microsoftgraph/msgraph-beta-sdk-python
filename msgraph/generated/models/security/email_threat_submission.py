from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_info = lazy_import('msgraph.generated.models.security.attack_simulation_info')
submission_category = lazy_import('msgraph.generated.models.security.submission_category')
tenant_allow_or_block_list_action = lazy_import('msgraph.generated.models.security.tenant_allow_or_block_list_action')
threat_submission = lazy_import('msgraph.generated.models.security.threat_submission')

class EmailThreatSubmission(threat_submission.ThreatSubmission):
    @property
    def attack_simulation_info(self,) -> Optional[attack_simulation_info.AttackSimulationInfo]:
        """
        Gets the attackSimulationInfo property value. If the email is phishing simulation, this field will not be null.
        Returns: Optional[attack_simulation_info.AttackSimulationInfo]
        """
        return self._attack_simulation_info
    
    @attack_simulation_info.setter
    def attack_simulation_info(self,value: Optional[attack_simulation_info.AttackSimulationInfo] = None) -> None:
        """
        Sets the attackSimulationInfo property value. If the email is phishing simulation, this field will not be null.
        Args:
            value: Value to set for the attackSimulationInfo property.
        """
        self._attack_simulation_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EmailThreatSubmission and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.emailThreatSubmission"
        # If the email is phishing simulation, this field will not be null.
        self._attack_simulation_info: Optional[attack_simulation_info.AttackSimulationInfo] = None
        # Specifies the internet message id of the email being submitted. This information is present in the email header.
        self._internet_message_id: Optional[str] = None
        # The original category of the submission. The possible values are: notJunk, spam, phishing, malware and unkownFutureValue.
        self._original_category: Optional[submission_category.SubmissionCategory] = None
        # Specifies the date and time stamp when the email was received.
        self._received_date_time: Optional[datetime] = None
        # Specifies the email address (in smtp format) of the recipient who received the email.
        self._recipient_email_address: Optional[str] = None
        # Specifies the email address of the sender.
        self._sender: Optional[str] = None
        # Specifies the IP address of the sender.
        self._sender_i_p: Optional[str] = None
        # Specifies the subject of the email .
        self._subject: Optional[str] = None
        # It is used to automatically add allows for the components such as URL, file, sender; which are deemed bad by Microsoft so that similar messages in the future can be allowed.
        self._tenant_allow_or_block_list_action: Optional[tenant_allow_or_block_list_action.TenantAllowOrBlockListAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailThreatSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_simulation_info": lambda n : setattr(self, 'attack_simulation_info', n.get_object_value(attack_simulation_info.AttackSimulationInfo)),
            "internet_message_id": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "original_category": lambda n : setattr(self, 'original_category', n.get_enum_value(submission_category.SubmissionCategory)),
            "received_date_time": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipient_email_address": lambda n : setattr(self, 'recipient_email_address', n.get_str_value()),
            "sender": lambda n : setattr(self, 'sender', n.get_str_value()),
            "sender_i_p": lambda n : setattr(self, 'sender_i_p', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "tenant_allow_or_block_list_action": lambda n : setattr(self, 'tenant_allow_or_block_list_action', n.get_object_value(tenant_allow_or_block_list_action.TenantAllowOrBlockListAction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internet_message_id(self,) -> Optional[str]:
        """
        Gets the internetMessageId property value. Specifies the internet message id of the email being submitted. This information is present in the email header.
        Returns: Optional[str]
        """
        return self._internet_message_id
    
    @internet_message_id.setter
    def internet_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the internetMessageId property value. Specifies the internet message id of the email being submitted. This information is present in the email header.
        Args:
            value: Value to set for the internetMessageId property.
        """
        self._internet_message_id = value
    
    @property
    def original_category(self,) -> Optional[submission_category.SubmissionCategory]:
        """
        Gets the originalCategory property value. The original category of the submission. The possible values are: notJunk, spam, phishing, malware and unkownFutureValue.
        Returns: Optional[submission_category.SubmissionCategory]
        """
        return self._original_category
    
    @original_category.setter
    def original_category(self,value: Optional[submission_category.SubmissionCategory] = None) -> None:
        """
        Sets the originalCategory property value. The original category of the submission. The possible values are: notJunk, spam, phishing, malware and unkownFutureValue.
        Args:
            value: Value to set for the originalCategory property.
        """
        self._original_category = value
    
    @property
    def received_date_time(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTime property value. Specifies the date and time stamp when the email was received.
        Returns: Optional[datetime]
        """
        return self._received_date_time
    
    @received_date_time.setter
    def received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTime property value. Specifies the date and time stamp when the email was received.
        Args:
            value: Value to set for the receivedDateTime property.
        """
        self._received_date_time = value
    
    @property
    def recipient_email_address(self,) -> Optional[str]:
        """
        Gets the recipientEmailAddress property value. Specifies the email address (in smtp format) of the recipient who received the email.
        Returns: Optional[str]
        """
        return self._recipient_email_address
    
    @recipient_email_address.setter
    def recipient_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientEmailAddress property value. Specifies the email address (in smtp format) of the recipient who received the email.
        Args:
            value: Value to set for the recipientEmailAddress property.
        """
        self._recipient_email_address = value
    
    @property
    def sender(self,) -> Optional[str]:
        """
        Gets the sender property value. Specifies the email address of the sender.
        Returns: Optional[str]
        """
        return self._sender
    
    @sender.setter
    def sender(self,value: Optional[str] = None) -> None:
        """
        Sets the sender property value. Specifies the email address of the sender.
        Args:
            value: Value to set for the sender property.
        """
        self._sender = value
    
    @property
    def sender_i_p(self,) -> Optional[str]:
        """
        Gets the senderIP property value. Specifies the IP address of the sender.
        Returns: Optional[str]
        """
        return self._sender_i_p
    
    @sender_i_p.setter
    def sender_i_p(self,value: Optional[str] = None) -> None:
        """
        Sets the senderIP property value. Specifies the IP address of the sender.
        Args:
            value: Value to set for the senderIP property.
        """
        self._sender_i_p = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. Specifies the subject of the email .
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. Specifies the subject of the email .
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def tenant_allow_or_block_list_action(self,) -> Optional[tenant_allow_or_block_list_action.TenantAllowOrBlockListAction]:
        """
        Gets the tenantAllowOrBlockListAction property value. It is used to automatically add allows for the components such as URL, file, sender; which are deemed bad by Microsoft so that similar messages in the future can be allowed.
        Returns: Optional[tenant_allow_or_block_list_action.TenantAllowOrBlockListAction]
        """
        return self._tenant_allow_or_block_list_action
    
    @tenant_allow_or_block_list_action.setter
    def tenant_allow_or_block_list_action(self,value: Optional[tenant_allow_or_block_list_action.TenantAllowOrBlockListAction] = None) -> None:
        """
        Sets the tenantAllowOrBlockListAction property value. It is used to automatically add allows for the components such as URL, file, sender; which are deemed bad by Microsoft so that similar messages in the future can be allowed.
        Args:
            value: Value to set for the tenantAllowOrBlockListAction property.
        """
        self._tenant_allow_or_block_list_action = value
    

