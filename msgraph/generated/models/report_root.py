from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_sign_in_detailed_summary, app_credential_sign_in_activity, authentication_methods_root, credential_user_registration_details, entity, print_usage, print_usage_by_printer, print_usage_by_user, security_reports_root, service_principal_sign_in_activity, user_credential_usage_details

from . import entity

@dataclass
class ReportRoot(entity.Entity):
    # Represents a collection of sign-in activities of application credentials.
    app_credential_sign_in_activities: Optional[List[app_credential_sign_in_activity.AppCredentialSignInActivity]] = None
    # Represents a detailed summary of an application sign-in.
    application_sign_in_detailed_summary: Optional[List[application_sign_in_detailed_summary.ApplicationSignInDetailedSummary]] = None
    # Container for navigation properties for Azure AD authentication methods resources.
    authentication_methods: Optional[authentication_methods_root.AuthenticationMethodsRoot] = None
    # Details of the usage of self-service password reset and multi-factor authentication (MFA) for all registered users.
    credential_user_registration_details: Optional[List[credential_user_registration_details.CredentialUserRegistrationDetails]] = None
    # The dailyPrintUsage property
    daily_print_usage: Optional[List[print_usage.PrintUsage]] = None
    # The dailyPrintUsageByPrinter property
    daily_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The dailyPrintUsageByUser property
    daily_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The dailyPrintUsageSummariesByPrinter property
    daily_print_usage_summaries_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The dailyPrintUsageSummariesByUser property
    daily_print_usage_summaries_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The monthlyPrintUsageByPrinter property
    monthly_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The monthlyPrintUsageByUser property
    monthly_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The monthlyPrintUsageSummariesByPrinter property
    monthly_print_usage_summaries_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The monthlyPrintUsageSummariesByUser property
    monthly_print_usage_summaries_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the ability to launch a realistic simulated phishing attack that organizations can learn from.
    security: Optional[security_reports_root.SecurityReportsRoot] = None
    # Represents a collection of sign-in activities of service principals.
    service_principal_sign_in_activities: Optional[List[service_principal_sign_in_activity.ServicePrincipalSignInActivity]] = None
    # Represents the self-service password reset (SSPR) usage for a given tenant.
    user_credential_usage_details: Optional[List[user_credential_usage_details.UserCredentialUsageDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReportRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_sign_in_detailed_summary, app_credential_sign_in_activity, authentication_methods_root, credential_user_registration_details, entity, print_usage, print_usage_by_printer, print_usage_by_user, security_reports_root, service_principal_sign_in_activity, user_credential_usage_details

        from . import application_sign_in_detailed_summary, app_credential_sign_in_activity, authentication_methods_root, credential_user_registration_details, entity, print_usage, print_usage_by_printer, print_usage_by_user, security_reports_root, service_principal_sign_in_activity, user_credential_usage_details

        fields: Dict[str, Callable[[Any], None]] = {
            "appCredentialSignInActivities": lambda n : setattr(self, 'app_credential_sign_in_activities', n.get_collection_of_object_values(app_credential_sign_in_activity.AppCredentialSignInActivity)),
            "applicationSignInDetailedSummary": lambda n : setattr(self, 'application_sign_in_detailed_summary', n.get_collection_of_object_values(application_sign_in_detailed_summary.ApplicationSignInDetailedSummary)),
            "authenticationMethods": lambda n : setattr(self, 'authentication_methods', n.get_object_value(authentication_methods_root.AuthenticationMethodsRoot)),
            "credentialUserRegistrationDetails": lambda n : setattr(self, 'credential_user_registration_details', n.get_collection_of_object_values(credential_user_registration_details.CredentialUserRegistrationDetails)),
            "dailyPrintUsage": lambda n : setattr(self, 'daily_print_usage', n.get_collection_of_object_values(print_usage.PrintUsage)),
            "dailyPrintUsageByPrinter": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "dailyPrintUsageByUser": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "dailyPrintUsageSummariesByPrinter": lambda n : setattr(self, 'daily_print_usage_summaries_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "dailyPrintUsageSummariesByUser": lambda n : setattr(self, 'daily_print_usage_summaries_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthlyPrintUsageByPrinter": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthlyPrintUsageByUser": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthlyPrintUsageSummariesByPrinter": lambda n : setattr(self, 'monthly_print_usage_summaries_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthlyPrintUsageSummariesByUser": lambda n : setattr(self, 'monthly_print_usage_summaries_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security_reports_root.SecurityReportsRoot)),
            "servicePrincipalSignInActivities": lambda n : setattr(self, 'service_principal_sign_in_activities', n.get_collection_of_object_values(service_principal_sign_in_activity.ServicePrincipalSignInActivity)),
            "userCredentialUsageDetails": lambda n : setattr(self, 'user_credential_usage_details', n.get_collection_of_object_values(user_credential_usage_details.UserCredentialUsageDetails)),
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
        writer.write_collection_of_object_values("appCredentialSignInActivities", self.app_credential_sign_in_activities)
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
        writer.write_collection_of_object_values("servicePrincipalSignInActivities", self.service_principal_sign_in_activities)
        writer.write_collection_of_object_values("userCredentialUsageDetails", self.user_credential_usage_details)
    

