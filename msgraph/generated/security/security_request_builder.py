from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors import o_data_error
    from ..models.security import security
    from .alerts import alerts_request_builder
    from .alerts.item import alert_item_request_builder
    from .alerts_v2 import alerts_v2_request_builder
    from .alerts_v2.item import alert_item_request_builder
    from .attack_simulation import attack_simulation_request_builder
    from .cases import cases_request_builder
    from .cloud_app_security_profiles import cloud_app_security_profiles_request_builder
    from .cloud_app_security_profiles.item import cloud_app_security_profile_item_request_builder
    from .domain_security_profiles import domain_security_profiles_request_builder
    from .domain_security_profiles.item import domain_security_profile_item_request_builder
    from .file_security_profiles import file_security_profiles_request_builder
    from .file_security_profiles.item import file_security_profile_item_request_builder
    from .host_security_profiles import host_security_profiles_request_builder
    from .host_security_profiles.item import host_security_profile_item_request_builder
    from .incidents import incidents_request_builder
    from .incidents.item import incident_item_request_builder
    from .information_protection import information_protection_request_builder
    from .ip_security_profiles import ip_security_profiles_request_builder
    from .ip_security_profiles.item import ip_security_profile_item_request_builder
    from .labels import labels_request_builder
    from .provider_tenant_settings import provider_tenant_settings_request_builder
    from .provider_tenant_settings.item import provider_tenant_setting_item_request_builder
    from .secure_score_control_profiles import secure_score_control_profiles_request_builder
    from .secure_score_control_profiles.item import secure_score_control_profile_item_request_builder
    from .secure_scores import secure_scores_request_builder
    from .secure_scores.item import secure_score_item_request_builder
    from .security_actions import security_actions_request_builder
    from .security_actions.item import security_action_item_request_builder
    from .security_run_hunting_query import security_run_hunting_query_request_builder
    from .subject_rights_requests import subject_rights_requests_request_builder
    from .subject_rights_requests.item import subject_rights_request_item_request_builder
    from .threat_intelligence import threat_intelligence_request_builder
    from .threat_submission import threat_submission_request_builder
    from .ti_indicators import ti_indicators_request_builder
    from .ti_indicators.item import ti_indicator_item_request_builder
    from .triggers import triggers_request_builder
    from .trigger_types import trigger_types_request_builder
    from .user_security_profiles import user_security_profiles_request_builder
    from .user_security_profiles.item import user_security_profile_item_request_builder

