from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert = lazy_import('msgraph.generated.models.alert')
attack_simulation_root = lazy_import('msgraph.generated.models.attack_simulation_root')
cloud_app_security_profile = lazy_import('msgraph.generated.models.cloud_app_security_profile')
domain_security_profile = lazy_import('msgraph.generated.models.domain_security_profile')
entity = lazy_import('msgraph.generated.models.entity')
file_security_profile = lazy_import('msgraph.generated.models.file_security_profile')
host_security_profile = lazy_import('msgraph.generated.models.host_security_profile')
ip_security_profile = lazy_import('msgraph.generated.models.ip_security_profile')
provider_tenant_setting = lazy_import('msgraph.generated.models.provider_tenant_setting')
secure_score = lazy_import('msgraph.generated.models.secure_score')
secure_score_control_profile = lazy_import('msgraph.generated.models.secure_score_control_profile')
security_action = lazy_import('msgraph.generated.models.security_action')
security_provider_status = lazy_import('msgraph.generated.models.security_provider_status')
subject_rights_request = lazy_import('msgraph.generated.models.subject_rights_request')
ti_indicator = lazy_import('msgraph.generated.models.ti_indicator')
user_security_profile = lazy_import('msgraph.generated.models.user_security_profile')
alert = lazy_import('msgraph.generated.models.security.alert')
cases_root = lazy_import('msgraph.generated.models.security.cases_root')
incident = lazy_import('msgraph.generated.models.security.incident')
information_protection = lazy_import('msgraph.generated.models.security.information_protection')
labels_root = lazy_import('msgraph.generated.models.security.labels_root')
threat_submission_root = lazy_import('msgraph.generated.models.security.threat_submission_root')
trigger_types_root = lazy_import('msgraph.generated.models.security.trigger_types_root')
triggers_root = lazy_import('msgraph.generated.models.security.triggers_root')

