from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EmailThreatSubmissionPolicy(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new emailThreatSubmissionPolicy and sets the default values.
        """
        super().__init__()
        # Specifies the email address of the sender from which email notifications will be sent to end users to inform them whether an email is spam, phish or clean. The default value is null. Optional for creation.
        self._customized_notification_sender_email_address: Optional[str] = None
        # Specifies the destination where the reported messages from end users will land whenever they report something as phish, junk or not junk. The default value is null. Optional for creation.
        self._customized_report_recipient_email_address: Optional[str] = None
        # Indicates whether end users can report a message as spam, phish or junk directly without a confirmation(popup). The default value is true.  Optional for creation.
        self._is_always_report_enabled_for_users: Optional[bool] = None
        # Indicates whether end users can confirm using a popup before reporting messages as spam, phish or not junk. The default value is true.  Optional for creation.
        self._is_ask_me_enabled_for_users: Optional[bool] = None
        # Indicates whether the email notifications sent to end users to inform them if an email is phish, spam or junk is customized or not. The default value is false. Optional for creation.
        self._is_customized_message_enabled: Optional[bool] = None
        # If enabled, customized message only shows when email is reported as phishing. The default value is false. Optional for creation.
        self._is_customized_message_enabled_for_phishing: Optional[bool] = None
        # Indicates whether to use the sender email address set using customizedNotificationSenderEmailAddress for sending email notifications to end users. The default value is false. Optional for creation.
        self._is_customized_notification_sender_enabled: Optional[bool] = None
        # Indicates whether end users can simply move the message from one folder to another based on the action of spam, phish or not junk without actually reporting it. The default value is true. Optional for creation.
        self._is_never_report_enabled_for_users: Optional[bool] = None
        # Indicates whether the branding logo should be used in the email notifications sent to end users. The default value is false. Optional for creation.
        self._is_organization_branding_enabled: Optional[bool] = None
        # Indicates whether end users can submit from the quarantine page. The default value is true. Optional for creation.
        self._is_report_from_quarantine_enabled: Optional[bool] = None
        # Indicates whether emails reported by end users should be send to the custom mailbox configured using customizedReportRecipientEmailAddress.  The default value is false. Optional for creation.
        self._is_report_to_customized_email_address_enabled: Optional[bool] = None
        # If enabled, the email will be sent to Microsoft for analysis. The default value is false. Required for creation.
        self._is_report_to_microsoft_enabled: Optional[bool] = None
        # Indicates whether an email notification is sent to the end user who reported the email when it has been reviewed by the admin. The default value is false. Optional for creation.
        self._is_review_email_notification_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailThreatSubmissionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailThreatSubmissionPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailThreatSubmissionPolicy()
    
    @property
    def customized_notification_sender_email_address(self,) -> Optional[str]:
        """
        Gets the customizedNotificationSenderEmailAddress property value. Specifies the email address of the sender from which email notifications will be sent to end users to inform them whether an email is spam, phish or clean. The default value is null. Optional for creation.
        Returns: Optional[str]
        """
        return self._customized_notification_sender_email_address
    
    @customized_notification_sender_email_address.setter
    def customized_notification_sender_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the customizedNotificationSenderEmailAddress property value. Specifies the email address of the sender from which email notifications will be sent to end users to inform them whether an email is spam, phish or clean. The default value is null. Optional for creation.
        Args:
            value: Value to set for the customizedNotificationSenderEmailAddress property.
        """
        self._customized_notification_sender_email_address = value
    
    @property
    def customized_report_recipient_email_address(self,) -> Optional[str]:
        """
        Gets the customizedReportRecipientEmailAddress property value. Specifies the destination where the reported messages from end users will land whenever they report something as phish, junk or not junk. The default value is null. Optional for creation.
        Returns: Optional[str]
        """
        return self._customized_report_recipient_email_address
    
    @customized_report_recipient_email_address.setter
    def customized_report_recipient_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the customizedReportRecipientEmailAddress property value. Specifies the destination where the reported messages from end users will land whenever they report something as phish, junk or not junk. The default value is null. Optional for creation.
        Args:
            value: Value to set for the customizedReportRecipientEmailAddress property.
        """
        self._customized_report_recipient_email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "customized_notification_sender_email_address": lambda n : setattr(self, 'customized_notification_sender_email_address', n.get_str_value()),
            "customized_report_recipient_email_address": lambda n : setattr(self, 'customized_report_recipient_email_address', n.get_str_value()),
            "is_always_report_enabled_for_users": lambda n : setattr(self, 'is_always_report_enabled_for_users', n.get_bool_value()),
            "is_ask_me_enabled_for_users": lambda n : setattr(self, 'is_ask_me_enabled_for_users', n.get_bool_value()),
            "is_customized_message_enabled": lambda n : setattr(self, 'is_customized_message_enabled', n.get_bool_value()),
            "is_customized_message_enabled_for_phishing": lambda n : setattr(self, 'is_customized_message_enabled_for_phishing', n.get_bool_value()),
            "is_customized_notification_sender_enabled": lambda n : setattr(self, 'is_customized_notification_sender_enabled', n.get_bool_value()),
            "is_never_report_enabled_for_users": lambda n : setattr(self, 'is_never_report_enabled_for_users', n.get_bool_value()),
            "is_organization_branding_enabled": lambda n : setattr(self, 'is_organization_branding_enabled', n.get_bool_value()),
            "is_report_from_quarantine_enabled": lambda n : setattr(self, 'is_report_from_quarantine_enabled', n.get_bool_value()),
            "is_report_to_customized_email_address_enabled": lambda n : setattr(self, 'is_report_to_customized_email_address_enabled', n.get_bool_value()),
            "is_report_to_microsoft_enabled": lambda n : setattr(self, 'is_report_to_microsoft_enabled', n.get_bool_value()),
            "is_review_email_notification_enabled": lambda n : setattr(self, 'is_review_email_notification_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_always_report_enabled_for_users(self,) -> Optional[bool]:
        """
        Gets the isAlwaysReportEnabledForUsers property value. Indicates whether end users can report a message as spam, phish or junk directly without a confirmation(popup). The default value is true.  Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_always_report_enabled_for_users
    
    @is_always_report_enabled_for_users.setter
    def is_always_report_enabled_for_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAlwaysReportEnabledForUsers property value. Indicates whether end users can report a message as spam, phish or junk directly without a confirmation(popup). The default value is true.  Optional for creation.
        Args:
            value: Value to set for the isAlwaysReportEnabledForUsers property.
        """
        self._is_always_report_enabled_for_users = value
    
    @property
    def is_ask_me_enabled_for_users(self,) -> Optional[bool]:
        """
        Gets the isAskMeEnabledForUsers property value. Indicates whether end users can confirm using a popup before reporting messages as spam, phish or not junk. The default value is true.  Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_ask_me_enabled_for_users
    
    @is_ask_me_enabled_for_users.setter
    def is_ask_me_enabled_for_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAskMeEnabledForUsers property value. Indicates whether end users can confirm using a popup before reporting messages as spam, phish or not junk. The default value is true.  Optional for creation.
        Args:
            value: Value to set for the isAskMeEnabledForUsers property.
        """
        self._is_ask_me_enabled_for_users = value
    
    @property
    def is_customized_message_enabled(self,) -> Optional[bool]:
        """
        Gets the isCustomizedMessageEnabled property value. Indicates whether the email notifications sent to end users to inform them if an email is phish, spam or junk is customized or not. The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_customized_message_enabled
    
    @is_customized_message_enabled.setter
    def is_customized_message_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCustomizedMessageEnabled property value. Indicates whether the email notifications sent to end users to inform them if an email is phish, spam or junk is customized or not. The default value is false. Optional for creation.
        Args:
            value: Value to set for the isCustomizedMessageEnabled property.
        """
        self._is_customized_message_enabled = value
    
    @property
    def is_customized_message_enabled_for_phishing(self,) -> Optional[bool]:
        """
        Gets the isCustomizedMessageEnabledForPhishing property value. If enabled, customized message only shows when email is reported as phishing. The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_customized_message_enabled_for_phishing
    
    @is_customized_message_enabled_for_phishing.setter
    def is_customized_message_enabled_for_phishing(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCustomizedMessageEnabledForPhishing property value. If enabled, customized message only shows when email is reported as phishing. The default value is false. Optional for creation.
        Args:
            value: Value to set for the isCustomizedMessageEnabledForPhishing property.
        """
        self._is_customized_message_enabled_for_phishing = value
    
    @property
    def is_customized_notification_sender_enabled(self,) -> Optional[bool]:
        """
        Gets the isCustomizedNotificationSenderEnabled property value. Indicates whether to use the sender email address set using customizedNotificationSenderEmailAddress for sending email notifications to end users. The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_customized_notification_sender_enabled
    
    @is_customized_notification_sender_enabled.setter
    def is_customized_notification_sender_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCustomizedNotificationSenderEnabled property value. Indicates whether to use the sender email address set using customizedNotificationSenderEmailAddress for sending email notifications to end users. The default value is false. Optional for creation.
        Args:
            value: Value to set for the isCustomizedNotificationSenderEnabled property.
        """
        self._is_customized_notification_sender_enabled = value
    
    @property
    def is_never_report_enabled_for_users(self,) -> Optional[bool]:
        """
        Gets the isNeverReportEnabledForUsers property value. Indicates whether end users can simply move the message from one folder to another based on the action of spam, phish or not junk without actually reporting it. The default value is true. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_never_report_enabled_for_users
    
    @is_never_report_enabled_for_users.setter
    def is_never_report_enabled_for_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the isNeverReportEnabledForUsers property value. Indicates whether end users can simply move the message from one folder to another based on the action of spam, phish or not junk without actually reporting it. The default value is true. Optional for creation.
        Args:
            value: Value to set for the isNeverReportEnabledForUsers property.
        """
        self._is_never_report_enabled_for_users = value
    
    @property
    def is_organization_branding_enabled(self,) -> Optional[bool]:
        """
        Gets the isOrganizationBrandingEnabled property value. Indicates whether the branding logo should be used in the email notifications sent to end users. The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_organization_branding_enabled
    
    @is_organization_branding_enabled.setter
    def is_organization_branding_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOrganizationBrandingEnabled property value. Indicates whether the branding logo should be used in the email notifications sent to end users. The default value is false. Optional for creation.
        Args:
            value: Value to set for the isOrganizationBrandingEnabled property.
        """
        self._is_organization_branding_enabled = value
    
    @property
    def is_report_from_quarantine_enabled(self,) -> Optional[bool]:
        """
        Gets the isReportFromQuarantineEnabled property value. Indicates whether end users can submit from the quarantine page. The default value is true. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_report_from_quarantine_enabled
    
    @is_report_from_quarantine_enabled.setter
    def is_report_from_quarantine_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReportFromQuarantineEnabled property value. Indicates whether end users can submit from the quarantine page. The default value is true. Optional for creation.
        Args:
            value: Value to set for the isReportFromQuarantineEnabled property.
        """
        self._is_report_from_quarantine_enabled = value
    
    @property
    def is_report_to_customized_email_address_enabled(self,) -> Optional[bool]:
        """
        Gets the isReportToCustomizedEmailAddressEnabled property value. Indicates whether emails reported by end users should be send to the custom mailbox configured using customizedReportRecipientEmailAddress.  The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_report_to_customized_email_address_enabled
    
    @is_report_to_customized_email_address_enabled.setter
    def is_report_to_customized_email_address_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReportToCustomizedEmailAddressEnabled property value. Indicates whether emails reported by end users should be send to the custom mailbox configured using customizedReportRecipientEmailAddress.  The default value is false. Optional for creation.
        Args:
            value: Value to set for the isReportToCustomizedEmailAddressEnabled property.
        """
        self._is_report_to_customized_email_address_enabled = value
    
    @property
    def is_report_to_microsoft_enabled(self,) -> Optional[bool]:
        """
        Gets the isReportToMicrosoftEnabled property value. If enabled, the email will be sent to Microsoft for analysis. The default value is false. Required for creation.
        Returns: Optional[bool]
        """
        return self._is_report_to_microsoft_enabled
    
    @is_report_to_microsoft_enabled.setter
    def is_report_to_microsoft_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReportToMicrosoftEnabled property value. If enabled, the email will be sent to Microsoft for analysis. The default value is false. Required for creation.
        Args:
            value: Value to set for the isReportToMicrosoftEnabled property.
        """
        self._is_report_to_microsoft_enabled = value
    
    @property
    def is_review_email_notification_enabled(self,) -> Optional[bool]:
        """
        Gets the isReviewEmailNotificationEnabled property value. Indicates whether an email notification is sent to the end user who reported the email when it has been reviewed by the admin. The default value is false. Optional for creation.
        Returns: Optional[bool]
        """
        return self._is_review_email_notification_enabled
    
    @is_review_email_notification_enabled.setter
    def is_review_email_notification_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReviewEmailNotificationEnabled property value. Indicates whether an email notification is sent to the end user who reported the email when it has been reviewed by the admin. The default value is false. Optional for creation.
        Args:
            value: Value to set for the isReviewEmailNotificationEnabled property.
        """
        self._is_review_email_notification_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("customizedNotificationSenderEmailAddress", self.customized_notification_sender_email_address)
        writer.write_str_value("customizedReportRecipientEmailAddress", self.customized_report_recipient_email_address)
        writer.write_bool_value("isAlwaysReportEnabledForUsers", self.is_always_report_enabled_for_users)
        writer.write_bool_value("isAskMeEnabledForUsers", self.is_ask_me_enabled_for_users)
        writer.write_bool_value("isCustomizedMessageEnabled", self.is_customized_message_enabled)
        writer.write_bool_value("isCustomizedMessageEnabledForPhishing", self.is_customized_message_enabled_for_phishing)
        writer.write_bool_value("isCustomizedNotificationSenderEnabled", self.is_customized_notification_sender_enabled)
        writer.write_bool_value("isNeverReportEnabledForUsers", self.is_never_report_enabled_for_users)
        writer.write_bool_value("isOrganizationBrandingEnabled", self.is_organization_branding_enabled)
        writer.write_bool_value("isReportFromQuarantineEnabled", self.is_report_from_quarantine_enabled)
        writer.write_bool_value("isReportToCustomizedEmailAddressEnabled", self.is_report_to_customized_email_address_enabled)
        writer.write_bool_value("isReportToMicrosoftEnabled", self.is_report_to_microsoft_enabled)
        writer.write_bool_value("isReviewEmailNotificationEnabled", self.is_review_email_notification_enabled)
    