class SecurityRequestBuilder():
    """
    Provides operations to manage the security singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SecurityRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def alerts_by_id(self,id: str) -> alert_item_request_builder.AlertItemRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: alert_item_request_builder.AlertItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .alerts.item import alert_item_request_builder
        from .alerts_v2.item import alert_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["alert%2Did"] = id
        return alert_item_request_builder.AlertItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def alerts_v2_by_id(self,id: str) -> alert_item_request_builder.AlertItemRequestBuilder:
        """
        Provides operations to manage the alerts_v2 property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: alert_item_request_builder.AlertItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .alerts.item import alert_item_request_builder
        from .alerts_v2.item import alert_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["alert%2Did"] = id
        return alert_item_request_builder.AlertItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def cloud_app_security_profiles_by_id(self,id: str) -> cloud_app_security_profile_item_request_builder.CloudAppSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the cloudAppSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: cloud_app_security_profile_item_request_builder.CloudAppSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .cloud_app_security_profiles.item import cloud_app_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudAppSecurityProfile%2Did"] = id
        return cloud_app_security_profile_item_request_builder.CloudAppSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domain_security_profiles_by_id(self,id: str) -> domain_security_profile_item_request_builder.DomainSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the domainSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: domain_security_profile_item_request_builder.DomainSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .domain_security_profiles.item import domain_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainSecurityProfile%2Did"] = id
        return domain_security_profile_item_request_builder.DomainSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def file_security_profiles_by_id(self,id: str) -> file_security_profile_item_request_builder.FileSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the fileSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: file_security_profile_item_request_builder.FileSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .file_security_profiles.item import file_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileSecurityProfile%2Did"] = id
        return file_security_profile_item_request_builder.FileSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> Optional[security.Security]:
        """
        Get security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[security.Security]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security import security

        return await self.request_adapter.send_async(request_info, security.Security, error_mapping)
    
    def host_security_profiles_by_id(self,id: str) -> host_security_profile_item_request_builder.HostSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the hostSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: host_security_profile_item_request_builder.HostSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .host_security_profiles.item import host_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["hostSecurityProfile%2Did"] = id
        return host_security_profile_item_request_builder.HostSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def incidents_by_id(self,id: str) -> incident_item_request_builder.IncidentItemRequestBuilder:
        """
        Provides operations to manage the incidents property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: incident_item_request_builder.IncidentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .incidents.item import incident_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["incident%2Did"] = id
        return incident_item_request_builder.IncidentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def ip_security_profiles_by_id(self,id: str) -> ip_security_profile_item_request_builder.IpSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the ipSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: ip_security_profile_item_request_builder.IpSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .ip_security_profiles.item import ip_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ipSecurityProfile%2Did"] = id
        return ip_security_profile_item_request_builder.IpSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> Optional[security.Security]:
        """
        Update security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[security.Security]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security import security

        return await self.request_adapter.send_async(request_info, security.Security, error_mapping)
    
    def provider_tenant_settings_by_id(self,id: str) -> provider_tenant_setting_item_request_builder.ProviderTenantSettingItemRequestBuilder:
        """
        Provides operations to manage the providerTenantSettings property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: provider_tenant_setting_item_request_builder.ProviderTenantSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .provider_tenant_settings.item import provider_tenant_setting_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["providerTenantSetting%2Did"] = id
        return provider_tenant_setting_item_request_builder.ProviderTenantSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def secure_score_control_profiles_by_id(self,id: str) -> secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .secure_score_control_profiles.item import secure_score_control_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["secureScoreControlProfile%2Did"] = id
        return secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def secure_scores_by_id(self,id: str) -> secure_score_item_request_builder.SecureScoreItemRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: secure_score_item_request_builder.SecureScoreItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .secure_scores.item import secure_score_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["secureScore%2Did"] = id
        return secure_score_item_request_builder.SecureScoreItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def security_actions_by_id(self,id: str) -> security_action_item_request_builder.SecurityActionItemRequestBuilder:
        """
        Provides operations to manage the securityActions property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: security_action_item_request_builder.SecurityActionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .security_actions.item import security_action_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["securityAction%2Did"] = id
        return security_action_item_request_builder.SecurityActionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subject_rights_requests_by_id(self,id: str) -> subject_rights_request_item_request_builder.SubjectRightsRequestItemRequestBuilder:
        """
        Provides operations to manage the subjectRightsRequests property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: subject_rights_request_item_request_builder.SubjectRightsRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .subject_rights_requests.item import subject_rights_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subjectRightsRequest%2Did"] = id
        return subject_rights_request_item_request_builder.SubjectRightsRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def ti_indicators_by_id(self,id: str) -> ti_indicator_item_request_builder.TiIndicatorItemRequestBuilder:
        """
        Provides operations to manage the tiIndicators property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: ti_indicator_item_request_builder.TiIndicatorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .ti_indicators.item import ti_indicator_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tiIndicator%2Did"] = id
        return ti_indicator_item_request_builder.TiIndicatorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def user_security_profiles_by_id(self,id: str) -> user_security_profile_item_request_builder.UserSecurityProfileItemRequestBuilder:
        """
        Provides operations to manage the userSecurityProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: user_security_profile_item_request_builder.UserSecurityProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_security_profiles.item import user_security_profile_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userSecurityProfile%2Did"] = id
        return user_security_profile_item_request_builder.UserSecurityProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def alerts(self) -> alerts_request_builder.AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        """
        from .alerts import alerts_request_builder

        return alerts_request_builder.AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alerts_v2(self) -> alerts_v2_request_builder.Alerts_v2RequestBuilder:
        """
        Provides operations to manage the alerts_v2 property of the microsoft.graph.security entity.
        """
        from .alerts_v2 import alerts_v2_request_builder

        return alerts_v2_request_builder.Alerts_v2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attack_simulation(self) -> attack_simulation_request_builder.AttackSimulationRequestBuilder:
        """
        Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
        """
        from .attack_simulation import attack_simulation_request_builder

        return attack_simulation_request_builder.AttackSimulationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cases(self) -> cases_request_builder.CasesRequestBuilder:
        """
        Provides operations to manage the cases property of the microsoft.graph.security entity.
        """
        from .cases import cases_request_builder

        return cases_request_builder.CasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_app_security_profiles(self) -> cloud_app_security_profiles_request_builder.CloudAppSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the cloudAppSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .cloud_app_security_profiles import cloud_app_security_profiles_request_builder

        return cloud_app_security_profiles_request_builder.CloudAppSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_security_profiles(self) -> domain_security_profiles_request_builder.DomainSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the domainSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .domain_security_profiles import domain_security_profiles_request_builder

        return domain_security_profiles_request_builder.DomainSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file_security_profiles(self) -> file_security_profiles_request_builder.FileSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the fileSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .file_security_profiles import file_security_profiles_request_builder

        return file_security_profiles_request_builder.FileSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_security_profiles(self) -> host_security_profiles_request_builder.HostSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the hostSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .host_security_profiles import host_security_profiles_request_builder

        return host_security_profiles_request_builder.HostSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incidents(self) -> incidents_request_builder.IncidentsRequestBuilder:
        """
        Provides operations to manage the incidents property of the microsoft.graph.security entity.
        """
        from .incidents import incidents_request_builder

        return incidents_request_builder.IncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> information_protection_request_builder.InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection property of the microsoft.graph.security entity.
        """
        from .information_protection import information_protection_request_builder

        return information_protection_request_builder.InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ip_security_profiles(self) -> ip_security_profiles_request_builder.IpSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the ipSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .ip_security_profiles import ip_security_profiles_request_builder

        return ip_security_profiles_request_builder.IpSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def labels(self) -> labels_request_builder.LabelsRequestBuilder:
        """
        Provides operations to manage the labels property of the microsoft.graph.security entity.
        """
        from .labels import labels_request_builder

        return labels_request_builder.LabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provider_tenant_settings(self) -> provider_tenant_settings_request_builder.ProviderTenantSettingsRequestBuilder:
        """
        Provides operations to manage the providerTenantSettings property of the microsoft.graph.security entity.
        """
        from .provider_tenant_settings import provider_tenant_settings_request_builder

        return provider_tenant_settings_request_builder.ProviderTenantSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_score_control_profiles(self) -> secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        """
        from .secure_score_control_profiles import secure_score_control_profiles_request_builder

        return secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_scores(self) -> secure_scores_request_builder.SecureScoresRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        """
        from .secure_scores import secure_scores_request_builder

        return secure_scores_request_builder.SecureScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_actions(self) -> security_actions_request_builder.SecurityActionsRequestBuilder:
        """
        Provides operations to manage the securityActions property of the microsoft.graph.security entity.
        """
        from .security_actions import security_actions_request_builder

        return security_actions_request_builder.SecurityActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_run_hunting_query(self) -> security_run_hunting_query_request_builder.SecurityRunHuntingQueryRequestBuilder:
        """
        Provides operations to call the runHuntingQuery method.
        """
        from .security_run_hunting_query import security_run_hunting_query_request_builder

        return security_run_hunting_query_request_builder.SecurityRunHuntingQueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subject_rights_requests(self) -> subject_rights_requests_request_builder.SubjectRightsRequestsRequestBuilder:
        """
        Provides operations to manage the subjectRightsRequests property of the microsoft.graph.security entity.
        """
        from .subject_rights_requests import subject_rights_requests_request_builder

        return subject_rights_requests_request_builder.SubjectRightsRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_intelligence(self) -> threat_intelligence_request_builder.ThreatIntelligenceRequestBuilder:
        """
        Provides operations to manage the threatIntelligence property of the microsoft.graph.security entity.
        """
        from .threat_intelligence import threat_intelligence_request_builder

        return threat_intelligence_request_builder.ThreatIntelligenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_submission(self) -> threat_submission_request_builder.ThreatSubmissionRequestBuilder:
        """
        Provides operations to manage the threatSubmission property of the microsoft.graph.security entity.
        """
        from .threat_submission import threat_submission_request_builder

        return threat_submission_request_builder.ThreatSubmissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ti_indicators(self) -> ti_indicators_request_builder.TiIndicatorsRequestBuilder:
        """
        Provides operations to manage the tiIndicators property of the microsoft.graph.security entity.
        """
        from .ti_indicators import ti_indicators_request_builder

        return ti_indicators_request_builder.TiIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def triggers(self) -> triggers_request_builder.TriggersRequestBuilder:
        """
        Provides operations to manage the triggers property of the microsoft.graph.security entity.
        """
        from .triggers import triggers_request_builder

        return triggers_request_builder.TriggersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_types(self) -> trigger_types_request_builder.TriggerTypesRequestBuilder:
        """
        Provides operations to manage the triggerTypes property of the microsoft.graph.security entity.
        """
        from .trigger_types import trigger_types_request_builder

        return trigger_types_request_builder.TriggerTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_security_profiles(self) -> user_security_profiles_request_builder.UserSecurityProfilesRequestBuilder:
        """
        Provides operations to manage the userSecurityProfiles property of the microsoft.graph.security entity.
        """
        from .user_security_profiles import user_security_profiles_request_builder

        return user_security_profiles_request_builder.UserSecurityProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Get security
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SecurityRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SecurityRequestBuilder.SecurityRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SecurityRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