class Security(entity.Entity):
    @property
    def alerts(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts property value. Notifications for suspicious or potential security issues in a customer’s tenant.
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts property value. Notifications for suspicious or potential security issues in a customer’s tenant.
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @property
    def alerts_v2(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts_v2 property value. A collection of alerts in Microsoft 365 Defender.
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts_v2
    
    @alerts_v2.setter
    def alerts_v2(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts_v2 property value. A collection of alerts in Microsoft 365 Defender.
        Args:
            value: Value to set for the alerts_v2 property.
        """
        self._alerts_v2 = value
    
    @property
    def attack_simulation(self,) -> Optional[attack_simulation_root.AttackSimulationRoot]:
        """
        Gets the attackSimulation property value. Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
        Returns: Optional[attack_simulation_root.AttackSimulationRoot]
        """
        return self._attack_simulation
    
    @attack_simulation.setter
    def attack_simulation(self,value: Optional[attack_simulation_root.AttackSimulationRoot] = None) -> None:
        """
        Sets the attackSimulation property value. Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
        Args:
            value: Value to set for the attackSimulation property.
        """
        self._attack_simulation = value
    
    @property
    def cases(self,) -> Optional[cases_root.CasesRoot]:
        """
        Gets the cases property value. The cases property
        Returns: Optional[cases_root.CasesRoot]
        """
        return self._cases
    
    @cases.setter
    def cases(self,value: Optional[cases_root.CasesRoot] = None) -> None:
        """
        Sets the cases property value. The cases property
        Args:
            value: Value to set for the cases property.
        """
        self._cases = value
    
    @property
    def cloud_app_security_profiles(self,) -> Optional[List[cloud_app_security_profile.CloudAppSecurityProfile]]:
        """
        Gets the cloudAppSecurityProfiles property value. The cloudAppSecurityProfiles property
        Returns: Optional[List[cloud_app_security_profile.CloudAppSecurityProfile]]
        """
        return self._cloud_app_security_profiles
    
    @cloud_app_security_profiles.setter
    def cloud_app_security_profiles(self,value: Optional[List[cloud_app_security_profile.CloudAppSecurityProfile]] = None) -> None:
        """
        Sets the cloudAppSecurityProfiles property value. The cloudAppSecurityProfiles property
        Args:
            value: Value to set for the cloudAppSecurityProfiles property.
        """
        self._cloud_app_security_profiles = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Security and sets the default values.
        """
        super().__init__()
        # Notifications for suspicious or potential security issues in a customer’s tenant.
        self._alerts: Optional[List[alert.Alert]] = None
        # A collection of alerts in Microsoft 365 Defender.
        self._alerts_v2: Optional[List[alert.Alert]] = None
        # Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
        self._attack_simulation: Optional[attack_simulation_root.AttackSimulationRoot] = None
        # The cases property
        self._cases: Optional[cases_root.CasesRoot] = None
        # The cloudAppSecurityProfiles property
        self._cloud_app_security_profiles: Optional[List[cloud_app_security_profile.CloudAppSecurityProfile]] = None
        # The domainSecurityProfiles property
        self._domain_security_profiles: Optional[List[domain_security_profile.DomainSecurityProfile]] = None
        # The fileSecurityProfiles property
        self._file_security_profiles: Optional[List[file_security_profile.FileSecurityProfile]] = None
        # The hostSecurityProfiles property
        self._host_security_profiles: Optional[List[host_security_profile.HostSecurityProfile]] = None
        # A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        self._incidents: Optional[List[incident.Incident]] = None
        # The informationProtection property
        self._information_protection: Optional[information_protection.InformationProtection] = None
        # The ipSecurityProfiles property
        self._ip_security_profiles: Optional[List[ip_security_profile.IpSecurityProfile]] = None
        # The labels property
        self._labels: Optional[labels_root.LabelsRoot] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The providerStatus property
        self._provider_status: Optional[List[security_provider_status.SecurityProviderStatus]] = None
        # The providerTenantSettings property
        self._provider_tenant_settings: Optional[List[provider_tenant_setting.ProviderTenantSetting]] = None
        # The secureScoreControlProfiles property
        self._secure_score_control_profiles: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None
        # Measurements of tenants’ security posture to help protect them from threats.
        self._secure_scores: Optional[List[secure_score.SecureScore]] = None
        # The securityActions property
        self._security_actions: Optional[List[security_action.SecurityAction]] = None
        # The subjectRightsRequests property
        self._subject_rights_requests: Optional[List[subject_rights_request.SubjectRightsRequest]] = None
        # A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        self._threat_submission: Optional[threat_submission_root.ThreatSubmissionRoot] = None
        # The tiIndicators property
        self._ti_indicators: Optional[List[ti_indicator.TiIndicator]] = None
        # The triggers property
        self._triggers: Optional[triggers_root.TriggersRoot] = None
        # The triggerTypes property
        self._trigger_types: Optional[trigger_types_root.TriggerTypesRoot] = None
        # The userSecurityProfiles property
        self._user_security_profiles: Optional[List[user_security_profile.UserSecurityProfile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Security
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Security()
    
    @property
    def domain_security_profiles(self,) -> Optional[List[domain_security_profile.DomainSecurityProfile]]:
        """
        Gets the domainSecurityProfiles property value. The domainSecurityProfiles property
        Returns: Optional[List[domain_security_profile.DomainSecurityProfile]]
        """
        return self._domain_security_profiles
    
    @domain_security_profiles.setter
    def domain_security_profiles(self,value: Optional[List[domain_security_profile.DomainSecurityProfile]] = None) -> None:
        """
        Sets the domainSecurityProfiles property value. The domainSecurityProfiles property
        Args:
            value: Value to set for the domainSecurityProfiles property.
        """
        self._domain_security_profiles = value
    
    @property
    def file_security_profiles(self,) -> Optional[List[file_security_profile.FileSecurityProfile]]:
        """
        Gets the fileSecurityProfiles property value. The fileSecurityProfiles property
        Returns: Optional[List[file_security_profile.FileSecurityProfile]]
        """
        return self._file_security_profiles
    
    @file_security_profiles.setter
    def file_security_profiles(self,value: Optional[List[file_security_profile.FileSecurityProfile]] = None) -> None:
        """
        Sets the fileSecurityProfiles property value. The fileSecurityProfiles property
        Args:
            value: Value to set for the fileSecurityProfiles property.
        """
        self._file_security_profiles = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(alert.Alert)),
            "alerts_v2": lambda n : setattr(self, 'alerts_v2', n.get_collection_of_object_values(alert.Alert)),
            "attack_simulation": lambda n : setattr(self, 'attack_simulation', n.get_object_value(attack_simulation_root.AttackSimulationRoot)),
            "cases": lambda n : setattr(self, 'cases', n.get_object_value(cases_root.CasesRoot)),
            "cloud_app_security_profiles": lambda n : setattr(self, 'cloud_app_security_profiles', n.get_collection_of_object_values(cloud_app_security_profile.CloudAppSecurityProfile)),
            "domain_security_profiles": lambda n : setattr(self, 'domain_security_profiles', n.get_collection_of_object_values(domain_security_profile.DomainSecurityProfile)),
            "file_security_profiles": lambda n : setattr(self, 'file_security_profiles', n.get_collection_of_object_values(file_security_profile.FileSecurityProfile)),
            "host_security_profiles": lambda n : setattr(self, 'host_security_profiles', n.get_collection_of_object_values(host_security_profile.HostSecurityProfile)),
            "incidents": lambda n : setattr(self, 'incidents', n.get_collection_of_object_values(incident.Incident)),
            "information_protection": lambda n : setattr(self, 'information_protection', n.get_object_value(information_protection.InformationProtection)),
            "ip_security_profiles": lambda n : setattr(self, 'ip_security_profiles', n.get_collection_of_object_values(ip_security_profile.IpSecurityProfile)),
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(labels_root.LabelsRoot)),
            "provider_status": lambda n : setattr(self, 'provider_status', n.get_collection_of_object_values(security_provider_status.SecurityProviderStatus)),
            "provider_tenant_settings": lambda n : setattr(self, 'provider_tenant_settings', n.get_collection_of_object_values(provider_tenant_setting.ProviderTenantSetting)),
            "secure_score_control_profiles": lambda n : setattr(self, 'secure_score_control_profiles', n.get_collection_of_object_values(secure_score_control_profile.SecureScoreControlProfile)),
            "secure_scores": lambda n : setattr(self, 'secure_scores', n.get_collection_of_object_values(secure_score.SecureScore)),
            "security_actions": lambda n : setattr(self, 'security_actions', n.get_collection_of_object_values(security_action.SecurityAction)),
            "subject_rights_requests": lambda n : setattr(self, 'subject_rights_requests', n.get_collection_of_object_values(subject_rights_request.SubjectRightsRequest)),
            "threat_submission": lambda n : setattr(self, 'threat_submission', n.get_object_value(threat_submission_root.ThreatSubmissionRoot)),
            "ti_indicators": lambda n : setattr(self, 'ti_indicators', n.get_collection_of_object_values(ti_indicator.TiIndicator)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_object_value(triggers_root.TriggersRoot)),
            "trigger_types": lambda n : setattr(self, 'trigger_types', n.get_object_value(trigger_types_root.TriggerTypesRoot)),
            "user_security_profiles": lambda n : setattr(self, 'user_security_profiles', n.get_collection_of_object_values(user_security_profile.UserSecurityProfile)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_security_profiles(self,) -> Optional[List[host_security_profile.HostSecurityProfile]]:
        """
        Gets the hostSecurityProfiles property value. The hostSecurityProfiles property
        Returns: Optional[List[host_security_profile.HostSecurityProfile]]
        """
        return self._host_security_profiles
    
    @host_security_profiles.setter
    def host_security_profiles(self,value: Optional[List[host_security_profile.HostSecurityProfile]] = None) -> None:
        """
        Sets the hostSecurityProfiles property value. The hostSecurityProfiles property
        Args:
            value: Value to set for the hostSecurityProfiles property.
        """
        self._host_security_profiles = value
    
    @property
    def incidents(self,) -> Optional[List[incident.Incident]]:
        """
        Gets the incidents property value. A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        Returns: Optional[List[incident.Incident]]
        """
        return self._incidents
    
    @incidents.setter
    def incidents(self,value: Optional[List[incident.Incident]] = None) -> None:
        """
        Sets the incidents property value. A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        Args:
            value: Value to set for the incidents property.
        """
        self._incidents = value
    
    @property
    def information_protection(self,) -> Optional[information_protection.InformationProtection]:
        """
        Gets the informationProtection property value. The informationProtection property
        Returns: Optional[information_protection.InformationProtection]
        """
        return self._information_protection
    
    @information_protection.setter
    def information_protection(self,value: Optional[information_protection.InformationProtection] = None) -> None:
        """
        Sets the informationProtection property value. The informationProtection property
        Args:
            value: Value to set for the informationProtection property.
        """
        self._information_protection = value
    
    @property
    def ip_security_profiles(self,) -> Optional[List[ip_security_profile.IpSecurityProfile]]:
        """
        Gets the ipSecurityProfiles property value. The ipSecurityProfiles property
        Returns: Optional[List[ip_security_profile.IpSecurityProfile]]
        """
        return self._ip_security_profiles
    
    @ip_security_profiles.setter
    def ip_security_profiles(self,value: Optional[List[ip_security_profile.IpSecurityProfile]] = None) -> None:
        """
        Sets the ipSecurityProfiles property value. The ipSecurityProfiles property
        Args:
            value: Value to set for the ipSecurityProfiles property.
        """
        self._ip_security_profiles = value
    
    @property
    def labels(self,) -> Optional[labels_root.LabelsRoot]:
        """
        Gets the labels property value. The labels property
        Returns: Optional[labels_root.LabelsRoot]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[labels_root.LabelsRoot] = None) -> None:
        """
        Sets the labels property value. The labels property
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
    @property
    def provider_status(self,) -> Optional[List[security_provider_status.SecurityProviderStatus]]:
        """
        Gets the providerStatus property value. The providerStatus property
        Returns: Optional[List[security_provider_status.SecurityProviderStatus]]
        """
        return self._provider_status
    
    @provider_status.setter
    def provider_status(self,value: Optional[List[security_provider_status.SecurityProviderStatus]] = None) -> None:
        """
        Sets the providerStatus property value. The providerStatus property
        Args:
            value: Value to set for the providerStatus property.
        """
        self._provider_status = value
    
    @property
    def provider_tenant_settings(self,) -> Optional[List[provider_tenant_setting.ProviderTenantSetting]]:
        """
        Gets the providerTenantSettings property value. The providerTenantSettings property
        Returns: Optional[List[provider_tenant_setting.ProviderTenantSetting]]
        """
        return self._provider_tenant_settings
    
    @provider_tenant_settings.setter
    def provider_tenant_settings(self,value: Optional[List[provider_tenant_setting.ProviderTenantSetting]] = None) -> None:
        """
        Sets the providerTenantSettings property value. The providerTenantSettings property
        Args:
            value: Value to set for the providerTenantSettings property.
        """
        self._provider_tenant_settings = value
    
    @property
    def secure_score_control_profiles(self,) -> Optional[List[secure_score_control_profile.SecureScoreControlProfile]]:
        """
        Gets the secureScoreControlProfiles property value. The secureScoreControlProfiles property
        Returns: Optional[List[secure_score_control_profile.SecureScoreControlProfile]]
        """
        return self._secure_score_control_profiles
    
    @secure_score_control_profiles.setter
    def secure_score_control_profiles(self,value: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None) -> None:
        """
        Sets the secureScoreControlProfiles property value. The secureScoreControlProfiles property
        Args:
            value: Value to set for the secureScoreControlProfiles property.
        """
        self._secure_score_control_profiles = value
    
    @property
    def secure_scores(self,) -> Optional[List[secure_score.SecureScore]]:
        """
        Gets the secureScores property value. Measurements of tenants’ security posture to help protect them from threats.
        Returns: Optional[List[secure_score.SecureScore]]
        """
        return self._secure_scores
    
    @secure_scores.setter
    def secure_scores(self,value: Optional[List[secure_score.SecureScore]] = None) -> None:
        """
        Sets the secureScores property value. Measurements of tenants’ security posture to help protect them from threats.
        Args:
            value: Value to set for the secureScores property.
        """
        self._secure_scores = value
    
    @property
    def security_actions(self,) -> Optional[List[security_action.SecurityAction]]:
        """
        Gets the securityActions property value. The securityActions property
        Returns: Optional[List[security_action.SecurityAction]]
        """
        return self._security_actions
    
    @security_actions.setter
    def security_actions(self,value: Optional[List[security_action.SecurityAction]] = None) -> None:
        """
        Sets the securityActions property value. The securityActions property
        Args:
            value: Value to set for the securityActions property.
        """
        self._security_actions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("alerts_v2", self.alerts_v2)
        writer.write_object_value("attackSimulation", self.attack_simulation)
        writer.write_object_value("cases", self.cases)
        writer.write_collection_of_object_values("cloudAppSecurityProfiles", self.cloud_app_security_profiles)
        writer.write_collection_of_object_values("domainSecurityProfiles", self.domain_security_profiles)
        writer.write_collection_of_object_values("fileSecurityProfiles", self.file_security_profiles)
        writer.write_collection_of_object_values("hostSecurityProfiles", self.host_security_profiles)
        writer.write_collection_of_object_values("incidents", self.incidents)
        writer.write_object_value("informationProtection", self.information_protection)
        writer.write_collection_of_object_values("ipSecurityProfiles", self.ip_security_profiles)
        writer.write_object_value("labels", self.labels)
        writer.write_collection_of_object_values("providerStatus", self.provider_status)
        writer.write_collection_of_object_values("providerTenantSettings", self.provider_tenant_settings)
        writer.write_collection_of_object_values("secureScoreControlProfiles", self.secure_score_control_profiles)
        writer.write_collection_of_object_values("secureScores", self.secure_scores)
        writer.write_collection_of_object_values("securityActions", self.security_actions)
        writer.write_collection_of_object_values("subjectRightsRequests", self.subject_rights_requests)
        writer.write_object_value("threatSubmission", self.threat_submission)
        writer.write_collection_of_object_values("tiIndicators", self.ti_indicators)
        writer.write_object_value("triggers", self.triggers)
        writer.write_object_value("triggerTypes", self.trigger_types)
        writer.write_collection_of_object_values("userSecurityProfiles", self.user_security_profiles)
    
    @property
    def subject_rights_requests(self,) -> Optional[List[subject_rights_request.SubjectRightsRequest]]:
        """
        Gets the subjectRightsRequests property value. The subjectRightsRequests property
        Returns: Optional[List[subject_rights_request.SubjectRightsRequest]]
        """
        return self._subject_rights_requests
    
    @subject_rights_requests.setter
    def subject_rights_requests(self,value: Optional[List[subject_rights_request.SubjectRightsRequest]] = None) -> None:
        """
        Sets the subjectRightsRequests property value. The subjectRightsRequests property
        Args:
            value: Value to set for the subjectRightsRequests property.
        """
        self._subject_rights_requests = value
    
    @property
    def threat_submission(self,) -> Optional[threat_submission_root.ThreatSubmissionRoot]:
        """
        Gets the threatSubmission property value. A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        Returns: Optional[threat_submission_root.ThreatSubmissionRoot]
        """
        return self._threat_submission
    
    @threat_submission.setter
    def threat_submission(self,value: Optional[threat_submission_root.ThreatSubmissionRoot] = None) -> None:
        """
        Sets the threatSubmission property value. A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        Args:
            value: Value to set for the threatSubmission property.
        """
        self._threat_submission = value
    
    @property
    def ti_indicators(self,) -> Optional[List[ti_indicator.TiIndicator]]:
        """
        Gets the tiIndicators property value. The tiIndicators property
        Returns: Optional[List[ti_indicator.TiIndicator]]
        """
        return self._ti_indicators
    
    @ti_indicators.setter
    def ti_indicators(self,value: Optional[List[ti_indicator.TiIndicator]] = None) -> None:
        """
        Sets the tiIndicators property value. The tiIndicators property
        Args:
            value: Value to set for the tiIndicators property.
        """
        self._ti_indicators = value
    
    @property
    def triggers(self,) -> Optional[triggers_root.TriggersRoot]:
        """
        Gets the triggers property value. The triggers property
        Returns: Optional[triggers_root.TriggersRoot]
        """
        return self._triggers
    
    @triggers.setter
    def triggers(self,value: Optional[triggers_root.TriggersRoot] = None) -> None:
        """
        Sets the triggers property value. The triggers property
        Args:
            value: Value to set for the triggers property.
        """
        self._triggers = value
    
    @property
    def trigger_types(self,) -> Optional[trigger_types_root.TriggerTypesRoot]:
        """
        Gets the triggerTypes property value. The triggerTypes property
        Returns: Optional[trigger_types_root.TriggerTypesRoot]
        """
        return self._trigger_types
    
    @trigger_types.setter
    def trigger_types(self,value: Optional[trigger_types_root.TriggerTypesRoot] = None) -> None:
        """
        Sets the triggerTypes property value. The triggerTypes property
        Args:
            value: Value to set for the triggerTypes property.
        """
        self._trigger_types = value
    
    @property
    def user_security_profiles(self,) -> Optional[List[user_security_profile.UserSecurityProfile]]:
        """
        Gets the userSecurityProfiles property value. The userSecurityProfiles property
        Returns: Optional[List[user_security_profile.UserSecurityProfile]]
        """
        return self._user_security_profiles
    
    @user_security_profiles.setter
    def user_security_profiles(self,value: Optional[List[user_security_profile.UserSecurityProfile]] = None) -> None:
        """
        Sets the userSecurityProfiles property value. The userSecurityProfiles property
        Args:
            value: Value to set for the userSecurityProfiles property.
        """
        self._user_security_profiles = value
    

