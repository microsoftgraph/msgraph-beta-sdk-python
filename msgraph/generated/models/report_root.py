from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_sign_in_detailed_summary = lazy_import('msgraph.generated.models.application_sign_in_detailed_summary')
authentication_methods_root = lazy_import('msgraph.generated.models.authentication_methods_root')
credential_user_registration_details = lazy_import('msgraph.generated.models.credential_user_registration_details')
entity = lazy_import('msgraph.generated.models.entity')
print_usage = lazy_import('msgraph.generated.models.print_usage')
print_usage_by_printer = lazy_import('msgraph.generated.models.print_usage_by_printer')
print_usage_by_user = lazy_import('msgraph.generated.models.print_usage_by_user')
security_reports_root = lazy_import('msgraph.generated.models.security_reports_root')
user_credential_usage_details = lazy_import('msgraph.generated.models.user_credential_usage_details')

class ReportRoot(entity.Entity):
    @property
    def application_sign_in_detailed_summary(self,) -> Optional[List[application_sign_in_detailed_summary.ApplicationSignInDetailedSummary]]:
        """
        Gets the applicationSignInDetailedSummary property value. Represents a detailed summary of an application sign-in.
        Returns: Optional[List[application_sign_in_detailed_summary.ApplicationSignInDetailedSummary]]
        """
        return self._application_sign_in_detailed_summary
    
    @application_sign_in_detailed_summary.setter
    def application_sign_in_detailed_summary(self,value: Optional[List[application_sign_in_detailed_summary.ApplicationSignInDetailedSummary]] = None) -> None:
        """
        Sets the applicationSignInDetailedSummary property value. Represents a detailed summary of an application sign-in.
        Args:
            value: Value to set for the applicationSignInDetailedSummary property.
        """
        self._application_sign_in_detailed_summary = value
    
    @property
    def authentication_methods(self,) -> Optional[authentication_methods_root.AuthenticationMethodsRoot]:
        """
        Gets the authenticationMethods property value. Container for navigation properties for Azure AD authentication methods resources.
        Returns: Optional[authentication_methods_root.AuthenticationMethodsRoot]
        """
        return self._authentication_methods
    
    @authentication_methods.setter
    def authentication_methods(self,value: Optional[authentication_methods_root.AuthenticationMethodsRoot] = None) -> None:
        """
        Sets the authenticationMethods property value. Container for navigation properties for Azure AD authentication methods resources.
        Args:
            value: Value to set for the authenticationMethods property.
        """
        self._authentication_methods = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ReportRoot and sets the default values.
        """
        super().__init__()
        # Represents a detailed summary of an application sign-in.
        self._application_sign_in_detailed_summary: Optional[List[application_sign_in_detailed_summary.ApplicationSignInDetailedSummary]] = None
        # Container for navigation properties for Azure AD authentication methods resources.
        self._authentication_methods: Optional[authentication_methods_root.AuthenticationMethodsRoot] = None
        # Details of the usage of self-service password reset and multi-factor authentication (MFA) for all registered users.
        self._credential_user_registration_details: Optional[List[credential_user_registration_details.CredentialUserRegistrationDetails]] = None
        # The dailyPrintUsage property
        self._daily_print_usage: Optional[List[print_usage.PrintUsage]] = None
        # The dailyPrintUsageByPrinter property
        self._daily_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The dailyPrintUsageByUser property
        self._daily_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The dailyPrintUsageSummariesByPrinter property
        self._daily_print_usage_summaries_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The dailyPrintUsageSummariesByUser property
        self._daily_print_usage_summaries_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The monthlyPrintUsageByPrinter property
        self._monthly_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The monthlyPrintUsageByUser property
        self._monthly_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The monthlyPrintUsageSummariesByPrinter property
        self._monthly_print_usage_summaries_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The monthlyPrintUsageSummariesByUser property
        self._monthly_print_usage_summaries_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Provides the ability to launch a realistic simulated phishing attack that organizations can learn from.
        self._security: Optional[security_reports_root.SecurityReportsRoot] = None
        # Represents the self-service password reset (SSPR) usage for a given tenant.
        self._user_credential_usage_details: Optional[List[user_credential_usage_details.UserCredentialUsageDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReportRoot()
    
    @property
    def credential_user_registration_details(self,) -> Optional[List[credential_user_registration_details.CredentialUserRegistrationDetails]]:
        """
        Gets the credentialUserRegistrationDetails property value. Details of the usage of self-service password reset and multi-factor authentication (MFA) for all registered users.
        Returns: Optional[List[credential_user_registration_details.CredentialUserRegistrationDetails]]
        """
        return self._credential_user_registration_details
    
    @credential_user_registration_details.setter
    def credential_user_registration_details(self,value: Optional[List[credential_user_registration_details.CredentialUserRegistrationDetails]] = None) -> None:
        """
        Sets the credentialUserRegistrationDetails property value. Details of the usage of self-service password reset and multi-factor authentication (MFA) for all registered users.
        Args:
            value: Value to set for the credentialUserRegistrationDetails property.
        """
        self._credential_user_registration_details = value
    
    @property
    def daily_print_usage(self,) -> Optional[List[print_usage.PrintUsage]]:
        """
        Gets the dailyPrintUsage property value. The dailyPrintUsage property
        Returns: Optional[List[print_usage.PrintUsage]]
        """
        return self._daily_print_usage
    
    @daily_print_usage.setter
    def daily_print_usage(self,value: Optional[List[print_usage.PrintUsage]] = None) -> None:
        """
        Sets the dailyPrintUsage property value. The dailyPrintUsage property
        Args:
            value: Value to set for the dailyPrintUsage property.
        """
        self._daily_print_usage = value
    
    @property
    def daily_print_usage_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the dailyPrintUsageByPrinter property value. The dailyPrintUsageByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._daily_print_usage_by_printer
    
    @daily_print_usage_by_printer.setter
    def daily_print_usage_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the dailyPrintUsageByPrinter property value. The dailyPrintUsageByPrinter property
        Args:
            value: Value to set for the dailyPrintUsageByPrinter property.
        """
        self._daily_print_usage_by_printer = value
    
    @property
    def daily_print_usage_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the dailyPrintUsageByUser property value. The dailyPrintUsageByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._daily_print_usage_by_user
    
    @daily_print_usage_by_user.setter
    def daily_print_usage_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the dailyPrintUsageByUser property value. The dailyPrintUsageByUser property
        Args:
            value: Value to set for the dailyPrintUsageByUser property.
        """
        self._daily_print_usage_by_user = value
    
    @property
    def daily_print_usage_summaries_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the dailyPrintUsageSummariesByPrinter property value. The dailyPrintUsageSummariesByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._daily_print_usage_summaries_by_printer
    
    @daily_print_usage_summaries_by_printer.setter
    def daily_print_usage_summaries_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the dailyPrintUsageSummariesByPrinter property value. The dailyPrintUsageSummariesByPrinter property
        Args:
            value: Value to set for the dailyPrintUsageSummariesByPrinter property.
        """
        self._daily_print_usage_summaries_by_printer = value
    
    @property
    def daily_print_usage_summaries_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the dailyPrintUsageSummariesByUser property value. The dailyPrintUsageSummariesByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._daily_print_usage_summaries_by_user
    
    @daily_print_usage_summaries_by_user.setter
    def daily_print_usage_summaries_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the dailyPrintUsageSummariesByUser property value. The dailyPrintUsageSummariesByUser property
        Args:
            value: Value to set for the dailyPrintUsageSummariesByUser property.
        """
        self._daily_print_usage_summaries_by_user = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_sign_in_detailed_summary": lambda n : setattr(self, 'application_sign_in_detailed_summary', n.get_collection_of_object_values(application_sign_in_detailed_summary.ApplicationSignInDetailedSummary)),
            "authentication_methods": lambda n : setattr(self, 'authentication_methods', n.get_object_value(authentication_methods_root.AuthenticationMethodsRoot)),
            "credential_user_registration_details": lambda n : setattr(self, 'credential_user_registration_details', n.get_collection_of_object_values(credential_user_registration_details.CredentialUserRegistrationDetails)),
            "daily_print_usage": lambda n : setattr(self, 'daily_print_usage', n.get_collection_of_object_values(print_usage.PrintUsage)),
            "daily_print_usage_by_printer": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "daily_print_usage_by_user": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "daily_print_usage_summaries_by_printer": lambda n : setattr(self, 'daily_print_usage_summaries_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "daily_print_usage_summaries_by_user": lambda n : setattr(self, 'daily_print_usage_summaries_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthly_print_usage_by_printer": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthly_print_usage_by_user": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthly_print_usage_summaries_by_printer": lambda n : setattr(self, 'monthly_print_usage_summaries_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthly_print_usage_summaries_by_user": lambda n : setattr(self, 'monthly_print_usage_summaries_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security_reports_root.SecurityReportsRoot)),
            "user_credential_usage_details": lambda n : setattr(self, 'user_credential_usage_details', n.get_collection_of_object_values(user_credential_usage_details.UserCredentialUsageDetails)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def monthly_print_usage_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the monthlyPrintUsageByPrinter property value. The monthlyPrintUsageByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._monthly_print_usage_by_printer
    
    @monthly_print_usage_by_printer.setter
    def monthly_print_usage_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the monthlyPrintUsageByPrinter property value. The monthlyPrintUsageByPrinter property
        Args:
            value: Value to set for the monthlyPrintUsageByPrinter property.
        """
        self._monthly_print_usage_by_printer = value
    
    @property
    def monthly_print_usage_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the monthlyPrintUsageByUser property value. The monthlyPrintUsageByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._monthly_print_usage_by_user
    
    @monthly_print_usage_by_user.setter
    def monthly_print_usage_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the monthlyPrintUsageByUser property value. The monthlyPrintUsageByUser property
        Args:
            value: Value to set for the monthlyPrintUsageByUser property.
        """
        self._monthly_print_usage_by_user = value
    
    @property
    def monthly_print_usage_summaries_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the monthlyPrintUsageSummariesByPrinter property value. The monthlyPrintUsageSummariesByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._monthly_print_usage_summaries_by_printer
    
    @monthly_print_usage_summaries_by_printer.setter
    def monthly_print_usage_summaries_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the monthlyPrintUsageSummariesByPrinter property value. The monthlyPrintUsageSummariesByPrinter property
        Args:
            value: Value to set for the monthlyPrintUsageSummariesByPrinter property.
        """
        self._monthly_print_usage_summaries_by_printer = value
    
    @property
    def monthly_print_usage_summaries_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the monthlyPrintUsageSummariesByUser property value. The monthlyPrintUsageSummariesByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._monthly_print_usage_summaries_by_user
    
    @monthly_print_usage_summaries_by_user.setter
    def monthly_print_usage_summaries_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the monthlyPrintUsageSummariesByUser property value. The monthlyPrintUsageSummariesByUser property
        Args:
            value: Value to set for the monthlyPrintUsageSummariesByUser property.
        """
        self._monthly_print_usage_summaries_by_user = value
    
    @property
    def security(self,) -> Optional[security_reports_root.SecurityReportsRoot]:
        """
        Gets the security property value. Provides the ability to launch a realistic simulated phishing attack that organizations can learn from.
        Returns: Optional[security_reports_root.SecurityReportsRoot]
        """
        return self._security
    
    @security.setter
    def security(self,value: Optional[security_reports_root.SecurityReportsRoot] = None) -> None:
        """
        Sets the security property value. Provides the ability to launch a realistic simulated phishing attack that organizations can learn from.
        Args:
            value: Value to set for the security property.
        """
        self._security = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("applicationSignInDetailedSummary", self.application_sign_in_detailed_summary)
        writer.write_object_value("authenticationMethods", self.authentication_methods)
        writer.write_collection_of_object_values("credentialUserRegistrationDetails", self.credential_user_registration_details)
        writer.write_collection_of_object_values("dailyPrintUsage", self.daily_print_usage)
        writer.write_collection_of_object_values("dailyPrintUsageByPrinter", self.daily_print_usage_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageByUser", self.daily_print_usage_by_user)
        writer.write_collection_of_object_values("dailyPrintUsageSummariesByPrinter", self.daily_print_usage_summaries_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageSummariesByUser", self.daily_print_usage_summaries_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageSummariesByPrinter", self.monthly_print_usage_summaries_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageSummariesByUser", self.monthly_print_usage_summaries_by_user)
        writer.write_object_value("security", self.security)
        writer.write_collection_of_object_values("userCredentialUsageDetails", self.user_credential_usage_details)
    
    @property
    def user_credential_usage_details(self,) -> Optional[List[user_credential_usage_details.UserCredentialUsageDetails]]:
        """
        Gets the userCredentialUsageDetails property value. Represents the self-service password reset (SSPR) usage for a given tenant.
        Returns: Optional[List[user_credential_usage_details.UserCredentialUsageDetails]]
        """
        return self._user_credential_usage_details
    
    @user_credential_usage_details.setter
    def user_credential_usage_details(self,value: Optional[List[user_credential_usage_details.UserCredentialUsageDetails]] = None) -> None:
        """
        Sets the userCredentialUsageDetails property value. Represents the self-service password reset (SSPR) usage for a given tenant.
        Args:
            value: Value to set for the userCredentialUsageDetails property.
        """
        self._user_credential_usage_details = value
    

