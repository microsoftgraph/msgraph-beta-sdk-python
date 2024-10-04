from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
    from .app_credential_sign_in_activity import AppCredentialSignInActivity
    from .authentication_methods_root import AuthenticationMethodsRoot
    from .credential_user_registration_details import CredentialUserRegistrationDetails
    from .entity import Entity
    from .health_monitoring.health_monitoring_root import HealthMonitoringRoot
    from .partners.partners import Partners
    from .print_usage import PrintUsage
    from .print_usage_by_printer import PrintUsageByPrinter
    from .print_usage_by_user import PrintUsageByUser
    from .security_reports_root import SecurityReportsRoot
    from .service_activity import ServiceActivity
    from .service_level_agreement_root import ServiceLevelAgreementRoot
    from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
    from .user_credential_usage_details import UserCredentialUsageDetails
    from .user_insights_root import UserInsightsRoot

from .entity import Entity

@dataclass
class ReportRoot(Entity):
    """
    The resource that represents an instance of Enrollment Failure Reports.
    """
    # Represents a collection of sign-in activities of application credentials.
    app_credential_sign_in_activities: Optional[List[AppCredentialSignInActivity]] = None
    # Represents a detailed summary of an application sign-in.
    application_sign_in_detailed_summary: Optional[List[ApplicationSignInDetailedSummary]] = None
    # Container for navigation properties for Microsoft Entra authentication methods resources.
    authentication_methods: Optional[AuthenticationMethodsRoot] = None
    # Details of the usage of self-service password reset and multifactor authentication (MFA) for all registered users.
    credential_user_registration_details: Optional[List[CredentialUserRegistrationDetails]] = None
    # The dailyPrintUsage property
    daily_print_usage: Optional[List[PrintUsage]] = None
    # Retrieve a list of daily print usage summaries, grouped by printer.
    daily_print_usage_by_printer: Optional[List[PrintUsageByPrinter]] = None
    # Retrieve a list of daily print usage summaries, grouped by user.
    daily_print_usage_by_user: Optional[List[PrintUsageByUser]] = None
    # The dailyPrintUsageSummariesByPrinter property
    daily_print_usage_summaries_by_printer: Optional[List[PrintUsageByPrinter]] = None
    # The dailyPrintUsageSummariesByUser property
    daily_print_usage_summaries_by_user: Optional[List[PrintUsageByUser]] = None
    # The healthMonitoring property
    health_monitoring: Optional[HealthMonitoringRoot] = None
    # Retrieve a list of monthly print usage summaries, grouped by printer.
    monthly_print_usage_by_printer: Optional[List[PrintUsageByPrinter]] = None
    # Retrieve a list of monthly print usage summaries, grouped by user.
    monthly_print_usage_by_user: Optional[List[PrintUsageByUser]] = None
    # The monthlyPrintUsageSummariesByPrinter property
    monthly_print_usage_summaries_by_printer: Optional[List[PrintUsageByPrinter]] = None
    # The monthlyPrintUsageSummariesByUser property
    monthly_print_usage_summaries_by_user: Optional[List[PrintUsageByUser]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents billing details for a Microsoft direct partner.
    partners: Optional[Partners] = None
    # Provides the ability to launch a simulated phishing attack that organizations can learn from.
    security: Optional[SecurityReportsRoot] = None
    # Reports that relate to tenant-level authentication activities in Microsoft Entra.
    service_activity: Optional[ServiceActivity] = None
    # Represents a collection of sign-in activities of service principals.
    service_principal_sign_in_activities: Optional[List[ServicePrincipalSignInActivity]] = None
    # Reports that relate to tenant-level Microsoft Entra SLA attainment.
    sla: Optional[ServiceLevelAgreementRoot] = None
    # Represents the self-service password reset (SSPR) usage for a given tenant.
    user_credential_usage_details: Optional[List[UserCredentialUsageDetails]] = None
    # Represents a collection of user activities on applications in a tenant that is configured for Microsoft Entra External ID for customers.
    user_insights: Optional[UserInsightsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReportRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
        from .app_credential_sign_in_activity import AppCredentialSignInActivity
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .credential_user_registration_details import CredentialUserRegistrationDetails
        from .entity import Entity
        from .health_monitoring.health_monitoring_root import HealthMonitoringRoot
        from .partners.partners import Partners
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .security_reports_root import SecurityReportsRoot
        from .service_activity import ServiceActivity
        from .service_level_agreement_root import ServiceLevelAgreementRoot
        from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
        from .user_credential_usage_details import UserCredentialUsageDetails
        from .user_insights_root import UserInsightsRoot

        from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
        from .app_credential_sign_in_activity import AppCredentialSignInActivity
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .credential_user_registration_details import CredentialUserRegistrationDetails
        from .entity import Entity
        from .health_monitoring.health_monitoring_root import HealthMonitoringRoot
        from .partners.partners import Partners
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .security_reports_root import SecurityReportsRoot
        from .service_activity import ServiceActivity
        from .service_level_agreement_root import ServiceLevelAgreementRoot
        from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
        from .user_credential_usage_details import UserCredentialUsageDetails
        from .user_insights_root import UserInsightsRoot

        fields: Dict[str, Callable[[Any], None]] = {
            "appCredentialSignInActivities": lambda n : setattr(self, 'app_credential_sign_in_activities', n.get_collection_of_object_values(AppCredentialSignInActivity)),
            "applicationSignInDetailedSummary": lambda n : setattr(self, 'application_sign_in_detailed_summary', n.get_collection_of_object_values(ApplicationSignInDetailedSummary)),
            "authenticationMethods": lambda n : setattr(self, 'authentication_methods', n.get_object_value(AuthenticationMethodsRoot)),
            "credentialUserRegistrationDetails": lambda n : setattr(self, 'credential_user_registration_details', n.get_collection_of_object_values(CredentialUserRegistrationDetails)),
            "dailyPrintUsage": lambda n : setattr(self, 'daily_print_usage', n.get_collection_of_object_values(PrintUsage)),
            "dailyPrintUsageByPrinter": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "dailyPrintUsageByUser": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "dailyPrintUsageSummariesByPrinter": lambda n : setattr(self, 'daily_print_usage_summaries_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "dailyPrintUsageSummariesByUser": lambda n : setattr(self, 'daily_print_usage_summaries_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "healthMonitoring": lambda n : setattr(self, 'health_monitoring', n.get_object_value(HealthMonitoringRoot)),
            "monthlyPrintUsageByPrinter": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "monthlyPrintUsageByUser": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "monthlyPrintUsageSummariesByPrinter": lambda n : setattr(self, 'monthly_print_usage_summaries_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "monthlyPrintUsageSummariesByUser": lambda n : setattr(self, 'monthly_print_usage_summaries_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "partners": lambda n : setattr(self, 'partners', n.get_object_value(Partners)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(SecurityReportsRoot)),
            "serviceActivity": lambda n : setattr(self, 'service_activity', n.get_object_value(ServiceActivity)),
            "servicePrincipalSignInActivities": lambda n : setattr(self, 'service_principal_sign_in_activities', n.get_collection_of_object_values(ServicePrincipalSignInActivity)),
            "sla": lambda n : setattr(self, 'sla', n.get_object_value(ServiceLevelAgreementRoot)),
            "userCredentialUsageDetails": lambda n : setattr(self, 'user_credential_usage_details', n.get_collection_of_object_values(UserCredentialUsageDetails)),
            "userInsights": lambda n : setattr(self, 'user_insights', n.get_object_value(UserInsightsRoot)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
        writer.write_object_value("healthMonitoring", self.health_monitoring)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageSummariesByPrinter", self.monthly_print_usage_summaries_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageSummariesByUser", self.monthly_print_usage_summaries_by_user)
        writer.write_object_value("partners", self.partners)
        writer.write_object_value("security", self.security)
        writer.write_object_value("serviceActivity", self.service_activity)
        writer.write_collection_of_object_values("servicePrincipalSignInActivities", self.service_principal_sign_in_activities)
        writer.write_object_value("sla", self.sla)
        writer.write_collection_of_object_values("userCredentialUsageDetails", self.user_credential_usage_details)
        writer.write_object_value("userInsights", self.user_insights)
    

